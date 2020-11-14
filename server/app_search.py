from flask import Blueprint, request, jsonify
from WS import Scraper
from app_file import dm, lpp, tf, idf
from VS import Selch
from threading import Thread

searchapp = Blueprint('searchapp', __name__)
ss = Selch(dm, lpp)
sc = Scraper(lpp)

#tinggal nunggu kinan
@searchapp.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        if 'keyword' in request.args and 'lang' in request.args:
            if not(request.args.get('lang') in ['id', 'en']):
                return jsonify({'message': 'Language not found.'})
            data = ss.search(request.args.get('keyword'), (request.args.get('lang') == 'id'))
            return jsonify({'data': data})
        else:
            return jsonify({})

@searchapp.route('/webscraping', methods=['POST'])
def webscrape():

    def process(lang: bool, filename: str):
        dm.read(lang, filename)
        tf.process(lang, filename)
        idf.process(lang, filename)
        print(f"{filename} Done.")

    if request.method == 'POST':
        if 'lang' not in request.form:
            return jsonify({'message': 'Language not found.'})
        if not(request.form.get('lang') in ['english', 'bahasa_indonesia']):
            return jsonify({'message': 'Language not found.'})
        if 'url' not in request.form:
            return jsonify({'message': 'Url not found.'})
        scrape = sc.htmlScraper((request.form.get('lang') == 'bahasa_indonesia'), request.form.get('url'))
        if not(scrape[0]):
            return jsonify({'message': 'Error.'})
        else:
            thread = Thread(target=process, kwargs={'filename': scrape[1], 'lang': (request.form.get('lang') == 'bahasa_indonesia')})
            thread.start()
        return jsonify({'message': 'Success.'})