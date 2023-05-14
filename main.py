import sqlalchemy
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
from datetime import datetime

from models import User, Measurement, create_tables

LOGIN = 'postgres'
PASSWORD = 'MPuzo1920'
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

def show_diagramm(_user_id):
    hp_list = []
    lp_list = []
    dates = []
    for m in session.query(Measurement).join(User.measurements).filter(User.id == _user_id).all():
        hp_list.append(m.hp)
        lp_list.append(m.lp)
        dates.append(str(m.date.date()))
    plt.style.use('bmh')
    fig, ax = plt.subplots()
    ax.plot(dates, hp_list, c='blue', linewidth=2)
    ax.plot(dates, lp_list, c='red', linewidth=2)
    ax.set_title("HP and LP measurements", fontsize=18)
    ax.set_xlabel('Dates', fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel('Pressure', fontsize=14)
    ax.tick_params(axis='both', labelsize=11)
    plt.show()


session.close()


def main():
    now = datetime.now()
    # create_user(name=input("Как Вас зовут? "), lastname=input("Какая у Вас фамилия? "))
    # create_measurement(user_id=input("Укажите ID пользователя: "), date=now, hp=input("Введите верхнее давление: "), lp=input("Введите нижнее давление: "), heart_rate=input("Укажите частоту сердцебиения: "))
    # get_users()
    # get_measurements(_user_id=input("Укажите ID пользователя: "))
    show_diagramm(_user_id=input("Укажите ID пользователя: "))

if __name__ == "__main__":
    main()
