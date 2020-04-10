# Write your MySQL query statement below

select Name as 'Customers'
from Customers
where Id not in (
    select Customers.Id
    from Customers
    join Orders
    on Customers.Id = Orders.CustomerId
);
