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
    # create_table_query = """
    #     CREATE TABLE IF NOT EXISTS candidatos (
    #         id SERIAL PRIMARY KEY,
    #         first_name VARCHAR,
    #         last_name VARCHAR,
    #         email VARCHAR,
    #         application_date DATE,
    #         country VARCHAR,
    #         YOE INTEGER,
    #         seniority VARCHAR,
    #         technology VARCHAR,
    #         code_challenge_score INTEGER,
    #         technical_interview_Score INTEGER,
    #         hired BOOLEAN
    #     );
    # """

    # cursor.execute(create_table_query)
    # conn.commit

    #Insercion de los datos en las respectivas columnas 
    # sql = """
    #     COPY candidatos(first_name, last_name, email, application_date, country, YOE, seniority, technology, code_challenge_score, technical_interview_score)
    #     FROM 'C:/Users/kevin/ETL/Postgres/workshop_001/candidates.csv' DELIMITER ';' CSV HEADER;
    # """
    # cursor.execute(sql)

    #Se hace la condicion para agregar los que son contratados los cuales deben cumplir unas condiciones
    # update_hired = """
    #     UPDATE candidatos
    #     SET hired = (code_challenge_score >= 7) AND (technical_interview_score >= 7);
    # """
    # cursor.execute(update_hired)

    # conn.commit()

    # techology_group = """
    #     ALTER TABLE candidatos
    #     ADD COLUMN technology_group varchar;
    # """
    # cursor.execute(techology_group)
    # conn.commit()
    # print("columna creada")
     
    update_technology_group = """
        UPDATE candidatos
        SET technology_group = 
            CASE
                WHEN technology IN (
                    'Development - CMS Backend',
                    'Development - CMS Frontend',
                    'Development - Backend',
                    'Development - Frontend',
                    'Development - FullStack',
                    'Game Development',
                    'DevOps'
                ) THEN 'Software Development'
                WHEN technology IN (
                    'System Administration',
                    'Security',
                    'Security Compliance',
                    'Database Administration'
                ) THEN 'Administration and Security'
                WHEN technology IN (
                    'Sales',
                    'Client Success',
                    'Social Media Community Management'
                ) THEN 'Sales and Customer Management'
                WHEN technology IN (
                    'Data Engineer',
                    'Business Analytics / Project Management',
                    'Business Intelligence'
                ) THEN 'Data and Analytics'
                WHEN technology IN (
                    'QA Manual',
                    'QA Automation'
                ) THEN 'Test and QA'
                WHEN technology IN (
                    'Mulesoft',
                    'Salesforce',
                    'Adobe Experience Manager',
                    'Design'
                ) THEN 'Integration and Platforms'
                WHEN technology = 'Technical Writing' THEN 'Technical Writing'
                ELSE 'Other'
            END;
        """     
    cursor.execute(update_technology_group)
    conn.commit()
    print("listo los grupos :D")
    
except Exception as ex:
    print(ex)

finally:
    conn.close()
    print("Conexion finalizada u.u")