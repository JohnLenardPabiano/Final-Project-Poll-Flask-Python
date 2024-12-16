from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample poll data
poll_data = {
    "question": "What's your favorite programming language?",
    "options": ["Python", "JavaScript", "C++", "Java", "Other"],
    "votes": [0, 0, 0, 0, 0],
}

@app.route('/')
def index():
    return render_template('index.html', poll=poll_data, enumerate=enumerate)

@app.route('/vote', methods=['POST'])
def vote():
    option = request.form.get('option')
    if option and option.isdigit():
        option_index = int(option)
        if 0 <= option_index < len(poll_data['options']):
            poll_data['votes'][option_index] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html', poll=poll_data, zip=zip)


if __name__ == '__main__':
    app.run(debug=True)
2