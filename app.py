from flask import Flask, render_template

app = Flask(__name__)

# Sample data
projects = [
    {"name": "CI/CD Pipeline with Jenkins", "year": 2026},
    {"name": "Auto Scaling Web App on AWS", "year": 2026},
    {"name": "Monitoring with Prometheus & Grafana", "year": 2026}
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
