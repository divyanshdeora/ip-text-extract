from flask import *
from werkzeug import secure_filename
import scan
import os
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = '/home/divyansh/projects/textractor/'

@app.route('/', methods = ['GET', 'POST'])
@cross_origin()
def index():
	print "Requesting"
	if request.method == 'POST':
		print "Posting"
		print str(request.files)
		try:
			f = request.files['file']
			f.save(secure_filename(f.filename))
			imgText = scan.scan(str(app.config['UPLOAD_FOLDER']+f.filename))
			print "Viewing"
			return json.dumps({'status':True,'imgText':imgText})
		except Exception, e:
			print str(e)
			return json.dumps({'status':False,'description':str(e)})
	
	else:
		return render_template('index.html')
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')