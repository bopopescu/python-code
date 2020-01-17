from bottle import route, run, request,response,template,static_file
import json,os
@route('/')
def up():
    return template('index/upload.html')
@route('/dir')
def ups():
    return json.dumps("{'data':"+str(os.listdir('./wen'))+"}", ensure_ascii=False)
def enable_cors():
   response.headers['Access-Control-Allow-Origin'] = '*'
@route('/wen/<filename:path>')
def download(filename):
    print(os.listdir('./wen'))
    print(filename)
    return static_file(filename,root='./wen',download=filename)

@route('/api')
def hello():
    enable_cors()
    return "Hello World!"

@route('/upload', method = ['POST','GET'])
def do_upload():
    enable_cors()
    import time
    data= request.files['file']


    if data.file:
        import os.path
        #name, ext = os.path.splitext(data.filename) 限制上传文件
        print(data.filename)

        data.save("./wen/"+str(data.filename), overwrite=True)

        return json.dumps("{'code':1}")

    return json.dumps("{'code':0}")

run(host='127.0.0.1', port=8080, debug=True)