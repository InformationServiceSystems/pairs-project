# Hidden Problem Detector

## 1. Description


<p> 

The Hidden Problem Detector represents a system for graph-theoretic analysis of component criticality for detecting hidden problems in component-based supply chains. Driven by the increasing trade in intermediate goods, shortage of specific components like semiconductors, greater richness of variants in manufacturing industry as well as the global increase in lead times, supply chain disruptions has become a mass phenomenon. When manufacturing component-based products like sensors, engines or electronics, underlying supply chains are complex and increasingly non-transparent beyond tier 1 supplier. Due to the non-transparency of early supply chain stages traditional management approaches only have an effect at tier 1, maybe tier 2, i.e., they enable reactive instead of pro-active behavior in supply chain and risk management. In contrast to existing top-down approaches to analyze the market situation, the Hidden Problem Detector transform Bill-of-Materials into a knowledge graph and enrich the graph with hisorical and current market data for improving transparency of supply chain by enabling a transparent view of all supply chain levels including the identification and location of shortages.
    
</p>


## 2. How it works

<p> 

The system consits of four main modules: Mapper, Semantifier, Criticality Controller and Hidden Problem Detector:

- The Mapper receives Bill-of-Materials in form of excel files, representing the composition of the product in a tree-like structure, and maps the data onto a knowledge graph. 

- The Semantifier enrichs the knowledge graph by electronic component data. 

- The Criticality Controller analyzes the component knowledge graph with respect to critical components. Therefore several graph-theoretic concepts are used. 

- The Hidden Problem Detector receives historical electronic component data regarding market availability, estimated lead time (given in days), as well as median price and generates an overview of detected critical components augmented with the historical data as a decision support for end users. 

<p> 

## 3. Installation 

- Prerequisites:

	```Python 3.8.2 or higher.``` You can follow [this guide](https://phoenixnap.com/kb/upgrade-python) on how to install it on Windows/macOS/Linux.

	```Local Neo4j-Dekstop instance.``` You can download it on [this side](https://neo4j.com/download-neo4j-now/?gclid=Cj0KCQiAm5ycBhCXARIsAPldzoW9NdJ-fH7QScGYatY3X__TWloRG3UVIWT7qAgo-A-acjlUQSNAAn4aAqTyEALw_wcB)

	```Active local database, named 'HPD', in the Neo4j-Desktop DBMS (Version 4.4.5) with bolt-port 7687.``` You can follow [this guide](https://neo4j.com/developer/neo4j-desktop/) on how to create a DBMS, a local database and how to activate your DBMS. 

- Clone/Download the repository:

	- Open a terminal (Linux) or cmd (Windows) and run the following command to clone the repository:
	```
	git clone https://github.com/InformationServiceSystems/pairs-project
	```

- Install the dependencies 

	- In the terminal, run the following command to go to demo directory. 
	```
	cd pairs-project\Modules\HDP
	```
	- Then run this command to install the dependencies
	```
	pip install -r requirements.txt
	```