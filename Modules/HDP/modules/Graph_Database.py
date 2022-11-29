import logging
import sys
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from graphdatascience import GraphDataScience
from operator import itemgetter


class Graph:

    def create_component_node(self, node_id , dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._create_component_node, node_id)
            return result


    
    @staticmethod
    def _create_component_node(tx,node_id):

        # The strenght of a component is the sum of outgoing edge-weights, and denotes the intensity of an relationship.
        # In the case of BOM data, the strenght derives from the quantitiy of a component. E.g (ABADA {strength:3})->(BADAD)
        # denotes that to build BADAD, 3x ABADA is needed. The BOM data express the required amount in terms of component occurence.
        # When integrating several BOM into one Graph a Multi-Layer Graph is needed to distinguish between the different component requirements and edges. 
        # The HDP have a look at the component graph at whole, the criticality derives from the total sum of the requirements
        # and take the total amount of required material into account. A component that is consumed in high quanitiy is more critical
        # than a component that is consumed in less quantity. The approach does not distinguish how the high consumption is
        # exactly composed. Because it is easier, and what we are interested in is the total sum of requirements, the strenght is
        # saved as node-property. 
        
        query = (

            "MERGE (n:component { ident: $node_id } ) "
            "ON CREATE "
            "SET n.strength = 1 "
            "ON MATCH "
            "SET n.strenght = n.strenght + 1"
        )

        result = tx.run(query, node_id = node_id)
        return result


    
    def create_component_edge(self, source_id, destination_id, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._create_component_edge, source_id, destination_id)
            return result

    @staticmethod
    def _create_component_edge(tx,source_id,destination_id):

        query1 = (

            "MATCH (s:component), (t:component) "
            "WHERE s.ident = $source_id AND t.ident = $target_id "
            "MERGE (s)-[r:isComponent]->(t) "
        )

        
        query2 = (

            "MATCH (s:component), (t:component) "
            "WHERE s.ident = $source_id AND t.ident = $target_id "
            "MERGE (s)-[r:isSubstitue]->(t) "
        )


        # Substitue components start with an 'H'
        if source_id[0] == 'H':
            result = tx.run(query2, source_id = source_id, target_id = destination_id)
            return result
        else:
            result = tx.run(query1, source_id = source_id, target_id = destination_id)
            return result



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
                "MERGE (m)-[r:produce]->(n) "
                
                )

            result = tx.run(query,node_id=node_id, manufacturer=manufacturer)
            return result



    def update_componentNode(self, node_id, mpn, median_price, total_avail, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.write_transaction(self._update_componentNode, node_id, mpn, median_price, total_avail)

    @staticmethod
    def _update_componentNode(tx, node_id, mpn, median_price, total_avail):

        # Check if mpn value exists
        if (mpn == mpn and mpn != None):
            query = (

                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "SET n.mpn = $mpn"
            )

            result = tx.run(query, node_id=node_id, mpn=mpn)

        # Check if median_price value exists
        if (median_price == median_price and median_price != None):
            query = (

                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "SET n.median_price = $median_price"
            )

            result = tx.run(query, node_id=node_id, median_price=median_price)

        #Check if availability value exists
        if (total_avail == total_avail and total_avail != None):
            query = (

                "MATCH (n:component) "
                "WHERE n.ident = $node_id "
                "SET n.total_avail = $total_avail"
            )

            result = tx.run(query, node_id=node_id, total_avail=total_avail)


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

    def get_mostImportant_Nodes(self, dbname):
        with self.driver.session(database=dbname) as session:
            result = session.read_transaction(self._getmostImportant_Nodes)
            return result

    @staticmethod
    def _getmostImportant_Nodes(tx):

        query = (

            "MATCH (n:component) WHERE n.mpn is not null AND n.criticality > 4.14 "
            "RETURN n.ident, n.strength, n.out_degree_components, n.betweeness, n.in_degree_substitute, n.in_degree_components, n.is_SingleSource, n.criticality"

        )
        result = tx.run(query)

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




