from flask import url_for, redirect

def erro(nome):
    return redirect(url_for('home'))
