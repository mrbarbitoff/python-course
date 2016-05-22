-- All user info
select * from Users;

-- User count
select count(*) from Users;

-- Starpers
select count(*) from Users where birth_date <= date("1976-05-22");

-- By country
select country, count(*) from Users group by country;

-- Users with equal name
select name, count(*) as cnt from Users group by name order by cnt desc limit 1;
-- They exist

-- Orders in 2016
select count(*) from Orders where created >= date("2016-01-01");

-- Best day ever
select date(created), count(*) as cnt from Orders group by date(created) order by cnt desc limit 1; 

-- Percent not paid
select 1 - sum(paid)*1.0/count(*) from Orders;

-- All about bread
select * from Goods where name like "%bread%";

-- 10 most popular goods
select Goods.id, Goods.name, count(*) as cnt from GoodsInOrders inner join Goods on GoodsInOrders.good_id = Goods.id inner join Orders on GoodsInOrders.order_id = Orders.id group by Goods.name order by cnt desc limit 10;

-- Profit in 2016
select sum(price) from GoodsInOrders inner join Goods on Goods.id = GoodsInOrders.good_id inner join Orders on Orders.id = GoodsInOrders.order_id where paid = 1;

-- WOMEN!
select Goods.id, Goods.name from GoodsInOrders inner join Goods on GoodsInOrders.good_id = Goods.id inner join Orders on GoodsInOrders.order_id = Orders.id inner join Users on Orders.user_id = Users.id where Users.gender = "F" group by Goods.name order by count(*) desc limit 10;

-- Kilos
select Users.id, Users.name from GoodsInOrders inner join Goods on GoodsInOrders.good_id = Goods.id inner join Orders on GoodsInOrders.order_id = Orders.id inner join Users on Orders.user_id = Users.id where Goods.units like "%KG%" group by Users.id order by sum(case when units = 'KG' then 1 else cast(units as decimal) end) desc limit 1;

-- Most popular good in each country
select country, good_id, name, max(cnt) from (select *, count(*) as cnt from GoodsInOrders inner join Goods on Goods.id = GoodsInOrders.good_id inner join Orders on Orders.id = GoodsInOrders.order_id inner join Users on Orders.user_id = Users.id group by Users.country, Goods.id) group by country;
-- Do not guarantee it is OK
