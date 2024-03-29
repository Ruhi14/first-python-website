from flask import Flask, render_template ,jsonify

app = Flask(__name__)
JOBS = [
  {
    'id': 1,
   'title': 'Data Analyst',
   'location': 'Bengaluru',
   'salary': '10,00,000'
  },
  {'id': 2,
   'title': 'Data Scientist',
   'location': 'Hydrabad',
   'salary': '12,00,000'
  },
{'id': 3,
 'title': 'Backend-Engineer',
 'location': 'Remote',
},
{'id': 4,
 'title': 'Frontend-Engineer',
 'location': 'Pune',
 'salary': '15,00,000'
}
]


@app.route("/")
def helloruhi():
  return render_template("home.html", jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
