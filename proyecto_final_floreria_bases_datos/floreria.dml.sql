use florerias;


INSERT INTO proveedores (nombre_empresa, telefono) 
VALUES ('Cultivos del Sur S.A.', '+541145678901');


INSERT INTO categoria (nombre_categoria) 
VALUES ('Flores de Estacion');


INSERT INTO metodos_pago (nombre_metodo) 
VALUES ('Efectivo');


INSERT INTO articulos (nombre, precio, stock, id_proveedor, id_categoria) 
VALUES ('Ramo de Rosas Rojas x12', 25000.00, 15, 1, 1);



INSERT INTO clientes (id_cliente, nombre, telefono, email) 
VALUES (101, 'Rosalba Benitez', '+541123333333', 'rosalba15@email.com');


INSERT INTO ventas (fecha, total, id_cliente, id_metodo_pago) 
VALUES ('2026-06-22 10:30:00', 0.00, 101, 1);



