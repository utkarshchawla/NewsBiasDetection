import pygal
import cairosvg
from pygal.style import Style

def create_sentiment_missing_plot(trusted_src_dict):
    custom_style = Style(label_font_size = 14, major_label_font_size=14,value_font_size=14,value_label_font_size=14, colors=('#5C52CD','#5C52CD'))
    line_chart = pygal.Bar(style=custom_style)
    
    for key in trusted_src_dict.keys():
        line_chart.add(key,trusted_src_dict[key])
    line_chart.render_to_png('./egg.png')

if __name__=="__main__":
	#pass trusted_src_sentiment_np dict
	sample_dict = {'reaction': 0.0, 'Congress': -0.5720998333333334, 'bluff': -0.6205890000000001, 'team': 0.864898, 'Rs': -0.784545, 'opposition alliance': -0.87991, 'Congress slogan': -0.5720998333333334, 'minister Indira Gandhi': -0.16101150000000003, 'attacks': -0.939998, 'seats': -0.4246145, 'Twitter': 0.0, 'chief Rahul Gandhi': -0.1288092, 'Mayawati': -0.714007, 'Garibi Hatao': -0.4963905, 'Akhilesh Yadav': -0.7935106666666667, 'rival Akhilesh Yadav': -0.7935106666666667}
	create_sentiment_missing_plot(ample_dict)