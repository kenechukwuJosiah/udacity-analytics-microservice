from flask import Flask
app = Flask(__name__)

def log():
    print("logging................................")
    print("loading................................")

log()

@app.route('/')
def hello_world():
    print("hello world")
    return 'Hello, Docker!'

@app.route("/health_check")
def health_check():
    return "ok"


@app.route("/readiness_check")
def readiness_check():
        return "ok"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5153"), debug=False)