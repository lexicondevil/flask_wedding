from flask_assets import Bundle, Environment
from app import app

js = Bundle(
        'js/lib/bootstrap.js',
        'js/lib/grayscale.js',
        'js/lib/jquery.js',
        output='gen/js_bundle.js',
        filters='jsmin'),

css = Bundle(
        'css/lib/bootsrap.css',
        'css/lib/grayscale.css',
        output='gen/css_bundle.css',
        filters='cssmin')

assets = Environment(app)

assets.register('js_all', js)
asssets.register('css_all', css)