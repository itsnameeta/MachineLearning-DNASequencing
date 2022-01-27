from flask import Flask
from flask import render_template, request, redirect, url_for
from Bio import SeqIO
import neatbio.sequtils as utils
from collections import Counter
from Bio.Seq import Seq
import requests
import io
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import base64


app = Flask(__name__)
app.debug = True

@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/intro")
def get_intro():
    return render_template("intro.html")

@app.route("/upload")
def get_upload():
    print("**********Before file upload")
    test = []
    test.append({})
    return render_template("upload.html", data={}) 

@app.route('/sequence', methods=['POST'])
#@app.route('/sequence')
def upload_file():
    print("**********After file upload")
    
    seqdata= []

    uploaded_file = request.files['file']

    data = uploaded_file.read()
    
    decdata = data.decode('UTF-8')
    dnarecord= SeqIO.read(io.StringIO(decdata),"fasta")
    dnasequence= dnarecord.seq
    dnafreq=Counter(dnasequence)

    seqdata.append(dnarecord)
    seqdata.append(dnasequence)
    seqdata.append(dnafreq)

    seqdataList = {'dnarecord': dnarecord, 'dnasequence': dnasequence, 'dnafreq': dnafreq}
    

    print("seqdataList")
    print (seqdataList)


    return render_template("sequence.html", data=seqdataList) 

if __name__ == '__main__':
    app.run(debug=True)