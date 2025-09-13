CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    is_public BOOLEAN DEFAULT TRUE
);

-- Many2many relationship table between products and categories
CREATE TABLE products_product_categories_rel (
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    category_id INT NOT NULL REFERENCES product_categories(category_id) ON DELETE CASCADE,
    PRIMARY KEY (product_id, category_id)
);