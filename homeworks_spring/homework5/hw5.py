#!/usr/bin/env python3

import sqlite3 as sq


def unpaid(user_id):
    query = "select Users.name, Orders.id, sum(price) from GoodsInOrders inner join Orders on Orders.id = GoodsInOrders.order_id inner join Goods on Goods.id = GoodsInOrders.good_id inner join Users on Users.id = Orders.user_id where Users.id = ? and Orders.paid = 0 group by Orders.id;"
    with sq.connect('data.sqlite') as dbh:
        cur = dbh.cursor()
        output = cur.execute(query, [user_id]).fetchall()
        return output
