from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    print('ok')
    return "Hello from GET API1!"

@app.route("/api/motivation", methods=["GET"])
def motivation():
    category = request.args.get('category', 'กำลังใจ')
    url = f"http://app2:5000/api/quote?category={category}"
    response = requests.get(url)
    print('ok')
    return response.json()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
