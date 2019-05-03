import pandas as pd
import ast
import altair as alt
#alt.renderers.enable('notebook')

def add_to_df(rows,new_df):
    for item in rows:
        new_df = new_df.append({'keywords':item[0],'c2':item[1],'values':item[2],'Emotion':item[3]},ignore_index=True)
    return new_df

def get_rows_src(values_dict,src,word):
    rows = []
    if(values_dict is not None):
        for item in values_dict.keys():
            rows.append([word,src,values_dict[item],item])
    else:
        rows.append([word,src,0,'sadness'])
        rows.append([word,src,0,'joy'])
        rows.append([word,src,0,'fear'])
        rows.append([word,src,0,'disgust'])
        rows.append([word,src,0,'anger'])
    return rows


def create_viz(emotions_dict, src_list):
    
    new_df = pd.DataFrame(columns=['keywords','c2','values','Emotion'])
    
    for key in emotions_dict.keys():
        word = key
        value_trusted_src = emotions_dict[key][src_list[0]]
        value_other_src1 = emotions_dict[key][src_list[1]]
        value_other_src2 = emotions_dict[key][src_list[2]]
    
        rows_trusted_src = get_rows_src(value_trusted_src,"Trusted Source",word)
        rows_other_src1 = get_rows_src(value_other_src1, "Other Source 1",word)
        rows_other_src2 = get_rows_src(value_other_src2,'Other Source 2',word)
    
        new_df = add_to_df(rows_trusted_src,new_df)
        new_df = add_to_df(rows_other_src1,new_df)
        new_df = add_to_df(rows_other_src2,new_df)
    
    
    chart = alt.Chart(new_df).mark_bar().encode(

    x=alt.X('c2:N',
        axis=alt.Axis(
            title='')),

    y=alt.Y('sum(values):Q',
        axis=alt.Axis(
            grid=False,
            title='')),

    column=alt.Column('keywords:N'
                ),
        
    color=alt.Color('Emotion:N',
            scale=alt.Scale(
                range=['#96ceb4', '#ffcc5c','#ff6f69','#ff9BD8','#877DD8'],
            )
        ))
    chart = chart.properties(width=200, height=500)
    chart.save('./emotion_sample.svg')

if __name__ == "__main__":
	#0: DD, 1: NDTV, 2: Times - sentiments dicts arrangement
	sample_dict = {'Lok Sabha elections': [{'sadness': 0.466028, 'joy': 0.013319, 'fear': 0.227061, 'disgust': 0.194058, 'anger': 0.227388}, {'sadness': 0.507983, 'joy': 0.096838, 'fear': 0.098207, 'disgust': 0.252794, 'anger': 0.272717}, {'sadness': 0.184811, 'joy': 0.268776, 'fear': 0.115392, 'disgust': 0.155639, 'anger': 0.206985}], 'BJP candidates': [{'sadness': 0.466028, 'joy': 0.013319, 'fear': 0.227061, 'disgust': 0.194058, 'anger': 0.227388}, {'sadness': 0.591634, 'joy': 0.065504, 'fear': 0.121462, 'disgust': 0.250559, 'anger': 0.211343}, {'sadness': 0.434451, 'joy': 0.186665, 'fear': 0.131167, 'disgust': 0.087593, 'anger': 0.096391}]}
	src_list = [0,1,2]
	create_viz(sample_dict,src_list)