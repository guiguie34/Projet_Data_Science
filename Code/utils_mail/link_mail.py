import json
import re
from .meta_mail import meta_mail, dic_mail


def clean_subject_regex(subject):
    mailREGEX = "(Re|RE|FW) *([:] *)| *$"
    return re.sub(mailREGEX, "", subject)


def get_link_mails(df):
    subject_mail = {}
    #for i in range(200, 300):

    #subject = df["Subject"][i]
    clean_subject = clean_subject_regex("Re: Western Wholesale Activities - Gas & Power Conf. Call")
    if (clean_subject != "NoData" and clean_subject != "") and clean_subject not in subject_mail:
        relatedmail = get_all_mails_by_subject(df, clean_subject)  # Mails qui appartiennent aux même sujets
        relatedmail2 = dispatch_mails(relatedmail)  # Mails sous forme de conversations
        #relatedmail2 = sorted(relatedmail2, key=lambda k: k['Date'])
        subject_mail[clean_subject] = relatedmail2
    print(subject_mail)

    return subject_mail


def get_all_mails_by_subject(df, subject):
    mails = []
    for i in range(0, len(df.index)):

        if subject in df['Subject'][i]:
            new_subject = clean_subject_regex(df['Subject'][i])

            if new_subject in subject:
                tmp = {}
                tmp["id"] = int(df["Unnamed: 0"][i])
                tmp["Date"] = df['Date'][i]
                tmp["From"] = df['From'][i]
                tmp["To"] = df['To'][i]
                tmp["Subject"] = df['Subject'][i]
                tmp["content"] = df['content'][i]
                # tmp['user'] = df['user'][i]
                mails.append(tmp)
    return mails


def dispatch_mails(related):
    dispatch = dic_mail()

    for i in range(0, len(related)):
        #found = False
        #j = 0
        courant = meta_mail(related[i])
        #keys = list(dispatch)
        # while (found == False) and j < len(keys):
        #     #print(dispatch,len(dispatch))
        #     #print(keys)
        #     d = keys[j]
        #     print(keys[j])
        #     if courant.appartient(d):
        #         dispatch[d].append(related[i])
        #         found = True
        #     j = j + 1

        # print(related[i])
        # print(courant, dispatch, courant in dispatch)
        sim = dispatch.sim(courant)
        if sim is not None:
            tmp = dispatch[sim]
            dispatch.pop(sim,None)
            for receiver in courant.toList:
                if receiver not in sim:
                    sim += receiver

            dispatch[sim]= tmp

            dispatch[sim] += [related[i]]
        else:
            dispatch[courant.__str__()] = [related[i]]

    for k,v in dispatch.items():
        dispatch[k] = sorted(dispatch[k], key=lambda j: j['Date'])
    return dispatch


def concatenate_mail(tab):
    content_mails = ""
    for i in range(0,len(tab)):
        content_mails += tab[i].get("content")
    return content_mails


