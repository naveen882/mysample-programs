from flask import Flask
from flask import Flask, render_template, request
import six
from flask import jsonify
app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['POST'])
def index():
	di = {}
	a = []
	print("==============")
	print(type(request.files))
	print(type(request.files['file']))
	for i in request.files['file']:
		for word in i.decode().split(' '):
			if word not in di:
				di[word] = 1
			else:
				#Top 3 words
				di[word] += 1

	li = [*di.values()]
	print(li)
	for i in range(3):
		a.append(li.pop(max(li)))
	print(a)
	print(di)
	new_di = {}
	for ele in a:
		for k,v in six.iteritems(di):
			if ele == v:
				new_di[k] = v 
				break
			
	print("=================================")
	print(new_di)
	print("returning...........................")
	return jsonify(new_di)


#How to run flask app on linux
##export FLASK_APP=flask_app
##export FLASK_ENV=development
##flask run

if __name__ == '__main__':
	app.run()
