UPDATE test
SET password=PASSWORD('FoodBar')
WHERE name='Foo';

INSERT INTO test_color(fav_color)
VALUES ('Purple'),
       ('White');
