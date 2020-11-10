"""
如需从 Company 列中仅选取唯一不同的值，我们需要使用 SELECT DISTINCT 语句：
SELECT DISTINCT Company FROM Orders

ORDER BY 语句默认按照升序对记录进行排序
如果您希望按照降序对记录进行排序，可以使用 DESC 关键字。
以逆字母顺序显示公司名称，并以数字顺序显示顺序号：
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC, OrderNumber ASC

我们也可以指定所要插入数据的列：
INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)

Update 语句用于修改表中的数据。
UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值

DELETE 语句用于删除表中的行。
DELETE FROM 表名称 WHERE 列名称 = 值

通过使用 NOT 关键字，我们可以从 "Persons" 表中选取居住在不包含 "lon" 的城市里的人：
SELECT * FROM Persons
WHERE City NOT LIKE '%lon%'   "%" 可用于定义通配符（模式中缺少的字母



"""