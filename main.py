import sqlalchemy
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from models import User, Measurement, create_tables

LOGIN = 'postgres'
PASSWORD = input('Password: ')
DB = 'pm_db'

DSN = f"postgresql://{LOGIN}:{PASSWORD}@localhost:5432/{DB}"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_user(name, lastname):
    user = User(name=name, lastname=lastname)
    session.add(user)
    session.commit()

def create_measurement(user_id, date, hp, lp, heart_rate):
    measurement = Measurement(user_id=user_id, date=date, hp=hp, lp=lp, heart_rate=heart_rate)
    session.add(measurement)
    session.commit()

def get_users():
    for u in session.query(User).all():
        print(u)

def get_measurements(_user_id):
    for m in session.query(Measurement).join(User.measurements).filter(User.id == _user_id).all():
        print(m)


session.close()


def main():
    now = datetime.now()
    # create_user(name=input("Как Вас зовут? "), lastname=input("Какая у Вас фамилия? "))
    # create_measurement(user_id=input("Укажите ID пользователя: "), date=now, hp=input("Введите верхнее давление: "), lp=input("Введите нижнее давление: "), heart_rate=input("Укажите частоту сердцебиения: "))
    get_users()
    # get_measurements(_user_id=input("Укажите ID пользователя: "))


if __name__ == "__main__":
    main()
