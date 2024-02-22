from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars2.db")
    # app.run()
    user1 = User()
    user1.surname = "Scott"
    user1.name = "Ridley"
    user1.age = 21
    user1.position = "captain"
    user1.speciality = "research engineer"
    user1.address = "module_1"
    user1.email = "scott_chief@mars.org"
    user1.hashed_password = "cap"
    user2 = User()
    user2.surname = "John"
    user2.name = "Cook"
    user2.age = 22
    user2.position = "cook"
    user2.speciality = "cook"
    user2.address = "module_3"
    user2.email = "john_cooker@mars.org"
    user2.hashed_password = "food"
    user3 = User()
    user3.surname = "Lisa"
    user3.name = "Moner"
    user3.age = 20
    user3.position = "nurse"
    user3.speciality = "practitian doctor"
    user3.address = "module_2"
    user3.email = "lisa1234@mars.org"
    user3.hashed_password = "h1e1l1p1p1l1a1n1e1t"
    db_sess = db_session.create_session()
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()


if __name__ == '__main__':
    main()