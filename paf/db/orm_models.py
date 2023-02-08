from peewee import *
from config import host, user, password, db_name, port

db = PostgresqlDatabase(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )


# A base model that will use our PostgreSQL database
class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel):
    first_name = CharField(50)
    nickname = CharField(50)

    class Meta:
        db_table = 'users'


class Order(BaseModel):
    user_id = ForeignKeyField(User)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"{self.user_id}, {self.id}"
