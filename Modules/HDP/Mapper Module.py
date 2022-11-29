## Mapper Module (Step 1 of 4 to detect hidden problems within the supply chain)
## Accepts BOM .xlsx-files and create a graph-structure

## The xlsx.-files have the following features:

# - Ebene --> The column contains the path description for components regarding the BOM structure
# - IdenNr --> The column contains the ID's of the BOM components
# - HERSTELLER --> The column contains the manufacturer name for some components
# - KURZTEXT-DE --> The column contains a short description of the components
# - Ebene der Stückliste --> The column denotes on which stage the component is within the BOM structure
# - Bestellbezeichnung --> The column contains information about on which description the component is ordered by supplier
# - Bemerkung --> The column contains comments about the components



## 1. Get Files -------- Read xlsx.-files from the folder 'files' and create pandas dataframes
## the files folder should be at the same directory as the mapper module

import pandas as pd
import glob


path = 'files'
file_paths = glob.glob(path + "/*.xlsx")
dataframe_collection = {}
for file_path in file_paths:
    dataframe = pd.read_excel(file_path)
    filename = file_path.split('\\')[1]
    dataframe_collection[filename] = dataframe

## All xlsx.-files from the files folder are read and stored into a dictionary.
## The keys are the filenames and the values are the corresponding pandas dataframes
print(dataframe_collection)
    



## 2. Build the Graph -------- To build up the graph we have to extract from each dataframe the nodes and edges
## ! -- Caution -- ! - There is no standard to extract nodes and edges out of the data, the following steps
## assume that the BOM files have the specification described above


## 2.1 Create Nodes -------- Extract the nodes from the dataframe collection. The nodes are descirbed by the feature 'IdentNr'
## To create nodes and store them into the Graph-DBMS we have to build up a connection to the Graph-DBMS.
## I used the Neo4j-Desktop database: https://neo4j.com/download/ (Version of database 4.4.5)

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from modules import Graph_Database as db
import logging
import sys


# The bolt-port can also be different for your DBMS - I assume that the Bolt-port is the standard 7687-port and the password
# for the DBMS is 'password'. The sub-functions to communicate with the Graph-Database are in the python-file 'Graph-Database'
graph = db.Graph('bolt://localhost:7687', 'neo4j', 'password')
graph.enable_log(logging.INFO, sys.stdout)

## The nodes will now created
for filename in dataframe_collection:
    dataframe = dataframe_collection[filename]
    #The nodes dataframe is a dataframe-series which contains Node-ID's where a Node-ID serves 
    # as identification for the created node
    nodes = dataframe['IdentNr']
    for node in nodes:
        # The sub-function create-node takes an Node-ID and the database name as input
        # In your DBMS you can create several database and name them what you want.
        # I assume that in the DBMS with bolt 7687 there exists a database named 'HDP'.
        # The occurence of a component is interpreted as strenght.
        graph.create_component_node(node,'HDP')

## 2.2 Create Edges -------- Extract the edges from the dataframe collection. The feature 'Ebene' contains a path-description
# of the BOM structure for the component e.g. [1.2.3] where the path is desribed by a series of numbers. Each component has such
# a path description so that the component with the path description [1.2.3] is a sub-component of the component with the path 
# description [1.2]. Keeping that in mind. The edges can be extractet from this feature.

    #2.2.1 The first step is to extract from 'Ebene' a list of lists. Which contains two Component-ID's.
    # The left is the Component-ID where the edge is starting, the right is the Component-ID where the edge is ending.
    # E.g [[ABAD,DABAD]] denotes that the component with the ID ABAD has a relationship to the Component DABAD,
    # so that an edge like (ABAD)-->(DABAD) is created
    # The extraction of the edges are outsourced to the sub-function create-relation-list of the Data_Preperation class of 
    # the Data_Preperation.py

    from modules import Data_Preparation as prepare
    prepare = prepare.Data_Preparation()


from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from modules import Graph_Database as db
import logging
import sys

graph = graph = db.Graph('bolt://localhost:7687', 'neo4j', 'password')
graph.enable_log(logging.INFO, sys.stdout)

#The edges will now created
for filename in dataframe_collection:
    dataframe = dataframe_collection[filename]
    edges = dataframe[['Ebene']]
    edge_list = prepare.create_relation_list(edges)
    for element in edge_list:
        source = element[0]
        target = element[1]


        # Before we create the edges we have to consider wether the relationship reflects the BOM structure or 
        # is an subsitute-reltionship. The BOM data which we used, contains two types of components. There are 
        # components which can be identified as subsitutes and components which are not. The type of component 
        # from which an edge starts determines the type of relationship. So in this step we create two types of
        # relationships 1. (ABASA)-[r:isComponent]->(ABADA) denotes that ABASA is a sub-component of ABADA or
        # 2. (ABASA)-[r:isSubsite]->(ABADA) denotes that ABASA is a substitue of the sub-component ABADA

        #The creation of edges is outsourced to the sub-function 'create_edge' in the Graph_Database.py
        graph.create_component_edge(source,target,'HDP')



## 2.3 Integrating the Manufacturer-Information into the Graph -------- Extract manufacturer information from 
# the dataframe collection. The BOM data provide manufacturer names to some components. This information can
# be integrated into the graph, by creating manufacturer nodes and edges between manufacturer and components


from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from modules import Graph_Database as db
import logging
import sys

graph = graph = db.Graph('bolt://localhost:7687', 'neo4j', 'password')
graph.enable_log(logging.INFO, sys.stdout)


## The nodes will now created
for filename in dataframe_collection:
    dataframe = dataframe_collection[filename]
    #The nodes dataframe is a dataframe which contains the component ID's and the corresponding manufacturer information
    nodes = dataframe[['IdentNR','HERSTELLER']]
    for row in nodes.iterrows():
        component_id = row[1][0]
        manufacturer = row[1][1].upper()
        # The sub-function create-manufacturer takes a Component-ID, a manufacturer name and the database name as input
        # I assume that in the DBMS with bolt 7687 there exists a database named 'HDP'.
        graph.create_manufacturer(component_id, manufacturer,'HDP')


## -------------------- Result after the Mapper Module has finished -------------------------------------------------- ##

# 1. The BOM-Data are processed so that we create component nodes in the graph
# 2. The BOM-Data are processed so that we create "isComponent" and "isSubsitue" edges
# 3. The BOM-Data are processed so that we create manufacturer-nodes and "produce" edges

