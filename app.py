from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('poll'))

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        choice = request.form.get('vote')
        return redirect(url_for('summary', choice=choice))
    return render_template('poll.html')

@app.route('/summary/<choice>')
def summary(choice):
    return render_template('summary.html', choice=choice)

if __name__ == '__main__':
    app.run(debug=True)
