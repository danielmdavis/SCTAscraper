from flask import Flask
import sctaScript

app = Flask(__name__)
@app.route("/")
def output():
    return sctaScript.opportunity_payload()

if __name__ == "__main__":
    app.run()

