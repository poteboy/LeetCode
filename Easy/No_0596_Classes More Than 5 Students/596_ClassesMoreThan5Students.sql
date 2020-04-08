#Runtime: 237 ms, faster than 65.29% of MySQL online submissions for Classes More Than 5 Students.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Classes More Than 5 Students.

# Write your MySQL query statement below
select class
from courses
group by class
having count(distinct(student)) >= 5;
