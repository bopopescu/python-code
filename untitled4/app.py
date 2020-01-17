from flask import Flask, json, request

app = Flask(__name__)

def jsonr(data):
    return json.dumps(data, ensure_ascii=False)

def getr(name):
       return request.args.get(name)
def postr(name):
    return request.form.get(name)
@app.route('/api', methods=['GET', 'POST'])
def hello_world():
    get = getr('name')
    post = postr('name')
    if get:
        data = {'code': 1, 'err': 0, 'data': 'hello word!世界' + get}
    elif post:
        data = {'code': 1, 'err': 0, 'data': 'hello word!世界' + post}
    else:
        data = {'code': 0, 'err': 1, 'data': ''}
    return jsonr(data)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '访问有误！'


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run()
