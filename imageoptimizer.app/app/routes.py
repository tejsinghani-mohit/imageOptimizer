from flask import Blueprint, render_template, current_app, url_for
import urllib.parse

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("we got here")
    return render_template('base.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/routes')
def list_routes():
    routes = []
    for rule in current_app.url_map.iter_rules():
        # Exclude static files and error handlers
        if not str(rule).startswith('/static') and not str(rule).startswith('/error'):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            routes.append({
                'endpoint': rule.endpoint,
                'methods': ','.join(rule.methods),
                'url': urllib.parse.unquote(url)
            })
    return render_template('routes.html', routes=routes)