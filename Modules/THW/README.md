# ProPlan: Proactive Operation Planning in Civil Protection

During occurring crisis events, time of response, allocation of equipment, tasks and personnel pose critical success factors to crisis operations conducted by responders (e.g., professional units and volunteers within civil protection and related domains). Respective operation plans are currently compiled manually by experienced planning officers or in combination with supporting systems, that either lack concrete planning recommendations, or focus on post-disaster recommendations for operation plans on-site of a crisis event. We present ProPlan, a model to support proactive operation planning by means of an early event prediction and semantically enhanced historical knowledge using operational scenario patterns. ProPlan was applied on data of a German organization within civil protection and predicts weather-based crisis events for the next 7 days in combination with automated planning recommendations. We plan to evaluate the effectiveness of the instantiated service within a qualitative study in the future.

## ProPlan: Model overview

![Screenshot 2023-08-01 at 23 43 22](https://github.com/InformationServiceSystems/pairs-project/assets/65232571/cee41361-f87c-4937-a8b9-2ba81231b5c3)


## Operational Scenario Patterns

Operational Scenario Patterns(OPS) semantically enhance historical knowledge on crisis operations. OPS build up on the works of [1,2}, describing scenario patterns as representation of crisis events [3,4,5,6,7,8,9,10,11]. We adjusted naming conventions and entities based on existing ontologies and requirements of operations within civil protection and related domains [12,13,14]. OPS contain the following entities and use existing semantic vocabularies and ontologies, such as [foaf](http://xmlns.com/foaf/0.1/), [beAware](https://github.com/beAWARE-project/ontology), [LODE](https://linkedevents.org/ontology), [Empathi](https://w3id.org/empathi/1.0), [schema.org](http://schema.org), to transfer historical data into a knowledge graph operationalized in JSON-LD.
The resulting knowledge graph is used as foundation in order to generate planning recommendations for predicted crisis events.

![ScenarioPatternTHW drawio (9)](https://github.com/InformationServiceSystems/pairs-project/assets/65232571/0907132e-2058-4368-a541-47dd1486db5f)

## German Federal Agency for Technical Relief
Our model was instantiated as a service in cooperation with the German Federal Agency for Technical Relief (German abbreviation 'THW'), an agency of the German Federal Ministry of the Interior and Community. Operation options include e.g. debris clearance, electricity supply, bridge building, refugee aid or logistics, which serve the general purpose of maintaining public structures and critical infrastructure. Furthermore, THW units can be requested to aid operations of external organizations (e.g., fire departments). Presently, operation plans at THW are compiled manually by planning officers in combination with weather forecasts (i.e., a [German weather service](https://www.dwd.de/DE/Home/home_node.html) to have a rough estimate of incoming crisis events. Although THW collects historical information on conducted operations, reports can differ (i.e., regarding format, details on conducted tasks) and are stored within large data bases. Furthermore, general information on operation options and actions, units and resources are only available within unstructured textual documentations (PDF files). Historical data are therefore only of limited use to planning experts for allocating tasks and human resources to crisis operations and they currently depend on acquired knowledge to make planning decisions.

## Service Features
- Explorable knowledge graph representation of historical datasets in the form of OSP
- Crisis operation prediction for the next 7 days
- Recommendations for Operations Planning to handle crises events

## Data requirements
Our service accepts CSV files as initial data input. Data should contain the following information in order to be mapped onto OSP.

Operation data:

Data on personnel:

Data on units:

## Prediction of Crisis Operations
We predict rain and snow based events (i.e., snowfall, avalanches, frost), such as heavy rain and floods for 10 locations in Germany (Göttingen, Aachen, Trier, Augsburg, Biberach, Chemnitz, Regensburg, Neubrandenburg, Schwerin, Kiel): 
![MicrosoftTeams-imagec97461883700fae13698badebbd06679cd13df90686356f9bde747b1dbd64983](https://github.com/InformationServiceSystems/pairs-project/assets/65232571/de1564d0-fbb5-402d-8fb5-fcd916f47847)

We tested several forecasting models, while XGBoost outperformed all other models in terms of overall accuracy and F1 scores per event type.

To enable early planning of operations, we included a early prediction of crisis operations focusing on weather-dependent events (e.g., rain, snow, landslides, wild fires), as these almost cover 24\% of the overall historical data set on THW operations. We adapted the approach used in \cite{Janzen2023,Gdanitz2023} for our prediction, using historical weather data \footnote{\url{https://www.kaggle.com/datasets/noaa/gsod?select=gsod2019}} (e.g., coordinates of weather station, temperature, wind speed, gust, precipitation). We calculated the coordinates of each historical operation location using the Geopy library, in order to map operations to the closest weather station using Euclidean distance. The event prediction was treated as a multi-class classification problem. The data set was divided into training, validation and test set with a ratio of 70:10:20. We experimented with different forecasting models, while XGBoost outperformed all other models in terms of overall accuracy (0.92) (see fig. \ref{fig: eventPred2}) and f1-score per event type \footnote{F1 score is an essential metric that combines precision (correct predictions per class) and recall (completeness of correct predictions per class) into a single value, providing a comprehensive evaluation of a model's performance}(see fig. \ref{fig: eventPred}). Based on the amount of available data per weather-dependent crisis event, we needed to cluster similar events in order to increase data quality. We were able to receive best F1-scores for rain based event types (0.9) (i.e., heavy rain and flood events) and snow event types (0.94) (i.e., snowfall, avalanches, frost). All other events within the THW data set (e.g., wildfires, landslides, but also weather-independent events) were furthermore clustered within the class 'other events' (0.86). Based on selected location of the user (see fig. \ref{fig: approach}), the forecasting model is applied to current weather data \footnote{\url{https://openweathermap.org/}} in order to generate an event prediction for the next 7 days.  The event prediction was evaluated for 10 THW locations across Germany (i.e., Göttingen, Aachen, Trier, Augsburg, Biberach, Chemnitz, Regensburg, Neubrandenburg, Schwerin, Kiel) within our service prototype \footnote{TODO Github Link, Link to screencast}

Table1: Comparison of achieved accuracy by diverse forecasting models
<img width="650" alt="TableEventPred" src="https://github.com/InformationServiceSystems/pairs-project/assets/65232571/39719731-58c4-488d-8c40-9885c1170f04">

Table 2: Classification results of different models on predicting crisis events in Germany (P = precision, R = recall, F1 = f1 score)
<img width="635" alt="TableEventPred2" src="https://github.com/InformationServiceSystems/pairs-project/assets/65232571/e72c5982-e341-4ee3-bb85-e21cb43ab3be">




## Screencast
A screencast of the service (including event prediction and generated recommendations) can be viewed here:

## References
[1] S. Janzen, N. Gdanitz, L. Abdel Khaliq, T. Munir, C. Franzius, W. Maass. (2023). Anticipating Energy-driven Crises in Process Industry by AI-based Scenario Planning, HICSS (2023). <br>
[2] S. Leachu, J. Janßen, N. Gdanitz, M. Kirchhöfer, S. Janzen. (2023). Cascading Scenario Technique enabling Automated and Situation-based Crisis Management, CPSL (2023). <br>
[3] Watahiki, K., & Saeki, M. (2001). Scenario evolution in requirements elicitation processes: scenario pattern and framework approach. In Proceedings of the 4th International Workshop on Principles of Software Evolution (pp. 166-169). <br>
[4] Watahiki, K., & Saeki, M. (2001). Scenario patterns based on case grammar approach. Proc. of Fifth IEEE Int. Symposium on Requirements Engineering, 300–301. <br>
[5] Alspaugh, T. A., Anto ́n, A. I., Barnes, T., & Mott, B. W. (1999). An integrated scenario management strategy. Proc. of IEEE Int. Symposium on Requirements Engineering (Cat. No. PR00188), 142–149. <br>
[6] Do Prado Leite, J. C. S., Hadad, G. D., Doorn, J. H., & Kaplan, G. N. (2000). A scenario construction process. Requirements Engineering, 5(1), 38–61. <br>
[7] Hoekstra, R. (2009). Ontology representation: Design patterns and ontologies that make sense. University of Amsterdam. <br>
[́8] Smiałek,M. (2007). Software development with reusable requirements-based cases. Oficyna Wydawnicza Politechniki Warszawskiej. <br>
[9] Tsai, W.-T., Yu, L., Zhu, F., & Paul, R. (2005). Rapid embedded system testing using verification patterns. IEEE software, 22(4), 68–75. <br>
[10] Rolland, C., Ben Achour, C., Cauvet, C., Ralyte ́, J., Sutcliffe, A., Maiden, N., Jarke, M., Haumer, P., Pohl, K., Dubois, E., et al. (1998). A proposal for a scenario classification framework. Requirements Engineering, 3(1), 23–47. <br>
[11] Xie, Z., Jayanth, A., Yadav, K., Ye, G., & Hong, L. (2021). Multi-faceted classification for the identification of informative communications during crises: Case of covid-19. 2021 IEEE 45th Annual Computers, Software, and Applications Conference (COMPSAC), 924–933. <br>
[12] E. Kontopoulos, P. Mitzias, J. Moßgraber, P. Hertweck, et al., Ontology-based representation of crisis management procedures for climate events., in: ISCRAM, 2018. <br>
[13] M. Gaur, S. Shekarpour, A. Gyrard, A. Sheth, Empathi: An ontology for emergency managing and planning about hazard crisis, in: ICSC, IEEE, 2019, pp. 396–403. <br>
[14] S. Chehade, N. Matta, J.-B. Pothin, R. Cogranne, Data interpretation support in rescue operations: Application for french firefighters, in: AICCSA, IEEE, 2018, pp. 1–6 <br>

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
