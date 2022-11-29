## Hidden Problem Detector (Step 4 of 4 to detect hidden problems within the supply chain)
## Collect the most critical components and generate a user-report


import logging
import sys
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math
import datetime as dt
from datetime import datetime as datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import plotly.express as px
import locale
locale.setlocale(locale.LC_NUMERIC, "german")

# The bolt-port can also be different for your DBMS - I assume that the Bolt-port is the standard 7687-port and the password
# for the DBMS is 'password'. The sub-functions to communicate with the Graph-Database are in the python-file 'Graph-Database'
from modules import Graph_Database as db
graph = db.Graph('bolt://localhost:7687', 'neo4j', 'password')
graph.enable_log(logging.INFO, sys.stdout)

## 1. Read the historical-data
## The historical data is an xlsx.-file wich has the following specifications

# - Component-ID --> The column contains the component ID's
# - median_price_1000 column--> current median price (in dollar) for 1000 pieces of the components
# - total_avail column --> current market availability for the components
# - estimated_factory_lead_days column --> estimated lead time (in days) for the component
# - date --> denotes the date when the information was retrieved

import pandas as pd
import glob
path = 'octopart_data'
file_path = glob.glob(path + "/historical_data.xlsx")
historical_data = pd.read_excel(file_path[0])
print(historical_data)

## 2. Get the most cricital components
## By analyzing the criticality distribution (Outlier-Detection via Boxplot-Diagramm) the criticality score 4.15 was detected as treshold
## components with an criticality score with 4.15 or higher can bee seen as the most critical components. The sub-function 
## "get_mostImportantNodes", retrieve all component nodes with an criticality score greater or equal to 4.15, which provide 
## information about the median_price, the total availability and the lead-time. Only those compoents are consideres, 
## which has an database.

result = graph.get_mostImportant_Nodes('neo4j')
most_critical = pd.DataFrame(result, columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)'])
print(most_critical)

## 3. Create the user report
## The historical data + the most critical components could be used to create a user-report, which contains the following information

# - Tables for the median-price, the total-availability and the factory-lead-days. The tables show how the values 
# for lead time, price and market availabiltiy for the most critical components change over a certain time-horizon (30 days).
#  The value befor 30 days and the current value are compared, and the change in percent is displayed (performance of the value).
# 
# The second part of the report is a graph which displays the change of the values for the time-horizon


# 3.1 Filter the historical data for values regarding the last 30 days
historical = historical_data.copy()
historical['date'] = pd.to_datetime(historical_data['date'], format= '%d.%m.%Y').dt.date
today = dt.date.today()
month_ago = today - dt.timedelta(days=30)
historical = historical[(historical['date'] <= today) & (historical['date'] >= month_ago)]

# 3.2 Filter the historical data on the most critical components
list_of_important_nodes = most_critical['Component ID'].tolist()
df = historical[historical['Component ID'].isin(list_of_important_nodes)]

# --> df is now the dataframe that contains the historical data for the last 30 days and considering only the most critical components

# 3.3 Calculate the value performance of the last 30 days for the most critical components
price_performance = list()
avail_performance = list()
lead_day_performance = list()
from_price = list()
to_price = list()
from_avail = list()
to_avail = list ()
from_time = list()
to_time = list()

for node in most_critical['Component ID']:
    node_data = historical[historical['Component ID'].isin([node])]
        
    #Median price performance
    change_price = str(round((((node_data['median_price_1000'].iloc[-1] -
                            node_data['median_price_1000'].iloc[0])/ 
                        node_data['median_price_1000'].iloc[0]) * 100),2)) + ' %'
        
        
    if change_price == 'nan %': change_price = 'No results'
    price_performance.append(change_price)
            
        
    from_ = str(node_data['median_price_1000'].iloc[0])
    to_ = str(node_data['median_price_1000'].iloc[-1])
    if from_ == 'nan': from_ = 'No results'
    if to_ == 'nan': to_ = 'No results'
    
    from_price.append(from_)
    to_price.append(to_)
        
        
    #Availability perfomance
    try: 
        change_avail = str(round((((node_data['total_avail'].iloc[-1] -
                            node_data['total_avail'].iloc[0])/ 
                        node_data['total_avail'].iloc[0]) * 100),2)) + ' %'
            
        if change_avail == 'nan %': change_avail = 'No results'
        avail_performance.append(change_avail)
            
        from_ = locale.format_string("%.2f", node_data['total_avail'].iloc[0] , grouping = True)
        to_ = locale.format_string("%.2f", node_data['total_avail'].iloc[-1] , grouping = True)
        if from_ == 'nan': from_ = 'No results'
        if to_ == 'nan': to_ = 'No results'
        
        from_avail.append(from_)
        to_avail.append(to_)
                
    except ZeroDivisionError: avail_performance.append('0.0 %')
            
    #Lead_Time performance
    change_time = str(round((((node_data['estimated_factory_lead_days'].iloc[-1] -
                            node_data['estimated_factory_lead_days'].iloc[0])/ 
                        node_data['estimated_factory_lead_days'].iloc[0]) * 100),2)) + ' %'
        
        
    if change_time == 'nan %': change_time = 'No results'
    lead_day_performance.append(change_time)
        
    from_ = str(node_data['estimated_factory_lead_days'].iloc[0])
    to_ = str(node_data['estimated_factory_lead_days'].iloc[-1])
        
    if from_ == 'nan': from_ = 'No results'
    if to_ == 'nan': to_ = 'No results'
    from_time.append(from_)
    to_time.append(to_)

#3.4 Get the categories for the most critical components
    category_list = list()
    
    for node in most_critical['Component ID']:
        
        # To get the categories for each critical component, we retrieve this information from the graph
        # The sub-function "get_category" is in the Graph_Databyse.py file. I assume that the graph is stored in
        # the database named 'HDP'
        categories = graph.get_category('HDP',node)

        # It could be that no category, exactly one category or more than one category for one component is found
        if len(categories) == 0:
            category_list.append('No results')
            
        if len(categories) == 1:
            category_list.append(categories[0])
            
        if len(categories) > 1:
            category_list.append(" ,".join(categories))

#3.5 Get the manfuacturer for the most critical components
    manufacturer_list = list()
    
    for node in most_critical['Component ID']:
        
        # To get the manufacturers for each critical component, we retrieve this information from the graph
        # The sub-function "get_manfuacturer" is in the Graph_Databyse.py file. I assume that the graph is stored in
        # the database named 'HDP'
        manufacturer = graph.get_manufacturer('HDP',node)

        # It could be that no manufacturer, exactly one manufacturer or more than one manufacturer for one compoent is found
        if len(manufacturer) == 0:
            manufacturer_list.append('No results')
            
        if len(manufacturer) == 1:
            manufacturer_list.append(manufacturer[0])
            
        if len(manufacturer) > 1:
            manufacturer_list.append(" ,".join(manufacturer))

#3.6 Create the plot
#Create the plots
    fig_median_price = px.line(df, x = 'date', y = 'median_price_1000', color = 'Component ID', markers=True)
    fig_avail = px.line(df, x = 'date', y = 'total_avail', color = 'Component ID', markers=True)
    fig_lead_days = px.line(df, x = 'date', y = 'estimated_factory_lead_days', color = 'Component ID', markers=True)
   
    
    #Break down the express figures into it's traces to plot them in differen subplots
    fig_median_price_traces = []
    fig_avail_traces = []
    fig_lead_days_traces = []
    
    for trace in range(len(fig_median_price["data"])):
        fig_median_price_traces.append(fig_median_price["data"][trace])
    
    for trace in range(len(fig_avail["data"])):
        fig_avail_traces.append(fig_avail["data"][trace])
    
    for trace in range(len(fig_lead_days["data"])):
        fig_lead_days_traces.append(fig_lead_days["data"][trace])

    #Create the Subplots
    figure = make_subplots( rows=3, cols=2 ,subplot_titles=("Median-Price Performance: Last 30-Days", 
                                                           "30-Day Trend: Median-Price", 
                                                           "Total Availability Performance: Last 30-Days", 
                                                           "30-Day Trend: Total Availability",
                                                           "Factory Lead-Day Performance: Last 30-Days",
                                                          "30-Day Trend: Factory Lead-Days"),
                          specs=[[{"type": "table"},{"type":"scatter"}],
           [{"type": "table"}, {"type": "scatter"}],
           [{"type": "table"}, {"type": "scatter"}]])
    
    figure.update_layout(height=1000, 
                         width=1250, 
                         title_text="30-Days Trend of supply chain KPI's", 
                         title_x = 0.5, 
                         title_y = 0.98,
                        legend_title_text='Components',
                        legend_y = 0.5)
    
    
    for traces in fig_median_price_traces:
        figure.append_trace(traces, row=1, col=2)
    
    for traces in fig_avail_traces:
        traces.showlegend = False
        figure.append_trace(traces, row=2, col=2)
    
    for traces in fig_lead_days_traces:
        traces.showlegend = False
        figure.append_trace(traces, row=3, col=2)
     
    figure.add_trace(go.Table(header=dict(values=['Component ID', 'Performance', 'Value before 30 Days', 'Current value', 'Category', 'Manufacturer']),
                 cells=dict(values=[list_of_important_nodes, price_performance, from_price, to_price, category_list, manufacturer_list])), row = 1, col = 1)

    
    figure.add_trace(go.Table(header=dict(values=['Component ID', 'Performance', 'Value before 30 Days', 'Current value', 'Category', 'Manufacturer']),
                 cells=dict(values=[list_of_important_nodes, avail_performance, from_avail, to_avail, category_list, manufacturer_list])), row = 2, col = 1)
    
    figure.add_trace(go.Table(header=dict(values=['Component ID', 'Performance', 'Value before 30 Days', 'Current value', 'Category', 'Manufacturer']),
                 cells=dict(values=[list_of_important_nodes, lead_day_performance, from_time, to_time, category_list, manufacturer_list])), row = 3, col = 1)

figure.show()