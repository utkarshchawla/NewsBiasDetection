import pygal
import cairosvg
from pygal.style import Style

def plot_bubble_centralities_chart(trusted_src_dict,other_src1_dict,other_src2_dict):
    
    
    trusted_src = []
    other_src1= []
    other_src2= []
    labels = []
    
    for key in trusted_src_dict.keys():
        labels.append(key)
        trusted_src.append(trusted_src_dict[key])
        other_src1.append(other_src1_dict[key])
        other_src2.append(other_src2_dict[key])
        
    custom_style = Style(
    background = 'white',
    plot_background='white', 
    value_label_font_size = 14,
    value_font_size = 14,
    major_label_font_size = 14 ,
    label_font_size = 14)
    
    dot_chart = pygal.Dot(x_label_rotation=90,logarithmic=True,style = custom_style,width=800,height=700)
    dot_chart.title = ''
    dot_chart.x_labels = labels
    dot_chart.add('Trusted Source', trusted_src )
    dot_chart.add('Other Source 1', other_src1)
    dot_chart.add('Other Source 2', other_src2)
    dot_chart.render_to_png('./bubble_sample.png')

if __name__ == "__main__":
	ts = {'Lok Sabha elections': 0.2222222222222222, 'BJP candidates': 0.4444444444444444, 'parliamentary constituencies': 0.2962962962962963, 'list': 0.14814814814814814, 'meet': 0.1111111111111111, 'Congress': 0, 'Mayawati': 0, 'seats': 0, 'opposition alliance': 0, 'party': 0, 'bluff': 0, 'minister Indira Gandhi': 0, 'Garibi Hatao': 0, 'team': 0, 'rival Akhilesh Yadav': 0, 'impression': 0, 'feather': 0, 'labourers': 0, 'reaction': 0, 'Rs': 0, 'attacks': 0, 'Twitter': 0, 'New Delhi unit': 0, 'PTI': 0, 'cricketer Gautam Gambhir': 0, 'priority': 0, 'dedicated leaders': 0, 'workers': 0, 'Jaibhan Singh Pawaiya': 0, 'national capital': 0, 'objections': 0, 'recommendations': 0, 'celebrities': 0, 'Parliament': 0}
	os = {'Lok Sabha elections': 0.0, 'BJP candidates': 0.6145454545454546, 'parliamentary constituencies': 0, 'list': 0.20108018280016618, 'meet': 0, 'Congress': 0.36580086580086585, 'Mayawati': 0.2845117845117845, 'seats': 0.24780058651026396, 'opposition alliance': 0.2327823691460055, 'party': 0.2327823691460055, 'bluff': 0.20761670761670764, 'minister Indira Gandhi': 0.20761670761670764, 'Garibi Hatao': 0.20761670761670764, 'team': 0.19696969696969696, 'rival Akhilesh Yadav': 0.19696969696969696, 'impression': 0.19696969696969696, 'feather': 0.0818181818181818, 'labourers': 0.0818181818181818, 'reaction': 0.0818181818181818, 'Rs': 0.0, 'attacks': 0.0, 'Twitter': 0.0, 'New Delhi unit': 0, 'PTI': 0, 'cricketer Gautam Gambhir': 0, 'priority': 0, 'dedicated leaders': 0, 'workers': 0, 'Jaibhan Singh Pawaiya': 0, 'national capital': 0, 'objections': 0, 'recommendations': 0, 'celebrities': 0, 'Parliament': 0}
	os1 = {'Lok Sabha elections': 0.20353238015138772, 'BJP candidates': 0.5135278514588859, 'parliamentary constituencies': 0, 'list': 0, 'meet': 0, 'Congress': 0, 'Mayawati': 0, 'seats': 0.2225287356321839, 'opposition alliance': 0, 'party': 0.2828755113968439, 'bluff': 0, 'minister Indira Gandhi': 0, 'Garibi Hatao': 0, 'team': 0, 'rival Akhilesh Yadav': 0, 'impression': 0, 'feather': 0, 'labourers': 0, 'reaction': 0, 'Rs': 0, 'attacks': 0, 'Twitter': 0, 'New Delhi unit': 0.2736009044657999, 'PTI': 0.26918798665183535, 'cricketer Gautam Gambhir': 0.2225287356321839, 'priority': 0.2225287356321839, 'dedicated leaders': 0.21960072595281308, 'workers': 0.21960072595281308, 'Jaibhan Singh Pawaiya': 0.20108018280016618, 'national capital': 0.17945865776789025, 'objections': 0.17945865776789025, 'recommendations': 0.15172413793103448, 'celebrities': 0.06896551724137931, 'Parliament': 0.04597701149425287}
	plot_bubble_centralities_chart(ts,os,os1)