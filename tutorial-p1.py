#sentdex tutorial p1- https://www.youtube.com/watch?v=J_Cy_QjG6NE&t=317s
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash tutorial'),
    dcc.Graph(id='example',
        figure={
            'data':[{'x':[1,2,3,4,5], 
                'y':[12,34,2,14,56], 
                'type':'line',
                'name':'apples'}],
            'layout': {
                'title':'basic example'
            }
        }
    )
    ])

if __name__ == "__main__":
    app.run_server(debug=True)