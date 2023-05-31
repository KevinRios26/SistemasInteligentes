from FarmApp import *
from DatosFA import *
from ChatGPT import interactuar_con_chatgpt
from flask import Flask, render_template, request, redirect, url_for, jsonify
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)


@app.route('/')
def index():
    saludo = "Bienvenido a FarmApp - Bienestar a tu puerta"
    return render_template('index.html', saludo=saludo)

@app.route('/resultado', methods=['POST'])
def resultado():    
    medicamento = request.form['medicamento']
    usuario={'nombre': request.form['nom'], 'edad': request.form['eda'],'direccion':request.form['dir'] }    
    datos = buscar_med(medicamento)
    bus1="que es el "+medicamento+"en 30 palabras"
    bus2="posología de "+medicamento+" en personas de "+usuario['edad']+"años en 30 palabras"
    bus3="cuales son los efectos secundarios de "+medicamento+" en personas de "+usuario['edad']+"años en 30 palabras"
    respuesta1 = interactuar_con_chatgpt(bus1)
    respuesta2 = interactuar_con_chatgpt(bus2)
    respuesta3 = interactuar_con_chatgpt(bus3)
    resultado_busqueda = datos.to_dict(orient='records')
    return render_template('results.html', r1=respuesta1, r2=respuesta2, r3=respuesta3, resultado_busqueda=resultado_busqueda, medicamento=medicamento, usuario=usuario)

@app.route('/leer-r1', methods=['POST'])
def leer_r1():
    texto = request.form['r1']
    engine = pyttsx3.init()    
    engine.say(texto)
    engine.runAndWait()
    return render_template('mas_info.html', texto=texto)

@app.route('/leer-r2', methods=['POST'])
def leer_r2():
    texto = request.form['r2']
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    return render_template('mas_info.html', texto=texto)

@app.route('/leer-r3', methods=['POST'])
def leer_r3():
    texto = request.form['r3']
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    return render_template('mas_info.html', texto=texto)

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


@app.route('/recognize', methods=['POST'])
def recognize():    
    recognizer = sr.Recognizer()
    idpersona = request.form['nom']    
    usuario = buscar_usuario(idpersona)
    with sr.Microphone() as source:
        print('Escuchando...')
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        print('Texto reconocido:', text)
        return render_template('busqueda.html', texto=text, usuario=usuario)
    except sr.UnknownValueError:
        print('No se pudo reconocer el audio')
        return 'No se pudo reconocer el audio'
    except sr.RequestError as e:
        print('Error al realizar la solicitud al servicio de reconocimiento de voz:', e)
        return 'Error al realizar la solicitud al servicio de reconocimiento de voz'

if __name__ == '__main__':
    app.run(debug=True)