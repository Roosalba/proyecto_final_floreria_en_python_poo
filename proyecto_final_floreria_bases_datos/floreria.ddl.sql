DROP DATABASE IF EXISTS florerias;
CREATE DATABASE IF NOT EXISTS florerias;
USE florerias;

CREATE TABLE proveedores(
id_proveedor int primary key  auto_increment,
nombre_empresa VARCHAR (50) NOT NULL,
telefono VARCHAR (20)

);


CREATE TABLE categoria(
id_categoria int primary key auto_increment,
nombre_categoria varchar (50)

);

CREATE TABLE metodos_pago(
id_metodo_pago int primary key auto_increment,
nombre_metodo VARCHAR (30) NOT NULL

);


CREATE TABLE articulos(
id_articulo int primary key auto_increment,
nombre varchar (50) NOT NULL,
precio decimal (10,2) NOT NULL,
stock int NOT NULL,
id_proveedor int,
id_categoria int,
foreign key (id_proveedor) references proveedores(id_proveedor) on delete set null,
foreign key (id_categoria) references categoria (id_categoria) on delete set null
);



CREATE TABLE clientes(
id_cliente int primary key,
nombre VARCHAR (50) NOT NULL,
telefono VARCHAR (20),
email VARCHAR (50)

);


CREATE TABLE ventas(
id_venta int primary key auto_increment,
fecha datetime default current_timestamp,
total decimal(10,2),
id_cliente int,
id_metodo_pago int,
foreign key (id_cliente) references clientes(id_cliente) on delete set null,
foreign key (id_metodo_pago) references metodos_pago (id_metodo_pago) on delete set null

);

CREATE TABLE detalle_ventas(
id_detalle int primary key auto_increment,
cantidad int,
sub_total decimal(10,2),
id_articulo int,
id_venta int,
foreign key (id_articulo) references articulos(id_articulo) on delete set null,
foreign key (id_venta) references ventas(id_venta) on delete set null
);
