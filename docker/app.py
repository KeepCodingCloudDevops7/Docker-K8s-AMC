from flask import Flask
from flask_mysqldb import MySQL
import random
import datetime
import os

app = Flask(__name__)
app.config['MYSQL_DB'] = os.environ['MYSQL_DATABASE'] or 'db-partidos'
app.config['MYSQL_USER'] = os.environ['MYSQL_USER'] or 'user'
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD'] or 'user'
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST'] or 'db'
mysql = MySQL(app)

@app.route('/crear-partidos')
def crear_partidos():
    equipos = ['Real Madrid', 'Barcelona', 'Atletico de Madrid', 'Valencia', 'Sevilla', 'Villarreal', 'Real Sociedad', 'Real Betis', 'Athletic Club', 'Getafe']
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(''' DROP TABLE IF EXISTS partidos; ''')
        cursor.execute(''' CREATE TABLE partidos (id INT PRIMARY KEY AUTO_INCREMENT, equipo_local VARCHAR(255), equipo_visitante VARCHAR(255), resultado VARCHAR(255), fecha DATETIME); ''')
        fecha = datetime.datetime.now()
        for i in range(10):
            local = random.choice(equipos)
            visitante = random.choice([x for x in equipos if x != local])
            resultado = f"{random.randint(0, 5)} - {random.randint(0, 5)}"
            fecha_str = fecha.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(f''' INSERT INTO partidos (equipo_local, equipo_visitante, resultado, fecha) VALUES ('{local}', '{visitante}', '{resultado}', '{fecha_str}'); ''')
        cursor.execute(''' COMMIT; ''')
        cursor.close()
        return 'Partidos creados'
    except mysql.connection.Error as e:
        return f'Error: {e}'

@app.route('/')
def mostrar_partidos():
    s = "<table style='border:1px solid red'>"
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM partidos; ''')
        for row in cursor.fetchall():
            s = s + "<tr>"
            for x in row:
                s = s + "<td>" + str(x) + "</td>"
            s = s + "</tr>"
        cursor.close()
        return "<html><body>" + s + "</body></html>"
    except mysql.connection.Error as e:
        return f'Error: {e}'


if __name__ == '__main__':
    app.run()
