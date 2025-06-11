# STATIC_ROOT = 'staticfiles'
""" pip freeze>requirements.txt """
# python manage.py collectstatic

# create Repository name in github
# open git bash

""" 
echo "# aiquest-batch3" >> README.md
git init
git add . # all commit korar jonno
git commit -m "first upload"
git branch -M main
git remote add origin https://github.com/Mrm-abdullah/aiquest-batch3.git
git push -u origin main
"""

# git init
# git add . # all commit korar jonno
# git commit -m "first upload"
""" 
  git config --global user.email "mohammodraselmia128@gmail.com"
  git config --global user.name "mrmabdullah"

"""
# git remote add origin https://github.com/Mrm-abdullah/aiquest-batch3.git
# git push -u origin master

#  anywhere--->>>
#  go to  console , click Bash
# terminal a ---->  git clone https://github.com/Mrm-abdullah/aiquest-batch3.git # github theke

# mkvirtualenv --python=/usr/bin/python3.10 jekono env name


# command
""" 
pwd #bortoman directory dekhabe
ls #bortoman folder a acen ta dekhabe
cd name #
pip list #
"""
# manage.py a r directory lagbe --->
# /home/mrmabdullah/aiquest-batch3/Ecommerce

#  go to anywhere web
""" 
 Add a new web app
 next
 Manual configuration (including virtualenvs)
Python 3.10
next
"""
""" 
pip list
pip install django django==4.2.3
"""
# Virtualenv: te
""" 
/home/mrmabdullah/.virtualenvs/env-batchthree # manage.py porjonto path
"""
# Code:
""" 
Source code: /home/mrmabdullah/aiquest-batch3/Ecommerce
WSGI configuration file: # click new tab
"""

# cooment out koro
""" 
import os
import sys

if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""

""" 
#path = '/home/mrmabdullah/mysite' # atar poriborte nicer ta line= 34+48
path = '/home/mrmabdullah/aiquest-batch3/Ecommerce'

#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings' # atar poriborte nicer ta
os.environ['DJANGO_SETTINGS_MODULE'] = 'Ecommerce.settings'
"""
# save kore reload koro

# click file new tab for setting ar jonno

# web>Static files: 
""" 
URL: /static/
Directory: /home/mrmabdullah/aiquest-batch3/Ecommerce/Shop/static/

URL: /media/
Directory: /home/mrmabdullah/aiquest-batch3/Ecommerce/media/

URL: /static/
Directory: /home/mrmabdullah/aiquest-batch3/Ecommerce/staticfiles/
"""

# Force HTTPS: enable korio jodi https na dekhay.