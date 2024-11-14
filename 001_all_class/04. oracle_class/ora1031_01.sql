select * from member;

update member set id = 'abc',pw = '1111',name='홍길동',email='aaaa' where id='Trineman'; 

commit;

select * from member;

update member set pw='2222' where id='Towell';

select sysdate-1,sysdate,sysdate+1 from dual;

select hire_date,round(hire_date,'month') from employees;

select hire_date,trunc(hire_date,'month') from employees;

select add_months(trunc(sysdate,'month'),1) from dual;

-- vip요금제로 변경을 하면 다음달부터 1일부터 혜택
select sysdate from dual;
select add_months(trunc(sysdate,'month'),1) from dual;

-- 입사일 기준 다음달 1일부터 혜택
select add_months(trunc(hire_date,'month'),1) from employees;

-- 입사일 기준 1년 후 날짜 출력
select hire_date+365,add_months(hire_date,12) from employees;


-- 입사일 기준 1년 후 날짜, 1년 후 그 달의 마지막 날짜를 출력하시오.
select add_months(hire_date,12),last_day(add_months(hire_date,12)) from employees;

select hire_date,last_day(hire_date) from employees;


-- 입력일 기준 1년 후 마지막 날짜가 10/31일인 학생들을 모두 출력
select name,last_day(add_months(sdate,12)) from students where last_day(add_months(sdate,12)) in ('25/08/31', '25/09/30', '25/10/31','24/08/31','24/11/30','24/12/31') order by sdate;

select sdate from students;


--extract 함수 : 년,월,일,시,분,초 만 분리해서 가져오는 함수
select sysdate from dual;
select extract(year from sysdate) from dual;
select extract(month from sysdate)from dual;
select extract(day from sysdate) from dual;

select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

select sdate,extract(month from sdate),extract(year from sdate) 
from students 
where extract(month from last_day(sdate+365)) in (9,11,12);

-- substr 함수 : 문자에서 시작위치, 가져올 개수
-- 오라클에서는 위치점이 0이 아닌 1부터 시작
select substr(sysdate,0,2) from dual;

select sdate,last_day(sdate+365) sdate2 from students where substr(sdate,4,2) in (8,11,12)
order by sdate2;



-- 날짜 -> 문자 to_char
-- 문자 -> 날짜 to_date
-- 숫자 -> 문자 to_char
-- 문자 -> 숫자 to_number

-- 날짜 형변환해서 날짜 포맷을 변경
-- date타입 -> char 타입으로 변경해서 포맷.
select sysdate from dual;
select to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate,to_char(sysdate,'YYYY-Mon-dd hh24:mm:ss Dy') from dual;
select sysdate,to_char(sysdate,'YYYY-Mon-dd am hh:mm:ss Dy') from dual;


select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss') from employees;


-- sdate 2024/01/01
select sdate,to_char(sdate,'yyyy/mm/dd') from students;

select kor from students
where kor>=70;

-- 숫자타입 -> 문자타입으로 변경해서 포맷, 천단위(,) 표시
-- 9 : 0을 채우지 않음, 0 : 0을 채움
-- L : 국가 통화기호 표시, $ : 달러 표시
select to_char(salary*1382.86*12,'L000,999,999') from employees;

select to_char(12,'000') from dual;

select 1 from dual;

select 12 from dual;

select to_char(123456, '0000000000'),to_char(123456,'999,999,999') from dual;

create table chartable(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);
-- number,number,str - number 타입을 넣어도 됨,str
-- 문자형 타입에는 숫자형 타입 가능
insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000'));
insert into chartable values(
1,10000,10000,10000);

create table chartable2(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);
-- 숫자형 타입은 숫자 앞에 0이 있어도 표시가 되지 않음 : str 타입만 가능
-- 천단위 표시(,)는 숫자형 타입에 입력이 안됨 : 문자형 타입만 가능
insert into chartable2 values(
4,4000000,4000000,04000000
);

rollback;
commit;

select * from chartable2;

-- 숫자형 타입과 문자형(숫자) 타입은 사칙연산 가능 = 두 타입 결과값 출력
select kor+kor_char from chartable;
-- 숫자형 타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능
select kor+kor_char+kor_mark from chartable;



desc chartable; -- number, varchar2
desc chartable2; -- 모든 타입 number

alter table chartable2 modify kor_char number(10);

-- 2일 이후의 날짜를 출력하시오
select '20241031' from dual;
select sysdate,sysdate+2 from dual;
select '20241031'+2 from dual;
select to_date('20241031')+2 from dual;
select to_date('20241031') from dual;
select to_date('2024-10-31'),to_date('24/1/1') from dual;

select to_char(to_date('20231031'),'yyyy-mm-dd') from dual;

-- number형 타입 -> 날짜형 타입
-- 문자형 타입 -> 날짜형 타입
select sysdate-to_date('20241031') from dual;

-- 천단위 문자형 타입 -> 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

select * from chartable;

select kor,to_number(to_char(kor_mark,'999,999,999')) from chartable;


insert into chartable values(3,30000,'0030000','3,000,000');

select kor+to_number(kor_mark,'999,999,999') from chartable;

-- 날짜 -> 문자 to_char ## 날짜포맷
-- 문자 -> 날짜 to_date ## 날짜사칙연산
-- 숫자 -> 문자 to_char ## 천단위, 0과9
-- 문자 -> 숫자 to_number ## 천단위 표시 삭제 후 계산


select department_id from employees;

select department_id from employees where department_id is null;

select commission_pct from employees where commission_pct is not null;

-- 월급 * 커미션을 계산하시오

select salary*(1+nvl(commission_pct,0)) from employees;

-- null인 경우 : 0
-- null인 경우 : CEO 표시
select nvl(department_id,0) from employees;
select nvl(to_char(department_id),'ceo') from employees;

-- 그룹함수
-- sum(합계), avg(평균), count(개수), min(최소), max(최대), median(중간값)
select to_char(sum(salary)) from employees;

select avg(salary) from employees;
-- 소숫점 둘째자리 반올림
select round(avg(salary),2) from employees;
-- 버림
select trunc(avg(salary),2) from employees;

select max(salary) from employees;
select min(salary) from employees;

-- 평균보다 월급이 높은 사원 출력
-- 조건절에 그룹함수를 넣을 때 주의
select count(salary) from employees where salary >= (select avg(salary) from employees);

-- emp_name : 단일함수, avg : 그룹함수
select emp_name,avg(salary) from employees;

-- students 테이블 모든 학생의 kor 점수 합계와 평균 최대 최소를 구하시오
select sum(kor),avg(kor),max(kor),min(kor) from students;

-- 부서번호가 50인 사원들의 월급의 합,평균,최대,최소을 출력
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id =50;

-- 부서번호가 30
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id =30;
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id =10;

-- group by : 단일함수를 출력하고 싶을 때, 단일함수를 입력하면 됨.
select department_id,max(salary) from employees group by department_id;

select emp_name,salary from employees;

-- 107명의 평균
select avg(salary) from employees;

-- 단일함수와 그룹함수를 함께 사용하려면 group by로 지정해야함.
select department_id,avg(salary) from employees group by department_id;


select emp_name,max(salary) from employees group by emp_name;

select department_id,round(avg(salary),2),count(salary) from employees group by department_id order by department_id;
-- 평균월급보다 높은 사람 수를 출력하시오
select count(*) from employees where salary > (select avg(salary) from employees);


-- 수학함수 : abs,ceil,floor,round,trunc,mod,power,sqrt

select power(2,3),2*2*2 from dual;

-- 문자,숫자형 타입 -> 날짜형 타입 변경 가능
-- 숫자,날짜형 타입 -> 문자형 타입 변경 가능
-- 문자 -> 숫자형 타입 변경가능
-- 날짜 -> 숫자형 타입 변경불가
-- 날짜 -> 문자 -> 숫자형 타입 변경 가능
select 20240101,to_date(20240101) from dual;

select sysdate,to_number(sysdate) from dual;

select '20240101',to_number('20240101') from dual;

select 20240101,to_number(to_date(20240101)) from dual;

select Sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;

-- 날짜형 타입을 문자형 타입으로 변경시, '년','월','일' 한글,특수문자 입력 방법
select sysdate,to_char(sysdate,'yyyy"년" mm"월" dd"일" day') from dual;
select sysdate,to_char(sysdate,'yyyy"년"-MON-dd"일" dy') from dual;


-- 문자형 타입을 합쳐서 + 기호를 사용해서 합치려고 하면 에러
select emp_name,email from employees;
select emp_name||email from employees;

-- 숫자형 타입 : 사칙연산 계산해서 출력됨.
desc employees;

-- lower : 소문자 치환, upper : 대문자 치환, initcap : 첫글자 대문자
select * from member where lower(name)='bryan';

select 'joHn',initcap('joHn'),lower('joHn'),upper('joHn') from dual;

--lpad
select 'john',lpad('john',10,'#') from dual;
--rpad
select 'john',rpad('john',10,'#') from dual;
--trim : 앞,뒤공백없애기, ltrim,rtrim
-- 공백도 길이에 포함
select length('    aaa   '),length(trim('    aaa   ')),ltrim('    aaa   '),rtrim('    aaa   ') from dual;
--replace:치환
select '  a b c    ',trim('  a b c    ') from dual;
select '  a b c    ',trim('  a b c    '),length(replace('  a b c    ',' ','')) from dual;

--substr : 특정 위치 자르기 (시작위치,개수)
select 'abcdefg',substr('abcdefg',0,3),substr('abcdefg',3,3) from dual;

-- 입사일 3월인 사원 출력
select * from employees where hire_date like '%/03/%'; 
select * from employees where extract(month from hire_date)=3;
select * from employees where substr(hire_date,4,2) = 03;
select * from employees where substr(hire_date,4,2) in(03,08,10);

-- 입사일 7월 이상
select * from employees where substr(hire_date,4,2) > 07;

-- translate 치환
-- translate : 일대일 대응(한글자씩 해당되는 단어를 각각의 단어로 치환, 순서에 없는 변환글자는 삭제처리)
-- replace : '' 안의 단어가 일치하는 문자만 치환 
select 'axyz',translate('axyz','xy','ab') from dual;
select 'axyz',translate('jxyzxkkcyjccx','xy','ab'),replace('jxyzxkkcyjccx','xy','ab') from dual;
select 'axyz',replace('jxyzxkkcyjccx','xy','ab') from dual;

-- length() : 문자열 길이
-- students 테이블 name 글자 길이가 10자 이상인 학생만 출력
select * from students where length(name) >=10;


-- 사원 월급의 합과 평균을 구하시오
select sum(salary),avg(salary) from employees;
-- 영어점수의 합, 평균, 최대값, 최소값을 구하시오
select sum(eng),avg(eng),max(eng),min(eng) from students;
-- students 테이블에서 홍길동, 2023년 12월 02일 << 표현 
select name,to_char(sdate,'"등록일 : "yyyy"년" mm"월" dd"일"') from students;


-- nvl,group by, translate, replace, substr(오라클은 0이 아닌 1이 시작), length, trim, pad, lower/upper/initcat
-- 수학함수 : abs,ceil,floor,round,trunc,mod,power,sqrt
-- 그룹 함수 : sum(합계), avg(평균), count(개수), min(최소), max(최대), median(중간값)
-- null값 대체 : nvl(문자를 받기 위해선 0을 문자로 치환해야함)

-- 숫자타입 -> 문자타입으로 변경해서 포맷, 천단위(,) 표시
-- 9 : 0을 채우지 않음, 0 : 0을 채움
-- L : 국가 통화기호 표시, $ : 달러 표시

-- select nvl(to_char(department_id),'ceo') from employees;
-- 날짜 -> 문자 to_char ## 날짜포맷
-- 문자 -> 날짜 to_date ## 날짜사칙연산
-- 숫자 -> 문자 to_char ## 천단위, 0과9
-- 문자 -> 숫자 to_number ## 천단위 표시 삭제 후 계산