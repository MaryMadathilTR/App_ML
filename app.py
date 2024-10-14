import dash
from dash import html, dcc, Input, Output, State
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Initialize the Dash app
app = dash.Dash(__name__)

#Define the layout of the app
app.layout = html.Div([
    html.H1('Real Estate Price Prediction'),
    html.Div([
        html.Label('Distance to the nearest MRT station'),
        dcc.Input(id='mrt', type='number', value=0,
                  style={'margin': '10px', 'padding': '10px'}),
        html.Label('Number of convenience stores'),
        dcc.Input(id='stores', type='number', value=0,
                  style={'margin': '10px', 'padding': '10px'}),
        html.Label('Latitude'),
        dcc.Input(id='lat', type='number', value=0,
                  style={'margin': '10px', 'padding': '10px'}),
        html.Label('Longitude'),
        dcc.Input(id='long', type='number', value=0,
                  style={'margin': '10px', 'padding': '10px'}),
        html.Button('Predict', id='predict-button'),
    ]),
    html.Div(id='output')
])


# Define the callback
@app.callback(
    Output('output', 'children'),
    Input('predict-button', 'n_clicks'),
    State('mrt', 'value'),
    State('stores', 'value'),
    State('lat', 'value'),
    State('long', 'value')
)



# Define the function that will be called when the button is clicked
# def predict(n_clicks, mrt, stores, lat, long):
#     if n_clicks is None:
#         return ''
    
#     # Load the model
#     model = LinearRegression()
#     model.fit(X_train, y_train)
    
#     # Make a prediction
#     prediction = model.predict([[mrt, stores, lat, long]])
    
#     return f'The predicted price is {prediction[0]:.2f}'
def predict(n_clicks, mrt, stores, lat, long):
    if n_clicks > 0:
        # Load data
        data = pd.read_csv('Real_Estate.csv')

        # Prepare data
        features = ['Distance to the nearest MRT station', 'Number of convenience stores','Latitude','Longitude']
        target = 'House price of unit area'

        X = data[features]
        y = data[target]

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        
        # Load the model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Make a prediction
        prediction = model.predict([[mrt, stores, lat, long]])
        
        return f'The predicted price is {prediction[0]:.2f}'
    elif n_clicks > 0:
        return 'Please enter the values'
    else:
        return ''


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)