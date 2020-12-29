import string
import nltk
import operator
import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
from nltk.corpus import wordnet as wn  # Import wordnet from the NLTK
from nltk.stem import WordNetLemmatizer

global pos
pos = ["A", "V", "N"]

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
    message = message.lower()
    # stop_words = stopwords.words('english') + [",", ";", ":", ".", "?", "!", "«", "»", "(", ")", "\"", "…", "'", "-",
    #                                            "’", "--", "<", ">","@","=","]","cc","&","$","''" ]
    # tokenizer = nltk.RegexpTokenizer(r"\w+")  # regexp des ponctuations
    # message_split = tokenizer.tokenize(message)  # Separe le message en tableau de message sans les pontcuations
    # # message_split = nltk.word_tokenize(message)
    # stemming = PorterStemmer()
    # stemmed_list = [stemming.stem(word) for word in message_split]  # rassamble les mots qui sont similaire
    # meaningful_words = [w for w in stemmed_list if not w.lower() in stop_words]

    message=lemmatize_word(message)

    # topopOut=[]
    # for i in range(0,len(meaningful_words)):
    #     if re.match("[0-9]", meaningful_words[i]) is not None:
    #         topopOut.append(meaningful_words[i])
    # for i in range(0,len(topopOut)):
    #     meaningful_words.remove(topopOut[i])

    return message

def lemmatize_word(sentence):
    new_sentence = nltk.pos_tag(nltk.word_tokenize(sentence), tagset='universal')
    final_sentence =[]
    for i in range(0,len(new_sentence)):
        first_char_in_pos = new_sentence[i][1][0]
        if first_char_in_pos in pos:
            word =new_sentence[i][0]
            if len(wn.synsets(word, pos=first_char_in_pos.lower()))!=0:
                final_sentence.append(wn.synsets(word, pos=first_char_in_pos.lower())[0])
    return final_sentence

def nb_occ(message, occurrences):
    for c in message:
        synset = c.name().split('.')
        word, position = synset[0],synset[1]
        if occurrences.get(word, 0) != 0:
            if position in occurrences.get(word, 0)[0] :
                occurrences.get(word,0)[1] += 1
            else:
                occurrences[word] = [position, 1]
        else:
            occurrences[word] = [position, 1]

    return occurrences


def get_words_content(df):
    index = df.index
    number_of_rows = len(index)
    occurrences = {}
    for i in range(0, number_of_rows):
        courant = df['content'][i]
        courant = modification_ntlk(courant)
        occurrences = nb_occ(courant, occurrences)

    occurrences_sorted = sorted(occurrences.items(), key = lambda item : item[1][1])
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

def test_order():
    dico = {'test':['n',4],'eat':['v',18],'eatable':['a',38],'adopted':['a',2],'adopt':['v',22]}
    dico = sorted(dico.items(), key = lambda item : item[1][1])
    print(dico)