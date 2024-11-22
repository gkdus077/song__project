create table users(
 userid integer primary key autoincrement, 
 username text not null, 
 password text not null,
 gender text check(gender in ('male', 'female'))
);



