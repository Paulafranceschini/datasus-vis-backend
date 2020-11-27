from app import app, db, db_properties, engine
from app.alchemyEncoder import AlchemyEncoder
import time
from app.util import formatCid
from datetime import datetime
from flask import json
from sqlalchemy import create_engine 
import pandas as pd

def get_cid_list_data():

    sql =  "select cod, descricao from cid10_geral cg "
    
    sql_df = pd.read_sql(sql, con=engine)

    return sql_df.to_json(orient='records')


def get_uf_list_data():
    sql = "select id, sigla, nome from uf uf  order by nome"

    
    sql_df = pd.read_sql(sql, con=engine)

    return sql_df.to_json(orient='records')




def get_mvc_data(cid, uf, year):
    df_data = {};
    df_data["timeline"] = get_timeline_data_ps(cid, uf, year)  
    df_data["heatmap"] = cid_heatmap_idade_ps(cid, uf, year)  
    df_data["pyramid"] = gender_age_pyramid_data_ps(cid, uf, year)
    return json.dumps(df_data);

def cid_heatmap_idade_ps(cid, uf, year):
    yearS = str(year)
    sql =     "select * from cid_heatmap_idade chi \
                where \"COD\" = '" + cid + "' \
                and ano = " + yearS + " and uf = '" + uf + "' order by data_, ordem "
    
    sql_df = pd.read_sql(sql, con=engine, parse_dates=['data'])

    total = sql_df["count"].sum();
    sql_df["per"] = sql_df["count"]/total;
    return sql_df.to_json(orient='records')




def get_timeline_data_ps(cidList, uf, year):
    yearS = str(year)
    sql =     "select tdv.*, descricao from timeline_data_view tdv \
                inner join cid10_geral as cg on cg.cod  = tdv.\"COD\"  \
                where \
                data >= '" + yearS + "-01-01 00:00:00'  and  data <= '" + yearS +"-12-31'\
                and uf = '" + uf + "'";
    
    if(cidList != None):
        cidList = cidList.split(",")
        cidStr = "";
        for cid in cidList:
            if(cidStr != ""):
                cidStr = cidStr + ","
            cidStr = cidStr +  "'" +  cid + "'"

        sql = sql + " and \"COD\" in ("  + cidStr + ") order by data ";

    print(sql)

    sql_df = pd.read_sql(sql, con=engine, parse_dates=['data'])
    return sql_df.to_json(orient='records')

def gender_age_pyramid_data_ps(cid, uf, year):
    yearS = str(year)
    sql =     "select * from gender_age_pyramid_data where \
    ano = " + yearS + "\
    and uf = '" + uf + "'\
    and \"COD\"  = '"  + cid + "'";

    print(sql)

    sql_df = pd.read_sql(sql, con=engine, parse_dates=['data'])
    return sql_df.to_json(orient='records')


def get_diag_gender_data_ps(cidList, uf, year):
    yearS = str(year)
    sql =     "select * from diag_gender_data where \
    ano = " + yearS + "\
    and uf = '" + uf + "'";
    
    if(cidList != None):
        cidList = cidList.split(",")
        cidStr = "";
        for cid in cidList:
            if(cidStr != ""):
                cidStr = cidStr + ","
            cidStr = cidStr +  "'" +  cid + "'"
    
    sql = sql + " and \"COD\" in ("  + cidStr + ")";

    print(sql)

    sql_df = pd.read_sql(sql, con=engine, parse_dates=['data'])
    return sql_df.to_json(orient='records')

    
def arrow_list_cid_data_ps(uf, anoInicial, anoFinal):
  anoInicial = str(anoInicial)
  anoFinal = str(anoFinal)

  sql = "select inicial.pos as pos1, inicial.\"COD\" as \"COD\", descricao, final.pos as pos2, \
            inicial.count as c1, final.count as c2 \
            from arrow_list_cid_data inicial \
            inner join arrow_list_cid_data  final \
            on inicial.\"COD\" = final.\"COD\" \
            inner join cid10_geral cg  on inicial.\"COD\" = cg.cod  \
            where \
            inicial.uf = final.uf and  \
            inicial.uf = '" + uf + "' and  \
            inicial.ano = " + anoInicial + " and \
            final.ano = " + anoFinal + "order by pos1";
  
  sql_df = pd.read_sql(sql, con=engine)
  
  total_incial = sql_df["c1"].sum();
  sql_df["per1"] = sql_df["c1"]/total_incial;

  total_final = sql_df["c2"].sum();
  sql_df["per2"] = sql_df["c2"]/total_incial;

  
  return sql_df.to_json(orient='records')

def cid_local_heatmap_data_ps(ano):
  ano = str(ano)

  sql = "select * from cid_local_heatmap_data \
            where \
            ano = " + ano + " order by \"SIGLA_UF\", \"COD\""
            
  print(sql)   
  sql_df = pd.read_sql(sql, con=engine)

  
  return sql_df.to_json(orient='records')
 

def get_pie_data(uf, year):
    yearS = str(year)
    sql =     "select * from gender_pie_data where \
        ano = " + yearS + "\
        and uf = '" + uf + "'";
    
    sql_df = pd.read_sql(sql, con=engine)

    total = sql_df["count"].sum();
    sql_df["percent"] = sql_df["count"]/total;

    return sql_df.to_json(orient='records')


def get_timeline_dashboard_data(uf, year):
    yearS = str(year)
    sql =     "select * from timeline_dashboard_data where \
        ano = " + yearS + "\
        and uf = '" + uf + "'";
    
    sql_df = pd.read_sql(sql, con=engine)
    return sql_df.to_json(orient='records')

def get_mais_iternacoes(uf, year):
    sql = "select \"COD\", descricao, sum(total) as tot \
                from timeline_data_view tdv  \
                inner join cid10_geral cg on cod = \"COD\" \
                where ano = " + year + "\
                and uf = '" + uf + "' \
                group by \"COD\", descricao \
                order by tot desc \
                limit 1"
    sql_df = pd.read_sql(sql, con=engine)
    return sql_df.to_json(orient='records')


def get_menos_iternacoes(uf, year):
    sql = "select \"COD\", descricao, sum(total) as tot \
                from timeline_data_view tdv  \
                inner join cid10_geral cg on cod = \"COD\" \
                where ano = " + year + "\
                and uf = '" + uf + "' \
                group by \"COD\", descricao \
                order by tot asc \
                limit 1"
    sql_df = pd.read_sql(sql, con=engine)
    return sql_df.to_json(orient='records')

def get_total_registros(uf, year):
    yearS = str(year)
    sql =     "  select count from total_reg_ano  where \
                ano = " + yearS + "\
                and uf = '" + uf + "'";
    
    sql_df = pd.read_sql(sql, con=engine)
    return sql_df.to_json(orient='records')
  
def get_total_aih(uf, year):
    yearS = str(year)
    sql =     "select count from total_aih_ano where \
                  ano = " + yearS + "\
                and uf = '" + uf + "'";
    print(sql)
    sql_df = pd.read_sql(sql, con=engine)
    return sql_df.to_json(orient='records')

def get_media_dia(uf, year):
    yearS = str(year)
    sql =     "    select round(avg(total)) from timeline_dashboard_data where  \
                  ano = " + year + "\
                and uf = '" + uf + "'";
    print(sql)
    sql_df = pd.read_sql(sql, con=engine)
    return sql_df.to_json(orient='records')

def get_total_mortes(uf, year):
    yearS = str(year)
    sql =     "  select count from total_mortes_ano  where \
                  ano = " + yearS + "\
                and uf = '" + uf + "'";
    
    sql_df = pd.read_sql(sql, con=engine)
    return sql_df.to_json(orient='records')

def get_total_altas(uf, year):
    yearS = str(year)
    sql =     "  select count from total_altas_ano  where \
                  ano = " + yearS + "\
                and uf = '" + uf + "'";
    
    sql_df = pd.read_sql(sql, con=engine)
    return sql_df.to_json(orient='records')


def dashboard_data(uf, year):  
    print(uf)
    print(year)
    df_data = {};
    df_data["totalRegistros"] = get_total_registros(uf, year);
    df_data["mediaDia"] = get_media_dia(uf, year);
    df_data["totalAltas"] = get_total_altas(uf, year);
    df_data["totalMortes"] = get_total_mortes(uf, year);
    df_data["maisInternacoes"] = get_mais_iternacoes(uf, year);
    df_data["menosInternacoes"] = get_menos_iternacoes(uf, year);

    df_data["dataPieChart"] = get_pie_data(uf, year)
    df_data["timelineDashboardData"] = get_timeline_dashboard_data(uf, year)


    return json.dumps(df_data);