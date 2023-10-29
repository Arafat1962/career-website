from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title': 'Data Analyst',
        'location' : 'Gulshan, Dhaka',
        'salary': '40,000 tk'
    }, 
    {
        'id' : 2,
        'title': 'Frontend Engineer',
        'location' : 'Mohakhali, Dhaka',
        'salary': '35,000 tk'
    }, {
        'id' : 3,
        'title': 'Data Scientist',
        'location' : 'Mohakhali, Dhaka',
        'salary': '45,000 tk'
    }, {
        'id' : 4,
        'title': 'Backend Engineer',
        'location' : 'Bashundhara, Dhaka',
        'salary': '43,000 tk'
    }, {
        'id' : 5,
        'title': 'Backend Engineer',
        'location' : 'Bashundhara, Dhaka',
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name='Arafat')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)