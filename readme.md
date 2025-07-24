📊 InvestHub
A Python-based desktop application that simplifies stock market analysis and empowers users with data-driven investment insights.

🔍 About the Project
InvestHub is a user-friendly stock market analysis tool designed to assist investors, traders, and financial enthusiasts in understanding stock trends and making informed decisions. It provides real-time data visualization, stock comparisons, financial news, and educational resources — all in one place.

✨ Key Features

🔎 Search Stocks – View interactive line charts of price vs. time using historical stock data

📈 Compare Stocks – Analyze two stocks side-by-side with zoom and reset functionalities

🎓 Learn Tab – Access curated YouTube content for stock market learning

📰 Live News – Get the latest financial news via integrated APIs

🧠 Interactive Games – Engage with quizzes and word jumbles to test financial knowledge

📝 Notes & Notifications – Add notes and receive custom notifications within the app

🛠 Tech Stack

Frontend & GUI: Python, Tkinter

Data Handling: yfinance, matplotlib

APIs: NewsAPI for live market news

Other Tools: Custom quiz and word game logic, YouTube video embeds



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
https://github.com/Anuprita579/Investhub/assets/141035951/4eb26ae1-5a20-44a4-ad65-fd4f0b55a329

## REPORT 
[InvestHub_Report_D10A_Grp11.pdf](https://github.com/Anuprita579/Investhub/files/14920603/InvestHub_Report_D10A_Grp11.pdf)

## PRESENTATION
[InvestHub_D10A_Grp11.pptx](https://github.com/Anuprita579/Investhub/files/14920601/InvestHub_D10A_Grp11.pptx)
