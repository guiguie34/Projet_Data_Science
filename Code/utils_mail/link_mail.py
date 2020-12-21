import re


def clean_subject_regex(subject):
    mailREGEX = "(Re|RE|FW) *([:] *)| *$"
    return re.sub(mailREGEX, "", subject)

def get_link_mails(df):
    subject_mail = {}
    for i in range (0,10):
        subject = df["Subject"][i]
        clean_subject = clean_subject_regex(subject)
        if (clean_subject != "NoData" and clean_subject != "") and clean_subject not in subject_mail:
            relatedmail = get_all_mails(df,clean_subject)
            subject_mail[clean_subject] = relatedmail
    return subject_mail

def get_all_mails(df, subject):
    mails = []
    for i in range(0, len(df.index)):

        if (subject in df['Subject'][i]):
            newSubject = clean_subject_regex(df['Subject'][i])

            if (newSubject in subject ):
                tmp = {}
                tmp['Date'] = df['Date'][i]
                tmp['From'] = df['From'][i]
                tmp['To'] = df['To'][i]
                tmp['Subject'] = df['Subject'][i]
                tmp['content'] = df['content'][i]
                tmp['user'] = df['user'][i]
                mails.append(df["Unnamed: 0"][i])
    return mails
