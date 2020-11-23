
import pandas
import operator
import json


def modification_texte(message):
    ponctuation = [",", ";", ":", ".", "?", "!", "«", "»", "(", ")", "\"", "…", "'", "-", "’"]
    message2 = ""
    for c in message:
        if (c in ponctuation) or (c == "\n"):
            message2 += ""
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


if __name__ == '__main__':
    data = pandas.read_csv("../Sources/data.csv", sep=',', low_memory=False)
    data.fillna("NoData", inplace=True)  # Replace the null value by a space
    df = pandas.DataFrame(data);
    get_words_subject(df)
