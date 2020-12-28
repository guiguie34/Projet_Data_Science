import json
from nltk.corpus import wordnet as wn  # Import wordnet from the NLTK
from nltk.corpus import stopwords
from Code.utils_mail import processing_mail
import numpy as np
import operator

# jsonfile = open('../Generated Data/data_themes.json', 'r')
# data = json.load(jsonfile)


def get_general_words():
    general_words = {}
    jsonfile = open('../Generated Data/data_content.json', 'r')
    data = json.load(jsonfile)
    for i in range(len(data) - 1, len(data)-30, -1):
        # regarder s'il se trouve dans les synonyme existant
        # regarder si ses synonymes le sont
        # taux de corrélation
        # ajout sinon

        # similarité clé > 0.? -> ajoute dans les données du mot
        added = False
        if (len(wn.synsets(data[i][0])) != 0):
            current_word = wn.synsets(data[i][0])[0]
            #current_word = data[i][0]
            for key, value in general_words.items():

                if key.wup_similarity(current_word) is not None and key.wup_similarity(current_word) > 0.6:
                    general_words[key] += [data[i][0]]
                    added = True
            if (not added):
                general_words[current_word] = []
    a_file = open("../Generated Data/data_themes.json", "w")
    json.dump(general_words, a_file)
    a_file.close()
    return general_words


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

    newData = get_general_words()
    newText = processing_mail.modification_ntlk(text)
    print(newText)
    saveSentence=newText
    for i in range (0,len(newText)) :
        print(newText[i])
        newText[i] = get_similarity_of_word(newText[i],newData)
    print(saveSentence)
    print(newText)

#return the most similar word for a specific word

def get_similarity_of_word(word,Thedata):
    current_word = wn.synsets(word)[0]
    maxTheme=""
    maxValue=0
    for key,values in Thedata.items():
        tmpSimil = []
        tmpSimil.append(float(key.wup_similarity( current_word )))
        for i in range(0,len(values)):
            newValue = wn.synsets(values[i])[0]
            tmpSimil.append(float(newValue.wup_similarity(current_word)))

        mean = np.mean(tmpSimil)
        if(mean>maxValue):
            maxValue = mean
            maxTheme = (key.name()).split('.')[0]
    return maxTheme




