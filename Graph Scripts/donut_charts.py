import pygal
from pygal import style
import cairosvg

def create_donut_charts(os1_ts_not_present,os2_ts_not_present, ts_os1_not_present, ts_os2_not_present):
    
    # merge_dictionaries of trusted source not present vals
    (ts_os1_not_present.update(ts_os2_not_present)) 
    ts_np_combined = dict(ts_os1_not_present)
    
    #___CHART_1___
    #trusted_source present entities chart, (entities absent in other two sources)
    chart_1 = pygal.Pie(inner_radius=.4)
    for key in ts_np_combined.keys():
        chart_1.add(key,ts_np_combined[key])
    
    chart_1.render_to_png('ts_donut.png')
    
    #___CHART_2___
    #other_source_1 present entities,which are absent in trusted source
    chart_2 = pygal.Pie(inner_radius=.4)
    for key in os1_ts_not_present.keys():
        chart_2.add(key,os1_ts_not_present[key])
    
    chart_2.render_to_png('os1_donut.png')
        
    #___CHART_3___
    #other_source_1 present entities,which are absent in trusted source
    chart_3 = pygal.Pie(inner_radius=.4)
    for key in os2_ts_not_present.keys():
        chart_3.add(key,os2_ts_not_present[key])
    chart_3.render_to_png('os2_donut.png')

if __name__ == "__main__":

	""" eg: suppose trusted source is DD, OtherSource1 = NDTV, OtherSource2 = Times Now
		we'll pass dd_ndtv_not_present, dd_tn_not_present, ndtv_dd_not_present, tn_dd_not_present as arguments to create_donut charts function... """
	""" This function will create 3 charts to be displayed along side each other"""
	dd_tn_not_present = {'parliamentary constituencies': 0.2962962962962963, 'Minister Narendra Modi': 0.1111111111111111, 'meet': 0.1111111111111111} 
	dd_ndtv_not_present = {'central election committee': 0.35555555555555557, 'parliamentary constituencies': 0.2962962962962963, 'candidates': 0.19753086419753085, 'list': 0.14814814814814814, 'Odisha assembly constituency': 0.14814814814814814, 'meet': 0.1111111111111111} 

	ndtv_dd_not_present = {'Congress': 0.36580086580086585, 'Mayawati': 0.2845117845117845, 'seats': 0.24780058651026396, 'opposition alliance': 0.2327823691460055, 'party': 0.2327823691460055, 'Congress slogan': 0.20761670761670764, 'bluff': 0.20761670761670764, 'Garibi Hatao': 0.20761670761670764, 'team': 0.19696969696969696, 'rival Akhilesh Yadav': 0.19696969696969696, 'impression': 0.19696969696969696, 'Akhilesh Yadav': 0.17864693446088795, 'Congress party': 0.13636363636363635, 'feather': 0.0818181818181818, 'labourers': 0.0818181818181818, 'reaction': 0.0818181818181818, 'Rs': 0.0, 'chief Rahul Gandhi': 0.0, 'attacks': 0.0, 'Twitter': 0.0} 
	tn_dd_not_present = {'party': 0.2828755113968439, 'New Delhi unit': 0.2736009044657999, 'PTI': 0.26918798665183535, 'Delhi unit': 0.23180076628352492, 'cricketer Gautam Gambhir': 0.2225287356321839, 'New Delhi seat': 0.2225287356321839, 'priority': 0.2225287356321839, 'dedicated leaders': 0.21960072595281308, 'workers': 0.21960072595281308, 'Jaibhan Singh Pawaiya': 0.20108018280016618, 'national capital': 0.17945865776789025, 'objections': 0.17945865776789025, 'recommendations': 0.15172413793103448, 'New Delhi': 0.15172413793103448, 'celebrities': 0.06896551724137931, 'Parliament': 0.04597701149425287, 'Bharatiya Janata Party': 0.0, 'Delhi': 0.0} 

	create_donut_charts(dd_tn_not_present,dd_ndtv_not_present,ndtv_dd_not_present,tn_dd_not_present)