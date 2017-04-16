from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment           
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
class NameForm(Form):                       
    name=StringField('what is your name?',validators=[Required()])
    submit=SubmitField('Submit')
app=Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap=Bootstrap(app)
moment=Moment(app)



@app.route('/',methods=['GET','POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template('index.html',form=form,name=name,current_time=datetime.utcnow())
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
if __name__=='__main__':
    app.run(debug=True)
