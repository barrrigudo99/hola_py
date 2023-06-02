from flask import Flask

app=Flask(__name__)

@app.route("/")
def hola():
    return "<h1> Bienvenido al servidor web en python </h1>"

if __name__=='__main__':
    app.run()
# Para lanzar el servidor flask -app nombre run
