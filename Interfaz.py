from FarmApp import *
from DatosFA import *
from ChatGPT import interactuar_con_chatgpt

from flask import Flask, render_template, request, redirect, url_for, jsonify

import pyttsx3



app = Flask(__name__)
engine = pyttsx3.init()

@app.route('/')
def index():
    saludo = "Bienvenido a FarmApp - Bienestar a tu puerta"
    return render_template('index.html', saludo=saludo)

@app.route('/ChatGPT', methods=['POST'])
def mostrar_respuesta():
    medicamento = request.form['med']
    usuario={'nombre': request.form['nom'], 'edad': request.form['eda'] }
    bus1="como se usa el "+medicamento+" en personas de "+usuario['edad']+"años"
    bus2="posología de "+medicamento+" en personas de "+usuario['edad']+"años"
    bus3="cuales son los efectos secundarios de "+medicamento+" en personas de "+usuario['edad']+"años"
    respuesta1 = interactuar_con_chatgpt(bus1)
    respuesta2 = interactuar_con_chatgpt(bus2)
    respuesta3 = interactuar_con_chatgpt(bus3)

    return render_template('mas_info.html', r1=respuesta1, r2=respuesta2, r3=respuesta3, usuario=usuario, medicamento=medicamento)



@app.route('/resultado', methods=['POST'])
def resultado():    
    medicamento = request.form['medicamento']
    usuario={'nombre': request.form['nom'], 'edad': request.form['eda'],'direccion':request.form['dir'] }
    
    datos = buscar_med(medicamento)   

    bus1="como se usa el "+medicamento+" en personas de "+usuario['edad']+"años"
    bus2="posología de "+medicamento+" en personas de "+usuario['edad']+"años"
    bus3="cuales son los efectos secundarios de "+medicamento+" en personas de "+usuario['edad']+"años"
    respuesta1 = interactuar_con_chatgpt(bus1)
    respuesta2 = interactuar_con_chatgpt(bus2)
    respuesta3 = interactuar_con_chatgpt(bus3)



    # <button type="submit" class="btn btn-primary" onclick="window.history.back()">Regresar</button> 
    resultado_busqueda = datos.to_dict(orient='records')
    return render_template('results.html', r1=respuesta1, r2=respuesta2, r3=respuesta3, resultado_busqueda=resultado_busqueda, medicamento=medicamento, usuario=usuario)

@app.route('/leer-texto')
def leer_texto():
    texto = 'Hola, esto es un ejemplo de texto a voz.'
    engine.say(texto)
    engine.runAndWait()
    #return texto


#gmaps = googlemaps.Client(key='AIzaSyBsm0adgLvMBb1jbz2YgIDvRRSCwmoRP0M')

@app.route('/usuario', methods=['POST'])
def usuario():
    print("buscando persona")
    idpersona = request.form['idpersona']    
    usuario = buscar_usuario(idpersona)
    if usuario:
        print("lo encuentra")
        edad = usuario['edad']
        return render_template('busqueda.html', usuario=usuario)
    else:
        print("no lo necuentra")        
        return render_template('usuario.html', usuario=idpersona)
    

@app.route('/busqueda', methods=['POST'])
def guardar_usuario():
    print('entro a guardar')
    idpersona = request.form['idpersona']
    edad = request.form['idedad']
    direccion = request.form['direccion']
    usuario = {'nombre': idpersona,'edad': edad,'direccion': direccion}
    agregar_usuario(usuario)
    return render_template('busqueda.html', usuario=usuario)

@app.route('/search_address', methods=['GET'])
def search_address():
    address = request.args.get('address')
    if not address:
        return jsonify({"error": "No se proporcionó una dirección"}), 400

    geocode_result = gmaps.geocode(address)

    if not geocode_result:
        return jsonify({"error": "No se encontró la dirección"}), 404

    location = geocode_result[0]['geometry']['location']

    return jsonify({"latitude": location['lat'], "longitude": location['lng']}), 200

if __name__ == '__main__':
    app.run(debug=True)