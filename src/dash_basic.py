from dash_test import Dash, dcc, html
from dash.dependencies import Input, Output


app = Dash(__name__)

# --- ADD THIS LAYOUT SECTION ---
app.layout = html.Div([
    html.H1("Hello Dash"),
    html.P("Welcome to your Dash application!"),
    html.Button('submit', id= 'number', ),
    dcc.Input(placeholder = "Enter a valid number", id= 'Data', type = 'number'),
    html.H1(id= 'Result')



])
# -------------------------------

@app.callback(Output('Result', 'children'), Input('number', 'n_clicks'), Input('Data', 'value'))
def play_data(n, data):
    if n:
        return f"your enter:{data}"
    return ""


if __name__ == '__main__':
    app.run(debug=True)


