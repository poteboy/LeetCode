
#Runtime: 297 ms, faster than 50.59% of MySQL online submissions for Duplicate Emails.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.


# Write your MySQL query statement below
select Email
from person
group by Email
having count(Email) >=2;
