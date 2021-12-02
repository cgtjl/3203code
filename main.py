import app as app
from flask import Flask, render_template, request, session, url_for, redirect



@app.route("/")
def main():
    return render_template('main.html')