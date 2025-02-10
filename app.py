import os
import random

from flask import Flask, redirect, render_template, request, url_for

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# # Configura banco de dados
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///careeafeto.db'
# app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True
# db = SQLAlchemy(app)


# ## Cria tabelas do banco
# with app.app_context():
#     db.create_all()


@app.route("/")
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4000)



