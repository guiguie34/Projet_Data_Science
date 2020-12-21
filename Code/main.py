import string

import nltk
import pandas
import operator
import json
import csv
import sys
from datetime import datetime
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet  # Import wordnet from the NLTK
from Code.utils_mail import link_mail

nltk.download('wordnet')

'''maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
'''


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
    stop_words = stopwords.words('english') + [",", ";", ":", ".", "?", "!", "«", "»", "(", ")", "\"", "…", "'", "-", "’","--","<",">",]
    tokenizer = nltk.RegexpTokenizer(r"\w+") #regexp des ponctuations
    message_split = tokenizer.tokenize(message) # Separe le message en tableau de message sans les pontcuations
    #message_split = nltk.word_tokenize(message)
    stemming = PorterStemmer()
    stemmed_list = [stemming.stem(word) for word in message_split] #rassamble les mots qui sont similaire
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
        #print(i)
    occurrences_sorted = sorted(occurrences.items(), key=operator.itemgetter(1))
    print(occurrences_sorted)

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
        print(i)
    occurrences_sorted = sorted(occurrences.items(), key=operator.itemgetter(1))
    print(occurrences_sorted)

    a_file = open("../Generated Data/data_subject.json", "w")
    json.dump(occurrences_sorted, a_file)
    a_file.close()


def csv_to_json(data):
    jsonfile = open('../Generated Data/data.json', 'w')
    reader = csv.reader(data)
    fieldnames = []
    for row in reader:
        fieldnames.append(row[0])
    fieldnames = fieldnames[0:15]
    csvfile = open('../Sources/data.csv', 'r')
    reader2 = csv.DictReader(csvfile, fieldnames)
    next(reader2)
    next(reader2)

    for row in reader2:
        # print(row)
        json.dump(row, jsonfile)
        jsonfile.write('\n')





# TODO Objet --> Calculer le temps de réponse par rapport aux mails récupérés
# TODO Thématique --> Déterminier une thématique par rapport aux mots présent dans le mails (enlever stop words)
# TODO FilterData --> Trouver les mails avec des réponses que l'on peut exploiter

if __name__ == '__main__':
    data = pandas.read_csv("../Sources/data_clean.csv", sep=',', low_memory=False)
    # data.fillna("NoData", inplace=True)  # Replace the null value by a string "NoData"
    df = pandas.DataFrame(data)
    # df.to_csv("../Sources/data_clean.csv", index=False)
    #nltk.download('stopwords')
    #nltk.download('punkt')
    #print(modification_ntlk("Nick frightened, likes, to > frightens play football, <however -- he - is : / not too frightening fond of tennis."))
    #get_words_subject(df)
    #stop_words = stopwords.words('english') + [",", ";", ":", ".", "?", "!", "«", "»", "(", ")", "\"", "…", "'", "-", "’"]
    #get_words_content(df)

    df = df.drop_duplicates(subset=["Date", "From", "To", "content"], keep="first", ignore_index=True)

    # mails = link_mail.get_all_mails(df, "test")
    # for i in range(0, len(mails)):
    #     mails[i]['Date'] = int(datetime.fromisoformat(mails[i]["Date"]).timestamp())
    # mails = sorted(mails, key=lambda i: i['Date'])
    # regexp = "frozenset\({|(}\))"
    #
    # for i in range(0, len(mails)):
    #     print(re.sub(regexp, "", mails[i]["To"]))
    #
    for k,v in link_mail.get_link_mails(df).items():
        print(k)
        for t in v:
            print("\t",t)

    #print(link_mail.get_link_mails(df))

    #first_word = wordnet.synset("Travel.v.01")
    #second_word = wordnet.synset("Walk.v.01")
    #print('Similarity: ' + str(first_word.wup_similarity(second_word)))
    #first_word = wordnet.synset("Power.n.01")
    #second_word = wordnet.synset("Energy.n.01")
    #print('Similarity: ' + str(first_word.wup_similarity(second_word)))