use e_waste;
select * from login_credentials;
select * from images;
select * from posts;

SELECT p.components, p.descript, l.loca ,l.mobile
FROM posts p 
INNER JOIN login_credentials l ON p.username = l.username 
WHERE p.post_id = 9;

desc login_credentials;