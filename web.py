from flask import Flask, request, redirect
from flask import abort

from stores.volatile_store import VolatileStore

url_store = VolatileStore()

app = Flask(__name__)


usage = {
    1: 'GET /url -> list all url store (temp)',
    2: 'GET /url/short_id -> return original url',
    3: 'POST /url -> return short url, original url is given in body with "url" key'
}


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/url', methods=['GET'])
def list_url_store():
    result = usage
    if result:
        return result
    abort(404)


@app.route('/url/<short_id>', methods=['GET'])
def get_original_url(short_id):
    result = url_store.get_original(short_id)
    if result:
        return redirect(result)
        # return result
    abort(404)


@app.route('/url', methods=['POST'])
def get_short_url():
    original_url = request.get_json()
    result = url_store.get_short(original_url['url'])
    if result:
        return result
    abort(404)


if __name__ == '__main__':
    app.run()
