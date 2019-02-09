from flask import Flask, render_template, request
import readText
app = Flask(__name__)

notes = []
location = -1

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/forward', methods=['POST'])
def forward():
    global notes
    global location
    if (notes == []):
        notes = readText.returnText(request.form['name'])
    print(notes)
    location +=1
    return render_template('notes.html', note=notes[location])

@app.route('/backward', methods=['POST'])
def backward():
    global notes
    global location
    if (notes == []):
        notes = readText.returnText(request.form['name'])
    print(notes)
    location -=1
    return render_template('notes.html', note=notes[location])

if __name__ == '__main__':
	app.run(debug=True)