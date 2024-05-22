from flask import Flask, jsonify
from decouple import config
import psycopg2

app = Flask(__name__)

@app.route("/")
def greeting():
    return 'Selamat Hari Raya Idul Fitri, mohon maaf lahir dan batin!'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
