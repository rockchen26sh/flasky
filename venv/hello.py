#-*- encoding=utf-8 -*-
from flask import Flask,render_template,request

from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField,FileField,ValidationError,SelectField
from wtforms.validators import Required,Length
import os
import imghdr
from flask.ext.sqlalchemy import SQLAlchemy



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = '127.0.0.1'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
'''
app.config['SECRET_KEY'] = 'top secret!'

#db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

'''
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique = True)
    users = db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique = True,index= True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

'''


class NameForm(Form):
    name = StringField("What is your name?",validators=[Required(),
                                                        Length(1,16)])
    submit = SubmitField('Submit')

@app.route('/weather')
def weather():
    months = ['Jan','Feb','Mar','Apl','May','Jun','Jul','Aug',
              'Sep','Oct','Nov','Dec']
    weather = {
        'Jan':{'min':38,'max':47,'rain':6.14},
        'Feb':{'min':38,'max':51,'rain':4.79},
        'Mar':{'min':41,'max':56,'rain':4.5},
        'Apl':{'min':44,'max':61,'rain':3.4},
        'May':{'min':49,'max':67,'rain':2.55},
        'Jun':{'min':53,'max':73,'rain':1.69},
        'Jul':{'min':57,'max':80,'rain':0.59},
        'Aug':{'min':58,'max':80,'rain':0.71},
        'Sep':{'min':54,'max':75,'rain':1.54},
        'Oct':{'min':48,'max':63,'rain':3.42},
        'Nov':{'min':41,'max':52,'rain':6.74},
        'Dec':{'min':36,'max':45,'rain':6.94}
    }
    highlight = {'min':40,'max':80,'rain':5}
    return render_template('index.html',city = 'Portland,OR',months=months,
                           weather = weather, highlight = highlight)

@app.route('/user',methods=['GET','POST'])
def user():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html',form = form,name = name)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

class paipaiForm(Form):
    baseTime = SelectField('BaseTime')
    submit = SubmitField('提交')


class uploadForm(Form):
    image_file = FileField('Image file')
    submit = SubmitField('Submit')

    def validata_image_file(self,field):
        if field.data.filename[-4:].lower() !='jpg':
            raise ValidationError('Invalid file extension')
        if imghdr.what(field.data) != 'jpeg':
            raise ValidationError('Invalid image format')

@app.route('/upload',methods=['GET','POST'])
def upload():
    image = None
    form = uploadForm()
    if form.validate_on_submit():
        image = 'uploads/' + form.image_file.data #与教程有变动
        open(os.path.join(app.static_folder,image),'w').write(form.image_file.data)
    return  render_template('upload.html',form=form,image=image)

@app.route('/paipai',methods=['GET','POST'])
def paipai():
    form = paipaiForm()
    return render_template('paipai.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)


