-- join
-- inner join - equi,non-equi / self join / outer join

-- employees 사원번호, 사원명, 부서번호, 부서명 - departments 출력
select employee_id,emp_name,a.department_id,department_name from employees a,departments b 
where a.department_id = b.department_id;

select * from stu_grade;

-- 두 테이블간 동일한 컬럼 없이 데이터를 가져오는 방법 - non-equi join
-- avg값을 가지고 다른 컬럼을 다른 테이블에서 가져와 출력
select * from students,stu_grade 
where avg between loscore and hiscore;

-- self-join : 자신의 테이블을 2번 호출

select a.employee_id,a.emp_name,a.manager_id,b.emp_name from employees a,employees b
where a.manager_id = b.employee_id;

select * from students;
select * from stu;

-- 컬럼 삭제
alter table stu drop column result;

-- 컬럼 추가
alter table stu add result varchar2(10);

-- avg 의 컬럼을 가지고, stu_grade 활용해서 이 값을 result 컬럼에 모두 입력하시오.
update stu a set result = (select result from
(select no,avg,result from stu,stu_grade
where avg between loscore and hiscore) b
where a.no = b.no -- avg를 사용하면 평균이 같은 곳이 2개 이상일 수 있음, 따라서 1대1 대응이 되는 no를 사용해야함
);

-- non-equi join update구문
update stu a set result = (
select grade from(
select no,grade as grades from stu,stu_grade
where avg between loscore and hiscore) b
where a.no = b.no);

select no,grade as grades from stu,stu_grade
where avg between loscore and hiscore;

commit;

-- rank()
select * from stu;
update stu set rank = 0;

select no,name,avg,rank() over(order by avg desc) as ranks from stu;

-- rank() 결과값을 rank컬럼에 모두 입력
update stu a set rank = (
select ranks from(
select no,name,avg,rank() over(order by avg desc) as ranks from stu) b
where a.no = b.no);

-- null값 제외 106개 포함 107개
select employee_id,emp_name,manager_id from employees;
-- manager_id가 null 이면 0 출력
select employee_id,emp_name,nvl(to_char(manager_id),'CEO') from employees;

-- self-join manager_id, 매니저의 이름을 출력
-- outer-join : 해당 컬럼에 null값이 존재할 시 null값을 포함해서 출력
select a.employee_id,a.emp_name,a.manager_id,b.emp_name,a.salary
from employees a, employees b
where a.manager_id = b.employee_id(+);

-- 사원번호, 사원명, 부서번호, 부서명 출력
select employee_id, emp_name, a.department_id, department_name from employees a,departments b
where a.department_id(+) = b.department_id;

-- ansi cross join
select * from employees cross join departments;
-- cross join
select * from employees,departments;

-- ansi inner join
select a.department_id, department_name
from employees a inner join departments b
on a.department_id = b.department_id;
-- equi join
select a.department_id,department_name from employees a,departments b
where a.department_id = b.department_id;

-- ansi join(using)
select department_id, department_name
from employees inner join departments
using (department_id);


-- ansi join : natural join
select department_id,department_name 
from employees a natural join departments b;

--select * from employees a natural join departments b

--outer join(left,right,full)
select employee_id,emp_name,a.department_id, department_name
from employees a left outer join departments b
on a.department_id = b.department_id;

-- 오라클 outer-join : 두개의 컬럼의 (+)는 에러
select employee_id,emp_name,a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id(+);


--union --49 // 24+35 = 59 - 10(중복제외)
select * from students where total >= 250 -- 24
union
select * from students where name like '%a%'; --35

select * from students where total >=250 or name like '%a%';

-- union : 같은 테이블, 다른 테이블 모두 사용가능, 컬럼의 타입만 맞으면 모두 출력
-- 조건1 : 위쪽 쿼리문과 아래쪽 쿼리문 개수 동일
-- 조건2 : 타입이 일치
select employee_id, emp_name from  employees
union
select no,name from students;

-- 자유게시판,공지사항,이벤트,종합게시판
-- 통합적으로 검색해서 출력하고 싶을 때

select employee_id,emp_name,no,name from employees,students;


-- employees 에서 department_id가 50인 사원 검색 -> 부서번호, 부서이름
-- employees에 salary가 5000보다 크고 8000보다 작은 사원 검색 -> 부서번호, 부서이름
-- 두개를 union
select a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id and a.department_id = 50
union
select department_id,department_name from departments a where not exists(
select 1 from employees b where a.department_id = b.department_id);


select department_id,department_name from departments a where not exists(
select 1 from employees b where a.department_id = b.department_id);


-- name,mdate / name,sdate union
select name,mdate from member
union
select name,sdate from students;

select * from board;

drop table board2;

create table board2 (
	bno number(4),
	btitle VARCHAR2(1000),
	bcontent clob,
	id VARCHAR2(30),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bdate DATE,
	bfile VARCHAR2(100)
);
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (1, 'Maury County Airport', 'Software Engineer IV', 'aaa', 1, 0, 0, 0, '2024-07-31', 'Garth');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (2, 'Ras Al Khaimah International Airport', 'Electrical Engineer', 'bbb', 2, 0, 0, 0, '2024-11-03', 'Carnoghan');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (3, 'Miller Field', 'Senior Sales Associate', 'ccc', 3, 0, 0, 0, '2023-12-10', 'Soughton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (4, 'Garowe Airport', 'Physical Therapy Assistant', 'ddd', 4, 0, 0, 0, '2024-01-14', 'Naisey');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (5, 'Kiryat Shmona Airport', 'Junior Executive', 'eee', 5, 0, 0, 0, '2024-01-13', 'Bassano');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (6, 'Playa Baracoa Airport', 'Software Consultant', 'abc', 6, 0, 0, 0, '2024-09-22', 'Houston');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (7, 'Southampton Airport', 'Media Manager IV', 'Goddard', 7, 0, 0, 0, '2024-05-21', 'Stroton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (8, 'Nushki Airport', 'Account Representative I', 'Jehu', 8, 0, 0, 0, '2024-07-27', 'Ginsie');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (9, 'Kashan Airport', 'Safety Technician IV', 'Reggie', 9, 0, 0, 0, '2024-01-02', 'Gillingham');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (10, 'Land''s End Airport', 'Teacher', 'Grace', 10, 0, 0, 0, '2024-07-02', 'Dinnington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (11, 'Marau Airport', 'Senior Sales Associate', 'Carrissa', 11, 0, 0, 0, '2024-09-26', 'Vannucci');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (12, 'Paros National Airport', 'Computer Systems Analyst IV', 'Charline', 12, 0, 0, 0, '2024-08-30', 'Pearn');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (13, 'Kazan International Airport', 'Web Designer IV', 'Petra', 13, 0, 0, 0, '2024-05-25', 'Tench');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (14, 'Abadan Airport', 'Social Worker', 'Guenevere', 14, 0, 0, 0, '2023-12-25', 'Whatford');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (15, 'Alerta Airport', 'Human Resources Manager', 'Rainer', 15, 0, 0, 0, '2023-12-13', 'Kagan');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (16, 'Ambatolhy Airport', 'Statistician II', 'Clemence', 16, 0, 0, 0, '2024-07-25', 'Abelovitz');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (17, 'Antrim County Airport', 'Graphic Designer', 'Atlanta', 17, 0, 0, 0, '2024-01-24', 'Puvia');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (18, 'Dayton-Wright Brothers Airport', 'Financial Analyst', 'Meriel', 18, 0, 0, 0, '2024-06-24', 'Towl');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (19, 'Caransebeş Airport', 'Media Manager III', 'Eada', 19, 0, 0, 0, '2023-11-12', 'Foresight');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (20, 'Kédougou Airport', 'Mechanical Systems Engineer', 'Franky', 20, 0, 0, 0, '2024-06-26', 'Connell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (21, 'Hosea Kutako International Airport', 'Operator', 'Aleta', 21, 0, 0, 0, '2024-06-04', 'O''Shields');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (22, 'Norsup Airport', 'Accountant I', 'Lucky', 22, 0, 0, 0, '2024-04-08', 'Peatman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (23, 'Kota Kinabalu International Airport', 'Business Systems Development Analyst', 'Wolf', 23, 0, 0, 0, '2024-11-03', 'Whymark');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (24, 'Yeva Airport', 'Systems Administrator I', 'Germain', 24, 0, 0, 0, '2024-06-13', 'Burril');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (25, 'Ampara Airport', 'Software Consultant', 'Costanza', 25, 0, 0, 0, '2024-01-11', 'De Giorgis');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (26, 'Madeira Airport', 'Executive Secretary', 'Jeane', 26, 0, 0, 0, '2024-05-01', 'Northedge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (27, 'Manang Airport', 'Electrical Engineer', 'Ramona', 27, 0, 0, 0, '2024-10-30', 'Camellini');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (28, 'Dirranbandi Airport', 'Teacher', 'Evelyn', 28, 0, 0, 0, '2024-10-22', 'Smitherham');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (29, 'Chevak Airport', 'Senior Editor', 'Alfi', 29, 0, 0, 0, '2024-08-05', 'Skiggs');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (30, 'Along Airport', 'Legal Assistant', 'Sinclare', 30, 0, 0, 0, '2024-08-31', 'Jay');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (31, 'Tongliao Airport', 'Graphic Designer', 'Randi', 31, 0, 0, 0, '2024-06-01', 'Nias');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (32, 'Videira Airport', 'Social Worker', 'Alfi', 32, 0, 0, 0, '2024-06-27', 'Rodge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (33, 'Lawrenceville Vincennes International Airport', 'Product Engineer', 'Ortensia', 33, 0, 0, 0, '2024-10-19', 'Cornew');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (34, 'St Marys Municipal Airport', 'Health Coach III', 'Edik', 34, 0, 0, 0, '2024-07-31', 'Greenway');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (35, 'Pimaga Airport', 'Nuclear Power Engineer', 'Melantha', 35, 0, 0, 0, '2024-06-07', 'Eixenberger');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (36, 'Sand Point Airport', 'Automation Specialist II', 'Mario', 36, 0, 0, 0, '2024-10-07', 'Szanto');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (37, 'Syangboche Airport', 'Tax Accountant', 'Goran', 37, 0, 0, 0, '2024-06-27', 'Height');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (38, 'Healy Lake Airport', 'Librarian', 'Mela', 38, 0, 0, 0, '2024-06-02', 'Collough');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (39, 'Midgard Airport', 'Database Administrator III', 'Bambie', 39, 0, 0, 0, '2024-05-09', 'Verduin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (40, 'Heglig Airport', 'Programmer IV', 'Bernelle', 40, 0, 0, 0, '2024-07-04', 'Sidry');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (41, 'Mossel Bay Airport', 'Health Coach IV', 'Perice', 41, 0, 0, 0, '2024-06-29', 'Moye');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (42, 'Siwo Airport', 'VP Marketing', 'Dallis', 42, 0, 0, 0, '2024-02-04', 'McGiff');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (43, 'Danilo Atienza Air Base', 'Speech Pathologist', 'Thaine', 43, 0, 0, 0, '2024-01-19', 'Tribbeck');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (44, 'Shelby Airport', 'Assistant Media Planner', 'Francyne', 44, 0, 0, 0, '2023-12-13', 'Crookshanks');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (45, 'Gage Airport', 'GIS Technical Architect', 'Hyacintha', 45, 0, 0, 0, '2023-12-23', 'Hearnes');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (46, 'Gelephu Airport', 'Internal Auditor', 'Hanny', 46, 0, 0, 0, '2024-09-12', 'McJerrow');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (47, 'Sugraly Airport', 'Chemical Engineer', 'Quentin', 47, 0, 0, 0, '2023-11-11', 'Brydell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (48, 'Myrtle Beach International Airport', 'Senior Developer', 'Karrah', 48, 0, 0, 0, '2024-03-16', 'McKue');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (49, 'Rustaq Airport', 'Accounting Assistant IV', 'Stepha', 49, 0, 0, 0, '2024-10-10', 'Charity');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (50, 'Southwest Oregon Regional Airport', 'Design Engineer', 'Marcille', 50, 0, 0, 0, '2024-08-16', 'Philbin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (51, 'New Stuyahok Airport', 'Data Coordinator', 'Armand', 51, 0, 0, 0, '2024-04-10', 'Bianco');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (52, 'Rabil Airport', 'Clinical Specialist', 'Abelard', 52, 0, 0, 0, '2024-03-23', 'D''eathe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (53, 'Walvis Bay Airport', 'Food Chemist', 'Janine', 53, 0, 0, 0, '2024-01-23', 'Klousner');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (54, 'Willow Airport', 'Executive Secretary', 'Tamar', 54, 0, 0, 0, '2024-02-10', 'Nanuccioi');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (55, 'Maquinchao Airport', 'Staff Scientist', 'Jobina', 55, 0, 0, 0, '2024-03-27', 'Danshin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (56, 'Smithton Airport', 'Structural Analysis Engineer', 'Pablo', 56, 0, 0, 0, '2024-03-20', 'Dulwitch');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (57, 'Los Menucos Airport', 'Health Coach IV', 'Ashlin', 57, 0, 0, 0, '2023-12-06', 'Serot');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (58, 'Jersey Airport', 'Occupational Therapist', 'Sarene', 58, 0, 0, 0, '2024-02-27', 'Fullard');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (59, 'Mikkeli Airport', 'Research Associate', 'Juana', 59, 0, 0, 0, '2024-08-11', 'Wolver');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (60, 'Granville Airport', 'Computer Systems Analyst II', 'Perl', 60, 0, 0, 0, '2024-05-14', 'Barkess');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (61, 'Mont Joli Airport', 'Sales Associate', 'Bradley', 61, 0, 0, 0, '2024-01-08', 'Crosi');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (62, 'Moabi Airport', 'Marketing Manager', 'Kiah', 62, 0, 0, 0, '2024-01-04', 'Wardel');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (63, 'Provo Municipal Airport', 'Paralegal', 'Mallory', 63, 0, 0, 0, '2024-03-26', 'Nashe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (64, 'Belgorod International Airport', 'Programmer III', 'Lory', 64, 0, 0, 0, '2024-04-24', 'Bowdrey');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (65, 'Northern Peninsula Airport', 'Professor', 'Augustin', 65, 0, 0, 0, '2023-12-01', 'Mantrip');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (66, 'Makemo Airport', 'Chief Design Engineer', 'Karia', 66, 0, 0, 0, '2024-07-06', 'Leppingwell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (67, 'Croker Island Airport', 'Software Test Engineer III', 'Baily', 67, 0, 0, 0, '2024-07-07', 'Vader');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (68, 'Vestmannaeyjar Airport', 'Electrical Engineer', 'Whit', 68, 0, 0, 0, '2024-03-28', 'Gill');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (69, 'Buri Ram Airport', 'Executive Secretary', 'Renato', 69, 0, 0, 0, '2023-11-07', 'Krug');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (70, 'Brochet Airport', 'Research Nurse', 'Dyanna', 70, 0, 0, 0, '2024-04-29', 'Milbourn');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (71, 'Mbarara Airport', 'Structural Analysis Engineer', 'Sydney', 71, 0, 0, 0, '2024-05-07', 'Rendell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (72, 'Manchester-Boston Regional Airport', 'Teacher', 'Jose', 72, 0, 0, 0, '2024-10-29', 'Northover');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (73, 'Kushiro Airport', 'Financial Advisor', 'Lyle', 73, 0, 0, 0, '2024-07-16', 'Lockyer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (74, 'Ulusaba Airport', 'Chemical Engineer', 'Marti', 74, 0, 0, 0, '2023-12-06', 'Readman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (75, 'Corvallis Municipal Airport', 'Software Engineer II', 'Terrill', 75, 0, 0, 0, '2024-07-21', 'Ianno');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (76, 'Anshan Air Base', 'Physical Therapy Assistant', 'Coleen', 76, 0, 0, 0, '2024-09-09', 'Philpot');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (77, 'Longdongbao Airport', 'Software Engineer I', 'Filberto', 77, 0, 0, 0, '2024-07-01', 'Simunek');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (78, 'Apple Valley Airport', 'Editor', 'Joycelin', 78, 0, 0, 0, '2023-11-22', 'Clampin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (79, 'Arthur N Neu Airport', 'Financial Advisor', 'El', 79, 0, 0, 0, '2024-06-18', 'Foggo');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (80, 'Inukjuak Airport', 'Nurse Practicioner', 'Dylan', 80, 0, 0, 0, '2024-09-07', 'Buzza');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (81, 'Rochester International Airport', 'Registered Nurse', 'Lindsay', 81, 0, 0, 0, '2023-11-10', 'O''Kenny');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (82, 'Prado Airport', 'Electrical Engineer', 'Fiorenze', 82, 0, 0, 0, '2024-04-18', 'Benterman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (83, 'Craig Seaplane Base', 'Health Coach I', 'Michaella', 83, 0, 0, 0, '2023-12-06', 'Gibbons');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (84, 'Fayetteville Municipal Airport', 'Software Engineer III', 'Alfredo', 84, 0, 0, 0, '2024-05-11', 'Karczinski');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (85, 'Whiting Field Naval Air Station - North', 'Research Associate', 'Randie', 85, 0, 0, 0, '2024-10-13', 'Holdworth');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (86, 'Harry P Williams Memorial Airport', 'Human Resources Assistant III', 'Shane', 86, 0, 0, 0, '2024-07-07', 'Longbone');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (87, 'Geilenkirchen Air Base', 'Programmer Analyst I', 'Margarita', 87, 0, 0, 0, '2024-01-26', 'Bryce');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (88, 'Cornélio Procópio Airport', 'Programmer IV', 'Arlene', 88, 0, 0, 0, '2024-03-11', 'Ranns');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (89, 'Witu Airport', 'Paralegal', 'Shawn', 89, 0, 0, 0, '2024-10-30', 'Hamblington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (90, 'Milyakburra Airport', 'Social Worker', 'Marion', 90, 0, 0, 0, '2024-02-22', 'Gillies');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (91, 'Monkey Bay Airport', 'Executive Secretary', 'Nedi', 91, 0, 0, 0, '2024-02-07', 'Tatterton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (92, 'Aeroclube de Bento Gonçalves Airport', 'Human Resources Manager', 'Lucila', 92, 0, 0, 0, '2024-10-20', 'Fust');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (93, 'Gregory Downs Airport', 'Marketing Assistant', 'Toddie', 93, 0, 0, 0, '2024-01-07', 'Dancer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (94, 'Bunyu Airport', 'Pharmacist', 'Francisco', 94, 0, 0, 0, '2024-02-08', 'Bordis');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (95, 'Lake Macquarie Airport', 'Financial Advisor', 'Georgi', 95, 0, 0, 0, '2024-09-02', 'Sparhawk');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (96, 'Nain Airport', 'Senior Quality Engineer', 'Carolan', 96, 0, 0, 0, '2024-02-20', 'O''Cuddie');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (97, 'Touggourt Sidi Madhi Airport', 'Civil Engineer', 'Roma', 97, 0, 0, 0, '2024-07-18', 'Berrington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (98, 'Lae Island Airport', 'Quality Control Specialist', 'Edin', 98, 0, 0, 0, '2024-06-21', 'Walewski');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (99, 'Chipinge Airport', 'Nurse', 'Hubie', 99, 0, 0, 0, '2023-11-08', 'Bristoe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (100, 'Tapini Airport', 'Product Engineer', 'Katine', 100, 0, 0, 0, '2024-01-13', 'Scrine');

commit;

select * from board2;

-- delete board2 where bno in (8, 11,12,16, 21,22,25,29,35,38,44,46,57,61,66,74,88,95,96,98);

select * from board2 where bno between 1 and 20;

-- rownum : 번호를 새롭게 부여
select rownum,bno,btitle,bdate from board2 order by bdate desc,btitle asc;


--rownum 번호가 순서대로 정렬됨, 서브쿼리 사용
-- 서브쿼리 : 정렬 >> 번호부여 >> 번호부여 중에서 검색
select rnum,bno,btitle from
(select rownum rnum,bno,btitle,bdate from (
select bno,btitle,bdate from board2 order by bdate desc,btitle asc))
where rnum between 11 and 20;

-- row_number() over() : 정렬한 후 번호를 부여
select rnum,bno,btitle,bdate from(
select row_number() over(order by bdate desc) rnum,bno,btitle,bdate from board2)
where rnum between 11 and 20;

select row_number() over(order by bdate desc) rnum,a.* from board2 a;
select bno,a.* from board2 a;

select * from (select row_number() over(order by bdate desc) rnum,a.* from board2 a);


-- 모든 컬럼을 출력하시오
-- 11~20번
-- 11~20으로 출력하기 위해서는 rownumber를 rnum으로 별칭 지정해줘야함(rnum을 생성 후 조건 대입)


select * from (select row_number() over(order by bdate desc) rnum,a.* from board2 a)
where rnum between 11 and 20;

select * from(
select rownum rnum,a.* from(
select * from board2 order by bdate desc) a)
where rnum between 11 and 20;

select * from(
select rownum rnum,a.* from(
select * from board2 order by bdate desc
) a
)
where rnum between 1 and 10
;

select rownum rnum,a.* from board2 a
order by bdate desc;



-- row num 11~20
select * from(
select rownum rnum,a.* from(
select rownum,no,name,avg,rank() over(order by avg desc) from students 
) a)
where rnum between 11 and 20;


-- rank() 값을 rank 컬럼에 입력
update students set rank = (select rank from(
select no,rank() over(order by avg desc) rank from students) a 
where a.no = students.no);

select * from students;

commit;

-- view
-- 상담원 : 전화번호를 보고 지역별 전화를 마케팅을 하려고 함.
-- 100명에게 사원 테이블 오픈 제공해달라고 요청 : 마케팅
-- 직원가 100만원 90% 10만원 아이폰16


-- view 생성 create
create or replace view employees_view
as
select employee_id,emp_name,email,phone_number,hire_date from employees;


-- 사원번호, 사원명, 이메일, 폰번호, 입사일, 부서번호, 부서명 출력
create or replace view employee_view2
as
select employee_id,emp_name,email,phone_number,a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id;

select * from emp_view;

-- view 삭제 drop
drop view emp_view;

-- view 컬럼 커멘트(주석-설명문) 추가
comment on column employees_view.employee_id is '사원번호에 해당 됩니다.';
select * from employees_view;
-- 컬럼 커멘트 주석 확인
select * from user_col_comments;
-- 테이블 커멘트 주석 확인
select * from user_table_comments;

create or replace view emp_view
as
select employee_id as e_id, emp_name as e_name from employees;

select * from emp02;

desc emp02;

drop table emp02;

create table emp02(
employee_id number(6),
emp_name varchar2(80),
hire_date date,
salary number(8,2),
department_id number(6)
);


insert into emp02(employee_id,emp_name,hire_date,salary,department_id)
select employee_id,emp_name,hire_date,salary,department_id from employees;

select * from emp02;
commit;

-- view 생성
-- with read only : select만 가능, insert,update,delete 불가
create or replace view emp02_view
as
select employee_id, emp_name,hire_date from emp02
with read only;

--view select
select * from emp02_view order by employee_id;


-- 단순 view : 1개 테이블루 구성된 것
-- insert,update,delete 가능, not null 제약조건이 되어 있으면 insert 불가할 수도 있음
-- 복합 view : 2개 이상의 테이블 조인, 함수 사용, group by절 같은 경우는 insert,update,delete 불가
-- 100번 이름을 '홍길동'으로 변경
update emp02_view set emp_name = '유관순' where employee_id=101;

insert into emp02_view values(
207,'유관순',sysdate);

select * from emp02_view order by employee_id desc;

select * from emp02;

alter table emp02 modify salary number(8,2) not null;

delete emp02 where emp_name = '유관순';

drop view emp02_view;



select * from students;
-- no : seq
-- total : 오라클에서 입력
-- avg : 오라클에서 입력
-- rank : 오라클에서 입력
-- sdate : sysdate 오라클에서 입력
-- 입력 데이터 : name,kor,eng,math

select students_seq.currval from dual;

-- students 테이블 no가 가장 큰 수
select max(no) from students;

select * from students;

-- avg 소숫점 2자리까지만 출력
-- no,name,kor,eng,math,total,avg,rank,sdate

select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students;

select * from students where name like '%a%';

select * from students order by name;
select * from students;


update students a set rank = (
select ranks from(
select rank() over(order by total) ranks,no from students) b
where a.no = b.no);

commit;