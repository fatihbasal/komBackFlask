from db import db

class ClotheModel(db.Model):
    __tablename__ = "clothes"
    
    id = db.Column(db.Integer,primary_key= True)
    type_id = db.Column(db.Integer,nullable = False)
    name = db.Column(db.String(80),unique = True,nullable = False)
    color = db.Column(db.String(80),nullable = False)
    
    #comment
    
    
    
    
    
    
    