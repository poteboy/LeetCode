
#Runtime: 563 ms, faster than 19.46% of MySQL online submissions for Combine Two Tables.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.

# Write your MySQL query statement below

select FirstName, LastName, City, State
from Person
left join Address
on Person.PersonId =  Address.PersonId;
