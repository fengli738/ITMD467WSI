/*
user
1.id
2.username
3.password
4.time
*/
create table if not exists user(
id int unsigned not null auto_incremnet key,
username varchar(20) not null,
password varchar(50) not null,
addtime datetime not null
);
/*
article
1.id
2.title
3.category
4.author
5.picture
6.content
7.time
*/
create table if not exists article(
id int unsigned not null auto_incremnet key,
title varchar(50) not null,
category tinyint unsigned not null,
user_id int unsigned not null,
logo varchar(50) not null,
content mediumtext not null,
addtime datetime not null,
);