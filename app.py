from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "test 2 o devops webhook  CI/CD pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
