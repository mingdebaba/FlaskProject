
源地址
https://blog.csdn.net/u014793102/article/details/80372815?spm=1001.2014.3001.5502
https://github.com/Liangchengdeye/FlaskQuickStart

使用nginx配置部署网页
ubuntu
cd /etc/nginx/conf.d
vi mysite.conf

server{
    listen 80;
    sercer_name 47.74.3.178;
    charset utf-8;
    access_log  /var/log/nginx/log/mysite.access.log main;
    error_log   /var/log/nginx/log/mysite.error.log warn;
    location    /{
        root    /srv/cms;
        index   index.html index.html;
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:5000;
    }
}