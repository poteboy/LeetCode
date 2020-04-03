
#Runtime: 242 ms, faster than 77.60% of MySQL online submissions for Big Countries.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Big Countries.

# Write your MySQL query statement below

select name, population, area
from World
where population > 25000000
or area > 3000000
group by population, area;
