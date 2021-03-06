from flask import request, redirect, render_template, session, flash
import cgi
from app import app, db
from models import Blog


@app.route("/newpost", methods=['POST', 'GET'])
def newpost():
    
    blog_title_error = ''
    blog_body_error = ''
    
    if request.method == 'POST':
        blog_title = request.form.get('blog')
        if len(blog_title) < 1:
            blog_title_error = ('Your title must contain at least 1 character')
            
        blog_body = request.form.get('blog-body')
        if len(blog_body) < 1:
            blog_body_error = ('Your blog body must contain at least 1 character')
        
        if any([blog_title_error, blog_body_error]):
            return render_template('newpost.html', blog_title_error=blog_title_error, blog_body_error=blog_body_error, blog_title=blog_title, blog_body=blog_body)
        else:
            new_blog = Blog(blog_title, blog_body)
            db.session.add(new_blog)
            db.session.commit()
            new_blog_id = new_blog.id
            blog = Blog.query.get(new_blog_id)
            return render_template('/blog.html', blog=blog)

    return render_template('newpost.html', title="Add New Blog Post")

def blog_checkoff():

    blog_id = int(request.form['blog-id'])
    blog = Blog.query.get(blog_id)
    blog.posted = True
    db.session.add(blog)
    db.session.commit()
    return redirect('/newpost')

@app.route('/blog', methods=['GET'])
def blog():
    
    blog_id = int(request.args.get('id'))
    blog = Blog.query.get(blog_id)
    
    return render_template('blog.html', blog=blog)
    

@app.route('/', methods=['GET','POST'])
def index():   
    
    
    posted_blogs = Blog.query.all()
    return render_template('index.html',posted_blogs=posted_blogs)

        


if __name__ == '__main__':
    app.run()