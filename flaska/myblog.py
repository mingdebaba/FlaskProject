from app import app
#命令行运行set FLASK_APP=myblog.py
#命令行运行set FLASK_ENV=development
#flask run
#防止被引用后执行，只有在当前模块中才可以使用
if __name__=='__main__':
    app.run()