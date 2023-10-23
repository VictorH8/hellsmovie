from flask import url_for, redirect

def page_not_found(e):
    return redirect(url_for('home'))
