# Operations Planning in Civil Protection

The increasing number of crises and cascading effects over the past years raises the complexity of the operation planning procedures of crisis responders. Planning factors e.g. a proper allocation of personnel and resources are critical for the success of an operation, which is why resilient planning procedures are needed. In cooperation with the German Federal Agency for Technical Relief (German abbr. THW), we aim to support operation planning within the domain of civil defense to increase resource efficiency and save time and costs. We provide a unified structure for the documentation of operations using Scenario Patterns, the prediction of potential future operations, and automated planning recommendations on personnel deployments, resources, and tasks.

## Features

- Overview of the historical Operations Planning
- Scenario Pattern description
- 3D explorable knowledge graph of the historical datasets
- Event prediction for the next 7 days
- Recommendations for Operations Planning to handle crises events

## Tech

- Django - python framework
- jQuery - JavaScript library
- neo4j -  a graph database 
- xgboost - an open-source machine learning library
- leaflet -  open-source JavaScript library for interactive maps
- 3d-force-graph -  represents a graph data structure in a 3-dimensional space

## Installation

1. Create and run the Neo4J graph database.
2. Create and activate the Python environment

```sh
cd .\Modules\THW\
virtualenv thw_test
thw_test\Scripts\activate
```

3. Install all dependencies

```sh
pip install -r requirements.txt
```

4. Run the application 

```sh
cd ./backend/
python manage.py runserver
```
