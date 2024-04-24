import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64

app = dash.Dash()

app.layout = html.Div(children=[

    html.Br(),
    
    html.Div([
        html.Img(src=r'assets/snowball_logo.png', alt='image', 
                style={'display': 'inline-block', 'height':'7%', 'width':'7%'}),
        html.Li(children='Snow Ball',
                style={'display': 'inline-block', 'color': '#5B9BD5', 'fontSize': 36, 'textAlign': 'left', 'verticalAlign':'top', 'font-family': "ptsans", 'margin-left': '.1%', 'margin-top': '.7%', "font-weight": "bold",}),
        html.Div(children='|',
                 style={'display': 'inline-block', 'color': '#CAD3D4', 'fontSize': 40, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '1vw', 'margin-top': '.4%'}),
        html.Div([
        html.Div(children='AI',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 22, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '0vw',"font-weight": "bold"}),
        html.Div(children='ntelli',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 18, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '0vw',"font-weight": "bold",'margin-top': '3%'}),
        html.Div(children='Scrape',
                 style={'display': 'inline-block', 'color': '#252328', 'fontSize': 22, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '.0vw'}),
        html.Div(children='goes further than OCR . . .',
                 style={'color': '#A7AFAD', 'fontSize': 11, 'textAlign': 'left',"font-weight": "bold",
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '.0vw'}),
        ],style={'display': 'inline-block','verticalAlign':'top','margin-left': '1vw', 'margin-top': '1%'}),
    ], className='row', style={'width': '100%'}),

    html.Hr(style={'height': '1px', 'width': '100%', 'color': '#E7F0F1', "borderColor": "#E7F0F1",
                   'backgroundColor': 'E7F0F1', 'border-top': '1px', 'align': 'left', 'margin-left': '0'}),
    
    html.Br(),
    
    html.Div([
        html.Div(children='Automating',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 22, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '2%', 'margin-top': '1.1%'}),
        html.Div(children='manual data entry using',
                 style={'display': 'inline-block', 'color': '#252328', 'fontSize': 22, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '.5vw', 'margin-top': '1.1%'}),
        html.Div(children='Artificial Intelligence',
                 style={'display': 'inline-block', 'color': '#252328', 'fontSize': 22, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '.5vw', 'margin-top': '1.1%','text-decoration': 'underline'}),
    ], className='row', style={'width': '100%'}),
    
    html.Br(),
    
    html.Div(children='''Intelligent Document Processing Engine (IDP - Engine) is an advanced technological capability that enables organizations to digitize and automate unstructured data originating from various documentation sources. These include digitized document images, pdfs, word processing files, online forms, and more. IDP uses technologies from computer vision, natural language processing, and workflow automation to mimic human abilities in identifying, contextualizing and processing documents.''', 
             style={'color': '#78867D', 'fontSize': 12, 'textAlign': 'left', 'font-family': "ptsans", 'width': '70%','margin-left': '2%'}),
    html.Br(),
    html.Br(),
    
    html.Div([
        html.Div(children='This functionality is customised for',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '2%'}),
        html.Div(children='ITAC Consulting',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '.4vw',"font-weight": "bold"}),
        html.Div(children='for processing documents.',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '.4vw'}),
        html.Div(children='Snow Ball',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '.4vw',"font-weight": "bold"}),
        html.Div(children='does not use or store any documents processed by ITCA Consulting.',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign':'top','margin-left': '.4vw'}),
    ], className='row', style={'width': '100%','font-style': 'italic'}),
    
    html.Br(),
    
    html.Div(children='Intelligent Document Processing Engine (IDP - Engine)', 
             style={'color': '#252328', 'fontSize': 12, 'textAlign': 'left', 'font-family': "ptsans", 'width': '100%','margin-left': '2%', "font-weight": "bold"}),

    html.Br(),
    html.Div([

        html.Div(children=[
            dcc.Upload(
                id='upload-files',
                children=['Drag and Drop or ', html.A('Select a File',style={'color': '#FFC91D','text-decoration': 'underline'})], style={
                    'display': 'inline-block','width': '100%', 'height': '33px', 'lineHeight': '30px', 'borderWidth': '1px', 'borderStyle': 'dashed', 'borderColor': '#DDDDDD', 'borderRadius': '5px', 'textAlign': 'center', 'verticalAlign':'middle', 'fontSize': 12, 'font-family': "ptsans", 'color': '#AFABAB', 'backgroundColor': '#E7F0F1',"font-weight": "bold"},
                multiple=True),
            ],
            style={'display': 'inline-block','width': '30%',  'vertical-align': 'top', 'margin-left': '2%',
                   'margin-top': '0vw'}
        ),

        html.Button(
                id='process-button', n_clicks=0, children='Process Files',
                style={ 'display': 'inline-block',"margin-left": "2%", 'width': '10%', 'height':'35px', 'borderColor': '#FFFFFF', 'borderRadius': '5px', 'textAlign': 'center', 'verticalAlign':'middle','fontSize': 12, 'font-family': "ptsans", 'color': '#FFFFFF', 'backgroundColor': '#8AC539',"font-weight": "bold"}
                ),

    ], className='row', style={'width': '100%'}), 
    
    html.Br(),
    html.Br(),
    
    html.Div([
        html.Div(id='input-file-uploaded',
             style={'display': 'inline-block','width': '20%','margin-left': '2vw'}),
        html.Div(id='output-files',
             style={'display': 'inline-block','width': '20%','margin-left': '2vw'}),
    ], className='row', style={'width': '100%'}),
    

])


#read input files
def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    return html.Div([
            html.Li(filename,
                    style={'display': 'inline-block', 'width': '100%','font-family': "ptsans",'fontSize': 11, 'color': '#8BA6AB',"font-weight": "bold"}),
            html.Hr(style={'height': '1px', 'width': '100%', 'color': '#E7F0F1', "borderColor": "#E7F0F1",
                   'backgroundColor': 'E7F0F1', 'border-top': '1px', 'align': 'left', 'margin-left': '0'}),
        ], className='row', style={'width': '100%'})

#doc2excel conversion
def doc2excel(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    return html.Div([
            html.Li(filename,
                    style={'display': 'inline-block', 'width': '100%','font-family': "ptsans",'fontSize': 11, 'color': '#8AC539',"font-weight": "bold"}),
            html.Hr(style={'height': '1px', 'width': '100%', 'color': '#E7F0F1', "borderColor": "#E7F0F1",
                   'backgroundColor': 'E7F0F1', 'border-top': '1px', 'align': 'left', 'margin-left': '0'}),
        ], className='row', style={'width': '100%'})


#read input files
@app.callback(Output('input-file-uploaded', 'children'),
              Input('upload-files', 'contents'),
              State('upload-files', 'filename'))
def update_output(list_of_files, list_of_names):
    if list_of_files is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_files, list_of_names)]
        return children

#doc2excel conversion
@app.callback(Output('output-files', 'children'),
              Input('upload-files', 'contents'),#Input('process-button', 'n_clicks'),
              State('upload-files', 'filename'))
def process_files(list_of_files, list_of_names):
    if list_of_files is not None:
        children = [
            doc2excel(c, n) for c, n in
            zip(list_of_files, list_of_names)]
        return children

if __name__=='__main__':
    app.run_server()