#sentdex tutorial p3- https://www.youtube.com/watch?v=wv2MXJIdKRY
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime


tickers=['AAPL','TSLA','GOOG','TRIP']
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Stock tracker tutorial'),

    dcc.Input(
        id='input',
        value='',
        type='text'
    ),

    html.Div(id='output-graph')
    # Static graph
    # dcc.Graph(
    #     id='stock-graph',
    #     figure={
    #         'data':[
    #             {'x':df.index,
    #             'y':df.Close,
    #             'type':'line',
    #             'name':stock+str(df.Close)}
    #         ],
    #         'layout' : {
    #             'title':stock
    #         }
    #     }
    # )
    
    # dcc.Input(id='input', value='Enter something', type='text'),
    # html.Div(id='output')
])

@app.callback(
    Output(component_id='output-graph',component_property='children'),
    [Input(component_id='input',component_property='value')]
)
def update_graph(input_data):
    
    if input_data=="":
        return None
    elif input_data not in tickers:
        return None
    else:
        
        start=datetime.datetime(2015,1,1)
        end=datetime.datetime.now()
        df=web.DataReader(str(input_data),'morningstar',start,end)
        df.reset_index(inplace=True)
        df.set_index("Date",inplace=True)
        df = df.drop("Symbol",axis=1)
        return dcc.Graph(
            id='output-graph',
            figure={
                'data':[
                    {'x':df.index,
                    'y':df.Close,
                    'type':'line',
                    'name':input_data}
                ],
                'layout' : {
                    'title':input_data
                }
            }
        )


if __name__ == "__main__":
    app.run_server(debug=True)