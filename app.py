from flask import Flask, render_template

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"]         = "postgresql:///adoptiondb"
app.config["SECRET_KEY"]                      = "colorsrock123"
app.config["DEBUG"]                           = False
app.config["TEMPLATES_AUTO_RELOAD"]           = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]    = False
app.config["SQLALCHEMY_ECHO"]                 = False

@app.route('/')
def home():
    return render_template("index.html")