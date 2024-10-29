--drop table member;
--drop table data_tab;
--drop table no_tab;
--drop table students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
create table member(
no number(4),
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20),
mdate date
);

-- insert 데이터 입력, update 데이터 수정, delete 데이터 삭제

insert into member values(
1,'aaa','1111','홍길동','111-1111-1111','2024-10-29'
);
insert into member values(
2,'bbb','1111','유관순','010-2222-2222','2024-09-20'
);


-- select 데이터 검색
select * from member;


-- delete 
--delete member where no='2'; 

--update
update member set name='홍길자' where no=1;

--drop table students;
create table students(
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);

insert into students values(
1,'홍길동',100,100,(100+100),sysdate);


commit;

-- 모든 컬럼 검색
select * from students;

-- 특정 컬럼을 입력하면 컬럼만 보여줌.
select name,sdate from students;


-- 특정 컬럼만 입력하면 컬럼 입력
insert into students (stuno,name) values(
2,'유관순');

select * from students; 


select * from employees;

-- 테이블을 생성하면서 테이블 내용을 모두 복사
create table emp2 as select * from employees;

rollback;

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
select * from emp2;
select count(*) from emp2;
select count(*) from employees;

-- 테이블이 존재할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
select * from member;
select * from member2;
insert into member2 select * from member;
select * from member2;

commit;


-- 테이블 구조
desc employees;

-- alter변경 member테이블 no컬럼의 타입길이를 변경
alter table member modify no number(10);
-- alter 컬럼의 이름을 변경
alter table member rename column no to memberNo;


update member set no = '';
-- alter 데이터타입을 변경하기 위해서는 해당 컬럼의 값이 모두 null이어야함
alter table member modify no varchar2(10);
select * from member;
select * from member where id = 'aaa';
select * from member where id = 'AAA';
desc member;

-- employees 테이블에서 사원번호,사원이름,입사일을 출력하시오.

select employee_id, emp_name, hire_date from employees;


--drop table member;
--drop table member2;
--drop table emp2;

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);

drop table students;
select * from member;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (1, '홍길동', 77, 70, 92, 239, 79.6666666667, 0, '2023-12-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (2, '유관순', 89, 69, 55, 213, 71, 0, '2024-01-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (3, '이순신', 75, 89, 53, 217, 72.3333333333, 0, '2024-04-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (4, '강감찬', 85, 91, 81, 257, 85.6666666667, 0, '2023-11-23');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (5, '김구', 62, 71, 54, 187, 62.3333333333, 0, '2024-09-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (6, 'Beek', 57, 68, 73, 198, 66, 0, '2024-01-17');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (7, 'Sleicht', 73, 55, 83, 211, 70.3333333333, 0, '2023-12-14');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (8, 'Hulburd', 96, 85, 81, 262, 87.3333333333, 0, '2023-12-25');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (9, 'Tunnick', 50, 66, 100, 216, 72, 0, '2024-08-20');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (10, 'Horsell', 89, 83, 91, 263, 87.6666666667, 0, '2024-01-27');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (11, 'Hunnicutt', 63, 71, 85, 219, 73, 0, '2024-01-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (12, 'Gillis', 53, 65, 89, 207, 69, 0, '2024-05-10');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (13, 'Shotbolt', 76, 54, 52, 182, 60.6666666667, 0, '2024-04-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (14, 'Neil', 87, 98, 92, 277, 92.3333333333, 0, '2024-09-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (15, 'Gever', 56, 99, 54, 209, 69.6666666667, 0, '2024-05-31');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (16, 'Dobrovsky', 74, 65, 55, 194, 64.6666666667, 0, '2024-07-08');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (17, 'Giles', 93, 66, 63, 222, 74, 0, '2024-06-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (18, 'Mengue', 70, 59, 65, 194, 64.6666666667, 0, '2024-01-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (19, 'Thacker', 60, 95, 66, 221, 73.6666666667, 0, '2024-05-31');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (20, 'Alenshev', 77, 63, 55, 195, 65, 0, '2024-03-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (21, 'Baddow', 61, 69, 53, 183, 61, 0, '2024-09-11');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (22, 'Cordery', 72, 52, 86, 210, 70, 0, '2024-01-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (23, 'Buddell', 51, 90, 94, 235, 78.3333333333, 0, '2024-02-29');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (24, 'Colgrave', 58, 89, 74, 221, 73.6666666667, 0, '2024-06-06');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (25, 'MacCumiskey', 70, 50, 66, 186, 62, 0, '2024-04-10');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (26, 'Earie', 79, 93, 69, 241, 80.3333333333, 0, '2024-04-10');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (27, 'Lendrem', 93, 72, 80, 245, 81.6666666667, 0, '2024-04-30');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (28, 'Fardoe', 100, 76, 61, 237, 79, 0, '2024-03-22');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (29, 'Alkins', 66, 64, 87, 217, 72.3333333333, 0, '2023-12-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (30, 'Worswick', 91, 77, 100, 268, 89.3333333333, 0, '2024-03-31');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (31, 'Keymer', 70, 82, 63, 215, 71.6666666667, 0, '2024-01-22');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (32, 'Jacson', 59, 98, 73, 230, 76.6666666667, 0, '2024-05-11');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (33, 'Eadmeades', 79, 63, 60, 202, 67.3333333333, 0, '2024-09-07');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (34, 'Weeden', 72, 64, 89, 225, 75, 0, '2024-07-15');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (35, 'Starsmore', 92, 60, 50, 202, 67.3333333333, 0, '2024-06-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (36, 'Badsworth', 78, 95, 87, 260, 86.6666666667, 0, '2024-05-07');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (37, 'Marthen', 78, 61, 87, 226, 75.3333333333, 0, '2024-04-11');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (38, 'Hearsum', 93, 68, 77, 238, 79.3333333333, 0, '2024-02-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (39, 'Barrim', 69, 94, 93, 256, 85.3333333333, 0, '2024-07-30');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (40, 'Postlewhite', 60, 100, 83, 243, 81, 0, '2024-06-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (41, 'Ilem', 95, 71, 90, 256, 85.3333333333, 0, '2023-11-15');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (42, 'Birdsey', 85, 76, 65, 226, 75.3333333333, 0, '2024-05-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (43, 'Gabbatiss', 74, 99, 86, 259, 86.3333333333, 0, '2024-04-23');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (44, 'Volet', 100, 86, 85, 271, 90.3333333333, 0, '2024-08-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (45, 'Stockell', 73, 88, 68, 229, 76.3333333333, 0, '2023-12-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (46, 'Brew', 91, 54, 84, 229, 76.3333333333, 0, '2024-03-18');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (47, 'Eversfield', 90, 67, 83, 240, 80, 0, '2024-08-05');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (48, 'Rottgers', 70, 85, 64, 219, 73, 0, '2023-12-27');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (49, 'Twyning', 88, 92, 98, 278, 92.6666666667, 0, '2024-06-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (50, 'Primett', 52, 52, 54, 158, 52.6666666667, 0, '2024-06-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (51, 'Wisedale', 94, 71, 65, 230, 76.6666666667, 0, '2024-05-13');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (52, 'O'' Mahony', 68, 58, 83, 209, 69.6666666667, 0, '2024-08-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (53, 'Curnok', 96, 91, 54, 241, 80.3333333333, 0, '2024-05-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (54, 'Stigger', 86, 91, 59, 236, 78.6666666667, 0, '2024-05-20');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (55, 'Martinie', 82, 88, 84, 254, 84.6666666667, 0, '2024-02-04');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (56, 'Bettaney', 54, 57, 89, 200, 66.6666666667, 0, '2024-07-04');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (57, 'Munnis', 75, 99, 64, 238, 79.3333333333, 0, '2024-01-30');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (58, 'Allbut', 59, 68, 58, 185, 61.6666666667, 0, '2024-03-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (59, 'Hencke', 64, 64, 72, 200, 66.6666666667, 0, '2024-05-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (60, 'Oakenfield', 91, 72, 91, 254, 84.6666666667, 0, '2024-02-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (61, 'Matignon', 59, 86, 56, 201, 67, 0, '2024-02-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (62, 'Gulk', 69, 74, 62, 205, 68.3333333333, 0, '2024-10-26');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (63, 'Ivell', 88, 68, 63, 219, 73, 0, '2024-10-22');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (64, 'Vaud', 86, 100, 93, 279, 93, 0, '2024-01-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (65, 'Aveling', 81, 97, 75, 253, 84.3333333333, 0, '2023-12-03');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (66, 'Vahey', 77, 84, 57, 218, 72.6666666667, 0, '2024-08-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (67, 'Albrooke', 71, 84, 87, 242, 80.6666666667, 0, '2024-04-05');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (68, 'Pawlett', 94, 83, 61, 238, 79.3333333333, 0, '2024-08-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (69, 'Sparrowhawk', 73, 85, 94, 252, 84, 0, '2024-03-03');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (70, 'Bodle', 64, 74, 80, 218, 72.6666666667, 0, '2024-03-20');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (71, 'Josskovitz', 83, 82, 75, 240, 80, 0, '2024-07-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (72, 'Rappa', 99, 88, 87, 274, 91.3333333333, 0, '2024-05-20');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (73, 'Adolfsen', 63, 74, 95, 232, 77.3333333333, 0, '2024-07-24');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (74, 'Colley', 58, 54, 79, 191, 63.6666666667, 0, '2024-04-13');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (75, 'Spark', 85, 84, 98, 267, 89, 0, '2024-05-01');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (76, 'Perrington', 100, 90, 74, 264, 88, 0, '2024-09-07');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (77, 'Steynor', 67, 70, 73, 210, 70, 0, '2024-08-15');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (78, 'Glanester', 65, 99, 63, 227, 75.6666666667, 0, '2024-08-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (79, 'Dalglish', 100, 51, 51, 202, 67.3333333333, 0, '2024-03-29');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (80, 'Bowditch', 61, 94, 79, 234, 78, 0, '2023-11-27');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (81, 'Cosbey', 55, 73, 74, 202, 67.3333333333, 0, '2024-02-06');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (82, 'MacRinn', 76, 93, 50, 219, 73, 0, '2023-12-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (83, 'Strettell', 89, 94, 73, 256, 85.3333333333, 0, '2024-08-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (84, 'Stote', 53, 69, 51, 173, 57.6666666667, 0, '2024-02-04');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (85, 'Hovert', 92, 64, 89, 245, 81.6666666667, 0, '2024-08-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (86, 'Mannering', 73, 72, 80, 225, 75, 0, '2024-10-23');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (87, 'Rowlands', 77, 57, 79, 213, 71, 0, '2023-12-05');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (88, 'Barthelme', 80, 61, 58, 199, 66.3333333333, 0, '2024-05-04');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (89, 'Connue', 89, 96, 85, 270, 90, 0, '2024-08-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (90, 'Argyle', 70, 59, 98, 227, 75.6666666667, 0, '2024-06-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (91, 'Cainey', 72, 55, 99, 226, 75.3333333333, 0, '2024-05-29');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (92, 'Arling', 83, 84, 94, 261, 87, 0, '2024-10-24');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (93, 'Ilchuk', 69, 75, 60, 204, 68, 0, '2024-09-13');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (94, 'Joiris', 88, 74, 79, 241, 80.3333333333, 0, '2024-08-08');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (95, 'Josefsen', 78, 68, 68, 214, 71.3333333333, 0, '2024-05-22');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (96, 'Slorance', 97, 95, 87, 279, 93, 0, '2023-11-05');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (97, 'Timmons', 68, 65, 88, 221, 73.6666666667, 0, '2023-11-12');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (98, 'Arnaldi', 67, 75, 57, 199, 66.3333333333, 0, '2024-04-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (99, 'Rodrigo', 62, 68, 78, 208, 69.3333333333, 0, '2023-12-18');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (100, 'Howes', 59, 52, 86, 197, 65.6666666667, 0, '2024-07-19');

select * from students;
commit;

select kor,eng,kor+eng,abs(kor-eng) from students;
select employee_id||emp_name from employees;

-- 달러환산 : 1384원
select salary from employees;
select salary*1384 from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999') from employees;

select emp_name,salary,salary*1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

insert into stu values(1,'홍길동',100);
insert into stu values(2,'유관순',99);

commit;

insert into stu values(3,'',0);
insert into stu values(4,null,null);

select * from stu;
-- null값 검색 is null
select * from stu where name is null;

select * from employees;
select commission_pct from employees where commission_pct is not null;

select salary from employees;
-- 연봉게산 *12
select salary, salary*12 from employees;
select salary, salary*12, salary*12*1384 from employees;


-- 커미션이 없는 사원은 null값이 있는데, null +,-,*,/ => null값으로 변경
select salary,salary*12,salary*12+(salary*12*commission_pct/100) from employees;

-- nvl() 함수, nvl(kor,0) : kor 컬럼에 null값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;
-- 컬럼명 별칭 사용 : as "" 특수문자+사이공간까지 컬럼명으로 사용 가능
select salary,salary*12,salary*12+(salary*12*nvl(commission_pct,0)/100) as "r e a l salary" from employees;

-- kor 번호,이름,국어,영어,수학,평균,등수,입력일 컬럼명 별칭 사용해서 출력
select * from students;

select no as 번호, name as 이름, kor as 국어, eng as 영어, math as 수학, total as 평균, rank as 등수, sdate as 등록일 from students;

-- 사원번호,이름,이메일을 합쳐서 출력하시오.
select * from employees;
select employee_id||emp_name||email from employees;
select concat(concat(employee_id,emp_name),email) from employees;
select emp_name||' is a '||job_id from employees;


-- 중복제거 : distinct
select department_id from employees;
-- 정렬 : order by - 순차정렬 : (asc) 생략가능 - 역순정렬 : desc
select distinct department_id from employees order by department_id asc;


-- job_id 중복제거 출력
select distinct job_id from employees;

-- 문자열 자르기 : substr(start,length) //cf) substring(start,end) 는 안됨.


-- 4번째 컬럼 데이터를 가져와서 중복을 제거함
select distinct substr(job_id,4) from employees;

-- where절 : 조건비교연산자 >,<,>=,<=,=,!=
select * from employees where manager_id = 124;
select * from employees where job_id = 'SH_CLERK';

select * from employees where employee_id >100;

-- students 합계 250 이상 출력하시오.
select * from students;
select * from students where total >=250;

-- 합계 250 이상, 국어 90점 이상
select * from students where total >= 250 and kor >=90;

-- 영어점수 70이상 90이하 출력
select * from students where eng >=70 and eng <=90;

-- 월급이 5000 이상 8000 이하 검색
select * from employees where salary >= 5000 and salary<= 8000;

-- 월급이 7000이 아닌 것을 출력
select * from employees where salary !=7000;

-- 부서 = 50, 50번이 아닌 것을 출력(개수)
select count(*) from employees where department_id = 50; -- 45
select count(*) from employees where department_id != 50; -- 61 106
select count(*) from employees where department_id is null; -- 1 107

-- null값은 count()에 포함되지 않음  
select count(*) from employees; -- 107
select count(employee_id) from employees; -- 107
select count(department_id) from employees; -- 106, null값이 1개 있기에 106개가 나옴

-- 급여 4000 이하 사원번호, 사원명, 급여 컬럼만 출력하시오.

select employee_id as 사원번호 ,emp_name as 사원명 ,salary as 급여 from employees where salary <=4000;

-- 숫자,날짜인 경우 비교연산자 가능
select emp_name,hire_date from employees;
select emp_name,hire_date from employees where hire_date >= '2002/01/01';

-- 1999-12-31 이전에 입사한 사람을 출력
select * from employees where hire_date <= '1999-12-31';

-- 2001-01-01 부터 2004-12-31 까지 출력
select * from employees where hire_date >= '2001-01-01' and hire_date <='2004-12-31';

-- 국어점수가 90점 이상 또는 영어점수가 90점 이상 출력
select count(*) from students where kor >= 90 or eng >=90;
select count(*) from students where kor >= 90 and eng >= 90;

-- 부서번호가 10번이면서 job이 man인 경우
select * from employees;
select * from employees where department_id = 80 and substr(job_id,4) = 'MAN';

-- 0.2,0.3,0.5만 출력
select commission_pct from employees where commission_pct is not null;
select commission_pct from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;

select commission_pct from employees where commission_pct in (0.2,0.3,0.5);

-- 사원번호 110,120,130번 출력
select * from employees where employee_id in (110,120,130);
select * from employees where employee_id =110 or employee_id = 120 or employee_id = 130;


-- between - and : <= 포함이 되어 있는 경우만 해당
select * from employees where employee_id > 150 and employee_id < 170;
select * from employees where employee_id between 150 and 170;

select hire_date from employees;
-- 날짜 in
select hire_date from employees where hire_date in ('2004/02/17','2002/06/07');
-- 날짜 between
select hire_date from employees where hire_date between '2002/06/17' and '2004/12/31'; 

-- job MAN 출력
select * from employees where substr(job_id,4) in('MAN');

-- like 연산자 : 포함되어 있는 글자 검색
select * from employees where job_id like '%MAN'; -- MAN으로 끝나는 단어를 검색
select * from employees where job_id like 'ST%'; -- ST로 시작되는 단어를 검색

-- 이름에 a가 들어가 있는 이름을 출력
select * from employees where emp_name like '%a%';

-- 2번째 자리에 t 가 들어가 있는 이름 출력
select * from employees where emp_name like '_a%';

-- 4번째 v가 들어가 있는 이름 출력
select * from employees where emp_name like '___v%';

-- 뒤에서 2번째 l
select * from employees where emp_name like '%l__';

-- 첫번째 P
select * from employees where emp_name like 'P%';
