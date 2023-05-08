import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    lastname = sq.Column(sq.String(length=40), nullable=False)

    def __str__(self):
        return f"ID:{self.id} {self.name} {self.lastname}"

class Measurement(Base):
    __tablename__ = 'measurement'

    id = sq.Column(sq.Integer, primary_key=True)
    date = sq.Column(sq.DateTime, index=True)
    hp = sq.Column(sq.Integer)
    lp = sq.Column(sq.Integer)
    heart_rate = sq.Column(sq.Integer)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("user.id"), nullable=False)

    user = relationship(User, backref='measurements')

    def __str__(self):
        return f"ID:{self.id} {self.date} Давление:{self.hp}/{self.lp} HR:{self.heart_rate};"

def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)