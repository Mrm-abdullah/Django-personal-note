# sortcut
# terminal a
"""
python -m pip install django-compressor
npm install tailwindcss @tailwindcss/cli --save-dev

"scripts": {
      "dev":"npx @tailwindcss/cli -i ./static/src/input.css -o ./static/src/output.css --watch",
      "build": "npx @tailwindcss/cli -i ./static/src/input.css -o ./static/src/output.css --minify"
    },

npm run dev
npm run build
"""





# go to ----    https://flowbite.com/docs/getting-started/django/

"""
python -m pip install django-compressor



INSTALLED_APPS = [
    ...
    'compressor',  # new
]

static
└── src
    └── input.css

"""
#    base.html --- a

"""
<!-- templates/_base.html -->

{% load compress %}
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django + Tailwind CSS + Flowbite</title>

    {% compress css %}
    <link rel="stylesheet" href="{% static 'src/output.css' %}">
    {% endcompress %}

</head>

<body class="bg-green-50">
    <div class="container mx-auto mt-4">
        {% block content %}
        {% endblock content %}
    </div>
</body>

</html>

"""
# npm install tailwindcss @tailwindcss/cli --save-dev

"""
/* static/src/input.css */
@import "tailwindcss";
"""
#  package.json a
"""
"scripts": {
      "dev":"npx @tailwindcss/cli -i ./static/src/input.css -o ./static/src/output.css --watch",
      "build": "npx @tailwindcss/cli -i ./static/src/input.css -o ./static/src/output.css --minify"
    },
"""
# terminal a
"""
npm run dev
npm run build
"""
# body ar age
"""
<script src="https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.js"></script>

"""

# pip install whitenoise
"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # 👈 ADD HERE
    ...
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

"""
# python manage.py collectstatic --noinput
