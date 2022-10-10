from flask import app, Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/')
@app.route('/quem-somos')
def quem_somos():
    return render_template('quem_somos.html')

    
if __name__ == '__main__':
    app.run('0.0.0.0')