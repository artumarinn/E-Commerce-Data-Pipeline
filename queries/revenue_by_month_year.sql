-- TODO: This query will return a table with the revenue by month and year. It
-- will have different columns: month_no, with the month numbers going from 01
-- to 12; month, with the 3 first letters of each month (e.g. Jan, Feb);
-- Year2016, with the revenue per month of 2016 (0.00 if it doesn't exist);
-- Year2017, with the revenue per month of 2017 (0.00 if it doesn't exist) and
-- Year2018, with the revenue per month of 2018 (0.00 if it doesn't exist).
-- Query definitiva para revenue_by_month_year

with revenue_time as (
    select o.customer_id, o.order_id, o.order_delivered_customer_date,
    strftime('%m', o.order_delivered_customer_date) as month_no,
    strftime('%Y', o.order_delivered_customer_date) as year,
    p.payment_value
    from olist_orders o 
    inner join olist_order_payments p on (o.order_id = p.order_id ) 
    where o.order_status = 'delivered'
    and o.order_delivered_customer_date is not null
    group by o.customer_id, o.order_id, o.order_delivered_customer_date, month_no, "year" 
)
select month_no,
case month_no
    when '01' then 'Jan' 
    when '02' then 'Feb' 
    when '03' then 'Mar' 
    when '04' then 'Apr' 
    when '05' then 'May' 
    when '06' then 'Jun' 
    when '07' then 'Jul' 
    when '08' then 'Aug' 
    when '09' then 'Sep' 
    when '10' then 'Oct' 
    when '11' then 'Nov' 
    when '12' then 'Dec' 
end as month,
coalesce(sum(case year when '2016' then payment_value end), 0.0) as Year2016,
coalesce(sum(case year when '2017' then payment_value end), 0.0) as Year2017,
coalesce(sum(case year when '2018' then payment_value end), 0.0) as Year2018
from revenue_time
group by month_no 
order by month_no