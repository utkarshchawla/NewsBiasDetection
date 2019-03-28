import datetime
from num2words import num2words
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


# logic to match every DD news article with a corresponding source article.
def get_match(dd_title, dd_date, source):
    hi = 0  # variable to keep track of the maximum number of matches.
    return_link = None  # variable used to return the link.

    # remove all non alphanumeric characters from the title.
    # translationtable = str.maketrans("", "", "!@#$%^&*()-_+=|/<>.`~,:\"")
    # change the title to lowercase and convert it to a list by splittin across " ".
    # dd_title = dd_title.translate(translationtable).lower().split(" ")
    dd_title = text_processing(dd_title)

    # calculate the prev and the next dates.
    prev_date = (datetime.datetime.strptime(dd_date, '%d-%m-%Y') - datetime.timedelta(1)).strftime('%d-%m-%Y')
    next_date = (datetime.datetime.strptime(dd_date, '%d-%m-%Y') + datetime.timedelta(1)).strftime('%d-%m-%Y')

    for date in [dd_date, next_date, prev_date]:
        article_list = source[date]  # get the list of source articles for the corresponding date "d".
        for tup in article_list:
            count = 0
            article_title = tup[0]
            article_link = tup[1]
            # article_title = article_title.translate(translationtable).lower().split(" ")
            article_title = text_processing(article_title)
            # do a keyword matching between title of the DD article and that of the NDTV article.
            for word in dd_title:
                # if len(word) < 4:
                #     continue  # ignore words of len < 4
                if word in article_title:
                    count += 1
            if count > hi:
                hi = count
                return_link = article_link
    # Return link if the number of keywords matched is greater than two, else return None.
    if hi > 2:
        return return_link
    else:
        return None


def text_processing(input_str):
    translationtable = str.maketrans("", "", "!@#$%^&*()-_+=|/<>.`~,:\"")
    input_str = input_str.translate(translationtable).lower().strip()
    input_str = re.sub("(\d+)", lambda x: num2words(int(x.group(0))), input_str)
    input_str = word_tokenize(input_str)
    rl = []
    for word in input_str:
        lem_word = lemmatizer.lemmatize(word)
        if lem_word not in stop_words:
            rl.append(lem_word)

    return rl
