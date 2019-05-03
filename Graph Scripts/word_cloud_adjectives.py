import matplotlib.pyplot as plt
from wordcloud import WordCloud

def makeWordCloud_adjectives(text):
	filename = './sample_cloud.png'
    wc = WordCloud(background_color="white", max_words=1000)
    # generate word cloud
    wc.generate_from_frequencies(text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    #save to file
    #wc.to_file(new_filename)

 if __name__ == "__main__":
 	sample_dict = {'central': 2, 'national': 1, 'bjp': 1, 'prime': 1, 'senior': 1, 'meet': 1, 'ninth': 2, 'parliamentary': 1, 'fourth': 1}
 	makeWordCloud_adjectives(sample_dict)