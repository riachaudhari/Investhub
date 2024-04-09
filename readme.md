# Stock Market Analysis
## TABLES
```sql
mysql> SHOW TABLES;
+-------------------+
| Tables_in_unifind |
+-------------------+
| userinfo          |
+-------------------+
```
## TABLE USERINFO
```sql
-- This is a MySQL code for creating Table userinfo
CREATE TABLE userinfo(
    userid integer primary key not null auto_increment,
    useremail varchar(100) not null,
    usercontact bigint not null,
    userage integer not null,
    username varchar(100) not null,
    userpassword varchar(100) not null
);

-- OUTPUT:
mysql> SHOW COLUMNS FROM userinfo;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| userid       | int          | NO   | PRI | NULL    | auto_increment |
| useremail    | varchar(100) | NO   |     | NULL    |                |
| usercontact  | bigint       | NO   |     | NULL    |                |
| userage      | int          | NO   |     | NULL    |                |
| username     | varchar(100) | NO   |     | NULL    |                |
| userpassword | varchar(100) | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
```

## DEMO
https://github.com/Anuprita579/Investhub/assets/141035951/1fdf2447-b757-4f88-a98c-6b7821e345c7

## REPORT 
[InvestHub_Report_D10A_Grp11.pdf](https://github.com/Anuprita579/Investhub/files/14920603/InvestHub_Report_D10A_Grp11.pdf)

## PRESENTATION
[InvestHub_D10A_Grp11.pptx](https://github.com/Anuprita579/Investhub/files/14920601/InvestHub_D10A_Grp11.pptx)
