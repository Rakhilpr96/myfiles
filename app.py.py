from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hi():
	return 'MY NEW WEBSITE'


if __name__ == "__main__":
	app.run()


