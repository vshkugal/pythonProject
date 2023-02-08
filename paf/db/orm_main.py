from orm_models import *

with db:
    db.create_tables([User, Order])
    print(f"[INFO] Tables created successfully")

with db:
    User(id=0, first_name='Ivan', nickname='python_mentor').save(force_insert=True)
    User.create(id=1, first_name='Andrei', nickname='python_learner1')
    User.create(id=2, first_name='Valentina', nickname='python_learner2')
    User.insert(id=3, first_name='Vladimir', nickname='python_learner3').execute()
    print(f"[INFO] User Data was successfully inserted")

with db:
    Order.insert_many([
        {'id': 16, 'user_id': 1},
        {'id': 17, 'user_id': 2},
        {'id': 18, 'user_id': 2},
        {'id': 19, 'user_id': 3},
    ]).execute()
    print(f"[INFO] Rows added to the Orders' table successfully")

with db:
    users = User.select()
    orders = [
        {'id': 26, 'user_id': users[1].id},
        {'id': 27, 'user_id': users[2].id},
        {'id': 28, 'user_id': users[2].id},
        {'id': 29, 'user_id': users[3].id},
    ]
    Order.insert_many(orders).execute()
    print(f"[INFO] Rows added to the Orders' table successfully")

with db:
    users = User.select()
    orders = [
        {'id': 36, 'user_id': users[1]},
        {'id': 37, 'user_id': users[2]},
        {'id': 38, 'user_id': users[2]},
        {'id': 39, 'user_id': users[3]},
    ]
    Order.insert_many(orders).execute()
    print(f"[INFO] Rows added to the Orders' table successfully")

with db:
    print('-------')
    result = User.select().dicts()
    for i in result:
        print(f"User {i}")

with db:
    print('-------')
    result = Order.select().where(Order.user_id == 1).dicts()
    for i in result:
        print(f"Order {i}")

with db:
    print('-------')
    result = Order.select().join(User).where(User.id == 3).dicts()
    for i in result:
        print(f"Order {i}")

with db:
    print('-------')
    result = Order.select().where(Order.user_id == 2)
    for i in result:
        print(f"Order: {i.id}, User: {i.user_id.first_name}")

with db:
    print('-------')
    result = Order.select()
    for i in result:
        print(f"Order: {i.id}, User: {i.user_id.first_name}")
