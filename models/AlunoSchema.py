from marshmallow import Schema, fields, ValidationError

class AlunoSchema(Schema):
    idade = fields.Integer(required=True)
    disciplina = fields.String(required=True)