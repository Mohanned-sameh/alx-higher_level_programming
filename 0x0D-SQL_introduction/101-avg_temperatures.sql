-- this script displays the average temperature(f) by city ordered by desc
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;