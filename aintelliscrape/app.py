import base64
import io
import os

import dash
import pandas as pd
from dash import dash_table
from dash import html, dcc
from dash.dependencies import Input, Output, State

from main import TableExtractor

table_object = TableExtractor()

BINARY_FILE_CONTENTS = []

app = dash.Dash()

app.layout = html.Div(children=[

    html.Br(),

    html.Div([
        html.Img(src=r'assets/snowball_logo.png', alt='image',
                 style={'display': 'inline-block', 'height': '5%', 'width': '5%','margin-top': '.7%'}),
        html.Li(children='Snow Ball',
                style={'display': 'inline-block', 'color': '#252328', 'fontSize': 34, 'textAlign': 'left',
                       'verticalAlign': 'top', 'font-family': "ptsans", 'margin-left': '.1%', 'margin-top': '.7%'}),
        html.Div(children='|',
                 style={'display': 'inline-block', 'color': '#CAD3D4', 'fontSize': 40, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '1vw',
                        'margin-top': '.4%'}),
        html.Div([
            html.Div(children='AI',
                     style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 22, 'textAlign': 'left',
                            'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '0vw',
                            "font-weight": "bold"}),
            html.Div(children='ntelli',
                     style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 18, 'textAlign': 'left',
                            'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '0vw',
                            "font-weight": "bold", 'margin-top': '3%'}),
            html.Div(children='Scrape',
                     style={'display': 'inline-block', 'color': '#252328', 'fontSize': 22, 'textAlign': 'left',
                            'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top',
                            'margin-left': '.0vw'}),
            html.Div(children='goes further than OCR . . .',
                     style={'color': '#A7AFAD', 'fontSize': 11, 'textAlign': 'left', "font-weight": "bold",
                            'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top',
                            'margin-left': '.0vw'}),
        ], style={'display': 'inline-block', 'verticalAlign': 'top', 'margin-left': '1vw', 'margin-top': '1%'}),
    ], className='row', style={'width': '100%'}),

    html.Hr(style={'height': '1px', 'width': '100%', 'color': '#C2DADC', "borderColor": "#C2DADC",
                   'backgroundColor': 'C2DADC', 'border-top': '1px', 'align': 'left', 'margin-left': '0'}),

    html.Br(),

    html.Div([
        html.Div(children='Automating',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 22, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '2%',
                        'margin-top': '1.1%'}),
        html.Div(children='manual data entry using',
                 style={'display': 'inline-block', 'color': '#252328', 'fontSize': 22, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '.5vw',
                        'margin-top': '1.1%'}),
        html.Div(children='Artificial Intelligence',
                 style={'display': 'inline-block', 'color': '#252328', 'fontSize': 22, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '.5vw',
                        'margin-top': '1.1%', 'text-decoration': 'underline'}),
    ], className='row', style={'width': '100%'}),

    html.Br(),

    html.Div(
        children='''Intelligent Document Processing Engine (IDP - Engine) is an advanced technological capability that enables organizations to digitize and automate unstructured data originating from various documentation sources. These include digitized document images, pdfs, word processing files, online forms, and more. IDP uses technologies from computer vision, natural language processing, and workflow automation to mimic human abilities in identifying, contextualizing and processing documents.''',
        style={'color': '#78867D', 'fontSize': 12, 'textAlign': 'left', 'font-family': "ptsans", 'width': '70%',
               'margin-left': '2%'}),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div(children='This functionality is customised for',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '2%'}),
        html.Div(children='ITAC Consulting',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '.4vw',
                        "font-weight": "bold"}),
        html.Div(children='for processing documents in doc or docx format.',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '.4vw'}),
    ], className='row', style={'width': '100%', 'font-style': 'italic'}),
    
    html.Div([
        html.Div(children='Snow Ball',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '.4vw',
                        "font-weight": "bold", 'margin-left': '2%'}),
        html.Div(children='does not use or store any documents or data processed by ITCA Consulting for its own use.',
                 style={'display': 'inline-block', 'color': '#ED7D31', 'fontSize': 12, 'textAlign': 'left',
                        'font-family': "ptsans", 'textAlign': 'left', 'verticalAlign': 'top', 'margin-left': '.4vw'}),
    ], className='row', style={'width': '100%', 'font-style': 'italic'}),

    html.Br(),
    html.Br(),

    html.Div(children='Intelligent Document Processing Engine (IDP - Engine)',
             style={'color': '#252328', 'fontSize': 12, 'textAlign': 'left', 'font-family': "ptsans", 'width': '100%',
                    'margin-left': '2%', "font-weight": "bold"}),

    html.Br(),
    html.Div([

        html.Div(children=[
            dcc.Upload(
                id='upload-files',
                children=['Drag and Drop or ',
                          html.A('Select a File', style={'color': '#FFC91D', 'text-decoration': 'underline'})], style={
                    'display': 'inline-block', 'width': '100%', 'height': '33px', 'lineHeight': '30px',
                    'borderWidth': '1px', 'borderStyle': 'dashed', 'borderColor': '#DDDDDD', 'borderRadius': '5px',
                    'textAlign': 'center', 'verticalAlign': 'middle', 'fontSize': 12, 'font-family': "ptsans",
                    'color': '#AFABAB', 'backgroundColor': '#E7F0F1', "font-weight": "bold"},
                multiple=True),
        ],
            style={'display': 'inline-block', 'width': '30%', 'vertical-align': 'top', 'margin-left': '2%',
                   'margin-top': '0vw'}
        ),

        html.Button(
            id='process-button', n_clicks=0, children='Process Files',
            style={'display': 'inline-block', "margin-left": "2%", 'width': '10%', 'height': '35px',
                   'borderColor': '#FFFFFF', 'borderRadius': '5px', 'textAlign': 'center', 'verticalAlign': 'middle',
                   'fontSize': 12, 'font-family': "ptsans", 'color': '#FFFFFF', 'backgroundColor': '#8AC539',
                   "font-weight": "bold"}
        ),

    ], className='row', style={'width': '100%'}),

    html.Br(),
    html.Br(),

    html.Div([
        html.Div(id='input-file-uploaded',
                 style={'display': 'inline-block', 'width': '20%', 'margin-left': '2vw'}),
        html.Div(id='table',
                 style={'display': 'inline-block', 'width': '50%', 'margin-left': '4vw', 'verticalAlign': 'top'}),
    ], className='row', style={'width': '100%'}),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(style={'height': '1px', 'width': '100%', 'color': '#C2DADC', "borderColor": "#C2DADC",
                   'backgroundColor': 'C2DADC', 'border-top': '1px', 'align': 'left', 'margin-left': '0'}),
    html.Br(),
    html.Div([
        html.Div(children='Contact: contact@snowball-a-vibe.com',
                 style={'display': 'inline-block', 'color': '#B3C1BD', 'fontSize': 10, 'textAlign': 'left',
                        'font-family': "ptsans", 'verticalAlign': 'top', 'margin-left': '2%', 'width': '50%'}),
        html.Div(children='Copyright 2021 Snow Ball. All Rights Reserved.',
                 style={'color': '#B3C1BD', 'fontSize': 10, 'textAlign': 'left', 'font-family': "ptsans",
                        'verticalAlign': 'top', 'margin-left': '2%'}),
    ], className='row', style={'width': '100%'}),
    html.Div(children='Company number: 73499626178',
             style={'color': '#B3C1BD', 'fontSize': 10, 'textAlign': 'left', 'font-family': "ptsans",
                    'verticalAlign': 'top', 'margin-left': '2%'}),
    html.Br(),

])


# read input files
def parse_contents(contents, filename):
    print("start 1")
    global BINARY_FILE_CONTENTS
    content_type, content_string = contents.split(',')
    decoded = io.BytesIO(base64.b64decode(content_string))
    BINARY_FILE_CONTENTS.append([filename, decoded])
    return html.Div([
        html.Li(filename, id='default_link',
                style={'display': 'inline-block', 'width': '100%', 'font-family': "ptsans", 'fontSize': 11,
                       'color': '#8BA6AB', "font-weight": "bold"}),
        html.Hr(style={'height': '1px', 'width': '100%', 'color': '#C2DADC', "borderColor": "#C2DADC",
                       'backgroundColor': 'C2DADC', 'border-top': '1px', 'align': 'left', 'margin-left': '0'}),
    ], className='row', style={'width': '100%'})


# doc2excel conversion
def doc2excel(file_name, binary_content):
    _, _ext = os.path.splitext(file_name)
    if _ext != ".docx":
        return None
    dt = table_object.get_dict(binary_content)
    dt.update({"file_name": file_name})
    # print(dt)
    return dt


# read input files
@app.callback(Output('input-file-uploaded', 'children'),
              Input('upload-files', 'contents'),
              State('upload-files', 'filename'))
def update_output(list_of_files, list_of_names):
    # recreate_save_dir()
    global BINARY_FILE_CONTENTS
    BINARY_FILE_CONTENTS = []
    if list_of_files is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_files, list_of_names)]
        return children


# doc2excel conversion
@app.callback(Output('table', 'children'),
              Input('process-button', 'n_clicks'),
              State('upload-files', 'filename'))
def process_files(n_clicks, list_of_names):
    if n_clicks > 0 and list_of_names is not None:
        dictionaries = [
            doc2excel(file_name, binary_content) for file_name, binary_content in
            BINARY_FILE_CONTENTS]
        _all_keys = ["file_name"] + table_object.get_keys()
        combined_dict = {k: [] for k in _all_keys}
        for d in dictionaries:
            if d is None:
                continue
            conv_d = table_object.convert_dict(d)
            for k in combined_dict.keys():
                combined_dict[k].append(conv_d[k])
        df = pd.DataFrame(combined_dict)
        return html.Div([
            dash_table.DataTable(id="table_data", columns=[{"name": i, "id": i} for i in df.columns],
                                 data=df.to_dict("records"), export_format="csv",
                                 style_table={'overflowY': 'hidden', 'overflowX': 'scroll', 'display': 'inline-block',
                                              'width': '100%', 'font-family': "ptsans", 'fontSize': 11,
                                              'color': '#8BA6AB', 'border-radius': '5px'},
                                 style_header={'backgroundColor': '#C7D7D7', 'fontSize': 12, 'font-family': "ptsans",
                                               'color': 'black', 'fontWeight': 'bold', 'textAlign': 'center',
                                               'border': '1px solid #A9C2C3', 'color': '#FFFFFF'},
                                 style_cell={'textAlign': 'left', 'fontSize': 11, 'font-family': 'ptsans',
                                             'border': '1px solid #A9C2C3', 'color': '#8BA6AB'})
        ])


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5000, debug=True)
