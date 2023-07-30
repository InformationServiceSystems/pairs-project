# Decision Support for Operations Planning in Civil Protection

With an increasing number of crises and cascading effects, the pressure on handling complex planning of operations on responder side is growing. While conceptual models serve as an important foundation for systems to support decision makers, existing approaches are not applicable to the civil protection domain and do not focus on recommendations on personnel deployment. We present a service to support decision making in operation planning, addressing executives and planning officers within organizations of civil protection and related domains. We combine a weather-based  prediction of crisis events for the next 7 days with the usage of a semantic model to generate planning recommendations on resources, personnel and human tasks. The event prediction was evaluated for 10 exemplary locations by a German organization within the civil protection domain. We plan to evaluate generated recommendations through a qualitative user study in the future.

## Features
- Explorable knowledge graph representation of historical datasets
- Crisis operation prediction for the next 7 days
- Recommendations for Operations Planning to handle crises events

## Prediction
We predict rain and snow based events, such as heavy rain and floods for 10 locations in Germany (Göttingen, Aachen, Trier, Augsburg, Biberach, Chemnitz, Regensburg, Neubrandenburg, Schwerin, Kiel): 
![MicrosoftTeams-imagec97461883700fae13698badebbd06679cd13df90686356f9bde747b1dbd64983](https://github.com/InformationServiceSystems/pairs-project/assets/65232571/de1564d0-fbb5-402d-8fb5-fcd916f47847)

We tested several forecasting models, while XGBoost outperformed all other models in terms of overall accuracy and F1 scores per event type.

Table1: Comparison of achieved accuracy by diverse forecasting models
<img width="650" alt="TableEventPred" src="https://github.com/InformationServiceSystems/pairs-project/assets/65232571/39719731-58c4-488d-8c40-9885c1170f04">

Table 2: Classification results of different models on predicting crisis events in Germany (P = precision, R = recall, F1 = f1 score)
<img width="635" alt="TableEventPred2" src="https://github.com/InformationServiceSystems/pairs-project/assets/65232571/e72c5982-e341-4ee3-bb85-e21cb43ab3be">


## Semantic Model: Operational Scenario Patterns

Building up on [1,2,3,4,5,6,7,8,9,10,11] we present Operational Scenario Patterns(OPS) as semantic model for the representation of crisis operations. OPS can be used to represent crisis operations within civil protection and related domains. OPS contain the following entities and use existign standard data vocabularies and ontologies, such as [foaf](http://xmlns.com/foaf/0.1/), [beAware](https://github.com/beAWARE-project/ontology), [LODE](https://linkedevents.org/ontology), [Empathi](https://w3id.org/empathi/1.0), [schema.org](http://schema.org).
We used OPS as foundation in order to generate planning recommendations for predicted crisis events.

![ScenarioPatternTHW drawio (9)](https://github.com/InformationServiceSystems/pairs-project/assets/65232571/0907132e-2058-4368-a541-47dd1486db5f)


## References
[1] S. Janzen, N. Gdanitz, L. Abdel Khaliq, T. Munir, C. Franzius, W. Maass. (2023). Anticipating Energy-driven Crises in Process Industry by AI-based Scenario Planning, HICSS (2023)
[2] S. Leachu, J. Janßen, N. Gdanitz, M. Kirchhöfer, S. Janzen. (2023). Cascading Scenario Technique enabling Automated and Situation-based Crisis Management, CPSL (2023).
[3] Watahiki, K., & Saeki, M. (2001). Scenario evolution in requirements elicitation processes: scenario pattern and framework approach. In Proceedings of the 4th International Workshop on Principles of Software Evolution (pp. 166-169).
[4] Watahiki, K., & Saeki, M. (2001). Scenario patterns based on case grammar approach. Proc. of Fifth IEEE Int. Symposium on Requirements Engineering, 300–301.
[5] Alspaugh, T. A., Anto ́n, A. I., Barnes, T., & Mott, B. W. (1999). An integrated scenario management strategy. Proc. of IEEE Int. Symposium on Requirements Engineering (Cat. No. PR00188), 142–149.
[6] Do Prado Leite, J. C. S., Hadad, G. D., Doorn, J. H., & Kaplan, G. N. (2000). A scenario construction process. Requirements Engineering, 5(1), 38–61.
[7] Hoekstra, R. (2009). Ontology representation: Design patterns and ontologies that make sense. University of Amsterdam
[́8] Smiałek,M. (2007). Software development with reusable requirements-based cases. Oficyna Wydawnicza Politechniki Warszawskiej
[9] Tsai, W.-T., Yu, L., Zhu, F., & Paul, R. (2005). Rapid embedded system testing using verification patterns. IEEE software, 22(4), 68–75.
[10] Rolland, C., Ben Achour, C., Cauvet, C., Ralyte ́, J., Sutcliffe, A., Maiden, N., Jarke, M., Haumer, P., Pohl, K., Dubois, E., et al. (1998). A proposal for a scenario classification framework. Requirements Engineering, 3(1), 23–47.
[11] Xie, Z., Jayanth, A., Yadav, K., Ye, G., & Hong, L. (2021). Multi-faceted classification for the identification of informative communications during crises: Case of covid-19. 2021 IEEE 45th Annual Computers, Software, and Applications Conference (COMPSAC), 924–933.

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
