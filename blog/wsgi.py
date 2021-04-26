"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
# import sys
# sys.path.append('E:\Python_Code\blog\blog')
# # 加入本项目的虚拟环境
# virtualenv_dir = 'E:\Python_Code\virtualenv\blog\Lib\site-packages'
# sys.path.insert(0, virtualenv_dir)  # 加入导包路径


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

application = get_wsgi_application()
