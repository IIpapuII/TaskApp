from flask import Flask , Blueprint, Response, render_template, jsonify
from ..models.exceptions import PageNotFound

check_errors = Blueprint('errors',__name__)

""" def __generate_error_reponse(error: Exception) -> Response:
    message ={
        'ErroType': str(type(error).__name__),
        'Menssage': str(error)
    }
    return render_template('404.html',**message) """

@check_errors.errorhandler(404)
def handle_page_not_found(error):
    #reponse = __generate_error_reponse(error)
    #reponse.status_code = 404
    print('Error econtrado')
    return render_template('404.html',error= error)