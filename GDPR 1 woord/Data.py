# -*- coding: utf-8 -*-
# 4 classes of training data
import json

def GetTrainingData():
    training_data = []

    trainingDataRaw = []
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

    for line in answers:
        line = line.split(':',1)
        if(line[0] == number):
            return line[1]
    return ""
