from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', iframe_src="/general")

@app.route('/general')
def general():
    return render_template('general.html')

@app.route('/telekom')
def telekom():
    return render_template('telekom.html')

@app.route('/poct')
def poct():
    return render_template('poct.html')

@app.route('/radiospektr')
def radiospektr():
    return render_template('radiospektr.html')

if __name__ == '__main__':
    app.run(debug=True)
