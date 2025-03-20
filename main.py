from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        astronaut_id = request.form['astronaut_id']
        astronaut_password = request.form['astronaut_password']
        captain_id = request.form['captain_id']
        captain_token = request.form['captain_token']
        return redirect(url_for('success'))

    return render_template('login.html')


@app.route('/success')
def success():
    return "Доступ предоставлен!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')