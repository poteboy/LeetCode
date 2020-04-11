#Runtime: 140 ms, faster than 78.38% of MySQL online submissions for Not Boring Movies.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Not Boring Movies.


# Write your MySQL query statement below

select *
from cinema
where id % 2 = 1
and description != 'boring'
order by rating desc;
