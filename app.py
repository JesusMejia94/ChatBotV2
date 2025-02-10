# Activar encapsulamiento: source venv/Scripts/activate
# activAR PAQUETE Flask:  pip install Flask
# generar carpeta requerimientos: pip freeze > requirements.txt
# Ruta de mi proyecto https://github.com/JesusMejia94/ChatBotV2.git
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hola_mundo():
    return render_template('holaFlask.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True) 



