from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Peltier server.</p>"
    
@app.route("/peltier/<temperature>")
def peltier(temperature):
    t = float(temperature)
    print(f"Temperature: {t}")
    return ""
    
