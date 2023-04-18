from flask import Blueprint, request, make_response, redirect , render_template

prt = Blueprint('prue',__name__)

todos = ['Todo 1', 'Todo 2', 'Todo 3', 'Todo 4']

@prt.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)
    return response

@prt.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)