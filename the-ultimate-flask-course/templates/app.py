from flask import Flask, request, session, render_template
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
    return render_template('home.html',name=name, display=True, mylist = ['one','two','three','four'])

#Route to a form
@app.route('/theform',methods=['GET','POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        return f'<h1>Hello {name} from {location}</h1>'
