import csv
import matplotlib.pyplot as plt
import pandas as pd

def create_csv_file():
    """ Create the csv file with headers to store predictions along with timestamp """
    with open('../data/predictions_table.csv', 'w') as csvfile:
        column_names = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
                        'total_bedrooms', 'population', 'households', 'median_income',
                        'ocean_proximity', 'predicted_price', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()


def display_table():
    """ Display all the previously computed predictions """
    df = pd.read_csv('../data/predictions_table.csv')

    # Generate HTML table from DataFrame
    html_table = df.to_html(index=False, classes='table table-striped')

    # Wrap the HTML table in a basic HTML structure
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Predictions History</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}
            th {{
                background-color: #f2f2f2;
                text-align: center;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Predictions History</h1>
        {html_table}
    </body>
    </html>
    """

    return html_content

def data_visualisation():
    """Display any valuable data in a single graph"""
    data_history = pd.read_csv('../data/predictions_table.csv')
    ocean_proximity_price = data_history.groupby('ocean_proximity')['predicted_price'].mean().reset_index()
    plt.bar(ocean_proximity_price['ocean_proximity'], ocean_proximity_price['predicted_price'])
    plt.xlabel('Ocean Proximity')
    plt.ylabel('Predicted Price')
    plt.title('Predicted Price for Housing on the basis of Ocean Proximity')

    # Save the figure
    plt.savefig('graph.png', format='png')
    plt.close()

# Run these functions as and when required
# create_csv_file()
# data_visualisation()