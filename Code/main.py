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
from Code.utils_mail import link_mail
from Code.utils_mail import processing_mail
from Code.utils_mail import get_themes
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('universal_tagset')

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
    #
    data = pandas.read_csv("../Sources/data_clean.csv", sep=',', low_memory=False)
    data.fillna("NoData", inplace=True)  # Replace the null value by a string "NoData"
    df = pandas.DataFrame(data)
    df = df.drop_duplicates(subset=["Date", "From", "To", "content"], keep="first", ignore_index=True)
    # processing_mail.get_words_content(df)
    # print("Content done")
    # df.to_csv("../Sources/data_clean.csv", index=False)
    # nltk.download('stopwords')
    # nltk.download('punkt')
    # print(modification_ntlk("Nick frightened, likes, to > frightens play football, <however -- he - is : / not too frightening fond of tennis."))
    # processing_mail.get_words_subject(df)
    # stop_words = stopwords.words('english') + [",", ";", ":", ".", "?", "!", "«", "»", "(", ")", "\"", "…", "'", "-", "’"]
    # processing_mail.get_words_content(df)


    # mails = link_mail.get_all_mails(df, "test")
    # for i in range(0, len(mails)):
    #     mails[i]['Date'] = int(datetime.fromisoformat(mails[i]["Date"]).timestamp())
    # mails = sorted(mails, key=lambda i: i['Date'])
    # regexp = "frozenset\({|(}\))"
    #
    # for i in range(0, len(mails)):
    #     print(re.sub(regexp, "", mails[i]["To"]))

    # for k, v in link_mail.get_link_mails(df).items():
    #     for k_v, v_v in v.items():
    #         print("\tFiles de discussion: ", k_v)
    #         for values in v_v:
    #             print("\t\t", values)

     #a_file = open("../Generated Data/link_mail.json", "a+")
    # json.dump(link_mail.get_link_mails(df), a_file)
     #a_file.close()


    a_file = open("../Generated Data/link_mail1.json", "w")
    json.dump(link_mail.get_link_mails(df), a_file, indent=4)
    a_file.close()

    # with open("../Generated Data/link_mail1.json") as f:
    #     data = json.loads(f.read())
    #     print(json.dumps(data, indent=4, sort_keys=True))

    #print(link_mail.get_link_mails(df))

    # first_word = wordnet.synset("Travel.v.01")
    # second_word = wordnet.synset("Walk.v.01")
    # print('Similarity: ' + str(first_word.wup_similarity(second_word)))
    # first_word = wordnet.synset("Power.n.01")
    # second_word = wordnet.synset("Energy.n.01")
    # print('Similarity: ' + str(first_word.wup_similarity(second_word)))

    #get_themes.get_general_words()


