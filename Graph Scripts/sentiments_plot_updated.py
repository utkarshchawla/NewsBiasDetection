import pygal
import cairosvg
from pygal.style import Style

def create_chart(sentiments_dict,src_list):
    
    #trusted src is src_list 0
    #other src1 is src_list 1
    #other src2 is src_list 2
    
    x_labels = []
    y_labels_vals = []
    trusted_src_vals = []
    other_src_1_vals = []
    other_src_2_vals = []
    
    for key in sentiments_dict.keys():
        
        x_labels.append(key)
        
        trusted_src_vals.append(sentiments_dict[key][src_list[0]])
        other_src_1_vals.append(sentiments_dict[key][src_list[1]])
        other_src_2_vals.append(sentiments_dict[key][src_list[2]])
    
    y_labels_vals.append(['Trusted Source',trusted_src_vals])
    y_labels_vals.append(['Other Source 1',other_src_1_vals])
    y_labels_vals.append(['Other Source 2',other_src_2_vals])
    
    #plot chart
    
    custom_style = Style(
    background = 'white',
    plot_background='white', 
    value_label_font_size = 14,
    value_font_size = 14,
    major_label_font_size = 14 ,
    label_font_size = 14)
    
    line_chart = pygal.Bar(style = custom_style)
    line_chart.x_labels = x_labels
    
    for item in y_labels_vals:
        y_label = item[0]
        y_val = item[1]
        line_chart.add(y_label,y_val)
    
    line_chart.render_to_png('./sentiment_sample.png')

if __name__ == "__main__":
	
	#0: DD, 1: NDTV, 2: Times - sentiments dicts arrangement in csv

	sentiments = {'Maharashtra government': [0, 0, -0.489173], 'Devendra Fadnavis': [-0.702881, 0.87539, -0.80566], 'loan waiver': [-0.702881, 0.868845, 0], 'farmers': [0.922089, 0, 0.363583], 'governments': [0.890551, None, None]}
	
	#trusted_src_index, other_src1,other_src2 - pass in this manner
	src_list = [2,1,0]
	create_viz(sentiments,src_list)
