# http://127.0.0.1:5000/

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
	return "Hey There Griffin how about a commit:"

if __name__ == "__main__":
	app.run()

