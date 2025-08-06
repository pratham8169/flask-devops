from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 Hello from Flask DevOps Pipeline! this is my start of devops tourand this is weebhook automation"

@app.route('/about')
def about():
    return "This is about page of my flask app. Pratham Shetty"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
