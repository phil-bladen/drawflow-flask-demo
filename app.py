from flask import Flask, render_template


app = Flask(__name__)

posts = [
    {
        'author': 'Dr. Nancy Smith',
        'title': 'FASTA Project 2.4',
        'attributes': '- Current Step: FASTA calculation 2\n- Total Calculations: 4\n - ETA: 7h',
        'description': 'PThis project computes the FASTA data necessary for iteration 2.4 of product codename Whitestar',
        'date_posted': 'January 10, 2022',
        'picURL': 'https://www.computerhope.com/jargon/f/flowchart.jpg'
    },
    {
        'author': 'Eric Eisenberg Ph.D.',
        'title': 'RNA Fold Attempt 3',
        'description': 'Project Description: \n-3 total calculations\n',
        'attributes': '- Protein Folds: 5\n',
        'date_posted': 'January 8, 2022',
        'picURL': 'https://miro.medium.com/max/432/1*0mFwslUH5H_X3HyfRia20Q.png',
    }
]

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

@app.route('/running_projects')
def projects():
    return render_template('running_projects.html', posts=posts)
