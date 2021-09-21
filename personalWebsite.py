from flask import Flask, render_template
app = Flask(__name__)

#make sure to set FLASK_APP to personalWebsite.py
#   export FLASK_APP=personalWebsite.py
#When you want to dubug set FLASK_DEBUG to 1
#   export FLASK_DEBUG=1

@app.route('/')
def FrontPage():
    return render_template('index.html')
