from flask import Flask, render_template, request
import requests

app = Flask(__name__)
url_api = "http://localhost:8080"

@app.route("/", methods=["GET", "POST"])
def inicio():
    pais_data = None
    if request.method == "POST":
        pais = request.form.get("pais")
        if pais:
            response = requests.get(f"{url_api}/pais?name={pais}")
            if response.status_code == 200:
                pais_data = response.json()
    return render_template("pag1.html", pais=pais_data)

@app.route("/pag2", methods=["GET", "POST"])
def inicio2():
    clima_data = None
    if request.method == "POST":
        lat = request.form.get("latitud")
        lon = request.form.get("longitud")
        if lat and lon:
            response = requests.get(f"{url_api}/clima?lat={lat}&lon={lon}")
            if response.status_code == 200:
                clima_data = response.json()
    return render_template("pag2.html", clima=clima_data)

@app.route("/pag3", methods=["GET", "POST"])
def inicio3():
    consejo_data = None
    if request.method == "POST":
        response = requests.get(f"{url_api}/consejo")
        if response.status_code == 200:
            consejo_data = response.json()
    return render_template("pag3.html", consejo=consejo_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
