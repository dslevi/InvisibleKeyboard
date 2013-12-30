from flask import Flask, render_template, redirect, request, url_for
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route("/")
def touch():
    return render_template("touch.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
