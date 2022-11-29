from xml.dom.minicompat import NodeList
import pandas as pd

class Data_Preparation():
    
    def __init__(self):
        pass
                                       
    def create_relation_list(self, df):
        
        relation_dict = dict()
        for row in df.iterrows():
            relation_dict[row[1][1]] = row[1][0]
        
        source_target_list = []
                     
        df = df.iloc[1:]
        
        for row in df.iterrows():
            source = row[1][1]
            source_id = relation_dict[source]
            target = source.split(".")
            target = target[:-1]
            string = '.'
            target = string.join(target) + "]"
            target_id = relation_dict[target]
            source_target_list.append([source_id,target_id])
                
        return source_target_list

    