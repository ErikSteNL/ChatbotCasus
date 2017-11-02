import nltk, os, json, time, Data, random
import numpy as np
from nltk.corpus import brown
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')
nltk.download('universal_tagset')

# probability threshold
ERROR_THRESHOLD = 0.5 # Onder de 50% stel de vraag opnieuw
CERTAIN_THRESHOLD = 0.9 # Boven de 90% weet hij het antwoord zeker
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
    print("TAGS: %s" % tags)
    
    sentence_words = []
    
    for word in tags:
        if word[1] == "NOUN" or word[1] == "NUM" or word[1] == "ADV" or word[1] == "X" or word[1] == "VERB":
            sentence_words.append(str(word[0]))

    #time.sleep(100)
    # stem each word
    print(sentence_words)
    sentence_words = [word.lower() for word in sentence_words]
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
        synapse = json.load(data_file) 
        synapse_0 = np.asarray(synapse['synapse0']) 
        synapse_1 = np.asarray(synapse['synapse1'])

        print("TrainingData loaded")
        return synapse, synapse_0, synapse_1
    
def classify(sentence, words, classes, show_details=False):
    history = []
    results, keywords = think(sentence, words, show_details)
    try:
        results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]

        if len(results) > 0:
            results.sort(key=lambda x: x[1], reverse=True) 
            return_results =[[classes[r[0]],r[1]] for r in results]
            answerToQuestion = Data.GetAnswer(return_results[0][0])
            print("\nClassNumber: %s \nCertainty: %s%%" % (return_results[0][0], return_results[0][1]))
            print("\nAnswer:\n")
            print(answerToQuestion)
            
            if return_results[0][1] < CERTAIN_THRESHOLD:
                print("NOT SURE")
                ask = True

                while ask:
                    time.sleep(1)
                    keys = ""
                    for i in keywords:
                        keys += i + " "
                    history.append(keys)
                    q = raw_input("%s Y/N\n" % Data.GetAnswer(99)) # code 99

                    if "y" in q.lower() or "yes" in q.lower(): # antwoord op vraag is goed
                        print("Added new sentences to brain")  
                        with open("Vragen.txt", "a+") as f:
                            for i in history:
                                print("New question: %s | %s" % (return_results[0][0],i))
                                f.writelines([return_results[0][0],":",i,"\r\n"])
                        ask = False
                    
                    elif "n" in q.lower() or "no" in q.lower(): # antwoord op vraag is NIET goed
                        print("NIET GOED")
                        opnieuw = raw_input("%s Y/N\n" % Data.GetAnswer(97)) # code 97

                        if "y" in opnieuw:  # user wilt opnieuw proberen
                            print("OPNIEUW")
                            sentence = raw_input("%s" % Data.GetAnswer(98)) # code 98
                            #classify(sentence, words, classes, show_details=False)
                            
                            results = think(sentence, words, show_details)
                            if len(results) > 0:
                                results = [[i,r] for i,r in enumerate(results)] # if r>ERROR_THRESHOLD
                                return_results =[[classes[r[0]],r[1]] for r in results]
                                answerToQuestion = Data.GetAnswer(return_results[0][0])
                                print("\nClassNumber: %s \nCertainty: %s%%" % (return_results[0][0], return_results[0][1]))
                                print("\nAnswer:\n%s" % answerToQuestion)
                            else:
                                print("%s" % Data.GetAnswer(100)) # code 100

                        else: # user wilt NIET opnieuw proberen
                            print("Okay")
                            ask = False
        else:
            print("%s\n" % Data.GetAnswer(100)) # code 100
            
    except Exception, e:
        print("Exception error: %s" % e)


synapse, synapse_0, synapse_1 = OpenFile()

while True:
    print("\n"+"#"*40)
    tempinput = raw_input("Ask me a question:\n")
    classify(str(tempinput), synapse['words'], synapse['classes'], show_details=False)
