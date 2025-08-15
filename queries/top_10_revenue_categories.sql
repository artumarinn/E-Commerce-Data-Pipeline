-- TODO: This query will return a table with the top 10 revenue categories in 
-- English, the number of orders and their total revenue. The first column will 
-- be Category, which will contain the top 10 revenue categories; the second one 
-- will be Num_order, with the total amount of orders of each category; and the 
-- last one will be Revenue, with the total revenue of each catgory.
-- HINT: All orders should have a delivered status and the Category and actual 
-- delivery date should be not null.


WITH order_revenue AS (
    SELECT 
        o.order_id,
        SUM(pay.payment_value) AS order_payment
    FROM olist_orders o
    JOIN olist_order_payments pay ON o.order_id = pay.order_id
    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL
    GROUP BY o.order_id
),
order_categories AS (
    SELECT 
        oi.order_id,
        t.product_category_name_english AS Category
    FROM olist_order_items oi
    JOIN olist_products p ON oi.product_id = p.product_id
    JOIN product_category_name_translation t ON p.product_category_name = t.product_category_name
)
SELECT
    oc.Category,
    COUNT(DISTINCT oc.order_id) AS Num_order,
    SUM(orv.order_payment) AS Revenue
FROM order_categories oc
JOIN order_revenue orv ON oc.order_id = orv.order_id
GROUP BY oc.Category
ORDER BY Revenue DESC
LIMIT 10;