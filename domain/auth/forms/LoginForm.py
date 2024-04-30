from apiflask import Schema
from apiflask.fields import String


class LoginForm(Schema):
    username = String(required=True)
    password = String(required=True)
