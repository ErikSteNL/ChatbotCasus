from bi.Chat import chat as biChat
from tri.Chat import chat as triChat
from googletrans import Translator
translator = Translator()

zinnen = [
    ("Nederlands", "Hallo mijn naam is bob en ik vindt het leuk"),
    ("Nederlands", "Sjors en Harold hebben bijna iedereen op school in de maling genomen"),
    ("Nederlands", "Dus beveilig jouw boek altijd met een slot"),
    ("Nederlands", "De tandarts vult mijn kies. Dat doet geen pijn. Hij geeft mij eerst een verdoving."),
    ("Nederlands", "Morgen is papa jarig. Ik hang slingers op. Dit vinden wij ook."),
    ("Nederlands", "Ik sta vroeg op. De zon schijnt. Ik maak een lange wandeling."),
    ("Nederlands", "Kijk uit! Blijf op de stoep staan! Op straat is het gevaarlijk."),
    ("Nederlands", "Wij vieren feest. Ik eet een stukje taart. Het smaakt goed."),
    ("Nederlands", "Mijn vriendje gaat verhuizen. Morgen gaan ze weg. Ik ben heel blij."),
    ("Nederlands", "Stan zit op zwemles."),
    ("Nederlands", "Jesse en Joeri ook."),
    ("Nederlands", "Ze staan aan de rand van het zwembad."),
    ("Nederlands", "Ze wachten op badmeester Koen."),
    ("Nederlands", "Als Koen er is, gaan ze beginnen."),
    ("Nederlands", "Ze springen in het diepe bad."),
    ("Nederlands", "Eerst moet Stan op zijn buik zwemmen."),
    ("Nederlands", "Dat kan hij al goed."),
    ("Nederlands", "Maar op zijn rug lukt het nog niet."),
    ("Nederlands", "Dat moet hij nog leren."),
    ("Nederlands", "Werkt de bot of klopt er helemaal niks van?"),
    ("Engels", "Hello my name is Bob and I like it"),
    ("Engels", "Sjors and Harold have almost scratched everyone at school"),
    ("Engels", "Always keep your book safe with a lock"),
    ("Engels", "The dentist fills my choice. It does not hurt, he first gives me an anesthesia."),
    ("Engels", "Tomorrow is Daddy's birthday. I hang up slingers. We also think so."),
    ("Engels", "I get up early, the sun shines. I'm making a long walk."),
    ("Engels", "Schau hinaus! Stay on the sidewalk! On the street it's dangerous."),
    ("Engels", "We celebrate party. I eat a piece of cake. It tastes good."),
    ("Engels", "My boyfriend is moving away. Tomorrow they leave. I'm very happy."),
    ("Engels", "Stan is on a swim lesson."),
    ("Engels", "Jesse and Joeri too."),
    ("Engels", "They are at the edge of the pool."),
    ("Engels", "They are waiting for Koen's lifeguard."),
    ("Engels", "If Koen is there, they'll start."),
    ("Engels", "They jump into the deep bath."),
    ("Engels", "First, Stan has to swim on his belly."),
    ("Engels", "He's already fine."),
    ("Engels", "But on his back, it's not possible yet."),
    ("Engels", "That's what he has to learn."),
    ("Engels", "Does the bone work or does not matter?"),
    ("Duits", "Hallo mein Name ist Bob und ich mag es"),
    ("Duits", "Sjors und Harold haben fast alle in der Schule verkratzt"),
    ("Duits", "Halten Sie Ihr Buch immer mit einem Schloss sicher"),
    ("Duits", "Der Zahnarzt fullt meine Wahl. Das tut nicht weh. Er gibt mir zuerst ein Betaubungsmittel."),
    ("Duits", "Morgen ist Geburtstag Papa. Ich hange Girlanden auf. Das ist, was wir finden."),
    ("Duits", "Ich stehe fruh auf, die Sonne scheint, ich mache einen langen Spaziergang."),
    ("Duits", "Watch out! Auf dem Burgersteig bleiben! Die Strassen sind gefahrlich."),
    ("Duits", "Wir feiern eine Party, ich esse ein Stuck Kuchen, es schmeckt gut."),
    ("Duits", "Mein Freund ist weg, morgen gehen sie, ich bin sehr glucklich."),
    ("Duits", "Stan ist eine Schwimmstunde"),
    ("Duits", "Jesse und Joeri auch."),
    ("Duits", "Sie sind am Rand des Pools."),
    ("Duits", "Sie warten auf Koens Rettungsschwimmer"),
    ("Duits", "Wenn Koen da ist, werden sie anfangen."),
    ("Duits", "Sie springen ins tiefe Bad."),
    ("Duits", "Erstens, Stan muss auf seinem Bauch schwimmen."),
    ("Duits", "Er ist schon in Ordnung."),
    ("Duits", "Aber auf dem Rucken ist es noch nicht moglich."),
    ("Duits", "Das muss er lernen"),
    ("Duits", "Arbeitet der Knochen oder spielt es keine Rolle?"),
    ("Frans", "Bonjour mon nom est Bob et je l'aime"),
    ("Frans", "Sjors et Harold ont presque egratigne tout le monde a l'ecole"),
    ("Frans", "Gardez toujours votre livre en securite avec une serrure"),
    ("Frans", "Le dentiste remplit mon choix, ca ne fait pas mal, il me fait d'abord une anesthesie."),
    ("Frans", "Demain c'est l'anniversaire de papa, je raccroche les frondeurs, nous le pensons aussi."),
    ("Frans", "Je me leve tot, le soleil brille, je fais une longue marche."),
    ("Frans", "Attention, restez sur le trottoir! Dans la rue c'est dangereux."),
    ("Frans", "Nous celebrons la fete, je mange un morceau de gateau, c'est bon."),
    ("Frans", "Mon copain s'eloigne, demain ils partent, je suis tres heureux."),
    ("Frans", "Stan est sur une lecon de natation."),
    ("Frans", "Jesse et Joeri aussi"),
    ("Frans", "Ils sont au bord de la piscine."),
    ("Frans", "Ils attendent le maitre nageur de."),
    ("Frans", "Si est la, ils vont commencer."),
    ("Frans", "Ils sautent dans le bain profond."),
    ("Frans", "Premierement, Stan doit nager sur son ventre."),
    ("Frans", "Il va deja bien."),
    ("Frans", "Mais sur son dos, ce n'est pas encore possible."),
    ("Frans", "C'est ce qu'il doit apprendre."),
    ("Frans", "Est-ce que l'os fonctionne ou n'a pas d'importance?"),
    ("Zweeds", "Hej jag heter Bob och jag gillar det"),
    ("Zweeds", "Sjors och Harold har hastan sett alla pa skolan"),
    ("Zweeds", "Hall alltid din bok saker med ett las"),
    ("Zweeds", "Tandlakaren fyller mitt val, vilket inte gor ont. Han ger mig forst en anestesi."),
    ("Zweeds", "Imorgon ar pappas fodelsedag. Jag hanger upp slingrar. Vi tror ocksa det."),
    ("Zweeds", "Jag star upp tidigt, solen skiner. Jag gar lang promenad."),
    ("Zweeds", "Se upp! Stanna pa trottoaren! Pa gatan ar det farligt."),
    ("Zweeds", "Vi firar fest. Jag ater en bit tarta. Det smakar gott."),
    ("Zweeds", "Min pojkvan flytta sig bort. I morgon lamnar de. Jag ar valdigt glad."),
    ("Zweeds", "Stan ar pa en leksak."),
    ("Zweeds", "Jesse och Joeri"),
    ("Zweeds", "de ar vid kanten av poolen."),
    ("Zweeds", "de vantar pa Koen livraddare"),
    ("Zweeds", "Om Koen ar dar borjar de."),
    ("Zweeds", "de hoppar i djupbadet."),
    ("Zweeds", "Forst maste Stan simma pa magen."),
    ("Zweeds", "han kan redan gora det."),
    ("Zweeds", "men pa ryggen ar det inte mojligt an."),
    ("Zweeds", "han maste lara sig det."),
    ("Zweeds", "Fungerar benet eller spelar ingen roll?"),
    ("Italiaans", "ciao il mio nome e Bob e mi piace"),
    ("Italiaans", "Sjors e Harold hanno quasi visto tutti a scuola"),
    ("Italiaans", "mantieni sempre il tuo libro con una serratura"),
    ("Italiaans", "il dentista riempie la mia scelta, che non fa male, prima mi da un'anestesia")
    ("Italiaans", "domani e il compleanno di papa, ho chiuso gli slingers e pensiamo cosi.")
    ("Italiaans", "mi alzo presto, il sole splende, sto facendo una lunga passeggiata")
    ("Italiaans", "guarda, stai sul marciapiede, per strada e pericoloso")
    ("Italiaans", "festeggiamo la festa, mangio un pezzo di torta, ha sapore buono"),
    ("Italiaans", "Il mio ragazzo si allontana, domani se ne vanno, sono molto felice")
    ("Italiaans", "Stan e in una lezione di nuoto"),
    ("Italiaans", "anche Jesse e Joeri"),
    ("Italiaans", "sono ai bordi della piscina"),
    ("Italiaans", "stanno aspettando il bagnino di Koen"),
    ("Italiaans", "se Koen e li, partiranno"),
    ("Italiaans", "saltano nel bagno profondo"),
    ("Italiaans", "prima, Stan deve nuotare sullo stomaco")
    ("Italiaans", "puo gia farlo"),
    ("Italiaans", "ma sulla schiena non e ancora possibile")
    ("Italiaans", "deve imparare"),
    ("Italiaans", "funziona o non importa?")
]

lenzin = len(zinnen)

totalBi = 0
failBi = 0
totalTri = 0
failTri = 0
totalGoogle = 0
failGoogle = 0

for zin in zinnen:
    print("_"*40)
    print("Bi-gram")
    biData = biChat(zin[1])
    if biData[0] == zin[0]:
        totalBi += biData[1]
    else:
        failBi += 1
    print("\nTri-gram")
    triData = triChat(zin[1])
    if triData[0] == zin[0]:
        totalTri += triData[1]
    else:
        failTri += 1
    print("\nGoogle Translate")
    print(zin[1])
    info = translator.detect(zin[1])
    print("Taal: %s" % info.lang)
    print("Zekerheid: %s" % info.confidence)
    if zin[0] == "Nederlands":
        langCode = "nl"
    elif zin[0] == "Duits":
        langCode = "de"
    elif zin[0] == "Engels":
        langCode = "en"
    elif zin[0] == "Frans":
        langCode = "fr"
    if info.lang == langCode:
        totalGoogle += info.confidence
    else:
        failGoogle += 1

print("#"*40)
print("Aantal zinnen: %s" % lenzin)
print("Total Bi-gram coverage: %.0f%% \tFails: %s/%s" % ((100*(totalBi/lenzin),failBi,lenzin)))
print("Total Tri-gram coverage: %.0f%% \tFails: %s/%s" % ((100*(totalTri/lenzin),failTri,lenzin)))
print("Total Google coverage: %.0f%% \tFails: %s/%s" % ((100*(totalGoogle/lenzin),failGoogle,lenzin)))
