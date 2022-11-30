## Semantifier Module (Step 2 of 4 to detect hidden problems within the supply chain)
## Accepts a .xlsx-file which containts component information and 
## enriches the graph 

# The xlsx.-file has the following specification:

# - index column --> component-id's from the BOM data
# - mpn column --> manufacturing part number (mpn) of the components
# - manufacturer_name column--> manfuacturer name for the components
# - sellers column--> list of seller names for the components
# - median_price_1000 column--> current median price (in dollar) for 1000 pieces of the components
# - total_avail column --> current market availability for the components
# - category column --> octopart componentn category classification
# - estimated_factory_lead_days column --> estimated lead time (in days) for the component
# - manufacturer_country --> information about the localisation of the manufacturer for the corresponding component



## 1. Get Files -------- Read the octopart_data from the folder octopart_data
import pandas as pd
import glob
path = 'octopart_data'
file_path = glob.glob(path + "/octopart_data.xlsx")
dataframe = pd.read_excel(file_path[0], index_col = 0)
print(dataframe)



## 2. Enriches the Graph -------- We will now add knowledge to the graph

## 2.1 add mpn, median_price and total_avail as node property for component_nodes


from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from modules import Graph_Database as db
import logging
import sys


# The bolt-port can also be different for your DBMS - I assume that the Bolt-port is the standard 7687-port and the password
# for the DBMS is 'password'. The sub-functions to communicate with the Graph-Database are in the python-file 'Graph-Database'
graph = db.Graph('bolt://localhost:7687', 'neo4j', 'password')
graph.enable_log(logging.INFO, sys.stdout)

for row in dataframe[['mpn','median_price_1000','total_avail']].iterrows():

        component_id = row[0]
        mpn = row[1][0]
        median_price = row[1][1]
        total_avail = row[1][2]
        # The sub-function update_componentNode takes the component_id, the mpn, the median_price 
        # and the availability as arguments
        # and add these information as node-properties to the corresponding component node
        # I assume that in the DBMS with bolt 7687 there exists a database with name 'HDP'
        graph.update_componentNode(component_id, mpn, median_price, total_avail, 'HDP')


## 2.2 Add new manufacturer nodes to the graph or update already existing manufacturer nodes with information
## Similar to adding manufacturer in the mapper moduel

for row in dataframe[['manufacturer_name','estimated_factory_lead_days','manufacturer_country']].iterrows():
    component_id = row[0]
    manufacturer = row[1][0]
    lead_time = row[1][1]
    country = row[1][2]
    

    # If the manufacturer node already exists the manufacturer_country is added as new node property
    # and the lead time is added to the corresponding 'produce' edge as edge-property. If no such 
    # manufacturer node exists than a new manufacturer node is created with the manufacturer country and manufacturer name as
    # node property and a new 'produce' edge with the corrsponding component is created. The lead time will be saved as 
    # new edge-property. I assume that there exists a database named 'HDP' on the DBMS with bolt 7687
    graph.update_manufacturer(component_id,manufacturer,lead_time,country,'HDP')


## 2.3 Add seller to the graph

for row in dataframe[['sellers']].iterrows():

    component_id = row[0]
    sellers = row[1][0]
    #There could be exists more thant one seller for one component. The sellers information are a string and 
    # could be interpreted as a list of seller names
    sellers = eval(sellers)

    # For each seller we have to create a new seller node, a 'sells'-edge with the corresponding component and save 
    # the seller name as node-property. I assume that there exists a database named 'HDP' on the DBMS with bolt 7687
    for seller in sellers:
        graph.create_seller(component_id,seller,'HDP')


## 2.4 Add category to the graph

for row in dataframe[['category']].iterrows():
    
    component_id = row[0]
    category = row[1][0]

    # We create a new cateogry node in the graph and a 'isCategory" edge with the corresponding component
    # The category name is saved as node property in the new category node. I assume that there exists a database named
    # 'HDP' on the DBMS with bolt 7687
    graph.create_category(component_id,category,'HDP')

