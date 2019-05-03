import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def makeWordCloud_Centrality(src_centrality_dict):
    word_cloud_dict = { key: (src_centrality_dict[key]*100 + 2) for key in src_centrality_dict.keys() }
    wordcloud_src = WordCloud(max_words=500, background_color="white",height = 500,width = 500,scale=5,relative_scaling=0.5,min_font_size=1,prefer_horizontal=1).generate_from_frequencies(word_cloud_dict)
    plt.imshow(wordcloud_src, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    new_filename = 'word_cloud_cent_sample.png'
    wordcloud_src.to_file(new_filename)

 if __name__ == "__main__":
 	sample_dict = {'central election committee': 0.35555555555555557, 'parliamentary constituencies': 0.2962962962962963, 'Lok Sabha elections': 0.2222222222222222, 'BJP candidates': 0.4444444444444444, 'BJP': 0, 'candidates': 0.19753086419753085, 'list': 0.14814814814814814, 'Odisha assembly constituency': 0.14814814814814814, 'Minister Narendra Modi': 0.1111111111111111, 'meet': 0.1111111111111111}
 	makeWordCloud_centrality(sample_dict)