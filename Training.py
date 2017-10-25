# 4 classes of training data

def GetTrainingData():
    training_data = []
    training_data.append({"class":"Nederlands", "sentence":"Hallo, hoe gaat het ermee?"})
    training_data.append({"class":"Nederlands", "sentence":"Dit is een willekeurige zin om het systeem te leren."})
    training_data.append({"class":"Nederlands", "sentence":"Mijn favoriete hobby is talen leren."})
    training_data.append({"class":"Nederlands", "sentence":"Ik hoop dat het goed met je gaat!"})
    training_data.append({"class":"Nederlands", "sentence":"Ik vind het heel leuk om met jou te praten."})
    training_data.append({"class":"Nederlands", "sentence":"Wil je eens schrijven hoe jouw dag eruitziet?"})

    training_data.append({"class":"Engels", "sentence":"Hello, how are you doing?"})
    training_data.append({"class":"Engels", "sentence":"This is a random sentence to learn the system."})
    training_data.append({"class":"Engels", "sentence":"My favorite hobby is learning languages."})
    training_data.append({"class":"Engels", "sentence":"I hope you are doing well!"})
    training_data.append({"class":"Engels", "sentence":"I like talking to you."})
    training_data.append({"class":"Engels", "sentence":"Want to write what your day looks like?"})

    training_data.append({"class":"Duits", "sentence":"Hallo, wie geht es dir?"})
    training_data.append({"class":"Duits", "sentence":"Dies ist ein zufalliger Satz, um das System zu lernen."})
    training_data.append({"class":"Duits", "sentence":"Mein Lieblingshobby ist das Sprachenlernen."})
    training_data.append({"class":"Duits", "sentence":"Ich hoffe es geht dir gut!"})
    training_data.append({"class":"Duits", "sentence":"Ich spreche gern mit dir."})
    training_data.append({"class":"Duits", "sentence":"Willst du schreiben, wie dein Tag aussieht?"})

    training_data.append({"class":"Frans", "sentence":"salut, comment ca vas?"})
    training_data.append({"class":"Frans", "sentence":"Ceci est une phrase aleatoire pour apprendre au systeme"})
    training_data.append({"class":"Frans", "sentence":"Mon hbby prefere est apprendre des languages"})
    training_data.append({"class":"Frans", "sentence":"J'espere que tu vas bien!"})
    training_data.append({"class":"Frans", "sentence":"J'aime bien parler avec toi."})
    training_data.append({"class":"Frans", "sentence":"Veux tu ecrire comment se passe ta journee"})
    return training_data
