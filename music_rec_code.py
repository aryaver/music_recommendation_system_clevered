#Project 2:-Spotify Dataset

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


data=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/top50.csv',encoding='latin-1')

# print(data.head())

app = dash.Dash(external_stylesheets=[dbc.themes.LUMEN])
server = app.server

app.layout = html.Div(children = [
    html.H1("Music Recommendation System", className="text-center fw-bold text-decoration-underline", style={'color': 'black'}),
    html.Br(),
    html.Div( [ dbc.Select( id='artist-dropdown',options=[{'label': 'Highest popularity', 'value': '01'},
                                                                        {'label': 'Highest energy', 'value': '02'},
                                                                        {'label': 'highest Beats.Per.Minute', 'value': '03'},
                                                                        {'label': 'Liveness', 'value': '04'},
                                                                        {'label': 'highest count in Spotify dataset', 'value': '05'},
                                                                        {'label': 'highest Dancibility', 'value': '06'},
                                                                        {'label': 'highest duration of Song', 'value': '07'},
                                                                        ],
                                                                placeholder="Recommend artist with... ",
                                                                style={'width': '90%', 'margin': '15px'},
                                                                className="px-2 border"# bg-white rounded-pill"
                        ),
                        html.Br(),
                                dbc.Select( id='genre-dropdown',options=[{'label': 'highest popularity', 'value': '01'},
                                                         {'label': 'highest Beats.Per.Minute', 'value': '02'},
                                                         {'label': 'highest Energy', 'value': '03'},
                                                         {'label': 'highest Liveness', 'value': '04'},
                                                         {'label': 'highest Dancibility', 'value': '05'},
                                                         ],
                            placeholder='Recommend Genre with...',
                            style={'width': '90%', 'margin': '15px'},
                            className="px-2 border"# bg-white rounded-pill"
                        ),]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(id = 'artist-recommendation-result', style={'width': '90%', 'margin': '15px'},),
    html.Div(id = 'genre-recommendation-result', style={'width': '90%', 'margin': '15px'},),
])
# #Task-1:-print(data.head())

# print(data.shape)

# print(data.columns)

# print(data.info())

# print(data.dtypes)

# print(data.isnull().sum())



#Task2:-Perform recommendations

@app.callback(
    Output('artist-recommendation-result', 'children'),
    Input('artist-dropdown', 'value'),
)
def recommend_artist(artist_option):
    if not artist_option:
        return ''

    if artist_option == '01':  # Highest popularity
        dance = data.groupby('Artist.Name')[['Popularity']].median().sort_values(by='Popularity', ascending=False)
        return  dbc.Alert(dance.index[0])

    elif artist_option == '02':  # Highest energy 
        dance = data.groupby('Artist.Name')[['Energy']].median().sort_values(by='Energy', ascending=False)     
        return dbc.Alert(dance.index[0])

    elif artist_option == '03':  # Highest Beats.Per.Minute  
        dance = data.groupby('Artist.Name')[['Beats.Per.Minute']].median().sort_values(by='Beats.Per.Minute', ascending=False)     
        return dbc.Alert(dance.index[0])
    
    elif artist_option == '04':  # Liveness        
        dance = data.groupby('Artist.Name')[['Liveness']].median().sort_values(by='Liveness', ascending=False)     
        return dbc.Alert(dance.index[0])

    elif artist_option == '05':  # Highest count in Spotify dataset        
        return dbc.Alert(data['Genre'].value_counts().idxmax())

    elif artist_option == '06':  # Highest Dancibility
        dance=data.groupby('Artist.Name')[['Danceability']].median().sort_values(by='Danceability',ascending =False)
        return dbc.Alert(dance.index[0])

    elif artist_option == '07':  # Highest duration of Song
        dance=data.groupby('Artist.Name')[['Valence.']].median().sort_values(by='Valence.',ascending =False)
        return dbc.Alert(dance.index[0])
    
    return ''


@app.callback(
    Output('genre-recommendation-result', 'children'),
    Input('genre-dropdown', 'value'),
)
def recommend_genre(genre_option):
    if not genre_option:
        return ''
    
    if genre_option == '01':  # Highest popularity
        popularity=data.groupby('Genre')[['Popularity']].median().sort_values(by='Popularity',ascending =False)
        # jumbotron = dbc.Row([dbc.Col(html.Div(
        #                                 [   html.H2(f"{popularity.index[0]}", className="display-3"),
        #                                     html.Hr(className="my-2"),
        #                                     html.P(f"{popularity.index[0]} is the artist with highest popularity!"
        #                                 )],
        #                                 className="h-100 p-5 text-white bg-dark rounded-3"), md=6)])
        # print(popularity.index[0])
        # return jumbotron
        return dbc.Alert(popularity.index[0])
    
    elif genre_option == '02':  # Highest Beats.Per.Minute          
        bpm=data.groupby('Genre')[['Popularity']].median().sort_values(by='Popularity',ascending =False)
        return dbc.Alert(bpm.index[0])

    elif genre_option == '03':  # Highest Energy   
        energy=data.groupby('Genre')[['Energy']].median().sort_values(by='Energy',ascending =False)
        return dbc.Alert(energy.index[0])
    
    elif genre_option == '04':  # Liveness        
        liveness=data.groupby('Genre')[['Liveness']].median().sort_values(by='Liveness',ascending =False)
        return dbc.Alert(liveness.index[0])


    elif genre_option == '05':  # Highest dancibility       
        dance=data.groupby('Genre')[['Danceability']].median().sort_values(by='Danceability',ascending =False)
        return dbc.Alert(dance.index[0])
    
    return ''


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8067)