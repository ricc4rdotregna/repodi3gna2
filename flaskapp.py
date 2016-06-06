from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import send_from_directory
import sqlite3

app=Flask(__name__)

def initDB():
    c=sqlite3.connect('../data/Alunni.db')
    
    stringSQLTableAlunni=\
        "create table if not exists REGISTROALUNNI(\
         NUMEROREG integer primary key,\
         NOME text not null,\
         COGNOME text not null,\
         ANNONASCITA text not null\
         );"
    cursor=c.cursor()
    cursor.execute(stringSQLTableAlunni)
    c.commit()
    c.close()
    
#initDB()
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index.html")
def hello1():
    return send_from_directory('.', 'index.html')

@app.route ("/alunnoByNumeroReg/",methods=["POST"])
def alunnoByNumeroReg():
    numreg=request.json['numreg']
    print numreg,"Nreg"
    c=sqlite3.connect('../data/Alunni.db')
    print "Opened database successfully ByNumero";
    cursor=c.cursor()
    cur= cursor.execute("SELECT*FROM registroAlunni WHERE NUMREG -- ?",[numreg])
    dizAlunno={}
    for alunno in cur:
        numreg=alunno[0]
        nome=alunno[1]
        cognome=alunno[2]
        annoNascita= alunno[3]
        
        dizAlunno={"numreg": numreeg,"nome":nome, "cognome": cognome, 
        "annoNasita": annoNascita}
        
        break
    print dizAlunno
    c.commit()
    c.close()
    
    stringJson=jsonify(**dizAlunno)
    return stringJson

@app.route ("/alunnoByNumeroReg/",methods=["POST"])
def inserisciAlunnoPOST():
    
    numreg=request.json['numreg']
    nome=request.json['nome']
    cognome=request.json['cognome']
    annoNascita=request.json['annoNascita']
    
    print [numreg,nome,cognome,annoNascita]
    
    c=sqlit3.connect('../data/Alunni.db')
    print "opened database successfully";
    cursor=c.cursor()
    cursor.execute("INSERT INTO registroAlunni\
    (NUMREG,NOME,COGNOME,ANNONASCITA)\
    VALUES (?,?,?,?)",[numreg,nome,cognome,annoNascita]);
    c.commit()
    
    c.close()
    return jsonify("")

if __name__ == "__main__":
    app.run(port=5000)

