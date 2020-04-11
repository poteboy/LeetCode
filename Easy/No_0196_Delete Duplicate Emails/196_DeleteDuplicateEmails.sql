#Runtime: 942 ms, faster than 62.87% of MySQL online submissions for Delete Duplicate Emails.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.

# Write your MySQL query statement below
delete p1
from Person p1, Person p2
where p1.Email = p2.Email
and p1.id > p2.id;
