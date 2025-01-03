# create virtual environment in cmd
""" python -m venv env """
""" env\Scripts\activate   """

#Install, uninstall and setup and cheack (Django) (env directory)
""" 
pip install django 
pip uninstall django 
django-admin --version
"""

# satart a django startproject
""" django-admin startproject (project name) """
""" cd (project name) """

#-------------------------------setting.py------------------------------#

#templates and static dir  (BASE_DIR ar pore likho) -------templates and static folder create koro age
"""
TEMPLATES_DIR = BASE_DIR/'templates'
STATIC_DIR = BASE_DIR/ 'static'
""" 

#-----------tamplate dir call dao
""" 'DIRS': [TEMPLATES_DIR,], """

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
""" 
from django.conf.urls.static import static
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


########################################################################
################################# 2nd file###########################
########################################################################


#------setting.py------#

#---------main urls.py-------#

""" 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """


# pip install -r requirements.txt

######################################################################################
##########################    aiquest ecommerce course    ##########################
######################################################################################

# app ar bitor 'templates' name folder create kore okhane static file rakhte paro. tokhon settings a TEMPLATES a DIRS deoya lagbena.