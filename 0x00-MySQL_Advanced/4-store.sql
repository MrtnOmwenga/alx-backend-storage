-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.

CREATE TRIGGER update_items_after_order
AFTER INSERT ON `orders` FOR EACH ROW
UPDATE items SET quantity = quantity - New.number WHERE name = NEW.item_name;
