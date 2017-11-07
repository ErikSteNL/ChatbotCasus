from apiclient.discovery import build
import nltk, os, json, time, Data, random, schedule
import numpy as np
import re
from collections import Counter
from nltk.stem.lancaster import LancasterStemmer

# probability threshold
ERROR_THRESHOLD = 0.5 # Onder de 0% stel de vraag opnieuw
CERTAIN_THRESHOLD = 0.9 # Boven de 90% is een zeker antwoord

BOTDEBUG = True

# load our calculated synapse values
synapse_file = 'brain.json'

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)

def clean_up_sentence(sentence):

    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # tag the words
    tags = nltk.pos_tag(sentence_words, tagset='universal')
    if(BOTDEBUG):
        print("TAGS: %s" % tags)



    sentence_words = []

    for word in tags:
        if word[1] == "NOUN" or word[1] == "NUM" or word[1] == "ADV" or word[1] == "X" or word[1] == "VERB" or word[1] == "ADJ":
            sentence_words.append(str(word[0]))

    # stem each word
    sentence_words = [word.lower() for word in sentence_words]
    if(BOTDEBUG):
        print(sentence_words)

    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):

    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    if(BOTDEBUG):
                        print ("found in bag: %s" % w)

    return(np.array(bag),sentence_words)

def think(sentence, words, show_details=False):

    x,keywords = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2, keywords

def OpenFile():

    with open(synapse_file) as data_file:
        global synapse
        global synapse_0
        global synapse_1

        synapse = json.load(data_file)
        synapse_0 = np.asarray(synapse['synapse0'])
        synapse_1 = np.asarray(synapse['synapse1'])
        if(BOTDEBUG):
            print("TrainingData loaded")

        return synapse, synapse_0, synapse_1

def classify(sentence, words, classes, detectedLanguageSource, show_details=False):

    history = []
    results, keywords = think(sentence, words, show_details)
    try:
        results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]

        if len(results) > 0:
            results.sort(key=lambda x: x[1], reverse=True)
            return_results =[[classes[r[0]],r[1]] for r in results]
            answerToQuestion = Data.GetAnswer(return_results[0][0], detectedLanguageSource)
            if(BOTDEBUG):
                print("\nClassNumber: %s \nCertainty: %s%%" % (return_results[0][0], return_results[0][1]))
                print("\nAnswer:\n")
            print(answerToQuestion)


            if return_results[0][1] < CERTAIN_THRESHOLD:
                if(BOTDEBUG):
                    print("NOT SURE")

                ask = True
                addToHistory = True

                while ask:
                    time.sleep(1)
                    if addToHistory:
                        keys = ""
                        for i in keywords:
                            keys += i + " "
                        history.append(keys)
                    q = raw_input("%s Yes/No:   " % Data.GetAnswer(99, detectedLanguageSource)) # code 99
                    print("\n")
                    if "y" in q.lower() or "yes" in q.lower(): # antwoord op vraag is goed
                        if(BOTDEBUG):
                            print("Added new sentences to brain")

                        with open("Questions.txt", "a+") as f:
                            for i in history:
                                if(BOTDEBUG):
                                    print("New question: %s | %s" % (return_results[0][0],i))
                                f.writelines([return_results[0][0],":",i,"\n"])
                        ask = False

                    elif "n" in q.lower() or "no" in q.lower(): # antwoord op vraag is NIET goed
                        if(BOTDEBUG):
                            print("NIET GOED")

                        opnieuw = raw_input("%s Yes/No   :\n" % Data.GetAnswer(97, detectedLanguageSource)) # code 97
                        print("\n\n")
                        if "y" in opnieuw:  # user wilt opnieuw proberen
                            if(BOTDEBUG):
                                print("OPNIEUW")

                            sentence = raw_input("%s" % Data.GetAnswer(98, detectedLanguageSource)) # code 98
                            #classify(sentence, words, classes, show_details=False)

                            results, keywords = think(sentence, words, show_details)
                            if len(results) > 0:
                                results = [[i,r] for i,r in enumerate(results)] # if r>ERROR_THRESHOLD
                                results.sort(key=lambda x: x[1], reverse=True)
                                return_results =[[classes[r[0]],r[1]] for r in results]
                                answerToQuestion = Data.GetAnswer(return_results[0][0], detectedLanguageSource)
                                if(BOTDEBUG):
                                    print("\nClassNumber: %s \nCertainty: %s%%" % (return_results[0][0], return_results[0][1]))
                                print(answerToQuestion)

                                if return_results[0][1] > CERTAIN_THRESHOLD:
                                    addToHistory = False
                                else:
                                    addToHistory = True
                            else:
                                print("%s" % Data.GetAnswer(100, detectedLanguageSource)) # code 100

                        else: # user wilt NIET opnieuw proberen
                            if(BOTDEBUG):
                                print("Okay")

                            ask = False
        else:
            if(BOTDEBUG):
                print("%s\n" % Data.GetAnswer(100, detectedLanguageSource)) # code 100


    except Exception, e:
        if(BOTDEBUG):
            print("Exception error: %s" % e)



synapse, synapse_0, synapse_1 = OpenFile()


#returns translate sentence
def g_translate(source, TranslateTo):
    service = (build('translate', 'v2', developerKey='AIzaSyB0x83parhwESgG8Ig8jhN5ZA34_VVyn8Q'))
    request = service.translations().list(q=source, target=TranslateTo)
    response = request.execute()
    detectedLanguageSource = response['translations'][0]['detectedSourceLanguage']
    print(detectedLanguageSource)
    return response['translations'][0]['translatedText'], detectedLanguageSource


schedule.every(6).minutes.do(OpenFile)

while True:
    schedule.run_pending()
    if(BOTDEBUG):
        print("\n"+"#"*40)

    tempinput = raw_input("What is your question?:\n")
    tempinput, detectedLanguageSource = g_translate(tempinput,'en')
    if(BOTDEBUG):
        print "Engels:", tempinput

    classify(str(tempinput), synapse['words'], synapse['classes'], detectedLanguageSource, show_details=False)
