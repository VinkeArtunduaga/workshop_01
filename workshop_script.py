import psycopg2
import csv
import pandas as pd
import json

#Carga de la configuracion de los datos de la database
with open('db_config.json') as config_file:
    config = json.load(config_file)

#Conexion a la base de datos
try:
    conn = psycopg2.connect(
        host = 'localhost',
        user = config['user'],
        password = config['password'],
        database = 'ETL'
    )

    print("Conexion exitosa uwu")

    cursor = conn.cursor()

    #Creacion de la tabla candidatos con sus respectivas columnas y tipo de valores
    create_table_query = """
        CREATE TABLE IF NOT EXISTS candidatos (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR,
            last_name VARCHAR,
            email VARCHAR,
            application_date DATE,
            country VARCHAR,
            YOE INTEGER,
            seniority VARCHAR,
            technology VARCHAR,
            code_challenge_score INTEGER,
            technical_interview_Score INTEGER,
            hired BOOLEAN
        );
    """

    cursor.execute(create_table_query)
    conn.commit

    #Insercion de los datos en las respectivas columnas 
    sql = """
        COPY candidatos(first_name, last_name, email, application_date, country, YOE, seniority, technology, code_challenge_score, technical_interview_score)
        FROM 'C:/Users/kevin/ETL/Postgres/workshop_001/candidates.csv' DELIMITER ';' CSV HEADER;
    """
    cursor.execute(sql)

    #Se hace la condicion para agregar los que son contratados los cuales deben cumplir unas condiciones
    update_hired = """
        UPDATE candidatos
        SET hired = (code_challenge_score >= 7) AND (technical_interview_score >= 7);
    """
    cursor.execute(update_hired)

    conn.commit()
    print("listo la tabla :D")
    
except Exception as ex:
    print(ex)

finally:
    conn.close()
    print("Conexion finalizada u.u")