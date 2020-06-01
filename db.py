from app import db
from sqlalchemy_serializer import SerializerMixin



class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String())
    created_on = db.Column(db.String)

    def __init__(self, message, created_on):
        self.message = message
        self.created_on = created_on

    def __repr__(self):
        return '<message_id {}>'.format(self.message_id)

    def serialize(self):
        return {
            'message_id': self.message_id,
            'message': self.message,
            'created_on': self.created_on,
        }

    def to_json(self):
        return {
            'message_id': self.message_id,
            'message': self.message,
            'created_on': self.created_on.strftime("%d-%b-%Y (%H:%M:%S.%f)"),
        }