from flask import Flask, render_template
import requests

app = Flask(name)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def pokemon(query):
	req = requests.get('https://www.pokeapi.co/api/v2/pokemon/'+query)
	r = req.json()

	if(req.status_code != 200):
		return "<h1>Sorry, that couldn't be found!</h1>"

	if (r["name"] == query):	
		return "<h1>The pokemon with id {} is {}!!</h1>".format(query, r["id"])

	elif(r["id"] == int(query)):
		return "<h1>{} has id {}</h1>!!!".format(query, r["name"])


if name == 'main':
    app.run()