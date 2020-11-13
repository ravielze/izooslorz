from flask import Blueprint, request, redirect, url_for, jsonify, send_from_directory
import time
import os
from werkzeug.utils import secure_filename
from DM import TEXTRACT_EXT
from LPP import LPP
from DM import DM
from TFIDF import TF, IDF
from VS import Selch

BAHASA_FOLDER = './Documents/bahasa'
ENGLISH_FOLDER = './Documents/english'
ALLOWED_EXT = set(TEXTRACT_EXT.copy())

lpp = LPP()
dm = DM(lpp)
tf = TF(dm, lpp)
tf.refresh(None)
idf = IDF(dm, lpp)
idf.refresh(None)
ss = Selch(dm, lpp)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

fileapp = Blueprint('fileapp', __name__)
#EROR DISINI

@fileapp.route('/file/bahasa/<filename>')
def bahasafile(filename):
    return send_from_directory(BAHASA_FOLDER, filename)

@fileapp.route('/file/english/<filename>')
def englishfile(filename):
    return send_from_directory(ENGLISH_FOLDER, filename)

fileapp.add_url_rule('/file/bahasa/<filename>', 'bahasafile', build_only=True)
fileapp.add_url_rule('/file/english/<filename>', 'englishfile', build_only=True)

@fileapp.route('/upload', methods=['GET', 'POST'])
def uf():
    """ {lang: bahasa_indonesia/english, file:[file]}"""
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'message': 'File not found.'})
        if 'lang' not in request.form:
            return jsonify({'message': 'Language not found.'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'message': 'File not found.'})
        if request.form.get('lang') in ['bahasa_indonesia', 'english']:
            if file and allowed_file(file.filename):
                filename = str(int(time.time())) + "_" + secure_filename(file.filename)
                folder = BAHASA_FOLDER if (request.form.get('lang') == 'bahasa_indonesia') else ENGLISH_FOLDER
                file.save(os.path.join(folder, filename))
                dm.read((request.form.get('lang') == 'bahasa_indonesia'), filename)
                tf.process((request.form.get('lang') == 'bahasa_indonesia'), filename)
                idf.refresh((request.form.get('lang') == 'bahasa_indonesia'))
                return jsonify({'message': 'Success.'})
        else:
            return jsonify({'message': 'Language not found.'})
    return jsonify({}), 404