from flask import Flask
app = Flask(__name__)
defensa = ["Blanco", "Rojo", "Costa" ,"Saracchi"]
@app.route('/')

def mostrar_defensa():
    eltexto = "<h3>Bien ahí, entonces serán:</h3>"
    eltexto += "<ul>"
    for nombre in defensa:
        eltexto += f"<li>{nombre}</li>"
    eltexto += "</ul>"
    return eltexto

if __name__ == '__main__':
    app.run(debug=True)
