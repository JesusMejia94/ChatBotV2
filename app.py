# Activar encapsulamiento: source venv/Scripts/activate
# activAR PAQUETE Flask:  pip install Flask
# generar carpeta requerimientos: 
# Ruta de mi proyecto https://github.com/JesusMejia94/Chatpip freeze > requirements.txtBotV2.git

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime


app=Flask(__name__)


# base de datos config  SQL lite
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///metapython.db' 
app.config['SQLQLCHEMY_TRACK__MODIFICATIONS']=False
db=SQLAlchemy(app)

#la tabla de logs estructura
class log_BIT_WathP(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fechaHora=db.Column(db.DateTime,default=datetime.utcnow())
    texto=db.Column(db.TEXT)

# creacion Tabla
with app.app_context():
    db.create_all()
    prueba1=log_BIT_WathP(texto='Test1')
    prueba2=log_BIT_WathP(texto='Test2')
    db.session.add(prueba1)
    db.session.add(prueba2)
    db.session.commit()

@app.route('/')
def index():
    registros=log_BIT_WathP.query.all()
    #obtener los registros de la base de datos
    return render_template('index.html',registros=registros)

mensajes_log=[]

#funcion para agregar mensajes y guardar en la base de datos
def agregar_mensajes_log(texto):
    mensajes_log.append(texto)
##guardar en la base de datos el mensaje  
    nuevo_registro=log_BIT_WathP(texto=texto)
    db.session.add(nuevo_registro)
    db.session.commit()



if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

