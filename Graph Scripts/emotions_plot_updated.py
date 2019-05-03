import pandas as pd
import ast
import pandas as pd
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

def create_emotions_dataframe(source_dict):
    
    indices = [key for key in source_dict.keys()]
    cols = ['sadness','anger','joy','disgust','fear']
    length = len(source_dict)
    
    df_temp = pd.DataFrame(index=indices, columns=cols)
    
    for col in cols:
        for index in indices:
            #print(col,index,source_dict[index][col])
            df_temp[col][index] = source_dict[index][col]
    #print(df_temp)
    return(df_temp)

def plot_clustered_stacked(dfall, labels=None, title="Emotions",  H="/", **kwargs):
    n_df = len(dfall)
    n_col = len(dfall[0].columns) 
    n_ind = len(dfall[0].index)

    f = plt.figure(figsize=(10,10))
    axe = f.add_subplot(111)

    for df in dfall : # for each data frame
        axe = df.plot(kind="bar",
                      linewidth=0,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      **kwargs)  # make bar plots

    h,l = axe.get_legend_handles_labels() # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
        for j, pa in enumerate(h[i:i+n_col]):
            for rect in pa.patches: # for each index
                rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
                rect.set_hatch(H * int(i / n_col)) #edited part     
                rect.set_width(1 / float(n_df + 1))

    axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)
    axe.set_xticklabels(df.index, rotation = 0)
    axe.set_title(title)

    # Add invisible data to add another legend
    n=[]        
    for i in range(n_df):
        n.append(axe.bar(0, 0, color="gray", hatch=H * i))

    l1 = axe.legend(h[:n_col], l[:n_col], loc=[1.01, 0.5])
    if labels is not None:
        l2 = plt.legend(n, labels, loc=[1.01, 0.1]) 
    axe.add_artist(l1)
    return (axe,plt)

def create_viz(emotions_dict, src_list):
    
    #src_list = [trusted,other1,other2]
    
    trusted_src_dict = {}
    other_source1_dict = {}
    other_source2_dict = {}
    
    for item in emotions_dict.keys():
        
        trusted_src_dict[item] = emotions_dict[item][src_list[0]]
        other_source1_dict[item] = emotions_dict[item][src_list[1]]
        other_source2_dict[item] = emotions_dict[item][src_list[2]]
    
    #print(trusted_src_dict)
    trusted_df = create_emotions_dataframe(trusted_src_dict)
    other_source_1_df = create_emotions_dataframe(other_source1_dict)
    other_source_2_df = create_emotions_dataframe(other_source2_dict)
    
    emotion_plot_vals = plot_clustered_stacked([trusted_df, other_source_1_df, other_source_2_df],["Trusted Source", "Other Source 1", "Other Source 2"],cmap=plt.cm.Blues)
    plot = emotion_plot_vals[1]
    plot.savefig('./sample.png',bbox_inches='tight')
    #make separate df for each source with index as words and columns as emotion values
    
    #trusted_src_df 
    
if __name__ == "__main__":

	#0: DD, 1: NDTV, 2: Times - emotions dicts arrangement in csv

	sample_dict = {'Lok Sabha elections': [{'sadness': 0.466028, 'joy': 0.013319, 'fear': 0.227061, 'disgust': 0.194058, 'anger': 0.227388}, {'sadness': 0.507983, 'joy': 0.096838, 'fear': 0.098207, 'disgust': 0.252794, 'anger': 0.272717}, {'sadness': 0.184811, 'joy': 0.268776, 'fear': 0.115392, 'disgust': 0.155639, 'anger': 0.206985}], 'BJP candidates': [{'sadness': 0.466028, 'joy': 0.013319, 'fear': 0.227061, 'disgust': 0.194058, 'anger': 0.227388}, {'sadness': 0.591634, 'joy': 0.065504, 'fear': 0.121462, 'disgust': 0.250559, 'anger': 0.211343}, {'sadness': 0.434451, 'joy': 0.186665, 'fear': 0.131167, 'disgust': 0.087593, 'anger': 0.096391}]}
	
	#trusted_src_index, other_src1,other_src2 - pass in this manner
	src_list = [0,1,2]
	create_viz(sample_dict,src_list)