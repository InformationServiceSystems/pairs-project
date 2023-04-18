import logging
import sys
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from graphdatascience import GraphDataScience
from operator import itemgetter


class Graph:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    @staticmethod
    def enable_log(level, output_stream):
        handler = logging.StreamHandler(output_stream)
        handler.setLevel(level)
        logging.getLogger("neo4j").addHandler(handler)
        logging.getLogger("neo4j").setLevel(level)

    def create_component(self, component_id, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._create_component, component_id)

    @staticmethod
    def _create_component(tx, component_id):
        query1 = (

            "MERGE (c:component { ident: $component_id , substitute: False }) "
            "ON CREATE "
            "SET c.strength = 0"
        )

        query2 = (

            "MERGE (c:component { ident: $component_id , substitute: True } ) "
            "ON CREATE "
            "SET c.strength = 0"
        )

        if ((component_id[0] == 'H' or component_id[0] == 'y') and component_id[0:2] != 'HA'):
            result = tx.run(query2, component_id=component_id)
        else:
            result = tx.run(query1, component_id=component_id)
        

    def delete_all(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._delete_all)

    @staticmethod
    def _delete_all(tx):
        query = ("MATCH (n) DETACH DELETE n")
        result = tx.run(query)

    def create_component_relation(self, source_id, target_id, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._create_component_relation, source_id, target_id)

    @staticmethod
    def _create_component_relation(tx, source_id, target_id):

        if(source_id[0:2] == 'HA'):
            print(source_id)

        
        query1 = (

            "MATCH (s:component), (t:component) "
            "WHERE s.ident = $source_id AND t.ident = $target_id "
            "MERGE (s)-[r:isComponent { label: 'isComponent' }]->(t) "
        )

        query2 = (
            "MATCH (s:component), (t:component) "
            "WHERE s.ident = $source_id AND t.ident = $target_id "
            "MERGE (s)-[r:isSubstitute {label: 'isSubstitute' }]->(t) "
        )

        # 
        if ((source_id[0] == 'H' or source_id[0] == 'y') and source_id[0:2] != 'HA'):
            result = tx.run(query2, source_id=source_id, target_id=target_id)

        else:
            result = tx.run(query1, source_id=source_id, target_id=target_id)

        

    def update_componentNode(self, node_id, mpn, median_price, total_avail, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._update_componentNode, node_id, mpn, median_price, total_avail)

    @staticmethod
    def _update_componentNode(tx, node_id, mpn, median_price, total_avail):

        if (mpn == mpn and mpn != None):
            query = (

                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "SET n.mpn = $mpn"
            )

            result = tx.run(query, node_id=node_id, mpn=mpn)

        if (median_price == median_price and median_price != None):
            query = (

                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "SET n.median_price = $median_price"
            )

            result = tx.run(query, node_id=node_id, median_price=median_price)

        if (total_avail == total_avail and total_avail != None):
            query = (

                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "SET n.total_avail = $total_avail"
            )

            result = tx.run(query, node_id=node_id, total_avail=total_avail)

    def create_manufacturer(self, node_id, manufacturer,dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._create_manufacturer, node_id,manufacturer)

    @staticmethod
    def _create_manufacturer(tx,node_id,manufacturer):

        if (manufacturer==manufacturer and manufacturer != None):
            query = (
                
                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "MERGE (m:manufacturer {name: $manufacturer}) "
                "MERGE (m)-[r:produce {label: 'produce'}]->(n) "
                
                )

            result = tx.run(query,node_id=node_id, manufacturer=manufacturer)


    def update_manufacturer(self, node_id, manufacturer, estimated_lead_time, location, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._update_manufacturer, node_id, manufacturer, estimated_lead_time, location)

    @staticmethod
    def _update_manufacturer(tx, node_id, manufacturer, estimated_lead_time, location):



        if (
                manufacturer == manufacturer and manufacturer != None and estimated_lead_time == estimated_lead_time and estimated_lead_time != None):
            query1 = (

                "MERGE (m:manufacturer {name: $manufacturer}) "
                
            )

            result= tx.run(query1, manufacturer=manufacturer)

            query2 = (

                "MATCH (m:manufacturer), (n:component) "
                "WHERE n.ident = $node_id AND m.name = $manufacturer "
                "MERGE (m)-[r:produce {label: 'produce'}]->(n) "
                "SET r.manufacturer_lead_days = $estimated_lead_time "

            )

            
            result = tx.run(query2, node_id=node_id, manufacturer=manufacturer, estimated_lead_time=estimated_lead_time, location=location)
            
            if(location==location and location != None):

                query3 = (

                    "MATCH (m:manufacturer) "
                    "WHERE m.name = $manufacturer "
                    "SET m.location = $location "

                )

                result = tx.run(query3, manufacturer=manufacturer, location=location)

    def create_category(self, node_id, category, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._create_category, node_id, category)

    @staticmethod
    def _create_category(tx, node_id, category):

        if (category == category and category != None):
            query = (

                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "MERGE (c:category {name: $category}) "
                "MERGE (n)-[r:is_category { label: 'is_category' }]->(c)"
            )

            result = tx.run(query, node_id=node_id, category=category)

    def create_seller(self, node_id, seller, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._create_seller, node_id, seller)

    @staticmethod
    def _create_seller(tx, node_id, seller):

        if (seller == seller and seller != None):
            query = (

                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "MERGE (s:seller {name: $seller}) "
                "MERGE (s)-[r:sells { label: 'sells' }]->(n)"
            )

            result = tx.run(query, node_id=node_id, seller=seller)

    def update_strength(self, node_id, strength, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._update_strength, node_id, strength)

    @staticmethod
    def _update_strength(tx, node_id, strength):

        query = (

            "MATCH (n:component) "
            "WHERE n.ident = $node_id "
            "SET n.strength = toInteger(n.strength) + $strength"
        )

        result = tx.run(query, node_id=node_id, strength=strength)

    def get_nodeLabels(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_nodeLabels)
            return result

    @staticmethod
    def _get_nodeLabels(tx):
        query = ("MATCH (n) RETURN distinct labels(n)")
        result = tx.run(query)
        return [row[0][0] for row in result]

    def get_RelationshipLabels(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_RelationshipLabels)
            return result

    @staticmethod
    def _get_RelationshipLabels(tx):
        query = ("MATCH (n)-[r]->(m) RETURN distinct type(r)")
        result = tx.run(query)
        return [row[0] for row in result]

    def delete_similarity_between_nonComponents(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._delete_similarity_between_nonComponents)

    @staticmethod
    def _delete_similarity_between_nonComponents(tx):
        query1 = ("MATCH (n)-[r:is_similar]->(m) WHERE NOT n:component DELETE r")
        result = tx.run(query1)
        query2 = ("MATCH (n)-[r:is_similar]->(m) WHERE NOT m:component DELETE r")
        result = tx.run(query2)
        query3 = ("MATCH (n:component)-[r:is_similar]->(m:seller) DELETE r")
        result = tx.run(query3)

    def add_similarity_label(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._add_similarity_label)

    @staticmethod
    def _add_similarity_label(tx):
        query = ("MATCH (n)-[r]-(m) WHERE r:is_similar "
                 "SET r.label = 'is_similar' "
                 )

        result = tx.run(query)

    def create_bidirectioanl_sameSimilarity(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._create_bidirectioanl_sameSimilarity)

    @staticmethod
    def _create_bidirectioanl_sameSimilarity(tx):
        query = ("MATCH (n1)-[r1:is_similar]->(m1), (m2)-[r2:is_similar]->(n2) "
                 "WHERE  r1.similarity_value = r2.similarity_value AND n1.ident = n2.ident AND m1.ident = m2.ident "
                 "MERGE (n)-[r3:is_similar {similarity_value: r1.similarity_value} ]-(m) "
                 "DELETE r1, r2 "
                 )
        result = tx.run(query)

    def get_mostImportant_Nodes(self, dbname, threshold):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._getmostImportant_Nodes, threshold)
            return result

    @staticmethod
    def _getmostImportant_Nodes(tx, threshold):

        query = (

            "MATCH (n:component) WHERE n.mpn is not null AND n.criticality > $threshold "
            "RETURN n.ident, n.strength, n.out_degree_components, n.betweeness, n.in_degree_substitute, n.in_degree_components, n.is_SingleSource, n.criticality"

        )
        result = tx.run(query, threshold = threshold)

        ergebniss = []

        for row in result:
            ident = row[0]
            strength = row[1]
            out_degree_components = row[2]
            betweeness = row[3]
            in_degree_substitute = row[4]
            in_degree_components = row[5]
            single_source = row[6]
            criticality = row[7]
            element = [ident, single_source, criticality, strength, out_degree_components, betweeness, in_degree_substitute, in_degree_components]
            ergebniss.append(element)

        return sorted(ergebniss, key=itemgetter(2), reverse=True)

    def get_similar_Nodes(self, ident, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_similar_Nodes, ident)
            return result

    @staticmethod
    def _get_similar_Nodes(tx, ident):

        query = (

            "MATCH (p:component) "
            "WHERE p.ident = $ident "
            "WITH p, [(x)-[:is_similar]->(p) | x] as similar "
            "RETURN p, similar "

        )

        result = tx.run(query, ident=ident)
        liste = [record for record in result.data()]
        return [liste[0]['p'], liste[0]['similar']]

    def get_all_childNodes(self, ident, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_all_childNodes, ident)
            return result

    @staticmethod
    def _get_all_childNodes(tx, ident):

        query = (

            'MATCH (n:component)-[r:isComponent]->(m:component) WHERE n.ident = $ident RETURN m'

        )

        result = tx.run(query, ident=ident)
        liste = [record for record in result.data()]
        return liste

    def remove_loops(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._remove_loops)
            return

    @staticmethod
    def _remove_loops(tx):

        query = ("MATCH (n:component)-[r]->(m:component) "
                 "WHERE n.ident = m.ident "
                 "DELETE r "
                 )

        result = tx.run(query)
        return

    def get_all_seller(self, ident, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_all_seller, ident)
            return result

    @staticmethod
    def _get_all_seller(tx, ident):

        query = (

            'MATCH (s:seller)-[r:sells]->(n:component) WHERE n.ident = $ident RETURN s'

        )

        result = tx.run(query, ident=ident)
        liste = [record for record in result.data()]
        return liste

    def find_single_source(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._find_single_source)

    @staticmethod
    def _find_single_source(tx):

        query = (

            'MATCH (c:component)-[r:isSubstitute]->(p:component) WITH c,p , '
            'CASE WHEN p.in_degree_substitute = 1.0 THEN True ELSE False END AS is_SingleSource_res '
            'SET c.is_SingleSource = is_SingleSource_res '

        )

        result = tx.run(query)

    def get_category(self, dbname, ident):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_category, ident)
            return result

    @staticmethod
    def _get_category(tx, ident):

        query = (

            'MATCH (n:component)-[r:is_category]->(c:category) WHERE n.ident = $ident '
            'RETURN c.name '

        )

        result = tx.run(query, ident=ident)
        liste = [record['c.name'] for record in result.data()]
        return liste

    def get_manufacturer(self, dbname, ident):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_manufacturer, ident)
            return result

    @staticmethod
    def _get_manufacturer(tx, ident):

        query = (

            'MATCH (p:manufacturer)-[r:produce]->(n:component) WHERE n.ident = $ident '
            'RETURN p.name '

        )

        result = tx.run(query, ident=ident)
        liste = [record['p.name'] for record in result.data()]
        return liste

    def get_seller(self, dbname, ident):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_seller, ident)
            return result

    @staticmethod
    def _get_seller(tx, ident):

        query = (

            'MATCH (s:seller)-[r:sells]->(n:component) WHERE n.ident = $ident '
            'RETURN s.name '

        )

        result = tx.run(query, ident=ident)
        liste = [record['s.name'] for record in result.data()]
        return liste

    def get_singlesource(self, dbname, ident):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._get_singlesource, ident)
            return result

    @staticmethod
    def _get_singlesource(tx, ident):

        query = (

            'MATCH (c:component) WHERE c.ident = $ident '
            'RETURN c.is_SingleSource '

        )

        result = tx.run(query, ident=ident)
        liste = [record['c.is_SingleSource'] for record in result.data()]
        return liste

    def remove_similarity(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._remove_similarity)

    @staticmethod
    def _remove_similarity(tx):

        query = ('MATCH ()-[r:is_similar]->() DELETE r')
        result = tx.run(query)

    def calculate_criticality(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._calculate_criticality)
            return result

    @staticmethod
    def _calculate_criticality(tx):

        query = (

            'MATCH (c:component) WHERE c.substitute = False WITH c , '
            'CASE WHEN c.in_degree_substitute <> 0 THEN (((c.strength + c.out_degree_components + c.betweeness)/c.in_degree_substitute) + c.in_degree_components) '
            'WHEN c.in_degree_substitute = 0 THEN (c.strength + c.out_degree_components + c.in_degree_components + c.betweeness) '
            'END AS criticality '
            'SET c.criticality = criticality '

        )

        result = tx.run(query)
        return result

    def move_component_crit_to_substitute(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._move_component_crit_to_substitute)
            return result

    @staticmethod
    def _move_component_crit_to_substitute(tx):

        query = (

            'MATCH (s:component)-[r:isSubstitute]->(c:component) WHERE s.substitute = True '
            'SET s.strength = c.strength '
            'SET s.out_degree_components = c.out_degree_components '
            'SET s.in_degree_components = c.in_degree_components '
            'SET s.betweeness = c.betweeness '
            'SET s.in_degree_substitute = c.in_degree_substitute '
            'SET s.criticality = c.criticality '
        
        )

        result = tx.run(query)
        return result

    def get_criticality(self,dbname):
        with self.driver.session(database = dbname) as session:
            result = session.read_transaction(self._get_criticality)
            return result
        
        
    @staticmethod
    def _get_criticality(tx):
        
  
        
        query = (
            
            'MATCH (c:component) '
            'RETURN c.criticality '
            
        )
        
        

        result = tx.run(query)
        crit_values = [record['c.criticality'] for record in result.data()]
        return crit_values


    def is_enriched(self,dbname, prop):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._is_enriched, prop)
            return result

    @staticmethod
    def _is_enriched(tx, prop):

        query = (


           "MATCH (n) return DISTINCT keys(n) "

        )

        result = tx.run(query)
        node_properties = [record['keys(n)'] for record in result.data()]
        set_res = {i for lst in node_properties for i in lst}
        print(set_res)
        print(prop)
        if prop in set_res:
            return True
        else: return False





    