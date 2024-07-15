import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import users
from schemas import UserSchema

blp = Blueprint("Users", __name__, description="Operations on users")


@blp.route("/user/<string:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(cls, user_id):
        try:
            return users[user_id]
        except KeyError:
            abort(404, message="User not found.")

    def delete(cls, user_id):
        try:
            del users[user_id]
            return {"message": "User deleted."}
        except KeyError:
            abort(404, message="User not found.")
            
@blp.route("/user")
class UserList(MethodView):
    
    def get(cls):
        return users.values()

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(cls, user_data):
        for user in users.values():
            if user_data["name"] == user["name"]:
                abort(400, message=f"User already exists.")

        user_id = uuid.uuid4().hex
        user = {**user_data, "id": user_id}
        users[user_id] = user

        return user
    
print(1)