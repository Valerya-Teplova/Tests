select 
  customer_id, 
  Customers.name,
  count(distinct order_id) all_orders,
  count(distinct case when OrderItems.name = N'Кассовый аппарат' then order_id end) cash_machine_orders 
from Orders
join OrderItems on Orders.row_id = OrderItems.order_id
join Customers on Customers.row_id = customer_id
where Orders.registered_at between '2020/01/01' and '2020/12/31'
group by Customers.name, customer_id
having count(distinct order_id) = count(distinct case when OrderItems.name = N'Кассовый аппарат' then order_id end);