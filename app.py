from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/pokemon/<query>', methods=['GET'])
def main():
	if type(query) == type(''):
		GET api/v2/ability/query
		return query + ' has id ' + str(id)
	if type(query) == type(1):
		GET api/v2/ability/query
		return 'The pokemon with id ' + query + ' is ' + str(name)

if __name__ == '__main__':
    app.run()
