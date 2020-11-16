from flask import Flask, jsonify, send_from_directory, request
from DM import TEXTRACT_EXT
from werkzeug.middleware.shared_data import SharedDataMiddleware
from IZOOSLORZ import IZOOSLORZ
import time, os
from threading import Thread
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
BAHASA_FOLDER = './Documents/bahasa'
ENGLISH_FOLDER = './Documents/english'
ALLOWED_EXT = set(TEXTRACT_EXT.copy())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

service = IZOOSLORZ()

@app.route('/file/bahasa/<filename>')
def bahasafile(filename):
    return send_from_directory(BAHASA_FOLDER, filename)

@app.route('/file/english/<filename>')
def englishfile(filename):
    return send_from_directory(ENGLISH_FOLDER, filename)

app.add_url_rule('/file/bahasa/<filename>', 'bahasafile', build_only=True)
app.add_url_rule('/file/english/<filename>', 'englishfile', build_only=True)

@app.route('/upload', methods=['GET', 'POST'])
def uf():

    def process(lang: bool, filename: str):
        print(f"{filename}: Reading.")
        service.dm.read(lang, filename)
        print(f"{filename}: Processing. 1/2")
        service.tf.process(lang, filename)
        print(f"{filename}: Processing. 2/2")
        service.idf.process(lang, filename)
        print(f"{filename}: Done.")
        
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
                thread = Thread(target=process, kwargs={'filename': filename, 'lang': (request.form.get('lang') == 'bahasa_indonesia')})
                thread.start()
                return jsonify({'message': 'Success.'})
        else:
            return jsonify({'message': 'Language not found.'})
    return jsonify({}), 404

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        data = request.get_json()
        if 'keyword' in data.keys() and 'lang' in data.keys():
            lang = data['lang']
            kw = data['keyword']
            if not(lang in ['id', 'en']):
                return jsonify({'message': 'Language not found.'})
            dur = time.time()*(-1)
            data = service.ss.search(kw, (lang == 'id'))
            ttab = service.ss.termTable(kw, (lang == 'id'))
            dur += time.time()
            return jsonify({'time_in_ms': dur*1000,'data': data, 'termtable': ttab})
        else:
            return jsonify({})

@app.route('/webscraping', methods=['POST'])
def webscrape():

    def process(lang: bool, filename: str):
        print(f"{filename}: Reading.")
        service.dm.read(lang, filename)
        print(f"{filename}: Processing. 1/2")
        service.tf.process(lang, filename)
        print(f"{filename}: Processing. 2/2")
        service.idf.process(lang, filename)
        print(f"{filename}: Done.")

    if request.method == 'POST':
        data = request.get_json()
        if 'lang' not in data.keys():
            return jsonify({'message': 'Language not found.'})
        lang = data['lang']
        if not(request.form.get('lang') in ['english', 'bahasa_indonesia']):
            return jsonify({'message': 'Language not found.'})
        if 'url' not in data.keys():
            return jsonify({'message': 'Url not found.'})
        url = data['url']
        scrape = service.sc.htmlScraper((lang == 'bahasa_indonesia'), url)
        if not(scrape[0]):
            return jsonify({'message': 'Error. ' + scrape[1]})
        else:
            thread = Thread(target=process, kwargs={'filename': scrape[1], 'lang': (lang == 'bahasa_indonesia')})
            thread.start()
        return jsonify({'message': 'Success.'})

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error.'}), 500

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/file/bahasa': BAHASA_FOLDER, '/file/english': ENGLISH_FOLDER})
app.run(debug=False, threaded=True, use_reloader=False)