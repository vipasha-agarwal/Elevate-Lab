use elevateecommerce;

CREATE TABLE online_sales (
    order_id INT,
    order_date DATE,
    amount DECIMAL(10, 2),
    product_id INT
);

INSERT INTO online_sales (order_id, order_date, amount, product_id) VALUES
(101, '2024-01-05', 120.50, 1),
(102, '2024-01-15', 85.00, 2),
(103, '2024-02-10', 220.00, 3),
(104, '2024-02-21', 150.75, 4),
(105, '2024-03-01', 95.25, 2),
(106, '2024-03-12', 305.00, 1),
(107, '2024-04-05', 410.50, 3),
(108, '2024-04-18', 75.00, 2),
(109, '2024-05-09', 199.99, 4),
(110, '2024-05-22', 180.00, 1);


SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM 
    online_sales
GROUP BY 
    EXTRACT(YEAR FROM order_date), 
    EXTRACT(MONTH FROM order_date)
ORDER BY 
    year, 
    month;