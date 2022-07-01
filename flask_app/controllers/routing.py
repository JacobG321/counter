from flask_app import app
from flask import render_template, redirect, session, request


@app.route('/')
def index():
    if 'plus1' not in session: #looking for plus1 key
        session['plus1'] = 0 #resets to zero if not in session
        print("working")
    else:
        session['plus1'] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/x2')
def x2():
    if 'plus1' not in session:
        session['plus1'] = 0 #indicates it is a brand new page
        
    else:
        session['plus1'] += 1
    return redirect('/') #the redirect adds another 1 so we only add 1

@app.route('/choose_num', methods=["POST"])
def choose_num():
    if 'plus1' not in session:
        session['plus1'] = 0
    else:
        incrementBy = int(request.form["incrementer"]) - 1
        session['plus1'] += incrementBy
    return redirect('/')
    



