from tortoise import fields, Model

class User(Model):
    tg_id = fields.IntField(pk=True)