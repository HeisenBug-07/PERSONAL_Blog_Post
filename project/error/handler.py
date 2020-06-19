from flask import render_template, Blueprint

error_blueprint = Blueprint('error', __name__, template_folder='templates/error')


@error_blueprint.app_errorhandler(404)
def error_404(errors):
    return render_template('404.html'), 404