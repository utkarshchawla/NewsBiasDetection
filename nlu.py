import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions
from pymongo import MongoClient
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
from stop_words import get_stop_words
en_stop = get_stop_words('en')
from nltk.stem.porter import PorterStemmer
import codecs

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='qWULvgI_e7tkQ6Aj_GDq--nAhasrZhA1y-WbDvXo-Mwb',
    url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
)

outfile = open('/Users/nishtha/PycharmProjects/Legal_text/keywords_opinion.txt','w+')

client = MongoClient('mongodb://reader:reader123@portal-ssl603-47.bmix-dal-yp-07d69ae5-71bd-4094-a024-206b3ab2b3da.250607799.composedb.com:18578,portal-ssl581-45.bmix-dal-yp-07d69ae5-71bd-4094-a024-206b3ab2b3da.250607799.composedb.com:18578/compose?authSource=legal&ssl=true')
db=client.legal
collection=db['Arkansas']

texts = {}

for content in collection.find():
    #data = content['casebody']['data']['head_matter']
    if content['id'] < int("609268"):
        continue
    print content['id']
    # print content['casebody']
    # print content['casebody']['data']

    print content['casebody']['data']['opinions']

  #  print content['casebody']['data']['opinions'][0]

   # print len(content['casebody']['data']['opinions'][0]['text'])

    if len(content['casebody']['data']['opinions']) > 0:
        data = content['casebody']['data']['opinions'][0]['text']

        texts[content['id']] = data
        keylist = []
        # response = natural_language_understanding.analyze(
        #     text=data,
        #     features=Features(keywords=KeywordsOptions(emotion=False, sentiment=False, limit=2)).get_result())
        try:
            response = natural_language_understanding.analyze(
                text=data,
                features=Features(keywords=KeywordsOptions(sentiment=False, emotion=False, limit=2))).get_result()

            #print(json.dumps(response, indent=2))

            for keyword in response["keywords"]:
                keytext = keyword['text']
                keylist.append(keytext)
                #print keytext
          #  print str(content['id'])+" SEP "+str(keylist[0])
          #  keylist[0] = re.sub(r'[^\x00-\x7F]+', ' ', keylist[0])
            keylist[0] = ''.join([i if ord(i) < 128 else ' ' for i in keylist[0]])
            print str(keylist[0])
            outfile.write(str(content['id'])+',')
            outfile.write(str(keylist[0])+'\n')
        except:
            pass

outfile.close()
