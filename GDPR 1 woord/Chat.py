import nltk, os, json, time, Data, random
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# probability threshold
ERROR_THRESHOLD = 0.5 # Onder de 50% stel de vraag opnieuw
CERTAIN_THRESHOLD = 0.9 # Boven de 90% weet hij het antwoord zeker
# load our calculated synapse values
synapse_file = 'brain.json'

# Answers when we don't understand the question
idk_answer = [
    "Ik begrijp uw vraag niet helemaal, kunt u de vraag anders stellen a.u.b?",
    "Die vraag vindt ik onduidelijk.",
    "Ik snap je vraag niet.",
    "Kun je misschien je vraag anders tellen?"
    ]

thx_answer = [
    "Thank you",
    "No problem"
    ]

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
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
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

    return(np.array(bag))

def think(sentence, words, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2

def OpenFile():
    with open(synapse_file) as data_file: 
        synapse = json.load(data_file) 
        synapse_0 = np.asarray(synapse['synapse0']) 
        synapse_1 = np.asarray(synapse['synapse1'])

        print("TrainingData geladen")
        return synapse, synapse_0, synapse_1
    
def classify(sentence, words, classes, show_details=False):
    results = think(sentence, words, show_details)
    history = []
    try:
        results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ]
        print("Results: %s" % results)
        if len(results) > 0:
            results.sort(key=lambda x: x[1], reverse=True) 
            return_results =[[classes[r[0]],r[1]] for r in results]
            answerToQuestion = Data.GetAnswer(return_results[0][0])
            print("\nVraagnummer: %s \nZekerheid: %s%%" % (return_results[0][0], return_results[0][1]))
            print("\nAnswer to question:\n")
            print(answerToQuestion)
            
            if return_results[0][1] < CERTAIN_THRESHOLD:
                time.sleep(1)
                history.append(sentence)
                q = raw_input("%s Y/N\n" % Data.GetAnswer(99)) # code 99
                if "y" in q.lower() or "yes" in q.lower():
                    print("Added %s to file %s" % (sentence, "brain.json")) # code 98
                elif "n" in q.lower() or "no" in q.lower():
                    new_q = raw_input("Sorry, can you reform your question?\n") # code 97
                    classify(new_q, synapse['words'], synapse['classes'], show_details=False)
                    
        else:
            idk = random.randint(0, len(idk_answer)-1)
            print(idk)
            print(idk_answer[idk])
            
    except Exception, e:
        print("Exception error: %s" % e)


synapse, synapse_0, synapse_1 = OpenFile()

while True:
    print("\n"+"#"*40)
    tempinput = raw_input("Type een zin:\n")
    classify(str(tempinput), synapse['words'], synapse['classes'], show_details=False)
