Base = None
""" 
Tipos de Datos

String
Integer
Float
Boolean
DateTime

"""
Column, Integer, String, Float, Boolean, DateTime, db  = None

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    
    
""" 
INSERT INTO table_name (field1, field2, ... fieldN) VALUES ( value1, value2, ...valueN);
"""

user = User()
user.username = "lrodriguez@4geeks.co"
user.password = "123456"

db.session.add(user) #
db.session.commit() #


""" 
UPDATE table_name SET field1=value1, field2=value2, ... WHERE id = 1
""" 

user = User.query.get(1) # SELECT * FROM users WHERE id = 1
user.username = "lrodriguez@gmail.com" # UPDATE users SET username="lrodriguez@gmail.com" WHERE id = 1

db.session.commit()

""" 
DELETE FROM table_name WHERE condicion
"""

user = User.query.filter_by(username="lrodriguez@gmail.com").first()
db.session.delete(user)
db.session.commit()
