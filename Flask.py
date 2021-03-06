#-*- encoding:utf-8 -*-
from flask import Flask,render_template,request,redirect,url_for,make_response,abort
from werkzeug.routing import BaseConverter
from os import path
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *




class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__()
        self.regex = items[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter
Bootstrap(app)
nav = Nav()

nav.register_element('top',Navbar(u'Flask入门',
                                  (u'主页','index'),
                                  (u'关于','about'),
                                  (u'服务','services'),
                                  (u'项目','project'),
                                  ))
@app.route('/')
def index():
   response = make_response(render_template('index.html',title='welcome'))
   response.set_cookie('username','')
   return response


@app.route('/services')
def services():
    return 'Services'

@app.route('/about')
def about():
    return 'About'

@app.route('/user/<username>')
def user(username):
    return 'User %s ' % username
@app.route('/project/')
@app.route('/our-works/')
def project():
    return 'The project page'


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    else:
        username = request.args['username']

    return render_template('login.html', method=request.method)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepath,'static/uploads')
        f.save(upload_path,secure_filename(f.filename))
        return redirect(url_for('upload'))
    return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
   app.run(debug=True)