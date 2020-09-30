from tntblog.blog_posts.views import blog_post
from flask import render_template,request,Blueprint
from tntblog.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    #grabing blogposts to display on index page
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=10)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/info')
def info():
    return render_template('info.html')
