# workshop_01

## ¿Como correr el script del taller?

1. Clone el repositorio con: `git clone https://github.com/VinkeArtunduaga/workshop_01.git`
2. Instale python 3.11
3. Instale la base de datos PostgreSQL
4. Para las librerias es necesario hacer un pip install y de esta manera las librerias psycopg, csv, pandas y json seran instaladas.
5. Crear un usuario y contraseña para el uso de postgreSQL
6. Crear una database en pgAdmin 4 llamada ETL (asi fue como le puse el nombre a la mia pero se puede cambiar)
7. Cambie las configuraciones de la conexion a la base de datos segun el usuario, contraseña y database asignados
8. Corra el codigo en la terminal mediante `python workshop_script.py`

## En caso de querer realizar el proceso de EDA:

1. Descargar Jupyter para mas facilidad con Jupyter lab
2. Al ya tener descargadas las librerias de json y pandas o no haber podido ser instaladas ejecutar en la terminal `pip install pandas` y `pip install json`
3. Cambiar la direccion de donde se encuentra el archivo csv de candidates.csv
4. Al ejecutar cada uno de los bloques o de corrido deberia apreciarse el analisis
