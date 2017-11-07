import random
from apiclient.discovery import build
from unidecode import unidecode
#json

def GetTrainingData():
    training_data = []

    trainingDataRaw = []
    with open("Questions.txt") as f:
        trainingDataRaw = f.readlines()
    trainingDataRaw = [x.strip("\n") for x in trainingDataRaw]

    for line in trainingDataRaw:
        print(line)
        line = line.split(':',1)
        training_data.append({"class":line[0], "sentence":line[1]})

    for line in training_data:
        line['sentence'] = line['sentence'].strip().decode("ascii", "ignore").encode("ascii")
        print(line['sentence'])
        if line['sentence'] == "":
            continue
    return training_data

def g_translate(source, TranslateTo):
    service = (build('translate', 'v2', developerKey='AIzaSyB0x83parhwESgG8Ig8jhN5ZA34_VVyn8Q'))
    request = service.translations().list(q=source, target=TranslateTo)
    response = request.execute()
    detectedLanguageSource = response['translations'][0]['detectedSourceLanguage']
    test = unidecode(response['translations'][0]['translatedText'])
    return test

def GetAnswer(number, detectedLanguageSource):

    answers = []


    with open("Answers.txt") as f:
        answers = f.readlines()

    possibleAnswers = []
    for line in answers:
        line = line.split(':',1)
        if(line[0] == str(number)):
            possibleAnswers.append(line[1])

    if len(possibleAnswers) == 0:
        return ""
    elif len(possibleAnswers) == 1:
        translatedAnswer = g_translate(possibleAnswers[0],detectedLanguageSource)
        return translatedAnswer
    else:
        idk = random.randint(0, len(possibleAnswers)-1)
        translatedAnswer = g_translate(possibleAnswers[idk],detectedLanguageSource)
        return translatedAnswer.strip()

    #return ""
