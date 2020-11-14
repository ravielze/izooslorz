from flask import Flask, jsonify
from werkzeug.middleware.shared_data import SharedDataMiddleware
from app_file import fileapp, BAHASA_FOLDER, ENGLISH_FOLDER
from app_file import lpp as xlpp, dm as xdm, tf as xtf, idf as xidf
from app_search import searchapp, ss as xss, sc as xsc

app = Flask(__name__)
lpp = xlpp
dm = xdm
tf = xtf
idf = xidf
ss = xss
sc = xsc
app.register_blueprint(fileapp)
app.register_blueprint(searchapp)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error.'}), 500

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/file/bahasa': BAHASA_FOLDER, '/file/english': ENGLISH_FOLDER})
app.run(debug=True, threaded=True)