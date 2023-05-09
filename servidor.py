from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
from server_modules.inputs import *

import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc

app = Flask(__name__)
app_dash = dash.Dash(__name__)
CORS(app)

@app.route('/values-info', methods=['GET'])
def setTextValues():
    
    return jsonify({
        'total': int(get_target_inputs()),
        'inputs': int(get_total_inputs()),
        'ativo' : int(get_total_ativos()),
        'analise' : int(get_total_analise()),
        'lgpd' : int(get_lgpd_true_inputs()),
        'limresp' : int(get_resp_true_inputs())
    })

@app.route('/chart-values', methods=['GET'])
def setChartsValues():
    
    circle_circunference = round(2*3.14*100, 0)
    
    analise = get_percentage_input_analise()
    ativo = get_percentage_input_ativo()
    lgpd = get_percentage_input_lgpd()
    resp = get_percentage_input_resp()
    
    total_ativo_pg = f"{(circle_circunference - (circle_circunference * ativo) / 100)}"
    total_analise_pg = f"{(circle_circunference - (circle_circunference * analise) / 100)}"
    total_lgpd_pg = f"{(circle_circunference - (circle_circunference * lgpd) / 100)}"
    total_limresp_pg = f"{(circle_circunference - (circle_circunference * resp) / 100)}"
    
    total_analise_abs = analise
    total_lgpd_abs = lgpd
    total_limresp_abs = resp
    
    
    return jsonify({
        'total_ativo_pg' : total_ativo_pg,
        'total_analise_pg' : total_analise_pg,
        'total_lgpd_pg' : total_lgpd_pg,
        'total_resp_pg' : total_limresp_pg,
        'total_analise_abs' : total_analise_abs,
        'total_lgpd_abs' : total_lgpd_abs,
        'total_resp_abs' : total_limresp_abs,
    })
    
if __name__ == '__main__':
    app.run(port=5000)