from app import db


class Message(db.Model):
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