-- Retrieve product IDs associated with more than 5 public categories
SELECT
    product_id
FROM
    products_product_categories_rel ppcr
JOIN
    product_categories pc ON ppcr.category_id = pc.category_id
WHERE
    pc.is_public
GROUP BY
    product_id
HAVING
    COUNT(*) > 5;