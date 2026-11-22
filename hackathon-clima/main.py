from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    total = None
    if request.method == "POST":
        km_carro = float(request.form["km_carro"])
        kwh = float(request.form["kwh"])
        carne = float(request.form["carne"])
        # valores aproximados, só para o template
        total = (km_carro * 0.17 * 52 + kwh * 0.08 * 12 + carne * 3 * 52) / 1000
        total = round(total, 2)
    return render_template("index.html", total=total)


if __name__ == "__main__":
    app.run(debug=True)
