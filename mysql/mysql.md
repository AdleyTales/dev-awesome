
## Mysql分类（四类）

### 一、DDL

#### 操作数据库

- 创建数据库

- 查询数据库

- 修改数据库

- 删除数据库

- 使用数据库

```sql
show databases;

-- 查看创建数据库的创建语句
show create database test;

-- 创建数据库
create database db1;
-- 是否存在
create database if not exists db1;
-- 如果不存在创建一个db3 字符集为gbk
create database if not exists db3 character set gbk;

-- 修改数据库的字符集
alter database db3 character set utf8;
 
--  删除数据库
drop database db2;
 
-- 数据库如果存在，则删除
drop database if exist db3;
 
-- 使用数据库
use db1;

```

#### 操作数据表

- 查询表
- 创建表
- 查看表结构 desc
- 修改表
- 删除表

```sql
-- 查询表
show tables;

-- 创建表
create table 表名 (
	列名1 数据类型1,
    列名2 数据类型2,
    ...
    列名n 数据类型n
);

create table student(
  id int,
  name varchar(32),
  score double(4,1),
  birthday date,
  create_time timestamp
);

-- 查看建表信息 查看引擎 字符集
show create table stu; 

-- 查看表结构
desc student;

-- 修改表名
alter table student rename to stu;

-- 修改表的字符集
alter table stu character set utf8;

-- 添加列
alter table stu add 列名 数据类型;
alter tabl stu add gender int;

-- 修改列名 新列名 新数据类型
alter table stu change 原列 新列 新数据类型;
alter table stu change gender sex varchar(10);
alter table stu change gender sex int(2);
-- 修改列的数据类型
alter table stu modify 列名 新数据类型

-- 删除表
drop table stu;
-- 如果表存在，删除 sql不报错
drop table if exists stu;

```

##### mysql中表常用数据类型

```sql
int 整数类型
-- age int,

double 小数类型
-- score double(5,2) 小数最多有5位，小数点后面保留2位

date 日期类型 只是包含 年月日 yyy-MM-dd

datetime 日期 包含年月日时分秒 yyyy-MM-dd HH:mm:ss

timestamp 时间戳类型 包含年月日时分秒 yyyy-MM-dd HH:mm:ss
-- 如果不给这个字段赋值，系统自动填充

varchar 字符串类型 
-- username varchar(20), 最大20个字符 超过会报错

```

### 二、DML (增删改表中数据)

```sql
-- 插入数据
INSERT INTO student(
id,
NAME,
score
) VALUES (
 1,
 '王建',
 21.32323
)

--  删除表中所有数据，有多少条数据，就删除多少次（不推荐使用）
DELETE FROM student;

-- 先删除表没然后创建一张一样的表 （推荐使用）
TRUNCATE TABLE stident;

DELETE FROM student WHERE id=1 AND NAME='lisan';

-- 修改数据 update 表名 set 列名1=值1 
UPDATE student SET NAME='孙晓辉', score=99 WHERE id=3;

```

### 三、DQL （所有的查询语句）

- 单表查询
- 多表查询

```sql
--  查询所有
select * from 表名

-- 语法
select 
	字段列表
from 
	表名列表
where 
	条件列表
group by 
	分组字段
having
	分组之后的条件
order by
	排序
limit
	分页限定
	
```

```sql
-- 建表
CREATE TABLE stu(
  id INT, -- 编号
  NAME VARCHAR(20), -- 姓名
  age INT, -- 年龄
  sex VARCHAR(5), -- 性别
  address VARCHAR(100), -- 地址
  math INT, -- 数学
  english INT -- 英语
);

INSERT INTO stu(id, NAME, age, sex, address, math, english) 
VALUES
  (1, '马云', 55, '男', '杭州', 66, 78),
  (2, '马化腾', 45, '女', '深圳', 98, 87),
  (3, '马景涛', 55, '男', '香港', 56, 77),
  (4, '柳岩', 20, '女', '湖南', 76, 65),
  (5, '柳青', 20, '男', '湖南', 86, NULL),
  (6, '刘德华', 57, '男', '香港', 99, 99),
  (7, '马德', 22, '女', '香港', 99, 99),
  (8, '德玛西亚', 18, '男', '南京', 56, 65);
  
 SELECT * FROM stu;
 
 
-- 只是查询具体的字段列表
SELECT NAME,age FROM stu; 
 
SELECT 
	NAME, -- 姓名
	age   -- 年龄
FROM 
	stu;
 
SELECT address FROM stu;

-- 去除重复的结果集
SELECT DISTINCT address FROM stu;


SELECT NAME, address FROM stu;

-- 计算和
SELECT NAME,math,english, math+english FROM stu;

SELECT NAME,math,english, (math+english) AS he FROM stu;

SELECT NAME,math,english, math+IFNULL(english,0)  FROM stu;

SELECT NAME,math,english, (math+IFNULL(english,0)) AS 总分 FROM stu;

SELECT NAME,math,english, math+IFNULL(english,0)  FROM stu;

-- 别名 空格代替as
SELECT NAME,math 数学,english 英语, (math+IFNULL(english,0))  总分 FROM stu;
```

- 条件查询 where
- 运算符

```sql
> < <= >= = <>
in 
between and
like (_ 单个任意字符 %多个任意字符)
is null
and 或 &&
or 或 || 
not 或 |
```

```sql
SELECT * FROM stu WHERE age >= 20;

-- 等于 只有一个=
SELECT * FROM stu WHERE age = 20;

-- 不等于
SELECT * FROM stu WHERE age <> 20;


-- 大于20 小于30
SELECT * FROM stu WHERE age >= 20 && age <= 30;
-- 推荐
SELECT * FROM stu WHERE age >= 20 AND age <= 30;

SELECT * FROM stu WHERE age BETWEEN 20 AND 30;

-- 有一个条件成立即可
SELECT * FROM stu WHERE age = 19 OR age = 22 OR age =33;
-- 推荐
SELECT * FROM stu WHERE age IN (19,22,33);

-- null 不能使用=判断 英语缺考
SELECT * FROM stu WHERE english IS NULL;

-- 参加过考试
SELECT * FROM stu WHERE english IS NOT NULL;

-- 模糊查询
SELECT * FROM stu WHERE NAME LIKE '马%';
SELECT * FROM stu WHERE NAME LIKE '马_';

-- 姓名中包含德的字 重要
SELECT * FROM stu WHERE NAME LIKE '%德%';

```

- 排序查询  ORDER BY ASC/DESC

```sql
SELECT * FROM stu ORDER BY math;

-- 降序
SELECT * FROM stu ORDER BY math DESC;

-- 按照数学排名，如果数学成绩一样，则按照英语排名
-- 如果有多个排序条件，如果前一个条件一样的，才会判断第二条件
SELECT * FROM stu ORDER BY math DESC, english ASC;
```

- 聚合查询 做纵向列的聚合计算 （count max min  sum）

  所有的聚合函数都是排除了null值

```sql
-- 一般选择主键
SELECT COUNT(id) FROM stu; -- 8
SELECT COUNT(english) FROM stu; -- 7
SELECT COUNT(IFNULL(english,0)) FROM stu; -- 8

SELECT AVG(math) FROM stu; -- 79.5
```

- 分组查询 当做一个整体，整体共性的东西

```sql
-- 分组字段、聚合字段
-- 查看男女生的平均值
SELECT sex, AVG(math) FROM stu GROUP BY sex;

-- 显示男女生的个数
SELECT sex, AVG(math), COUNT(id) FROM stu GROUP BY sex;

-- 分组之前，分数低于70分的不参与分组
-- 分组之前，对条件进行判断
SELECT sex, AVG(math), COUNT(id) FROM stu WHERE math > 70 GROUP BY sex;

-- 分组之后人数大于2个
SELECT sex, AVG(math), COUNT(id) FROM stu WHERE math > 70 GROUP BY sex HAVING COUNT(id) > 2;

-- 别名
SELECT sex, AVG(math), COUNT(id) 总数 FROM stu WHERE math > 70 GROUP BY sex HAVING 总数 > 2;

-- where 和 having的区别？ 都是对条件的限定
-- where在分组之前进行限定，如果不满足条件，不参与分组 不能跟聚合函数
-- having 在分组之后进行限定，如果不满足条件，则不会查询出来 可以跟聚合函数
```

- 分页查询  limit  开始的索引, 每页查询的条数

```sql
-- 第一页
SELECT * FROM stu LIMIT 0,3;

-- 第二页
SELECT * FROM stu LIMIT 3,3;

-- 分页公式
-- 开始的索引 = (当前的页码-1) * 每页显示的条数
```

## mysql的约束

## mysql的多表之间的关系

## mysql的范式

## mysql的备份和还原

