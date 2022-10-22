from flask import request, current_app
import jwt

from implemented import user_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get('HTTP_AUTHORIZATION', '').replace('Bearer ', '')

        if not token:
            return "Вы не передали токен в заголовке"

        try:
            jwt.decode(token,
                       key=current_app.config['SECRET_KEY'],
                       algorithms=current_app.config['ALGORITHM'])
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return "Ошибка валидации токена"

    return wrapper

def admin_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        if not token:
            return "Вы не передали токен в заголовке"

        try:
            data = jwt.decode(token,
                       key=current_app.config['SECRET_KEY'],
                       algorithms=current_app.config['ALGORITHM'])

            user = user_service.get_by_username(data.get("username"))
            if user:
                if not user.role == "admin":
                    return "Вам доступ запрещен"
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return "Ошибка валидации"

    return wrapper
