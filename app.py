#from flask import Flask, render_template
#
#app= Flask(__name__)
#
#@app.route('/')
#def main():
#    return render_template('index.html')
#
#app.run(host='0.0.0.0', port='5000')


from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/registro/<int:id>', methods=['PUT','DELETE'])
@app.route('/registro/<numero>', methods=['GET'])
def main(id,numero):
if request.method == 'GET':
return jsonify({
'msg':'This is the GET method'
})

if request.method == 'PUT':
return jsonify({
'msg': id
})



app.run(host='0.0.0.0', port='5000')


