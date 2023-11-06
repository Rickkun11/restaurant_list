from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

data_rest = [
        {
        "city": "Jakarta",
        "description": "Inilah satu lagi restoran paling keren namun nyaman di Senopati, Jakarta Selatan, yang hadir dengan tempat bertema art-deco-botanical.",
        "id": 1,
        "name": "Feast by Kokiku"
    },
    {
        "city": "Menteng",
        "description": "merupakan restoran yang direkomendasikan untuk tempat nongkrong rombongan sambil menikmati hidangan khas Jawa yang autentik. Makanan dapat disajikan dalam satu set makanan.",
        "id": 2,
        "name": "Kaum"
    },
    {
        "city": "Jakarta",
        "description": "Ini adalah salah satu restoran mewah yang tidak hanya memasak tetapi juga menyajikan masakan Indonesia terbaik. Daun Muda by Andrea Peresthu menawarkan cita rasa otentik",
        "id": 3,
        "name": "Daun Muda Soulfood by Andrea Peresthu"
    },
    {
        "city": "Jakarta",
        "description": "Mendjangan menawarkan masakan rumahan Indonesia di gedung yang menjadi restoran di Kemang, Jakarta Selatan. ",
        "id": 4,
        "name": "Mendjangan"
    },
    {
        "city": "Jakarta",
        "description": "Suwe Ora Jamu di Pasar Minggu, Jakarta Selatan, memang menarik karena masakannya yang asli Indonesia, seperti soto mie khas Bogor. ",
        "id": 5,
        "name": "Suwe Ora Jamu"
    },
    {
        "city": "Surabaya",
        "description": "Restoran Keluarga yang berasal dari surabaya memiliki sejumlah menu olahan bebek yang sangat berkualitas",
        "id": 6,
        "name": "Bebek Tepi Sawah"
    }
]


@app.route("/")
def index():
    return render_template("index.html", data=data_rest)


@app.route("/rest", methods=["GET", "POST"])
def resto():
    if request.method == "GET":
        if len(data_rest) > 0:
            return jsonify(data_rest)
        else:
            "Not Found", 404

    if request.method == "POST":
        new_city = request.form["city"]
        new_desc = request.form["description"]
        new_name = request.form["name"]
        id = data_rest[-1]["id"] + 1

        new_obj = {
            "id": id,
            "city": new_city,
            "description": new_desc,
            "name": new_name,
        }
        data_rest.append(new_obj)
        return jsonify(data_rest), 201


@app.route("/rest/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_rest(id):
    if request.method == "GET":
        for rest in data_rest:
            if rest["id"] == id:
                return jsonify(rest)
            pass
    if request.method == "PUT":
        for rest in data_rest:
            if rest["id"] == id:
                rest["city"] = request.form["city"]
                rest["description"] = request.form["description"]
                rest["name"] = request.form["name"]

                updated_rest = {
                    "id": id,
                    "city": rest["city"],
                    "description": rest["description"],
                    "name": rest["name"],
                }
                return jsonify(updated_rest)
    if request.method == "DELETE":
        for index, rest in enumerate(data_rest):
            if rest["id"] == id:
                data_rest.pop(index)
                return jsonify(data_rest)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
