from flask import Flask, jsonify, request, url_for, redirect, session
app = Flask(__name__)

#Key needed for sessions
app.config['SECRET_KEY'] =  'thisisasecretkey' 

#Simple route funtion
@app.route('/')
def index():
    # session.pop('name',None)  #Remove name from session
    return '<h1>Hello World</h1>'

#Dynamic route
@app.route('/home', defaults={'name': 'Stranger'}) #If a name is not provided, the defaul value will be Stranger
@app.route('/home/<string:name>')
def home(name):
    session['name'] = name #needs to import session
    return f'<h1>Hello {name} </h1>'

#Return a json document.  jsonify needs to be imported
@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'NotinSession'
    return jsonify({'key': 'value','listkey': [1,2,3], 'name': name})

#Route with parameters.  request needs to be imported.  For example: http://edclcldd104:5000/query?name=blas&location=florida
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h1>Hello {name} from {location}</h1>'

#Route to a form
@app.route('/theform',methods=['GET','POST'])
def theform():
    if request.method == 'GET':
        return '''  <form method="POST" action="/theform">
                        <input type="text" name="name">
                        <input type="text" name="location">
                        <input type="submit" value="Submit">
                    </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        return f'<h1>Hello {name} from {location}</h1>'

#Redirect.  Import redirect ansd url_for
@app.route('/redirect_home')
def redirect_home():
    return redirect(url_for('home',name='blas'))  #Redirect to /home with name = Blas