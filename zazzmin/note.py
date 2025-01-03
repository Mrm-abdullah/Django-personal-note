# settings.py

# app > sobar upore

'jazzmin',


JAZZMIN_SETTINGS = {

    "site_title": "World Talas News",
    "site_brand": "World Talas News",
    # "site_icon": None, # 32*32

    # # login 
    # "site_logo": "books/img/logo.png",
    # "login_logo_dark": None,
    # "site_logo_classes": "img-circle",
    "welcome_sign": "Welcome to the World Talas News",

    # "login_logo": "books/img/logo.png",
    # "site_header": "World Talas News",
    

    # # footer
    "copyright": "World Talas News",

    # ############
    # # Top Menu #
    # ############

    # # Links to put along the top menu
    "topmenu_links": [

        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://facebook.com/mrm.abdullah1234", "new_window": True},
        {"model": "auth.User"},
    ],


}
JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
}
