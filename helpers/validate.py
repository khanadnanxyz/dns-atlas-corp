from marshmallow import fields, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class DataSchema(ma.Schema):
    x = fields.Float(required=True)
    y = fields.Float(required=True)
    z = fields.Float(required=True)
    vel = fields.Float(required=True)
