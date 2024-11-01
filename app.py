
from flask import Flask
app = Flask(__name__)

@app.route("/pinto")
def index():
    return 'muito grande!'

if __name__ == "__main__":
    app.run()