from app.model.user import Users
import random, string
from flask_seeder import Seeder, Faker, generator



class User(Users):
    def _init_(self, name=None, email=None, password=None):
        self.name = name 
        self.email = email
        self.password = password

    def _str_(self):
        return "Name=%s, Email=%s, Password=%s" % (self.name, self.email, self.password)
    


class UserSeeder(Seeder):


    def run(self):

        name = generator.Name()
        faker = Faker(
            cls=User,
            init={
                "name": name,
                "email": ''.join(random.choice(string.ascii_letters) for i in range(10)) + "@mail.com",
                "password": "secret"
            }
        )


        for user in faker.create(1):
            print("Adding user: %s" % user)
            self.db.session.add(user)