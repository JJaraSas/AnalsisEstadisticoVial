from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, redirect, \
    url_for


accidentalidad = Blueprint("accidentalidad", __name__, url_prefix='')


@accidentalidad.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@accidentalidad.route('/accidentalidad_mes', methods=['GET', 'POST'])
def por_mes():
    return render_template('por_mes.html')


@accidentalidad.route('/accidentalidad_localidad', methods=['GET', 'POST'])
def por_localidad():
    return render_template('por_localidad.html')


@accidentalidad.route('/accidentalidad_localidad_datos', methods=['GET', 'POST'])
def por_localidad_datos():
    return render_template('por_localidad_datos.html')


@accidentalidad.route('/accidentalidad_hora', methods=['GET', 'POST'])
def por_hora():
    return render_template('por_hora.html')


@accidentalidad.route('/gravedad', methods=['GET', 'POST'])
def gravedad():
    return render_template('gravedad.html')


@accidentalidad.route('/objeto_choque', methods=['GET', 'POST'])
def objeto_choque():
    return render_template('objeto_choque.html')


@accidentalidad.route('/lugar', methods=['GET', 'POST'])
def lugar():
    return render_template('lugar.html')


@accidentalidad.route('/tipo_accidente', methods=['GET', 'POST'])
def tipo_accidente():
    return render_template('tipo_accidente.html')


@accidentalidad.route('/predicciones', methods=['GET', 'POST'])
def predicciones():
    return render_template('predicciones.html')
