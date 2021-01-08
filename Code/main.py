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
from Code.utils_mail.get_themes import get_discussion_themes
from Code.utils_mail import utils






if __name__ == '__main__':
    #
    df = utils.get_df_from_csv()
    # processing_mail.get_words_content(df)
    # print("Content done")
    # df.to_csv("../Sources/data_clean.csv", index=False)
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('universal_tagset')
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


    # a_file = open("../Generated Data/link_mail6.json", "w")
    # json.dump(link_mail.get_link_mails(df), a_file, indent=4,sort_keys=True)
    # a_file.close()

    with open("../Generated Data/link_mail1.json") as a:
        data1 = json.loads(a.read())
        with open("../Generated Data/link_mail2.json") as b:
            data2 = json.loads(b.read())
            with open("../Generated Data/link_mail3.json") as c:
                data3 = json.loads(c.read())
                with open("../Generated Data/link_mail4.json") as d:
                    data4 = json.loads(d.read())
                    with open("../Generated Data/link_mail5.json") as e:
                        data5 = json.loads(e.read())
                        with open("../Generated Data/link_mail6.json") as f:
                            data6 = json.loads(f.read())

                            anova_file = open("../Generated Data/dataForAnova.json", "w")
                            merged = {**data1, **data2,**data3,**data4,**data5,**data6}
                            get_discussion_themes(merged)
                            #json.dump(get_discussion_themes(merged),anova_file,indent=4,sort_keys=True)
                            #anova_file.close()

    # def clean_nones(value):
    #     """
    #     Recursively remove all None values from dictionaries and lists, and returns
    #     the result as a new dictionary or list.
    #     """
    #     if isinstance(value, list):
    #         return [clean_nones(x) for x in value if x]
    #     elif isinstance(value, dict):
    #         return {
    #             key: clean_nones(val)
    #             for key, val in value.items()
    #             if val
    #         }
    #     else:
    #         return value
    #
    # with open("../Generated Data/dataForAnova3.json") as a:
    #     data1 = json.loads(a.read())
    #     data1= clean_nones(data1)
    #     anova_file = open("../Generated Data/dataForAnova4.json", "w")
    #     json.dump(data1,anova_file,indent=4,sort_keys=True)

    # with open("../Generated Data/dataForAnova4.json") as a:
    #     data1 = json.loads(a.read())
    #     empty_keys = [k for k, v in data1.items() if not v]
    #     for k in empty_keys:
    #         del data1[k]
    #     anova_file = open("../Generated Data/dataForAnova5.json", "w")
    #     json.dump(data1,anova_file,indent=4,sort_keys=True)

    # with open("../Generated Data/link_mail1.json") as f:
    #     data = json.loads(f.read())
    #     anova_file = open("../Generated Data/dataForAnova.json", "w")
    #     json.dump(get_discussion_themes(data),anova_file,indent=4,sort_keys=True);

    #print(link_mail.get_link_mails(df))

    # first_word = wordnet.synset("Travel.v.01")
    # second_word = wordnet.synset("Walk.v.01")
    # print('Similarity: ' + str(first_word.wup_similarity(second_word)))
    # first_word = wordnet.synset("Power.n.01")
    # second_word = wordnet.synset("Energy.n.01")
    # print('Similarity: ' + str(first_word.wup_similarity(second_word)))

    #get_themes.get_mail_themes("During the American Revolution, George Washington worked to contain a smallpox epidemic by isolating anyone suspected of infection and limiting outside contact with his army. In 1776, when the British withdrew from Boston, Washington mandated that only soldiers that had already been infected be allowed into the city.")


