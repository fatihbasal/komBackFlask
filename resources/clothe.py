import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ClotheSchema, ClotheUpdateSchema
from db import clothes

blp = Blueprint("Clothes", __name__, description="Operations on clothes")


@blp.route("/clothe/<string:clothe_id>")
class Clothe(MethodView):
    @blp.response(200, ClotheSchema)
    def get(self, clothe_id):
        try:
            return clothes[clothe_id]
        except KeyError:
            abort(404, message="Clothe not found.")

    def delete(self, clothe_id):
        try:
            del clothes[clothe_id]
            return {"message": "Clothe deleted."}
        except KeyError:
            abort(404, message="Clothe not found.")

    @blp.arguments(ClotheUpdateSchema)
    @blp.response(200, ClotheSchema)
    def put(self, clothe_data, clothe_id):
        try:
            clothe = clothes[clothe_id]

            # https://blog.teclado.com/python-dictionary-merge-update-operators/ arastır surayı problem yasarsan
            clothe |= clothe_data

            return clothe
        except KeyError:
            abort(404, message="Clothe not found.")


@blp.route("/clothe")
class ClotheList(MethodView):
    @blp.response(200, ClotheSchema(many=True))
    def get(self):
        return clothes.values()

    @blp.arguments(ClotheSchema)
    @blp.response(201, ClotheSchema)
    def post(self, clothe_data):
        for clothe in clothes.values():
            if (
                clothe_data["name"] == clothe["name"]
            ):
                abort(400, message=f"Clothe already exists.")

        clothe_id = uuid.uuid4().hex
        clothe = {**clothe_data, "id": clothe_id}
        clothes[clothe_id] = clothe

        return clothe