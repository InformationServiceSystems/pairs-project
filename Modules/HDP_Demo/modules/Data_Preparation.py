from xml.dom.minicompat import NodeList
import pandas as pd

class Data_Preparation():
    
    def __init__(self):
        pass
    
    # Nimmt eine Stückliste in Form eines Dataframes entgegen und erstellt ein Liste welche die ID's der 
    # Komponenten der Stückliste widergibt
    def create_node_list(self, df):
        nodes = df.drop_duplicates(subset=['IdentNr'])
        return nodes[['IdentNr']].values.tolist()
    
    
    # Nimmt eine Stückliste in Form eines Dataframes entgegen und erstellt daraus ein dictionary der Knotenstärke
    # (Stärke =  Mengenverbrauch der Komponenten innerhalb der Stückliste) 
    def calculate_strength(self, df):
        strength = df['IdentNr'].value_counts().to_dict()
        return strength
    
                     
    # Nimmt eine Stückliste in Form eines Dataframes entgegen und erstellt eine Liste welches die Quellen & Ziel-Beziehungen
    #der Stückliste widergibt               
    def create_relation_list(self, df):
        
        relation_dict = dict()
        df = df[['IdentNr','Ebene']]
        for row in df.iterrows():
            relation_dict[row[1][1]] = row[1][0]
        
        source_target_list = []
                     
        df = df[['IdentNr','Ebene']].iloc[1:]
        
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

    def get_manufacturer(self,df):
        nodes = df.drop_duplicates(subset=['IdentNr'])
        return nodes[['IdentNr','HERSTELLER']].values.tolist()
    