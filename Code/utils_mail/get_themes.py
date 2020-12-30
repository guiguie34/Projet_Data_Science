import json
from nltk.corpus import wordnet as wn  # Import wordnet from the NLTK
from nltk.corpus import stopwords
from Code.utils_mail import processing_mail
import numpy as np
import operator

global themes
jsonfile = open('../Generated Data/data_themes.json', 'r')
themes = json.load(jsonfile)

def get_general_words():
    general_words = {}
    jsonfile = open('../Generated Data/data_content.json', 'r')
    data = json.load(jsonfile)
    for i in range(len(data)-1, 0, -1):
        # regarder s'il se trouve dans les synonyme existant
        # regarder si ses synonymes le sont
        # taux de corrélation
        # ajout sinon

        # similarité clé > 0.? -> ajoute dans les données du mot
        added = False
        word = data[i][0]
        position = data[i][1][0]
        if position in processing_mail.pos:
            if len(wn.synsets(word, pos=position)) != 0:
                current_word = wn.synsets(word,pos=position)[0]
                #current_word = data[i][0]
                for key, value in general_words.items():
                    if len(wn.synsets(key,pos=general_words.get(key,0)[0])) != 0 :
                        if wn.synsets(key)[0].wup_similarity(current_word) is not None and wn.synsets(key)[0].wup_similarity(current_word) > 0.6:
                            general_words.get(key,0)[1] += [word]
                            added = True
                if (not added):
                    general_words[word] = [position,[]]
    a_file = open("../Generated Data/data_themes.json", "w")
    json.dump(general_words, a_file,indent=4)
    a_file.close()


    # sinon clé -> ajoute synonyme

    # check les hypernyms


# compteur on the words and return the 3 main themes
def get_mail_themes(discussion):


    #discussion = fil de toutes les discussion
    #Pour chaque fil, regarder la similarité de cahque mot apres fitrage avec la liste créee.
    # a la fin, regarder les 3 thèmes qui ressortent et les stocker

    return discussion

# replace the text by the similar words
def get_similarity_of_text(text):

    newText = processing_mail.modification_ntlk(text)
    edited_text=[]
    for i in range (0,len(newText)):
        edited_text.append(get_similarity_of_word(newText[i]))
    print("old : ",newText)
    print("new : ",edited_text)

#return the most similar word for a specific word

def get_similarity_of_word(word):
    maxTheme = ""
    maxValue = 0
    for key,values in themes.items():
        key_synset = wn.synsets(key,pos=values[0])[0]
        key_simil = key_synset.wup_similarity(word)
        tmpSimil = []
        if key_simil!=None:
            tmpSimil.append(float(key_simil))
        for i in range(0,len(values[1])):
            synsets = wn.synsets(values[1][i])
            if len(synsets) != 0:
                newValue = wn.synsets(values[1][i])[0]
                simil_rate = newValue.wup_similarity(word)
                if simil_rate != None:
                    tmpSimil.append(float(simil_rate))
        if len(tmpSimil) != 0:
            mean = np.mean(tmpSimil)
        if mean>maxValue:
            maxValue = mean
            maxTheme = key
    return maxTheme

def testsimil():
    time=wn.synsets("Synset('thursday.n.01')")[0]
    week=wn.synsets("Synset('tuesday.n.01')")[0]
    print(time.wup_similarity(week))
    print(time.path_similarity(week))


