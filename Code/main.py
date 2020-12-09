import string
import pandas
import operator
import json
import csv
import sys
from datetime import datetime
import re

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


def nb_occ(message, occurrences):
    message = message.split(' ')
    for c in message:
        occurrences[c] = occurrences.get(c, 0) + 1

    return occurrences


def get_words_content(df):
    index = df.index
    number_of_rows = len(index)
    occurrences = {}
    for i in range(0, number_of_rows):
        courant = df['content'][i]
        courant = modification_texte(courant)
        occurrences = nb_occ(courant, occurrences)
        print(i)
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
        courant = modification_texte(courant)
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


def get_all_mails(df, subject):
    mails = []
    mailREGEX = "(Re|RE|FW) *([:] *)| *$"
    for i in range(0, len(df.index)):

        if (subject in df['Subject'][i]):
            newSubject = re.sub(mailREGEX, "", df['Subject'][i])
            print(df['Subject'][i], " ", newSubject)
            if (newSubject in subject ):
                tmp = {}
                tmp['Date'] = df['Date'][i]
                tmp['From'] = df['From'][i]
                tmp['To'] = df['To'][i]
                tmp['Subject'] = df['Subject'][i]
                tmp['content'] = df['content'][i]
                tmp['user'] = df['user'][i]
                mails.append(tmp)
    return mails


# TODO Objet --> Calculer le temps de réponse par rapport aux mails récupérés
# TODO Thématique --> Déterminier une thématique par rapport aux mots présent dans le mails (enlever stop words)
# TODO FilterData --> Trouver les mails avec des réponses que l'on peut exploiter

if __name__ == '__main__':
    data = pandas.read_csv("../Sources/data_clean.csv", sep=',', low_memory=False)
    # data.fillna("NoData", inplace=True)  # Replace the null value by a string "NoData"
    df = pandas.DataFrame(data)
    # df.to_csv("../Sources/data_clean.csv", index=False)
    # get_words_subject(df)

    df = df.drop_duplicates(subset=["Date", "From", "To", "content"], keep="last", ignore_index=True)

    mails = get_all_mails(df, "California Update 5/4/01")
    for i in range(0, len(mails)):
        mails[i]['Date'] = int(datetime.fromisoformat(mails[i]["Date"]).timestamp())
    mails = sorted(mails, key=lambda i: i['Date'])

    for i in range(0, len(mails)):
        print(mails[i])
