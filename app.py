from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola! La aplicación Docker en Python está funcionando correctamente."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)