# -*- coding: utf-8 -*-
# 4 classes of training data
import json, random

def GetTrainingData():
    training_data = []

    trainingDataRaw = []
    print"ik ben hier"
    with open("Vragen.txt") as f:
        trainingDataRaw = f.readlines()
    trainingDataRaw = [x.strip("\n") for x in trainingDataRaw]

    for line in trainingDataRaw:
        line = line.split(':',1)
        training_data.append({"class":line[0], "sentence":line[1]})

    for line in training_data:
        line['sentence'] = line['sentence'].strip().decode("ascii", "ignore").encode("ascii")
        if line['sentence'] == "":continue

    return training_data

def GetAnswer(number):

    answers = []

    with open("Answers.txt") as f:
        answers = f.readlines()

    possibleAnswers = []
    for line in answers:
        line = line.split(':',1)
        if(line[0] == str(number)):
            print("gevonden")
            possibleAnswers.append(line[1])

    if len(possibleAnswers) == 0:
        return ""
    if len(possibleAnswers) == 1:
        return possibleAnswers[0]
    else:
        idk = random.randint(0, len(possibleAnswers)-1)
        return possibleAnswers[idk]

    return ""
