# install koro

# pip install djangorestframework
""" pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support """

#seetting > app
""" 
INSTALLED_APPS = [
    ...
    'rest_framework',
]
"""
# main url
""" 
 urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
  """