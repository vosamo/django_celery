Django中使用Celery完成异步任务。没有使用Django-celery，而是在工程目录下新建Celery配置文件。

## 依赖描述

- Django 1.8.2
- Celery 3.1.23
- RabbitMQ-server 3.3.5-17.el17

## 使用说明

安装依赖，启动rabbitmq-server：`systemctl start rabbitmq-server`

克隆本仓库，进入工程目录下，`celery -A django_celery worker -l info`启动worker，其中django_celery是在`celery.py`中定义的Celery APP。

运行`python manage.py runserver 8008`，在浏览器中输入`http://127.0.0.1:8008/main`即可。

**注意：**启动worker必须在Django工程目录下，也就是manage.py同级目录下；如果部署在Apache上，每次修改tasks之后要重启Apache。
