import pygal
import cairosvg
from pygal.style import Style

def create_chart_attention(attn_dict,src_list):
    
    #trusted src is src_list 0
    #other src1 is src_list 1
    #other src2 is src_list 2
    
    x_labels = []
    y_labels_vals = []
    trusted_src_vals = []
    other_src_1_vals = []
    other_src_2_vals = []
    
    for key in attn_dict.keys():
        
        x_labels.append(key)
        
        trusted_src_vals.append(attn_dict[key][src_list[0]])
        other_src_1_vals.append(attn_dict[key][src_list[1]])
        other_src_2_vals.append(attn_dict[key][src_list[2]])
    
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
    
    line_chart = pygal.Bar(style = custom_style,title="Attention Values")
    line_chart.x_labels = x_labels
    
    for item in y_labels_vals:
        y_label = item[0]
        y_val = item[1]
        line_chart.add(y_label,y_val)
    
    line_chart.render_to_png('./attn_sample2.png')

if __name__=="__main__":
	#0: DD, 1: NDTV, 2: Times - sentiments dicts arrangement in csv

	sample = {'sukma': [0.158604801, 0.386931032, 0.152398303], 'rifle': [0.43261495200000005, 0.49709186, 0.487950683], 'four': [0.025523392000000002, 0.102399558, 0.024813866], 'insas': [0.016134197, 0.050385772999999995, 0.10037034], 'cobra': [0.328460246, 0.164412379, 0.106582955], '303': [0.13317462800000002, 0.20637802800000002, 0.266114026], 'commando': [0.49720877399999996, 0.315029591, 0.145171627]}
	
	#trusted_src_index, other_src1,other_src2 - pass in this manner
	create_chart_attention(sample,[0,1,2])