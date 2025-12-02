from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen, Request
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm2
  
@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/tawarano/')
def meteo():
    # Appel de l'API exemple OpenWeatherMap
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))

    results = []

    # Parcourir la liste des relevés météo
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')  # timestamp du relevé
        temp_value = list_element.get('main', {}).get('temp')  # température en Kelvin

        if temp_value is not None:
            temp_day_value = temp_value - 273.15  # conversion Kelvin → °C
            results.append({
                'Jour': dt_value,
                'temp': temp_day_value
            })

    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def histogramme():
    return render_template("histogramme.html")
  
if __name__ == "__main__":
  app.run(debug=True)
