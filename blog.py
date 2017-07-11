from flask import request, redirect, render_template, session, flash
import cgi
from app import app, db
from models import Blog

@app.route('/', methods=['GET','POST'])
def index():
    blog_ids = Blog.query.filter_by(id).all()