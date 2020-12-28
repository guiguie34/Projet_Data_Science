import json
from nltk.corpus import wordnet as wn  # Import wordnet from the NLTK
from nltk.corpus import stopwords


def get_general_words():
    general_words = {}
    jsonfile = open('../Generated Data/data_content.json', 'r')
    data = json.load(jsonfile)
    for i in range(len(data) - 20, len(data) - 820, -1):
        # regarder s'il se trouve dans les synonyme existant
        # regarder si ses synonymes le sont
        # taux de corrélation
        # ajout sinon

        # similarité clé > 0.? -> ajoute dans les données du mot
        added = False
        if (len(wn.synsets(data[i][0])) != 0):
            current_word = wn.synsets(data[i][0])[0]
            for key, value in general_words.items():

                if key.wup_similarity(current_word) is not None and key.wup_similarity(current_word) > 0.6:
                    general_words[key] += [data[i][0]]
                    added = True
            if (not added):
                general_words[current_word] = []
    print((general_words))
    print(len(general_words))

    # sinon clé -> ajoute synonyme

    # check les hypernyms

def get_mail_themes(discussion):
    #discussion = fil de toutes les discussion
    #Pour chaque fil, regarder la similarité de cahque mot apres fitrage avec la liste créee.
    # a la fin, regarder les 3 thèmes qui ressortent et les stocker

    return discussion

