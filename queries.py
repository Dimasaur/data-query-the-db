# pylint:disable=C0111,C0103

import sqlite3


def query_orders(db):
    # return a list of orders displaying each column
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    query = """
    SELECT * FROM Orders
    """
    results = db.execute(query)
    results = results.fetchall()
    return results


# conn = sqlite3.connect('data/ecommerce.sqlite')
# db = conn.cursor()
# results=query_orders(db)
# print(results)

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    query = f"""
    SELECT * FROM Orders
    WHERE OrderDate > '{date_from}' AND OrderDate <='{date_to}'
    """
    results = db.execute(query)
    results = results.fetchall()
    print(results)
    return results

# conn = sqlite3.connect('data/ecommerce.sqlite')
# db = conn.cursor()
# date_from = '2020-01-01'
# date_to = '2025-01-01'
# result = get_orders_range(db, date_from, date_to)
# print(result)


def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    query = """
    SELECT
	*,
	JULIANDAY(orders.ShippedDate) - JULIANDAY(orders.OrderDate) AS TimeDelta
    FROM Orders
    ORDER BY TimeDelta ASC
    """
    results = db.execute(query)
    results = results.fetchall()
    print(results)
    return results
