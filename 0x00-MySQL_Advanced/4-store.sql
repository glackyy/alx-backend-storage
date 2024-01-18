-- A Script that creates a trigger
-- Decreases the quantity of an item after adding a new order
CREATE TRIGGER d_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;