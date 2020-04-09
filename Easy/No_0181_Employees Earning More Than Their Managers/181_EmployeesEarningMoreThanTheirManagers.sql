
#Runtime: 345 ms, faster than 77.39% of MySQL online submissions for Employees Earning More Than Their Managers.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.

select e1.Name as 'Employee'
from Employee e1
join Employee e2
on e1.ManagerId = e2.Id
where e1.Salary > e2.Salary;
