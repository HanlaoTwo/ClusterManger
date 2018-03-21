from flask import Flask,request,url_for


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user', methods=['POST'])
def hello_user():
    return 'hello user'

@app.route('/users/<id>')
def user_id(id):
    return 'hello user:'+id

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query user:'+id

@app.route('/query_url')
def query_url():
    return 'query url:'+url_for('query_user')\

from CMD import GetComponets

@app.route('/getComps')
def get_comps():
    data =  GetComponets.getComp()
    res = app.make_response(data)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

if __name__ == '__main__':
    app.run()
