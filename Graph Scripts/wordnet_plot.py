import pandas as pd
import ast
import pygal
import cairosvg
from pygal.style import Style

def make_wordnet_plot(src_dict):
    
    custom_style = Style(background = 'white', plot_background='white',  value_label_font_size = 14, value_font_size = 14, major_label_font_size = 14 , label_font_size = 14,colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))
    dot_chart = pygal.Dot(x_label_rotation=90,logarithmic=True,style=custom_style)
    
    x_labels = []
    y_labels_values = []
    
    length = len(src_dict)
    
    for key in src_dict.keys():
        x_labels.append(key)
        y_label = src_dict[key][0]
        ind = x_labels.index(key)
        y_values = [0] * length
        y_values[ind] = src_dict[key][1] 
        y_labels_values.append([y_label,y_values])
    
    #add to dot chart
    dot_chart.x_labels = x_labels
    for item in y_labels_values:
        lab = item[0]
        vals = item[1]
        #print(lab)
        dot_chart.add(lab,vals)
    dot_chart.render()
    #dot_chart.render_to_png('./sample_plot_wordnet.png')

if __name__ == "__main__":
	sample_src_dict = {'meeting': ['congress', 0.2], 'ninth': ['insist', 0.33], 'constituency': ['difference', 0.12], 'party': ['party', 1.0], 'election': ['election', 1.0], 'list': ['anywhere', 0.88], 'delhi': ['field', 0.14], 'phase': ['calendar_month', 0.33], 'meet': ['contest', 0.33], 'campaigner': ['head', 0.25], 'capital': ['seating', 0.14], 'release': ['necktie', 0.12], 'leadership': ['leadership', 1.0]}
	make_wordnet_plot(sample_src_dict)