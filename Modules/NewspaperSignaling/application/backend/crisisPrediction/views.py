from django.shortcuts import render
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np

# Create views here
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {
        "model_response": main(),
        "plot_alarm_system": plot_alarm_system(),
        "plot_statistical_trend_analysis": plot_statistical_trend_analysis()
        })

def plot_alarm_system():

    # Data
    alerts = {
        'total_high_alert': 68.42,
        'total_low_alert': 28.94,
        'total_no_alert': 2.63
    }


    # Mapping of alert types to legend labels
    alert_labels = {
        'total_high_alert': 'Risk and Warning',
        'total_low_alert': 'Caution and Advice',
        'total_no_alert': 'Safe and Harmless'
    }

    # Extracting keys and values
    alert_types = list(alerts.keys())
    percentages = list(alerts.values())

    # X-axis labels
    x_labels = ['August']

    # Custom colors for the bars
    colors = ['red', 'blue', 'orange']

    # Creating the bar plot
    plt.figure(figsize=(6, 4))
    bars = plt.bar(alert_types, percentages, color=colors)
    plt.xlabel('August', fontsize=14)
    plt.ylabel('Percentage', fontsize=14)

    # Adding a legend with custom labels
    legend_labels = [alert_labels[alert_type] for alert_type in alert_types]
    plt.legend(bars, legend_labels, loc='upper right', fontsize=14)

    # Set x-axis label as "August"
    plt.xticks([])  # Remove x-axis ticks
    plt.gca().xaxis.set_label_coords(0.5, -0.1)  # Adjust label position
    plt.xlabel('August', labelpad=20,fontsize=12)  # Add x-axis label
    
    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_alarm = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_alarm

def plot_statistical_trend_analysis():
    months = ['May', 'June', 'July', 'August', 'September', 'October']
    May = [62.5, 25 , 12.5]
    June = [76, 12, 12]
    July = [66.6, 28.7, 4.62]
    August = [68.42, 28.94, 2.63]
    September = [75.5, 20.3, 4.07]
    October = [72.7, 18.18, 9.09]

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


def main():
    keyword = 'high energy prices'

    country = 'Germany'

    month = 'August'

    year = '2022'

    alerts = calculate_alert(keyword, country, month, year)

    print(alerts)

    generated_context = alerts['context']

    user_question = 'Wird der Gaspreis in Zukunft steigen?'

    response = get_qa_results(generated_context, user_question)

    print(response)

    response['alerts'] = alerts
    
    return response

def calculate_alert(keyword, country, month, year):

    """

    :param keyword: str

    :param country: str

    :param month: str

    :param year: str

    :return: dict

    """

 

    print(keyword, country, month, year)

    alerts = {}

    alerts['total_articles_extracted'] = 1411

    alerts['total_relevant_articles'] = 114

    alerts['total_high_alert'] = 68.42  # percentage

    alerts['total_low_alert'] = 28.94

    alerts['total_no_alert'] = 02.63

    alerts['relevant_keywords'] = {'gas_price_spikes': 92.7, 'energy_expensive': 72, 'russischen_gaslieferung': 78, 'ukraine_krieges_europa_erdgaspreis': 67.5}

    alerts['context'] = 'Experte warnt vor Energie Krise wir brauchen das Erdgas aus Russland Drastischer Preisanstieg bei Heiz und Spritpreisen wegen des Ukraine Krieges der Freistaat befindet sich in einer Energiekrise Wie geht es für Firmen und Bürger weiter Experten warnen dass es zu Versorgungsengpässen und Problemen bei der Produktion von verschiedenen Produkten Wir brauchen das Erdgas aus Russland sagt Manfred Gössl IHK Hauptgeschäftsführer in München und Oberbayern'

    return alerts

def get_qa_results(context, question):

    """

    :param context: str (received from calculate_alert function)

    :param question: str

    :return: dict

    """

    print(context, question)

    qa_results = {}

    qa_results['response'] = 'Drastischer Preisanstieg bei Heiz und Spritpreisen wegen des Ukraine Krieges'

    qa_results['score'] = 73.1

    qa_results['start'] = 5  # start index of the answer in the context

    qa_results['end'] = 18  # end index of the answer in the context

    # start and end is used as position where to highlight the answer in the context

    return qa_results