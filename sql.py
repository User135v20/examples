"""
SQL:
SELECT t.dt, u. name, t.price
FROM
transactions AS t
JOIN
users AS u USING(id)
"""

transactions = [{'dt': '2020-03-23', 'id': 'alyx', 'price': 1.0},
                {'dt': '1725-28-01', 'id': 'superpetr', 'price': 99.9},
                {'dt': '2019-11-23', 'id': 'alyx', 'price': 2.0},
                {'dt': '2013-12-02', 'id': 'morty', 'price': 13.5}, ]
users = [
    {'id': 'superpetr', 'name': 'Пётр Первый', 'gender': 'male', 'age': 52},
    {'id': 'alyx', 'name': 'Аликс Вэнс', 'gender': 'female', 'age': None}
]
# first
result_v1 = [
    {"dt": t['dt'], "name": u['name'], "price": t['price']} for t in transactions for u in users if u['id'] == t['id']
]

# second
users = {user["id"]: user["name"] for user in users}
result_v2 = [{"dt": t['dt'], "name": users[t["id"]], "price": t['price']} for t in transactions if t["id"] in users]
