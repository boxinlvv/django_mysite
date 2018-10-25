from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from django.conf import settings

#获取当前文件夹名，即为该Django的项目名
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name

#设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)
 
#实例化Celery
app = Celery(project_name)


# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
#使用django的settings文件配置celery
app.config_from_object('django.conf:settings', namespace='CELERY')

#Celery加载所有注册的应用
app.autodiscover_tasks()

# 允许root 用户运行celery
platforms.C_FORCE_ROOT = True

