from flask import Flask, render_template, request, redirect, url_for, Markup, flash

application = Flask(__name__)
application.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@application.route('/welcome')
def welcome():
    success = Markup('<strong>Wow!!</strong> Login is Successful.')
    flash(success, 'success')
    return render_template("welcome.html")

@application.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = Markup('<strong>Oops!!</strong> Login failed due to incorrect username and password. <strong>Please try again.</strong>')
            flash(error, 'warning')
        else:
            return redirect(url_for('welcome'))
    return render_template("login.html")


if __name__ == '__main__':
    application.debug = True
    application.run()
