from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
#def index():
#   user = {'username':'duke'}
 #   user = {'username':'duke'}
  #  html = '''
   # <html>
   # <head>
   #     <title>Home Page - Microblog</title>
   # </head>
   # <body>
   #     <h1>Hello, ''' + user['username'] + '''!</h1>
   # </body>
#</html>
#
#    '''
#    return html

#将需要展示的数据传递给模板进行显示
def index():
    user = {'username':'duduke'}
    
    post = [
        {
            'author':{'username':'liu'},
            'body':'这是第一个'
        },
        {
            'author':{'username':'dasan'},
            'body':'这是第二个'
        }
    ]

    return render_template('index.html',title='my',user=user,posts=post)


@app.route('/login',methods=['GET','POST'])
def login():
    #创建表单实例
    form = LoginForm()
    #验证表格中的数据格式是否正确
    if form.validate_on_submit():
        #闪现的信息会出现在页面，当然在页面上要设置
        flash('用户登录的用户名是{},是否记住我:{}'.format(
            form.username.data,form.remember_me.data))
            #重定向至首页
        return redirect(url_for('index'))
        #首次登录/数据格式错误都会是在登录界面
    return render_template('login.html',title='登录',form=form)
