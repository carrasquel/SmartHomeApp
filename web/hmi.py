from rackio import status_code, Rackio
from rackio.web import render_template, raw_template

app = Rackio()


@app.define_route('/')
def home():
    
    return render_template('main.html')


@app.define_route('/main')
def main():
    
    return render_template('home.html')


@app.define_route('/settings')
def settings():
    
    return render_template('settings.html')


@app.define_route('/radio')
def radio():
    return render_template('radio.html')

