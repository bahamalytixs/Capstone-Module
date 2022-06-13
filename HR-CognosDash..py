#https://dash.plotly.com/dash-core-components/tabs

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
#import dash
#import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = Dash(__name__, external_stylesheets=external_stylesheets)

# Read the airline data into pandas dataframe
survNorm_data =  pd.read_csv('F:/COURSERA/DATA%ANALYSIS%Professional%Certificate/9%IBM%DA%Capstone%Project/Mod%5%Building%a%Dashboardm5_survey_data_technbologies_normalised.csv', 
                            encoding = "ISO-8859-1"
                           )
						   
app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-graph", value='curr-tech-usge-graph', 
	    children=[
            dcc.Tab(label='Current Technology Usage', value='curr-tech-usge-graph'),		
            dcc.Tab(label='Future Technology Trend', value='fut-tech-trend-graph'),
		    dcc.Tab(label='Demographics', value='demograph-graph')
                ]
			 ),
             html.Div(id='tabs-out-graphs')			 
])


@app.callback(Output('tabs-out-graphs', 'children'),
			  Input(component_id='tabs-graph', component_property='value')              
			 )
def render_content(tab):
    if tab == 'curr-tech-usge-graph':
        return html.Div([
            html.H3('Current Technology Usage'),
            dcc.Graph(
			    #Figure BarChart - top 10 Lang Worked
                #figure={                    
				    #df = survNorm_data,
				    #mask = df["day"] == day
				    fig = px.bar(survNorm_data['LanguageWorkedWith'], x="Languages", y="Frequency", 
				    color="smoker",
					bars=vertical,
					length=len(survNorm['LanguageWorkedWith']),
					barmode='group',
					histfunc='count',
					show_value_labels=True,
					title='Top 10 Languages Worked With')
				#return fig	                    
                 #       }
				
				#Figure 2 - Col chart - top 10 Dbase Worked
					
           )
        ])
        	
if __name__ == '__main__':
    app.run_server(debug=True)


   app.run_server(debug=True)