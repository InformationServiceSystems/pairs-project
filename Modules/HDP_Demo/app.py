#Libraries for Flask
import os
from tokenize import String
from flask import Flask, session, request, redirect, url_for, render_template, flash, Response
from werkzeug.utils import secure_filename


# Python libraries for Hidden_Problem_Detector
import pandas as pd
import logging
import sys
import glob
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from graphdatascience import GraphDataScience
from operator import itemgetter
import json
from datetime import datetime as datetime
from datetime import timedelta as timedelta
from datetime import date as date
import locale
import os
locale.setlocale(locale.LC_NUMERIC, "german")
import numpy as np


#Other Python Modules
from modules import Graph_Database as db
from modules import Data_Preparation as prepare

#Global Variables
dbname = 'neo4j'
prepare = prepare.Data_Preparation()
added_data = list()

#Initialize the Neo4j GraphDatabase
graph = db.Graph('bolt://localhost:7687', 'neo4j', 'password')
graph.enable_log(logging.INFO, sys.stdout)
gds = GraphDataScience('bolt://localhost:7687', auth = ('neo4j','password'))
gds.set_database(dbname)


app = Flask(__name__)
UPLOAD_FOLDER = 'files'
UPLOAD_MARKET = 'octopart_data'
ALLOWED_EXTENSIONS = {'xlsx'}
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = 'my_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_MARKET'] = UPLOAD_MARKET


def prepare_summary_report(list_of_most_important_components,from_string,to_string):
    
    #Prepare everything for the summarize report
    summary_price = list()
    summary_avail = list()
    summary_lead = list()
    price_table_summary = list()
    avail_table_summary = list()
    lead_table_summary = list()
    component_table_summary = list()
    seller_list = list()
    time = list()

    minimal_time_point = ""
    maximal_time_point = ""

    
    for componentid in list_of_most_important_components:

        #Get the historical data

        historical_data = pd.read_excel('octopart_data/historical_data.xlsx').drop('Unnamed: 0', axis = 1)
        print(historical_data)
        historical_data.rename(columns={'SICK ID': 'Component ID'}, inplace=True)

        #Time Horizon
        today = datetime.strptime(to_global,'%Y-%m-%d').date()
        month_ago = datetime.strptime(from_global,'%Y-%m-%d').date()

        #Filter historical data on component id
        df = historical_data[historical_data['Component ID'] == componentid]

        #Filter historical data on time horizon
        df['date'] = pd.to_datetime(df['date'], format= '%d.%m.%Y').dt.date
        df = df[(df['date'] <= today) & (df['date'] >= month_ago)]

        price = df['median_price_1000'].tolist()
        avail = df['total_avail'].tolist()
        lead = df['estimated_factory_lead_days'].tolist()
        time =  list(map( lambda x: x.strftime("%Y-%m-%d"), df['date'].tolist() ))

        #Data Preperation for the Summarize overview
        price_current_component = [list(x) for x in zip(time, price)]
        avail_current_component = [list(x) for x in zip(time, avail)]
        lead_current_component = [list(x) for x in zip(time, lead)]


        try: minimal_time_point = df["date"].iloc[0]
            
        except IndexError:
            flash('The uploaded historical market data does not cover the current set time horizon')
            decision_data = {}
            return decision_data

        minimal_time_point = df["date"].iloc[0]
        minimal_time_point = minimal_time_point.strftime("%d.%m.%Y")
        print(minimal_time_point)

        maximal_time_point = df["date"].iloc[-1]
        maximal_time_point = maximal_time_point.strftime("%d.%m.%Y")
        print(maximal_time_point)

        #if decision_data is empyt just concatenate else extend the lists with the first element of the current price

        if len(summary_price) == 0:
            summary_price = price_current_component
        else:
            for element in summary_price:
                element.append(price.pop(0))

        if len(summary_lead) == 0:
            summary_lead = lead_current_component
        else:
            for element in summary_lead:
                element.append(lead.pop(0))

        if len(summary_avail) == 0:
            summary_avail = avail_current_component
        else:
            for element in summary_avail:
                element.append(avail.pop(0))
            
        #Median price performance
        try:
            change_price = str(round((((df['median_price_1000'].iloc[-1] -
                                    df['median_price_1000'].iloc[0])/ 
                                df['median_price_1000'].iloc[0]) * 100),2)) + ' %'

        except IndexError: 

            flash('The uploaded historical market data does not cover the current set time horizon')
            decision_data = {}
            return decision_data
            
        if change_price == 'nan %': change_price = 'No results'
               
            
        from_ = str(df['median_price_1000'].iloc[0])
        to_ = str(df['median_price_1000'].iloc[-1])
        if from_ == 'nan': from_ = 'No results'
        if to_ == 'nan': to_ = 'No results'

        # Add the data for price table
        price_table_summary.append([componentid,change_price,from_,to_])
            
            
        #Availability perfomance
        try: 
            change_avail = str(round((((df['total_avail'].iloc[-1] -
                                df['total_avail'].iloc[0])/ 
                            df['total_avail'].iloc[0]) * 100),2)) + ' %'
                
            if change_avail == 'nan %': change_avail = '0.0%'
                
            from_ = locale.format_string("%.2f", df['total_avail'].iloc[0] , grouping = True)
            to_ = locale.format_string("%.2f", df['total_avail'].iloc[-1] , grouping = True)
            if from_ == 'nan': from_ = 'No results'
            if to_ == 'nan': to_ = 'No results'

            avail_table_summary.append([componentid,change_avail,from_,to_])
                    
        except ZeroDivisionError: 

            if(from_ == to_): avail_table_summary.append([componentid,'0.0%',from_, to_])
            
            avail_table_summary.append([componentid,'0.0 %',from_,to_])
                
        #Lead_Time performance
        change_time = str(round((((df['estimated_factory_lead_days'].iloc[-1] -
                                df['estimated_factory_lead_days'].iloc[0])/ 
                            df['estimated_factory_lead_days'].iloc[0]) * 100),2)) + ' %'
            
            
        if change_time == 'nan %': change_time = 'No results'
            
        from_ = str(df['estimated_factory_lead_days'].iloc[0])
        to_ = str(df['estimated_factory_lead_days'].iloc[-1])
            
        if from_ == 'nan': from_ = 'No results'
        if to_ == 'nan': to_ = 'No results'

        lead_table_summary.append([componentid,change_time,from_,to_])
                
        #Get the category
        category_list = list()
        
            
        category = graph.get_category(dbname,componentid)
        if len(category) == 0:
            category_list.append('No results')
                
        if len(category) == 1:
            category_list.append(category[0])
                
        if len(category) > 1:
            category_list.append(" ,".join(category))


        #Get Single Source Property
        single_source_property = graph.get_singlesource(dbname,componentid)[0]

               
                
        #Get the manufacturers for the most important nodes:
        manufacturer_list = list()     
        manufacturer = graph.get_manufacturer(dbname,componentid)
        if len(manufacturer) == 0:
            manufacturer_list.append('No results')
                
        if len(manufacturer) == 1:
            manufacturer_list.append(manufacturer[0])
                
        if len(manufacturer) > 1:
            manufacturer_list.append(" ,".join(manufacturer))

        component_table_summary.append([componentid,','.join(category_list), ','.join(manufacturer_list), single_source_property])

        #Get the seller for the most important nodes:
        seller = str(graph.get_seller(dbname,componentid))
        seller_list.append([componentid,seller])

    #The data of the summary report is finish now
    #Add column_names to the summary report data

    chart_columns = list_of_most_important_components.copy()
    chart_columns.insert(0,'Time')
    summary_price.insert(0,chart_columns)
    summary_avail.insert(0,chart_columns)
    summary_lead.insert(0,chart_columns)
    price_table_summary.insert(0,['Component ID','Change', minimal_time_point, maximal_time_point])
    avail_table_summary.insert(0,['Component ID','Change', minimal_time_point, maximal_time_point])
    lead_table_summary.insert(0,['Component ID','Change', minimal_time_point,  maximal_time_point])
    component_table_summary.insert(0,['Component ID','Category','Manufacturer','Single Source'])

    decision_data = {'price_chart':summary_price, 'time':time, 'avail_chart':summary_avail, 'lead_chart':summary_lead,
        'price_table': price_table_summary, 'avail_table': avail_table_summary, 'lead_table': lead_table_summary,
        'component_table': component_table_summary, 'idents': list_of_most_important_components, 'from_date': from_string, 'to_date': to_string, 'sellers': seller_list}
    
    return decision_data
    

# ------------- Show the index.html ---------------------------------------------
# Method to show the index.html
@app.route('/', methods=['GET', 'POST'])
def index():

    #Alle Indexaktionen

    print("Wurde enriched?")


    files_available = glob.glob('files' + "/*.xlsx")
    filenames_available = []
    for file in files_available:
        filenames_available.append(file.split('\\')[1])
    pass_avail_files = {'data': filenames_available}
    files_selected = glob.glob('work' + "/*.xlsx")
    filenames_selected = []
    for file in files_selected:
        filenames_selected.append(file.split('\\')[1])
    pass_selected_files = {'data':filenames_selected}


    #All Filenames from BOMS to create delete options
    all_file_names = os.listdir('work')[1::]
    all_file_names.extend(os.listdir('files')[1::])
    pass_all_file_names = {'data': all_file_names}

    #All Filenames from Component data to create delete options
    all_component_names = os.listdir('octopart_data')[1::]
    pass_all_component_names = {'data': all_component_names}

    columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)']
    
    #Criticality-Threshold
    criticality_values = graph.get_criticality(dbname)

    try: q1 = np.quantile(criticality_values, .25)
    except IndexError: q1 = 0
    try: q3 = np.quantile(criticality_values, .75)
    except IndexError: q3 = 0
    iqr = q3-q1
    threshold = (q3+1.5*iqr)

    print("Hier kommt der Threshold")
    print(threshold)

    data = graph.get_mostImportant_Nodes(dbname, threshold)
    df = pd.DataFrame(data, columns=['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)'])
    list_of_most_important_components = df['Component ID'].values.tolist()
    row_data = list(df.values.tolist())

    #Der Zeitraum umfasst inital die letzten 30 Tage
    today = date.today()
    month_ago = today - timedelta(days = 30)
    today = today.strftime("%Y-%m-%d")
    month_ago = month_ago.strftime("%Y-%m-%d")

    global from_global 
    from_global = month_ago
    global to_global
    to_global = today

    
    current_time = ''
    try: from_global
    except NameError: current_time = 'Not set'
    try: to_global
    except NameError: current_time = 'Not set'

    if(current_time != 'Not set'):

        from_string = datetime.strptime(from_global, '%Y-%m-%d')
        from_string = from_string.strftime("%d.%m.%Y")
        to_string = datetime.strptime(to_global, '%Y-%m-%d')
        to_string = to_string.strftime("%d.%m.%Y")
        current_time = from_string + ' - ' + to_string

    

    try: from_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'BOM'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})
    try: to_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'BOM'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    try: pd.read_excel('octopart_data/historical_data.xlsx')
    except FileNotFoundError:
    #    flash("No historical market data are uploaded")
         return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'BOM'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})



    #Check if Komponenten Daten hochgeladen sind
    try: pd.read_excel('octopart_data/component_data.xlsx')
    except FileNotFoundError:
        decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'BOM'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    #Prepare the summary report
    decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
    component_data_columns = list(pd.read_excel('octopart_data/component_data.xlsx').columns.values)


    #Hole dir die Komponenten daten
    if "Unnamed: 0" in component_data_columns:
        component_data_columns.remove('Unnamed: 0')
    if "Component-ID" in component_data_columns:
        component_data_columns.remove('Component-ID')
    
    prop = component_data_columns[0]
    is_enriched = graph.is_enriched(dbname,prop)
    if is_enriched:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'BOM'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': component_data_columns}, search={})

    else:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'BOM'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})


# ------------- 0. Upload one or more Excel files -----------------------------------
# Method to check if the user upload an Excel file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/upload', methods=['GET', 'POST'])
def upload_files():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'files' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        uploaded_files = request.files.getlist('files')
        for file in uploaded_files:
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                #filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return redirect(url_for('index'))

@app.route('/upload_market', methods=['GET', 'POST'])
def upload_market_data():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'files' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        uploaded_files = request.files.getlist('files')
        for file in uploaded_files:
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                #filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_MARKET'], 'component_data.xlsx'))

    #Index-Seite vorbereiten
    files_available = glob.glob('files' + "/*.xlsx")
    filenames_available = []
    for file in files_available:
        filenames_available.append(file.split('\\')[1])
    pass_avail_files = {'data': filenames_available}
    files_selected = glob.glob('work' + "/*.xlsx")
    filenames_selected = []
    for file in files_selected:
        filenames_selected.append(file.split('\\')[1])
    pass_selected_files = {'data':filenames_selected}


    #All Filenames from BOMS to create delete options
    all_file_names = os.listdir('work')[1::]
    all_file_names.extend(os.listdir('files')[1::])
    pass_all_file_names = {'data': all_file_names}

    #All Filenames from Component data to create delete options
    all_component_names = os.listdir('octopart_data')[1::]
    pass_all_component_names = {'data': all_component_names}

    columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)']
    
    #Criticality-Threshold
    criticality_values = graph.get_criticality(dbname)

    try: q1 = np.quantile(criticality_values, .25)
    except IndexError: q1 = 0
    try: q3 = np.quantile(criticality_values, .75)
    except IndexError: q3 = 0
    iqr = q3-q1
    threshold = (q3+1.5*iqr)

    data = graph.get_mostImportant_Nodes(dbname, threshold)
    df = pd.DataFrame(data, columns=['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)'])
    list_of_most_important_components = df['Component ID'].values.tolist()
    row_data = list(df.values.tolist())
    
    current_time = ''
    try: from_global
    except NameError: current_time = 'Not set'
    try: to_global
    except NameError: current_time = 'Not set'

    if(current_time != 'Not set'):

        from_string = datetime.strptime(from_global, '%Y-%m-%d')
        from_string = from_string.strftime("%d.%m.%Y")
        to_string = datetime.strptime(to_global, '%Y-%m-%d')
        to_string = to_string.strftime("%d.%m.%Y")
        current_time = from_string + ' - ' + to_string

    try: from_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})
    try: to_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    try: pd.read_excel('octopart_data/historical_data.xlsx')
    except FileNotFoundError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    #Check if Komponenten Daten hochgeladen sind
    try: pd.read_excel('octopart_data/component_data.xlsx')
    except FileNotFoundError:
        decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    #Prepare the summary report
    decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
    component_data_columns = list(pd.read_excel('octopart_data/component_data.xlsx').columns.values)


    #Hole dir die Komponenten daten
    if "Unnamed: 0" in component_data_columns:
        component_data_columns.remove('Unnamed: 0')
    if "Component-ID" in component_data_columns:
        component_data_columns.remove('Component-ID')
    
    prop = component_data_columns[0]
    is_enriched = graph.is_enriched(dbname,prop)
    if is_enriched:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': component_data_columns}, search={})

    else:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})


@app.route('/upload_historical_market', methods=['GET', 'POST'])
def upload_historical_market_data():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'files' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        uploaded_files = request.files.getlist('files')
        for file in uploaded_files:
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                #filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_MARKET'], 'historical_data.xlsx'))

    
    #Index-Seite vorbereiten
    files_available = glob.glob('files' + "/*.xlsx")
    filenames_available = []
    for file in files_available:
        filenames_available.append(file.split('\\')[1])
    pass_avail_files = {'data': filenames_available}
    files_selected = glob.glob('work' + "/*.xlsx")
    filenames_selected = []
    for file in files_selected:
        filenames_selected.append(file.split('\\')[1])
    pass_selected_files = {'data':filenames_selected}


    #All Filenames from BOMS to create delete options
    all_file_names = os.listdir('work')[1::]
    all_file_names.extend(os.listdir('files')[1::])
    pass_all_file_names = {'data': all_file_names}

    #All Filenames from Component data to create delete options
    all_component_names = os.listdir('octopart_data')[1::]
    pass_all_component_names = {'data': all_component_names}

    columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)']
    
    #Criticality-Threshold
    criticality_values = graph.get_criticality(dbname)

    try: q1 = np.quantile(criticality_values, .25)
    except IndexError: q1 = 0
    try: q3 = np.quantile(criticality_values, .75)
    except IndexError: q3 = 0
    iqr = q3-q1
    threshold = (q3+1.5*iqr)

    data = graph.get_mostImportant_Nodes(dbname, threshold)
    df = pd.DataFrame(data, columns=['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)'])
    list_of_most_important_components = df['Component ID'].values.tolist()
    row_data = list(df.values.tolist())
    
    current_time = ''
    try: from_global
    except NameError: current_time = 'Not set'
    try: to_global
    except NameError: current_time = 'Not set'

    if(current_time != 'Not set'):

        from_string = datetime.strptime(from_global, '%Y-%m-%d')
        from_string = from_string.strftime("%d.%m.%Y")
        to_string = datetime.strptime(to_global, '%Y-%m-%d')
        to_string = to_string.strftime("%d.%m.%Y")
        current_time = from_string + ' - ' + to_string

    try: from_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})
    try: to_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    try: pd.read_excel('octopart_data/historical_data.xlsx')
    except FileNotFoundError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})



    #Check if Komponenten Daten hochgeladen sind
    try: pd.read_excel('octopart_data/component_data.xlsx')
    except FileNotFoundError:
        decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    #Prepare the summary report
    decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
    component_data_columns = list(pd.read_excel('octopart_data/component_data.xlsx').columns.values)


    #Hole dir die Komponenten daten
    if "Unnamed: 0" in component_data_columns:
        component_data_columns.remove('Unnamed: 0')
    if "Component-ID" in component_data_columns:
        component_data_columns.remove('Component-ID')
    
    prop = component_data_columns[0]
    is_enriched = graph.is_enriched(dbname,prop)
    if is_enriched:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': component_data_columns}, search={})

    else:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})


@app.route('/FilesToWork',methods=['POST'])
def FilesToWork():
    output = request.get_json()
    result = json.loads(output) #this converts the json output to a python dictionary
    files = result['data']
    for element in files:
        os.replace('files/' + element, 'work/' + element)
    return redirect(url_for('index'))

@app.route('/WorkToFiles',methods=['POST'])
def WorkToFiles():
    output = request.get_json()
    result = json.loads(output) #this converts the json output to a python dictionary
    files = result['data']
    for element in files:
        os.replace('work/' + element, 'files/' + element)
    return redirect(url_for('index'))


# ------------- 1. Build up the graph -----------------------------------

def mapper_module():

    path = 'work'
    filenames = glob.glob(path + "/*.xlsx")

    if len(filenames) == 0:
        flash('No Bill of Materials are uploaded or selected')
        return redirect(url_for('index'))

    for file in filenames:
        file_dataframe = pd.read_excel(file)
        nodes = prepare.create_node_list(file_dataframe)
        component_manufacturer_list = prepare.get_manufacturer(file_dataframe)
        strength = prepare.calculate_strength(file_dataframe)
        relations = prepare.create_relation_list(file_dataframe)

        # Erstelle die Komponentenknoten in unserem Graphen
        for node in nodes:
            graph.create_component(node[0], dbname)

        # Erstelle die Komponentenrelationen zwischen den Komponentenknoten in unserem Graphen
        for relation in relations:
            graph.create_component_relation(relation[0], relation[1], dbname)

        # Update die Knotenstärke der Komponentenknoten in unserem Graphen
        for node in nodes:
            node_id = node[0]
            node_strength = strength[node_id]
            graph.update_strength(node_id, node_strength, dbname)

        for element in component_manufacturer_list:
            component_id = element[0]
            manufacturer_name = element[1]
            graph.create_manufacturer(component_id, manufacturer_name, dbname)



@app.route('/build_graph', methods=['GET', 'POST'])
def flask_set_up_graph():
    if request.method == 'POST':
        graph.delete_all(dbname)
        #Map the BOM into a graph structure
        mapper_module()
        #Remove the Graph Loops
        graph.remove_loops(dbname)
        #Calculate Out-Degree for 'isComponent'-Relations
        G, res = gds.graph.project("knowledge2", 'component', "isComponent")
        result = gds.degree.write(G, writeProperty='out_degree_components')
        gds.graph.drop(G)  # same as G.drop()
        #Calculate In-Degree for 'isComponent-Relations'
        G, res = gds.graph.project("knowledge2", 'component', "isComponent")
        result = gds.degree.write(G, writeProperty='in_degree_components', orientation='REVERSE')
        gds.graph.drop(G)  # same as G.drop()
        #Calculate In-Degree for 'isSubstitute-Relations'
        G, res = gds.graph.project("knowledge2", 'component', "isSubstitute")
        result = gds.degree.write(G, writeProperty='in_degree_substitute', orientation='REVERSE')
        gds.graph.drop(G)  # same as G.drop()
        #Calculate Betweenees-Centrality only for 'isComponent'-Relations
        G, res = gds.graph.project("knowledge2", 'component', "isComponent")
        result = gds.betweenness.write(G, writeProperty='betweeness', nodeLabels=['component'],
                                       relationshipTypes=['isComponent'])
        gds.graph.drop(G)  # same as G.drop()
        #Calculate Criticality
        graph.calculate_criticality(dbname)
        #Analyse der Komponenten auf Single-Source Eigenschaft (wenn True oder False wird als Node-Property gesetzt)
        graph.find_single_source(dbname)
        graph.move_component_crit_to_substitute(dbname)

        #Index-Seite vorbereiten
    files_available = glob.glob('files' + "/*.xlsx")
    filenames_available = []
    for file in files_available:
        filenames_available.append(file.split('\\')[1])
    pass_avail_files = {'data': filenames_available}
    files_selected = glob.glob('work' + "/*.xlsx")
    filenames_selected = []
    for file in files_selected:
        filenames_selected.append(file.split('\\')[1])
    pass_selected_files = {'data':filenames_selected}


    #All Filenames from BOMS to create delete options
    all_file_names = os.listdir('work')[1::]
    all_file_names.extend(os.listdir('files')[1::])
    pass_all_file_names = {'data': all_file_names}

    #All Filenames from Component data to create delete options
    all_component_names = os.listdir('octopart_data')[1::]
    pass_all_component_names = {'data': all_component_names}

    columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)']
    
    #Criticality-Threshold
    criticality_values = graph.get_criticality(dbname)

    try: q1 = np.quantile(criticality_values, .25)
    except IndexError: q1 = 0
    try: q3 = np.quantile(criticality_values, .75)
    except IndexError: q3 = 0
    iqr = q3-q1
    threshold = (q3+1.5*iqr)

    data = graph.get_mostImportant_Nodes(dbname, threshold)
    df = pd.DataFrame(data, columns=['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)'])
    list_of_most_important_components = df['Component ID'].values.tolist()
    row_data = list(df.values.tolist())
    
    current_time = ''
    try: from_global
    except NameError: current_time = 'Not set'
    try: to_global
    except NameError: current_time = 'Not set'

    if(current_time != 'Not set'):

        from_string = datetime.strptime(from_global, '%Y-%m-%d')
        from_string = from_string.strftime("%d.%m.%Y")
        to_string = datetime.strptime(to_global, '%Y-%m-%d')
        to_string = to_string.strftime("%d.%m.%Y")
        current_time = from_string + ' - ' + to_string

    try: from_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})
    try: to_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    try: pd.read_excel('octopart_data/historical_data.xlsx')
    except FileNotFoundError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})




    #Check if Komponenten Daten hochgeladen sind
    try: pd.read_excel('octopart_data/component_data.xlsx')
    except FileNotFoundError:
        decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    #Prepare the summary report
    decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
    component_data_columns = list(pd.read_excel('octopart_data/component_data.xlsx').columns.values)


    #Hole dir die Komponenten daten
    if "Unnamed: 0" in component_data_columns:
        component_data_columns.remove('Unnamed: 0')
    if "Component-ID" in component_data_columns:
        component_data_columns.remove('Component-ID')
    
    prop = component_data_columns[0]
    is_enriched = graph.is_enriched(dbname,prop)
    if is_enriched:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': component_data_columns}, search={})

    else:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})




# ------------- 2. Enrich the graph -----------------------------------
def update_componentNodes(dataframe, octopart_data, dbname):

    identlist = dataframe.values.tolist()
    octopart_data = octopart_data.to_dict()
    for ident in identlist:
        mpn = octopart_data['mpn'][ident]
        median_price = octopart_data['median_price_1000'][ident]
        total_avail = octopart_data['total_avail'][ident]
        graph.update_componentNode(ident, mpn, median_price, total_avail, dbname)

def update_manufacturers(dataframe, octopart_data, dbname):
    identlist = dataframe.values.tolist()
    octopart_data = octopart_data.to_dict()
    for ident in identlist:
        manufacturer = octopart_data['manufacturer_name'][ident]
        location = octopart_data['manufacturer_country'][ident]
        if (type(manufacturer) is str):
            manufacturer = manufacturer.upper()
        lead_days = octopart_data['estimated_factory_lead_days'][ident]
        graph.update_manufacturer(ident, manufacturer, lead_days, location, dbname)


def create_category(dataframe, octopart_data, dbname):
    identlist = dataframe.values.tolist()
    octopart_data = octopart_data.to_dict()
    for ident in identlist:
        category = octopart_data['category'][ident]
        graph.create_category(ident, category, dbname)

def create_seller(dataframe, octopart_data, dbname):
    identlist = dataframe.values.tolist()
    octopart_data = octopart_data.to_dict()
    for ident in identlist:
        sellers = octopart_data['sellers'][ident]
        sellers = eval(sellers)
        for seller in sellers:
            graph.create_seller(ident,seller,dbname)

@app.route('/enrich_graph',methods = ['GET','POST'])
def flask_enrich_graph():
    if request.method == 'POST':
        #get the octopart_data

        try: pd.read_excel('octopart_data/component_data.xlsx')
        except FileNotFoundError:
            flash('No component data uploaded')
            return redirect(url_for('index'))

        if 'Component-ID' in pd.read_excel('octopart_data/component_data.xlsx').columns:
            octopart_data = pd.read_excel('octopart_data/component_data.xlsx').drop('Unnamed: 0', axis = 1)
            octopart_data = octopart_data.set_index(octopart_data.columns[0])
        else: 
            octopart_data = pd.read_excel('octopart_data/component_data.xlsx')
            octopart_data = octopart_data.set_index(octopart_data.columns[0])
        droped = octopart_data.index.name = None

        print(octopart_data.columns)

        #concat all the uploaded files
        path = 'work'
        filenames = glob.glob(path + "/*.xlsx")
        df = pd.DataFrame()

        for file in filenames:
            file_dataframe = pd.read_excel(file)
            df = pd.concat([df,file_dataframe], ignore_index=True)

        df.drop_duplicates(subset=['IdentNr'])

        # Enrich the Graph with all necessary informations
        update_componentNodes(df['IdentNr'], octopart_data, dbname)
        update_manufacturers(df['IdentNr'], octopart_data, dbname)
        create_category(df['IdentNr'], octopart_data, dbname)
        create_seller(df['IdentNr'], octopart_data, dbname)
        

    #Index-Seite vorbereiten
    files_available = glob.glob('files' + "/*.xlsx")
    filenames_available = []
    for file in files_available:
        filenames_available.append(file.split('\\')[1])
    pass_avail_files = {'data': filenames_available}
    files_selected = glob.glob('work' + "/*.xlsx")
    filenames_selected = []
    for file in files_selected:
        filenames_selected.append(file.split('\\')[1])
    pass_selected_files = {'data':filenames_selected}


    #All Filenames from BOMS to create delete options
    all_file_names = os.listdir('work')[1::]
    all_file_names.extend(os.listdir('files')[1::])
    pass_all_file_names = {'data': all_file_names}

    #All Filenames from Component data to create delete options
    all_component_names = os.listdir('octopart_data')[1::]
    pass_all_component_names = {'data': all_component_names}

    columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)']
    
    #Criticality-Threshold
    criticality_values = graph.get_criticality(dbname)

    try: q1 = np.quantile(criticality_values, .25)
    except IndexError: q1 = 0
    try: q3 = np.quantile(criticality_values, .75)
    except IndexError: q3 = 0
    iqr = q3-q1
    threshold = (q3+1.5*iqr)

    data = graph.get_mostImportant_Nodes(dbname, threshold)
    df = pd.DataFrame(data, columns=['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)'])
    list_of_most_important_components = df['Component ID'].values.tolist()
    row_data = list(df.values.tolist())
    
    current_time = ''
    try: from_global
    except NameError: current_time = 'Not set'
    try: to_global
    except NameError: current_time = 'Not set'

    if(current_time != 'Not set'):

        from_string = datetime.strptime(from_global, '%Y-%m-%d')
        from_string = from_string.strftime("%d.%m.%Y")
        to_string = datetime.strptime(to_global, '%Y-%m-%d')
        to_string = to_string.strftime("%d.%m.%Y")
        current_time = from_string + ' - ' + to_string

    try: from_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})
    try: to_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    try: pd.read_excel('octopart_data/historical_data.xlsx')
    except FileNotFoundError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})




    #Check if Komponenten Daten hochgeladen sind
    try: pd.read_excel('octopart_data/component_data.xlsx')
    except FileNotFoundError:
        decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    #Prepare the summary report
    decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
    component_data_columns = list(pd.read_excel('octopart_data/component_data.xlsx').columns.values)


    #Hole dir die Komponenten daten
    if "Unnamed: 0" in component_data_columns:
        component_data_columns.remove('Unnamed: 0')
    if "Component-ID" in component_data_columns:
        component_data_columns.remove('Component-ID')
    
    prop = component_data_columns[0]
    is_enriched = graph.is_enriched(dbname,prop)
    if is_enriched:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': component_data_columns}, search={})

    else:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Graph'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

# ------------ 3. Generate Decision Support -------------------------------

@app.route('/decision', methods = ['GET','POST'])
def flask_decision():

    componentid = request.form.to_dict()['input']
    ident = componentid


    """
    try: from_global
    except NameError:
        flash('Please set the time horizon on the Deep Dive tab to get a decision support')
        return redirect(url_for('index'))
    try: to_global
    except NameError:
        flash ('Please set the time horizon on the Deep Dive tab to get a decision support')
        return redirect(url_for('index'))

    """

    #Get the historical data

    try: pd.read_excel('octopart_data/historical_data.xlsx').drop('Unnamed: 0', axis = 1)
    except FileNotFoundError:
        flash('No historical market data uploaded')
        return redirect(url_for('index'))

    historical_data = pd.read_excel('octopart_data/historical_data.xlsx').drop('Unnamed: 0', axis = 1)
    historical_data.rename(columns={'SICK ID': 'Component ID'}, inplace=True)

    #Time Horizon
    from_string = datetime.strptime(from_global, '%Y-%m-%d')
    from_string = from_string.strftime("%d.%m.%Y")
    to_string = datetime.strptime(to_global, '%Y-%m-%d')
    to_string = to_string.strftime("%d.%m.%Y")

    #Create Detail Report
    decision_search = prepare_summary_report([ident],from_string,to_string)

    files_available = glob.glob('files' + "/*.xlsx")
    filenames_available = []
    for file in files_available:
        filenames_available.append(file.split('\\')[1])
    pass_avail_files = {'data': filenames_available}
    files_selected = glob.glob('work' + "/*.xlsx")
    filenames_selected = []
    for file in files_selected:
        filenames_selected.append(file.split('\\')[1])
    pass_selected_files = {'data':filenames_selected}

    columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)']

    #Criticality-Threshold
    criticality_values = graph.get_criticality(dbname)
    try: q1 = np.quantile(criticality_values, .25)
    except IndexError: q1 = 0
    try: q3 = np.quantile(criticality_values, .75)
    except IndexError: q3 = 0
    iqr = q3-q1
    threshold = (q3+1.5*iqr)

    print()

    
    data = graph.get_mostImportant_Nodes(dbname,threshold)
    df = pd.DataFrame(data, columns=['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)'])
    list_of_most_important_components = df['Component ID'].values.tolist()
    row_data = list(df.values.tolist())

    current_time = ''

    """
    try: from_global
    except NameError: current_time = 'Not set'
    try: to_global
    except NameError: current_time = 'Not set'

    """

    if(current_time != 'Not set'):

        from_string = datetime.strptime(from_global, '%Y-%m-%d')
        from_string = from_string.strftime("%d.%m.%Y")
        to_string = datetime.strptime(to_global, '%Y-%m-%d')
        to_string = to_string.strftime("%d.%m.%Y")
        current_time = from_string + ' - ' + to_string

    #All Filenames to create delete options
    all_file_names = os.listdir('work')[1::]
    all_file_names.extend(os.listdir('files')[1::])
    pass_all_file_names = {'data': all_file_names}

    #All Filenames from Component data to create delete options
    all_component_names = os.listdir('octopart_data')[1::]
    pass_all_component_names = {'data': all_component_names}

    #Check if Komponenten Daten hochgeladen sind
    try: pd.read_excel('octopart_data/component_data.xlsx')
    except FileNotFoundError:
        decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_search"}, added_data={'data': []}, search = decision_search)

    #Prepare the summary report
    decision_summary = prepare_summary_report(list_of_most_important_components, from_string, to_string)
    component_data_columns = list(pd.read_excel('octopart_data/component_data.xlsx').columns.values)

    #Hole dir die Komponenten daten
    if "Unnamed: 0" in component_data_columns:
        component_data_columns.remove('Unnamed: 0')
    if "Component-ID" in component_data_columns:
        component_data_columns.remove('Component-ID')
    
    prop = component_data_columns[0]
    is_enriched = graph.is_enriched(dbname,prop)
    if is_enriched:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_summary, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_search"}, added_data={'data': component_data_columns}, search=decision_search)

    else:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_summary, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_search"}, added_data={'data': []}, search=decision_search)


@app.route('/decision/<ident>')
def flask_decision2(ident):

    componentid = ident

    try: from_global
    except NameError:
        flash('Please set the time horizon on the Deep Dive tab to get a decision support')
        return redirect(url_for('index'))
    try: to_global
    except NameError:
        flash ('Please set the time horizon on the Deep Dive tab to get a decision support')
        return redirect(url_for('index'))

    #Get the historical data
    try: pd.read_excel('octopart_data/historical_data.xlsx').drop('Unnamed: 0', axis = 1)
    except FileNotFoundError:
        flash('No historical market data uploaded')
        return redirect(url_for('index'))

    historical_data = pd.read_excel('octopart_data/historical_data.xlsx').drop('Unnamed: 0', axis = 1)
    historical_data.rename(columns={'SICK ID': 'Component ID'}, inplace=True)


    #Time Horizon
    from_string = datetime.strptime(from_global, '%Y-%m-%d')
    from_string = from_string.strftime("%d.%m.%Y")
    to_string = datetime.strptime(to_global, '%Y-%m-%d')
    to_string = to_string.strftime("%d.%m.%Y")

    #Create Detail Report
    decision_data = prepare_summary_report([ident],from_string,to_string)

    files_available = glob.glob('files' + "/*.xlsx")
    filenames_available = []
    for file in files_available:
        filenames_available.append(file.split('\\')[1])
    pass_avail_files = {'data': filenames_available}
    files_selected = glob.glob('work' + "/*.xlsx")
    filenames_selected = []
    for file in files_selected:
        filenames_selected.append(file.split('\\')[1])
    pass_selected_files = {'data':filenames_selected}

    columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)']

    #Criticality-Threshold
    criticality_values = graph.get_criticality(dbname)
    try: q1 = np.quantile(criticality_values, .25)
    except IndexError: q1 = 0
    try: q3 = np.quantile(criticality_values, .75)
    except IndexError: q3 = 0
    iqr = q3-q1
    threshold = (q3+1.5*iqr)


    #Jetzt wird noch die decision summary erstellt
    data = graph.get_mostImportant_Nodes(dbname,threshold)
    df = pd.DataFrame(data, columns=['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)'])
    list_of_most_important_components = df['Component ID'].values.tolist()
    row_data = list(df.values.tolist())

    current_time = ''
    try: from_global
    except NameError: current_time = 'Not set'
    try: to_global
    except NameError: current_time = 'Not set'

    if(current_time != 'Not set'):

        from_string = datetime.strptime(from_global, '%Y-%m-%d')
        from_string = from_string.strftime("%d.%m.%Y")
        to_string = datetime.strptime(to_global, '%Y-%m-%d')
        to_string = to_string.strftime("%d.%m.%Y")
        current_time = from_string + ' - ' + to_string

    decision_summary = prepare_summary_report(list_of_most_important_components, from_string, to_string)

    #All Filenames to create delete options
    all_file_names = os.listdir('work')[1::]
    all_file_names.extend(os.listdir('files')[1::])
    pass_all_file_names = {'data': all_file_names}

    #All Filenames from Component data to create delete options
    all_component_names = os.listdir('octopart_data')[1::]
    pass_all_component_names = {'data': all_component_names}

    #Check if Komponenten Daten hochgeladen sind
    try: pd.read_excel('octopart_data/component_data.xlsx')
    except FileNotFoundError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = decision_data, current_time = current_time, decision_summary = decision_summary, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_critical_components"}, added_data={'data': []}, search={})


    component_data_columns = list(pd.read_excel('octopart_data/component_data.xlsx').columns.values)


    #Hole dir die Komponenten daten
    if "Unnamed: 0" in component_data_columns:
        component_data_columns.remove('Unnamed: 0')
    if "Component-ID" in component_data_columns:
        component_data_columns.remove('Component-ID')
    
    prop = component_data_columns[0]
    is_enriched = graph.is_enriched(dbname,prop)
    if is_enriched:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = decision_data, current_time = current_time, decision_summary = decision_summary, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_critical_components"}, added_data={'data': component_data_columns}, search={})

    else:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = decision_data, current_time = current_time, decision_summary = decision_summary, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_critical_components"}, added_data={'data': []}, search={})


@app.route('/set_dates', methods = ['GET','POST'])
def set_dates():

    dates = request.form.to_dict()
    from_date = dates['From']
    to_date = dates['To']
    global from_global 
    from_global = from_date
    global to_global 
    to_global = to_date

    from_string = datetime.strptime(from_global, '%Y-%m-%d')
    from_string = from_string.strftime("%d.%m.%Y")
    to_string = datetime.strptime(to_global, '%Y-%m-%d')
    to_string = to_string.strftime("%d.%m.%Y")
    current_time = from_string + ' - ' + to_string

    flash('The time horizon for the decision support is set on ' + current_time)
    #Alle Indexaktionen

    files_available = glob.glob('files' + "/*.xlsx")
    filenames_available = []
    for file in files_available:
        filenames_available.append(file.split('\\')[1])
    pass_avail_files = {'data': filenames_available}
    files_selected = glob.glob('work' + "/*.xlsx")
    filenames_selected = []
    for file in files_selected:
        filenames_selected.append(file.split('\\')[1])
    pass_selected_files = {'data':filenames_selected}


    #All Filenames from BOMS to create delete options
    all_file_names = os.listdir('work')[1::]
    all_file_names.extend(os.listdir('files')[1::])
    pass_all_file_names = {'data': all_file_names}

    #All Filenames from Component data to create delete options
    all_component_names = os.listdir('octopart_data')[1::]
    pass_all_component_names = {'data': all_component_names}

    columns = ['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)']
    
    #Criticality-Threshold
    criticality_values = graph.get_criticality(dbname)

    try: q1 = np.quantile(criticality_values, .25)
    except IndexError: q1 = 0
    try: q3 = np.quantile(criticality_values, .75)
    except IndexError: q3 = 0
    iqr = q3-q1
    threshold = (q3+1.5*iqr)

    data = graph.get_mostImportant_Nodes(dbname, threshold)
    df = pd.DataFrame(data, columns=['Component ID', 'Single-Source Property', 'Criticality', 'Strength', 'Out-Degree(components)', 'Betweeness', 'In-Degree(Substitute)', 'In-Degree(Components)'])
    list_of_most_important_components = df['Component ID'].values.tolist()
    row_data = list(df.values.tolist())
    
    current_time = ''
    try: from_global
    except NameError: current_time = 'Not set'
    try: to_global
    except NameError: current_time = 'Not set'

    if(current_time != 'Not set'):

        from_string = datetime.strptime(from_global, '%Y-%m-%d')
        from_string = from_string.strftime("%d.%m.%Y")
        to_string = datetime.strptime(to_global, '%Y-%m-%d')
        to_string = to_string.strftime("%d.%m.%Y")
        current_time = from_string + ' - ' + to_string

    try: from_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})
    try: to_global
    except NameError:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    try: pd.read_excel('octopart_data/historical_data.xlsx')
    except FileNotFoundError:
        flash("No historical market data is uploaded")
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = {}, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    #Check if Komponenten Daten hochgeladen sind
    try: pd.read_excel('octopart_data/component_data.xlsx')
    except FileNotFoundError:
        decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []}, search={})

    #Prepare the summary report
    decision_data = prepare_summary_report(list_of_most_important_components,from_global,to_global)
    component_data_columns = list(pd.read_excel('octopart_data/component_data.xlsx').columns.values)


    #Hole dir die Komponenten daten
    if "Unnamed: 0" in component_data_columns:
        component_data_columns.remove('Unnamed: 0')
    if "Component-ID" in component_data_columns:
        component_data_columns.remove('Component-ID')
    
    prop = component_data_columns[0]
    is_enriched = graph.is_enriched(dbname,prop)
    if is_enriched:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': component_data_columns},search={})

    else:
        return render_template('index.html', pass_avail_files = pass_avail_files, pass_selected_files = pass_selected_files,columns=columns, row_data_col=row_data, decision = {}, current_time = current_time, decision_summary = decision_data, pass_all_files = pass_all_file_names, pass_all_component = pass_all_component_names, tab={'data': 'Analyze'}, critical_components = {'data': list_of_most_important_components}, tab_side = {"data": "tab_alert"}, added_data={'data': []},search={})

# ------------- Delete the uploaded BOM ----------------------------------
@app.route('/delete_BOM', methods = ['GET','POST'])
def delete_BOM():
    
    file_name = request.form.to_dict()['todelete']
    if(os.path.exists('files/'+ file_name)):
        os.remove('files/'+ file_name)
        flash('The BOM ' + file_name + ' is deleted. Maybe you should also update your graph!')
        return redirect(url_for('index'))

    elif(os.path.exists('work/' + file_name)):
        os.remove('work/' + file_name)
        flash('The BOM ' + file_name + ' is deleted. Maybe you should also update your graph!')
        return redirect(url_for('index'))
    
    else:
        flash('The BOM ' + file_name + ' could not be found. Maybe you enter a wrong file name.')
        return redirect(url_for('index'))


# ------------- Delete the component data -------------------------------
@app.route('/delete_component_data', methods = ['GET','POST'])
def delete_component_data():

    file_name = request.form.to_dict()['todelete']
    if(os.path.exists('octopart_data/' + file_name)):
        os.remove('octopart_data/'+file_name)
        flash('The file ' + file_name + ' is deleted.')
        return redirect(url_for('index'))
    else:
        flash('The file' + file_name + ' could not be found. Maybe you enter a wrong file name.')
        return redirect(url_for('index'))




if __name__ == "__main__":
    app.run()