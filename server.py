from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/survey', methods=['POST'])
def survey_info():
  print "Submitted!"

  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']

  return render_template("result.html", name2=name, location2=location, language2=language, comment2=comment)

app.run(debug=True) # run our server
