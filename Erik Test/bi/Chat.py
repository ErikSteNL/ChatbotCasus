import nltk, os, json, time
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from nltk.util import bigrams

# probability threshold
ERROR_THRESHOLD = 0.4 # 40%
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
    sentence_words = []
    w = list(bigrams(sentence))
             
    for x in w:
        sentence_words.append(x[0] + x[1])
    
    # stem each word
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

with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])
    
def classify(sentence, words, classes, show_details=False):
    results = think(sentence, words, show_details)
    try:
        results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ]
        if len(results) > 0:
            results.sort(key=lambda x: x[1], reverse=True) 
            return_results =[[classes[r[0]],r[1]] for r in results]
            print ("%s \n Taal: %s \n Zekerheid: %s%%" % (sentence, return_results[0][0], return_results[0][1]))
        else:
            print("Kan de taal niet met zekerheid bepalen...")
    except Exception, e:
        print("Kaput: %s" % e)

while True:
    print("\n"+"#"*40)
    tempinput = raw_input("Type een zin:\n")
    classify(str(tempinput), synapse['words'], synapse['classes'], show_details=False)
