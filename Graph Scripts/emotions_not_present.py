import pygal
import cairosvg
from pygal.style import Style


def create_missing_emotions_chart(trusted_src_dict):
    
    keys = trusted_src_dict.keys()
    
    sadness_vals = []
    anger_vals = [] 
    joy_vals = []
    disgust_vals = []
    fear_vals = []
    
    for key in trusted_src_dict.keys():
        sadness_vals.append(trusted_src_dict[key]['sadness'])
        anger_vals.append(trusted_src_dict[key]['anger'])
        joy_vals.append(trusted_src_dict[key]['joy'])
        disgust_vals.append(trusted_src_dict[key]['disgust'])
        fear_vals.append(trusted_src_dict[key]['fear'])
    
    custom_style = Style(label_font_size = 14, major_label_font_size=14,value_font_size=14,value_label_font_size=14, colors=('#5599C8', '#E8537A', '#A854C6', '#5C52CD', '#C6549A'))
    line_chart = pygal.StackedBar(x_label_rotation=90,style=custom_style)
    line_chart.x_labels = keys
    line_chart.add('sadness', sadness_vals)
    line_chart.add('anger',  anger_vals)
    line_chart.add('joy',      joy_vals)
    line_chart.add('disgust',  disgust_vals)
    line_chart.add('fear',  fear_vals)
    line_chart.render_to_png('./example.png')

if __name__== "__main__":

	#<src>_emotion_np dictionary to be passed where src is trusted src
	sample_dict = {'parliamentary constituencies': {'sadness': 0.2136365, 'joy': 0.126812, 'fear': 0.1205415, 'disgust': 0.070205, 'anger': 0.0881405}, 'list': {'sadness': 0.340413, 'joy': 0.06362366666666668, 'fear': 0.161332, 'disgust': 0.08273433333333334, 'anger': 0.15526133333333333}, 'central election committee': {'sadness': 0.476266, 'joy': 0.020871, 'fear': 0.20968666666666666, 'disgust': 0.16958133333333336, 'anger': 0.22703533333333334}, 'candidates': {'sadness': 0.427697, 'joy': 0.03806966666666667, 'fear': 0.1906186666666667, 'disgust': 0.10397833333333334, 'anger': 0.179496}, 'Minister Narendra Modi': {'sadness': 0.24921, 'joy': 0.407144, 'fear': 0.036466, 'disgust': 0.162726, 'anger': 0.045164}, 'meet': {'sadness': 0.24921, 'joy': 0.407144, 'fear': 0.036466, 'disgust': 0.162726, 'anger': 0.045164}, 'Odisha assembly constituency': {'sadness': 0.2136365, 'joy': 0.126812, 'fear': 0.1205415, 'disgust': 0.070205, 'anger': 0.0881405}}
	create_missing_emotions_chart(sample_dict)