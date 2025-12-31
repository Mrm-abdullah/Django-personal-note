# project a commend calao
""" pip freeze>requirements.txt """

# py manage.py collectstatic

# all file zip koro
# c panel a jao --- poyojone subdomain create koro

# setup python app 
""" 
    click  to --- create aplications
    -- version
    Application root -- site name (termi)
    -- domain select

    create--
 """
# zip file ta etract koro (termi) te
# passenger_wsgi.py -- k edit koro
 
""" 
from project nam.wsgi import application
from termi.wsgi import application
 """
 # terminal theke pip install a 
"""  requirements.txt """
# host allow kore nin
""" setting theke 
'termi.alfikhbd.com','www.termi.alfikhbd.com'
app restart korun
 """

# debug= False koro

# (termi) theke ---media & static---- tarmi.domian.com a niye jao. ba public a root ar moto akta num ace dekho

""" 

# deploy a
""" 

"""
from django.urls import re_path as url
from django.views.static import serve

urlpatterns ar vitor upore> 
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
 """


# /home/alfikhbd/bondhu.alfikhbd.com """

######################################################
###################################################### Mysql
######################################################

# pip install mysqlclient
""" 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'your_database_name',
#         'USER': 'your_mysql_username',
#         'PASSWORD': 'your_mysql_password',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#             'init_command': "SET NAMES 'utf8mb4'",
#         }
#     }
# }
 """
# domain name dekhanor jonno
"""
<span id="domainName"></span>
<script>
  const domainNameElement = document.getElementById('domainName');
  domainNameElement.textContent = window.location.hostname;
</script>
 """