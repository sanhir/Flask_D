from flask import request, redirect, url_for, render_template, flash, session
from salary import app

@app.route('/')
def hoge():
    return