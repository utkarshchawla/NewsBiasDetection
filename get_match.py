import datetime


# logic to match every DD news article with a corresponding source article.
def get_match(dd_title, dd_date, source):
    hi = 0  # variable to keep track of the maximum number of matches.
    return_link = None  # variable used to return the link.

    # remove all non alphanumeric characters from the title.
    translationtable = str.maketrans("", "", "!@#$%^&*()-_+=|/<>.`~,:\"")
    # change the title to lowercase and convert it to a list by splittin across " ".
    dd_title = dd_title.translate(translationtable).lower().split(" ")

    # calculate the prev and the next dates.
    prev_date = (datetime.datetime.strptime(dd_date, '%d-%m-%Y') - datetime.timedelta(1)).strftime('%d-%m-%Y')
    next_date = (datetime.datetime.strptime(dd_date, '%d-%m-%Y') + datetime.timedelta(1)).strftime('%d-%m-%Y')

    for date in [dd_date, next_date, prev_date]:
        article_list = source[date]  # get the list of source articles for the corresponding date "d".
        for tup in article_list:
            count = 0
            article_title = tup[0]
            article_link = tup[1]
            article_title = article_title.translate(translationtable).lower().split(" ")
            # do a keyword matching between title of the DD article and that of the NDTV article.
            for word in dd_title:
                if len(word) < 4:
                    continue  # ignore words of len < 4
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
