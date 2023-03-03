from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testdb@postgres_db/noter'
db = SQLAlchemy(app)
Login = False

class Notes(db.Model):
    __tablename__= 'notes_db'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(25))
    content = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)

    def __init__(self,title,content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()

@app.route('/',methods=['POST','GET'])
def home():
    try:
        global Login
        notes = db.session.query(Notes)
        if Login == False:
            res = request.args.get('token')
            token = jwt.decode(res, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
            if 'pass' in token.keys() :
                Login = True
                return render_template('home.html',notes=notes)
            else:
                return "<h1>$404</h1>"
        elif Login:
            return render_template('home.html',notes=notes)
    except Exception as ex:
        print(ex)
        return f"<h1>$404{ex}</h1>"

@app.route('/create/',methods=['POST','GET'])   
def create(pk=None):
    if request.method == "POST" and pk==None:
        title = request.form['title']
        content = request.form['note_content']
        note = Notes(title,content)
        db.session.add(note)
        db.session.commit()
        return redirect('/')
    return render_template('notes.html',context = {})

@app.route('/update/<pk>',methods=['POST'])   
def update(pk=None):
    if request.method == "POST":
        context = {}
        context['title'] = request.form['title']
        context['content'] = request.form['note_content']
        notes = db.session.query(Notes).filter(Notes.id==pk).update(context)
        db.session.commit()
        return redirect('/')

@app.route('/notes/<pk>/',methods=['POST','GET'])
def notes(pk):
    context = {}
    notes = db.session.query(Notes).filter(Notes.id==pk)
    for note in notes:
        context['title'] = note.title
        context['content'] = note.content
        context['created_at'] = note.created_at
    return render_template('notes.html',context=context)

@app.route('/delete/<pk>',methods=['POST','GET'])
def delete(pk):
    if request.method == 'POST':
        db.session.query(Notes).filter(Notes.id==pk).delete()
        db.session.commit()
        return redirect('/')

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',port = 5010,debug = True)