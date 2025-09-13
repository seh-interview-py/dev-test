-- Insert some products
INSERT INTO products (name, price) VALUES
('Laptop', 1200.00),
('Mouse', 25.50),
('Keyboard', 45.00),
('Monitor', 300.00),
('Headphones', 75.00);

-- Insert some categories
INSERT INTO product_categories (name, is_public) VALUES
('Electronics', TRUE),
('Accessories', TRUE),
('Gaming', TRUE),
('Private Deals', FALSE),
('Office', TRUE),
('Premium', FALSE);
('Audio', TRUE),
('Computers', TRUE),
('Gaming Gear', TRUE);

-- Link products to categories
INSERT INTO products_product_categories_rel (product_id, category_id) VALUES
(1, 1), -- Laptop -> Electronics
(1, 3), -- Laptop -> Gaming
(1, 5), -- Laptop -> Office
(1, 6), -- Laptop -> Audio
(1, 7), -- Laptop -> Computers
(1, 8); -- Laptop -> Gaming Gear
(2, 1), -- Mouse -> Electronics
(2, 2), -- Mouse -> Accessories
(3, 2), -- Keyboard -> Accessories
(3, 5), -- Keyboard -> Office
(4, 1), -- Monitor -> Electronics
(4, 3), -- Monitor -> Gaming
(5, 2), -- Headphones -> Accessories
(5, 3); -- Headphones -> Gaming