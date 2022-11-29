## Criticality Controller (Step 3 of 4 to detect hidden problems within the supply chain)
## Calculates several centrality measures and the criticality score

import logging
import sys
import glob
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from graphdatascience import GraphDataScience
from modules import Graph_Database as db

# We build up a connection to the Neo4j DBMS and to calculate the centraliy measures we
# use the Neo4j Graph Data Science library

graph = db.Graph('bolt://localhost:7687', 'neo4j', 'password')
graph.enable_log(logging.INFO, sys.stdout)
gds = GraphDataScience('bolt://localhost:7687', auth = ('neo4j','password'))
# I assume that in the DBMS with bolt 7687 exists a database with name 'HDP'
gds.set_database('HDP')


#Calculate Out-Degree for 'isComponent'-Relations
G, res = gds.graph.project("knowledge2", 'component', "isComponent")
result = gds.degree.write(G, writeProperty='out_degree_components')
gds.graph.drop(G)

#Calculate In-Degree for 'isComponent-Relations'
G, res = gds.graph.project("knowledge2", 'component', "isComponent")
result = gds.degree.write(G, writeProperty='in_degree_components', orientation='REVERSE')
gds.graph.drop(G)

#Calculate In-Degree for 'isSubstitute-Relations'
G, res = gds.graph.project("knowledge2", 'component', "isSubstitute")
result = gds.degree.write(G, writeProperty='in_degree_substitute', orientation='REVERSE')
gds.graph.drop(G)

#Calculate Betweenees-Centrality only for 'isComponent'-Relations
G, res = gds.graph.project("knowledge2", 'component', "isComponent")
result = gds.betweenness.write(G, writeProperty='betweeness', nodeLabels=['component'],
                                       relationshipTypes=['isComponent'])
gds.graph.drop(G)

#Calculate Criticality --> Calcualtion takes place as presented 
graph.calculate_criticality('HDP')

## The substitue components does inherite their criticality from their counterparts. Substitue components
## reflects alternative supplies but their derive their criticality by their position in the BOM structure
graph.move_component_crit_to_substitute('HDP')



