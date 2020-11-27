from flask import render_template, jsonify, json
from app import app, db
from app.models import Atributos
from app.alchemyEncoder import AlchemyEncoder
from flask import request
#from app.sih_data_proc import *
from app.sih_data_proc import *


@app.route("/")
def index():
    return "ok 1.0"

@app.route("/get_cid_list", methods=['GET'])
def get_cid_list():
    start = time.time()
    ret = get_cid_list_data()
    end = time.time()
    print("get_cid_list: " + str(end - start))
    return ret;


@app.route("/get_uf_list", methods=['GET'])
def get_uf_list():
    start = time.time()
    ret = get_uf_list_data()
    end = time.time()
    print("get_uf_list_data(): " + str(end - start))
    return ret;

@app.route("/timeline_data", methods=['GET'])
def timeline_data():
    start = time.time()
    cid = request.args.get('cid', 'A00-B99')
    state = request.args.get('state', 'AC')
    year = request.args.get('year', 2015)
    ret = get_timeline_data_ps(cid, state, year)
    end = time.time()
    print("timeline_data(): " + str(end - start))
    return ret;

    
@app.route("/gender_age_pyramid_data")
def genderAgePyramidData():
    start = time.time()
    uf = request.args.get('uf', 'AC')
    year = request.args.get('year', 2016)
    cid = request.args.get('cid', 'A00-B99')
    ret = gender_age_pyramid_data_ps(cid, uf, year)
    end = time.time()
    print("gender_age_pyramid_data(): " + str(end - start))
    return ret;



@app.route("/diag_gender_data", methods=['GET'])
def diag_gender_data():
    start = time.time()
    cidList = request.args.get('cid', 'A00-B99')
    uf = request.args.get('uf', 'AC')
    year = request.args.get('year', 2015)
    ret = get_diag_gender_data_ps(cidList, uf, year)
    end = time.time()
    print("diag_gender_data(): " + str(end - start))
    return ret;


@app.route("/arrow_list_cid")
def arrow_list_cid():
    start = time.time()
    state = request.args.get('uf', 'RS')
    yearInicial = request.args.get('yearI', 2016)
    yearFinal = request.args.get('yearF', 2019)
    ret = arrow_list_cid_data_ps(state, yearInicial, yearFinal)
    end = time.time()
    print("arrow_list_cid(): " + str(end - start))
    return ret;


@app.route("/cid_local_heatmap_data", methods=['GET'])
def cid_local_heatmap():
    start = time.time()
    year = request.args.get('year', 2016)
    ret =  cid_local_heatmap_data_ps(year)
    end = time.time()
    print("cid_local_heatmap_data(): " + str(end - start))
    return ret;


@app.route("/total_linhas", methods=['GET'])
def total_linhas():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2016)
    ret = total_linhas_ps(uf, year)
    end = time.time()
    print("total_linhas(): " + str(end - start))
    return ret;


@app.route("/total_linhas_aih", methods=['GET'])
def total_linhas_aih():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2016)
    ret = total_linhas_aih_ps(uf, year)
    end = time.time()
    print("total_linhas_aih(): " + str(end - start))
    return ret;



@app.route("/total_anos_anteriores", methods=['GET'])
def total_anos_anteriores():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2016)
    ret = total_anos_anteriores_ps(uf, year)
    end = time.time()
    print("total_anos_anteriores(): " + str(end - start))
    return ret;

@app.route("/total_ano_atual", methods=['GET'])
def total_ano_atual():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2016)
    ret =  total_ano_atual(uf, year)
    end = time.time()
    print("total_anos_anteriores(): " + str(end - start))
    return ret;

@app.route("/total_mortes", methods=['GET'])
def total_mortes():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2016)
    ret = total_mortes_ps(uf, year)
    end = time.time()
    print("total_mortes(): " + str(end - start))
    return ret;


@app.route("/heatmap_cid_data", methods=['GET'])
def heatmap_cid_data():
    start = time.time()
    ret = heatmap_data_ps(uf, year)
    end = time.time()
    print("heatmap_cid_data(): " + str(end - start))
    return ret;

@app.route("/sihdatalist", methods=['GET'])
def sihdatalist():
    start = time.time()    
    atributos = Atributos.query.all()
    end = time.time()
    print(atributos)
    print("sihdatalist(): " + str(end - start))
    return json.dumps(atributos, cls=AlchemyEncoder)


@app.route("/mcv_data", methods=['GET'])
def mcv_data():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2015)
    cid = request.args.get('cid', 'A00-B99')
    ret = get_mvc_data(cid, uf,  year)
    end = time.time()    
    print("mcv_data(): " + str(end - start))
    return ret;

@app.route("/heatmap_cid_idade", methods=['GET'])
def heatmap_cid_idade():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2016)
    cid = request.args.get('cid', 'A00-B99')
    ret = heatmap_idade_ps(uf, year,cid)
    end = time.time()
    print("heatmap_cid_idade(): " + str(end - start))
    return ret;

@app.route("/gender_pie_data")
def gender_pie_data():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2016)
    ret = gender_pie_data_ps(uf, year)
    end = time.time()
    print("gender_pie_data(): " + str(end - start))
    return ret;

@app.route("/dashboard_data")
def datashboard_data():
    start = time.time()
    uf = request.args.get('uf', 'RS')
    year = request.args.get('year', 2016)
    cid = request.args.get('cid', None)
    ret = dashboard_data(uf, year)
    end = time.time()
    return ret;