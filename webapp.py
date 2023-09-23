from flask import Flask, jsonify, request

app = Flask(__name__)
  
@app.route('/home', methods = ['GET'])
def home():
    data = "Hi This is Sarbaroop Ghosh"
    return jsonify({'data': data})
  

if __name__ == '__main__':
  
    app.run(debug = True, host="0.0.0.0", port=80)