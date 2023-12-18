from django.shortcuts import render
from django.contrib import messages
from io import BytesIO
import base64

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import numpy as np
from .forms import UserInputForm
#from .tester import test
from .new_final import full_pipeline
import subprocess

# Create views here
def home_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            domain_specific_keyword = form.cleaned_data['domain_specific_keyword']
            #specific_alert_keyword = form.cleaned_data['specific_alert_keyword']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            country = form.cleaned_data['country']
            language = form.cleaned_data['language']
            
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')

            # Call functions in app.py with user inputs
            result = full_pipeline(domain_specific_keyword, start_date_str, end_date_str, country, language)
            
            # Create a success message
            messages.success(request, 'User Input loaded successfully')
            # Render the result in the template
            return render(request, 'home.html', {
                'form': form, 
                #"model_response": main(result), 
                "plot_alarm_system": plot_alarm_system(result, start_date_str, end_date_str)})
    else:
        form = UserInputForm()

    return render(request, 'home.html', {'form': form})


# Create views here
#def home_view(request, *args, **kwargs):
#    return render(request, 'home.html', {
#        "model_response": main(),
#        "plot_alarm_system": plot_alarm_system(),
#        "plot_statistical_trend_analysis": plot_statistical_trend_analysis()
#        })

def plot_alarm_system(alert_dict, start_date, end_date):
    # Extracting keys and values
    alert_types = list(alert_dict.keys())[1:4]
    values = list(alert_dict.values())[:4]
    percents = [round((value / values[0]) * 100, 2) for value in values][1:]
    
    x_labels = start_date + ' to ' + end_date
    
    # Custom colors for the bars
    colors = ['red', 'blue', 'orange']
    
    # Creating the bar plot
    plt.figure(figsize=(6, 4))
    bars = plt.bar(alert_types, percents, color=colors)
    plt.xlabel(x_labels, fontsize=14)
    plt.ylabel('Percentage', fontsize=14)

    # Set x-axis label as "August"
    plt.xticks([])  # Remove x-axis ticks
    plt.gca().xaxis.set_label_coords(0.5, -0.1)  # Adjust label position
    plt.xlabel(x_labels, labelpad=20,fontsize=12)  # Add x-axis label
    
    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_alarm = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_alarm

"""
def plot_statistical_trend_analysis(alert_dict):
    
    alert_labels = {
        'High alert': 'Risk and Warning',
        'Low alert': 'Caution and Advice',
        'Others': 'Safe and Harmless'
    }
    
    # Extracting keys and values
    alert_types = list(alert_dict.keys())[1:4]
    values = list(alert_dict.values())[:4]
    percents = [round((value / values[0]) * 100, 2) for value in values][1:]
    
    months = ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May']
    May = percents
    June = percents
    July = percents
    August = percents
    September = percents
    October = percents

    colors = ['red', 'blue', 'orange']
    risk_levels = ['Risk and Warning', 'Caution and Advice', 'Safe and Harmless']



    total_bars = len(risk_levels)
    bar_width = 0.2
    space_width = 0.05  # Adjust the space between groups
    index = np.arange(len(months))

    plt.figure(figsize=(10, 6))

    for i, risk_level in enumerate(risk_levels):
        plt.bar(index + (i - (total_bars - 1) / 2) * (bar_width + space_width), [May[i], June[i], July[i], August[i], September[i], October[i]], bar_width, label=f'{risk_level} Risk', color=colors[i])
    plt.ylabel('Percentage',fontsize=14)
    plt.xticks(index, months,fontsize=14)
    plt.legend()
    
    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_stat_analysis = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_stat_analysis


def main(alert_dict):
    alerts = calculate_alert(alert_dict)

    #print(alerts)

    generated_context = alerts['context']

    user_question = 'Wird der Gaspreis in Zukunft steigen?'

    response = get_qa_results(generated_context, user_question)

    print(response)

    response['alerts'] = alerts
    
    return response

def calculate_alert(alert_dict):
    
    alert_types = list(alert_dict.keys())[1:4]
    values = list(alert_dict.values())[:4]
    percents = [round((value / values[0]) * 100, 2) for value in values][1:]

    alerts = {}
    
    keys = list(alert_dict.keys())

    alerts['total_articles_extracted'] = alert_dict['Total news']

    alerts['total_relevant_articles'] = alert_dict['Total news'] - alert_dict['Others'] 

    alerts['total_high_alert'] = percents[0]  # percentage

    alerts['total_low_alert'] = percents[1]

    alerts['total_no_alert'] = percents[2]

    alerts['relevant_keywords'] = {'gas_price_spikes': 92.7, 'energy_expensive': 72, 'russischen_gaslieferung': 78, 'ukraine_krieges_europa_erdgaspreis': 67.5}

    alerts['context'] = 'Experte warnt vor Energie Krise wir brauchen das Erdgas aus Russland Drastischer Preisanstieg bei Heiz und Spritpreisen wegen des Ukraine Krieges der Freistaat befindet sich in einer Energiekrise Wie geht es für Firmen und Bürger weiter Experten warnen dass es zu Versorgungsengpässen und Problemen bei der Produktion von verschiedenen Produkten Wir brauchen das Erdgas aus Russland sagt Manfred Gössl IHK Hauptgeschäftsführer in München und Oberbayern'

    alerts['first_article'] = alert_dict['First high alert text']
    
    alerts['first_score'] = alert_dict['First high alert score']

    return alerts

def get_qa_results(context, question):


    :param context: str (received from calculate_alert function)

    :param question: str

    :return: dict



    print(context, question)

    qa_results = {}

    qa_results['response'] = 'Drastischer Preisanstieg bei Heiz und Spritpreisen wegen des Ukraine Krieges'

    qa_results['score'] = 73.1

    qa_results['start'] = 5  # start index of the answer in the context

    qa_results['end'] = 18  # end index of the answer in the context

    # start and end is used as position where to highlight the answer in the context

    return qa_results
"""