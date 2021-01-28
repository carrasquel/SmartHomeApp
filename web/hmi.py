from rackio import status_code, Rackio
from rackio.web import render_template, raw_template

app = Rackio()

@app.define_route('/')
def HMI():

    return render_template('login.html')


@app.define_route('/menu')
def menu():
    
    return render_template('menu.html')


@app.define_route('/settings')
def settings():
    
    return render_template('settings.html')


@app.define_route('/radio')
def radio():
    return render_template('radio.html')

