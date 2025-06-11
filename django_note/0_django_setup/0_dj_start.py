# create a Folder for project
# create virtual environment in cmd
""" python -m venv (env name) """
""" env\Scripts\activate   
    source  env/bin/activate #linux
"""

# active env
""" cd env, cd Scripts, activate """

#Install, uninstall and setup and cheack(Django) (env directory)
#back (cd .., cd ..)
""" 
pip install django 
pip uninstall django 
django-admin --version
"""

# satart a django startproject
""" django-admin startproject (project name) """
""" cd (project name) """

#-------------------------------setting.py------------------------------#
#import os >>>>for old version
""" import os """

#templates dir (BASE_DIR ar pore likho) -------templates folder create koro age
""" TEMPLATES_DIR = os.path.join(BASE_DIR,'templates') """ #>>>> old version 
""" TEMPLATES_DIR = BASE_DIR/'templates' """ #>>>> update version
#-----------tamplate dir call dao
""" 'DIRS': [TEMPLATES_DIR,], """


#static dir -------static folder create koro age 
""" STATIC_DIR = BASE_DIR/ 'static' """ #>>>> update version
#-----------static dir calling and Media file bebohar krar jonno >>> setting.py
"""
STATIC_URL = 'static/'
STATIC_ROOT = 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
STATICFILES_DIRS =[
    STATIC_DIR,
]
"""

#------time zone ----------#
""" Asia/Dhaka """


# imag restore koranor jonno...... main urls
""" from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
"""
#  pip install pillow



# showmigrations, makemigrations and migrate
""" python manage.py showmigrations """ #show showmigrations
""" python manage.py makemigrations """ # makemigrations
""" python manage.py migrate """ #migrate
""" python manage.py sqlmigrate app-name""" #ki kaj hoice ta dekhabe


# create super user
""" python manage.py createsuperuser """
# python manage.py runserver
# python manage.py collectstatic


# cmd command
""" 
mkdir (nam)    # folder toiri korar jonno
cls            #cmd clear korar jonno 

"""

########################################################################
################################# 2nd file###########################
########################################################################


#------setting.py------#
#import
""" import os """
#modiol
"""  pillow, crispy """


#---------main urls.py-------#

""" from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """
#ba----cleaver code

""" from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """

# deploy a
""" 
from django.urls import re_path as url
from django.views.static import serve

urlpatterns ar vitor upore> 
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
 """

# pip install -r requirements.txt

######################################################################################
##########################    aiquest ecommerce course    ##########################
######################################################################################

# app ar bitor 'templates' name folder create kore okhane static file rakhte paro. tokhon settings a TEMPLATES a DIRS deoya lagbena.