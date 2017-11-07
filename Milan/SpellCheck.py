import enchant
from enchant.checker import SpellChecker

while True:
    input_sentence = raw_input("Sentence:\n")
    #a = "This is some sample txt with errors"
    chkr = enchant.checker.SpellChecker("en_US")
    chkr.set_text(input_sentence)
    for err in chkr:
        print("Word: %s -> %s" % (err.word,err.suggest()))
        sug = err.suggest()[0]
        err.replace(sug)
    fixed = chkr.get_text() #returns corrected text
    print ("Fixed: %s" % fixed)
