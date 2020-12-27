import string
import nltk
import operator
import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def modification_texte(message):
    ponctuation = [",", ";", ":", ".", "?", "!", "«", "»", "(", ")", "\"", "…", "'", "-", "’"]
    alphabet = list(string.ascii_uppercase) + list(string.ascii_lowercase) + ["'"]
    message2 = ""
    for c in message:
        if (c not in alphabet) or (c == "\n"):
            message2 += " "
        else:
            message2 += c
    return message2


def modification_ntlk(message):
    stop_words = stopwords.words('english') + [",", ";", ":", ".", "?", "!", "«", "»", "(", ")", "\"", "…", "'", "-",
                                               "’", "--", "<", ">", ]
    tokenizer = nltk.RegexpTokenizer(r"\w+")  # regexp des ponctuations
    message_split = tokenizer.tokenize(message)  # Separe le message en tableau de message sans les pontcuations
    # message_split = nltk.word_tokenize(message)
    stemming = PorterStemmer()
    stemmed_list = [stemming.stem(word) for word in message_split]  # rassamble les mots qui sont similaire
    meaningful_words = [w for w in stemmed_list if not w.lower() in stop_words]
    return meaningful_words


def nb_occ(message, occurrences):
    for c in message:
        occurrences[c] = occurrences.get(c, 0) + 1

    return occurrences


def get_words_content(df):
    index = df.index
    number_of_rows = len(index)
    occurrences = {}
    for i in range(0, number_of_rows):
        courant = df['content'][i]
        courant = modification_ntlk(courant)
        occurrences = nb_occ(courant, occurrences)

    occurrences_sorted = sorted(occurrences.items(), key=operator.itemgetter(1))
    # print(occurrences_sorted)

    a_file = open("../Generated Data/data_content.json", "w")
    json.dump(occurrences_sorted, a_file)
    a_file.close()


def get_words_subject(df):
    index = df.index
    number_of_rows = len(index)
    occurrences = {}
    for i in range(0, number_of_rows):
        courant = df['Subject'][i]
        courant = modification_ntlk(courant)
        occurrences = nb_occ(courant, occurrences)
        # print(i)
    occurrences_sorted = sorted(occurrences.items(), key=operator.itemgetter(1))
    # print(occurrences_sorted)

    a_file = open("../Generated Data/data_subject.json", "w")
    json.dump(occurrences_sorted, a_file)
    a_file.close()
