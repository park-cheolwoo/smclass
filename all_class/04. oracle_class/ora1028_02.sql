-- C# 생략
alter session set "_ORACLE_SCRIPT" = true

-- 검색
select * from students

-- 테이블 추가
create table students(
no number(2),
name varchar(20),
kor number(3),
math number(3),
eng number(3),
total number(3),
avg number(10),
rank number(2)
);

-- 데이터 입력
insert into sutdents(no,name,kor,eng,math,total,avg,rank) values(
1,'홍길동',100,100,99,299,(299/3),1);

insert into sutdents(no,name,kor,eng,math,total,avg,rank) values(
2,'유관순',100,90,99,289,(289/3),2
);

rollback;

commit;

-- 테이블 삭제
--drop table students;


create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

insert into member(id,pw,name,phone) values(
'aaa','1111','홍길동','010-1111-1111');

select * from member;

commit;


-- 입력
-- insert into member values('ccc','이순신');
insert into member(id,name) values ('ccc','이순신');

commit;


-- 검색
select * from member;
select id,phone from member;
select name,id from member;
select * from employees;
select emp_name,salary from employees;
select * from member;

-- 수정
update member set name='홍길자' where id='aaa';

-- 삭제
delete member where id = 'ccc';

-- 데이터 확정 : commit, rollback
commit;
rollback;













