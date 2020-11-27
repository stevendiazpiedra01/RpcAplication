-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-11-2020 a las 01:43:54
-- Versión del servidor: 10.4.16-MariaDB
-- Versión de PHP: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbcaso5`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `numeroDocumento` int(10) NOT NULL,
  `idTipoDocumento_FK` int(1) NOT NULL,
  `nombres` tinytext NOT NULL,
  `apellidos` tinytext NOT NULL,
  `idTipoEmpleado_FK` int(11) NOT NULL,
  `clave` text NOT NULL,
  `fecIngreso` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`numeroDocumento`, `idTipoDocumento_FK`, `nombres`, `apellidos`, `idTipoEmpleado_FK`, `clave`, `fecIngreso`) VALUES
(6986, 1, 'cont', 'carro', 2, '5C19A7A9771B62DF', '2020-11-20 02:00:34.485124'),
(123456, 1, 'SAL', 'ERP', 1, 'DB756D33AC358FFCDA5845F392893B0B', '2020-11-26 10:49:41.794703'),
(159874, 1, 'brayan', 'diaz', 1, 'AC50F25EAB3F4681', '2020-11-26 12:30:50.487861'),
(5783188, 1, 'maria', 'fajon', 2, 'AC50F25EAB3F4681', '2020-11-26 15:47:12.542561'),
(1022416695, 1, 'brayan', 'diaz', 1, 'EF3C9BFCC8CE4C77ADC22F083BC79A78', '2020-11-20 02:04:48.219959');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registros`
--

CREATE TABLE `registros` (
  `registroID` int(11) NOT NULL,
  `fecha` varchar(25) NOT NULL,
  `hora_inicio` varchar(25) NOT NULL,
  `hora_fin` varchar(25) NOT NULL,
  `empleadoID` int(11) NOT NULL,
  `clienteID` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `registros`
--

INSERT INTO `registros` (`registroID`, `fecha`, `hora_inicio`, `hora_fin`, `empleadoID`, `clienteID`) VALUES
(1, '2013-01-20', '00:56:09', '22:54:43', 18, '700272437'),
(2, '1977-07-17', '12:01:42', '09:26:08', 20, '962362610'),
(3, '1941-10-25', '02:38:21', '01:48:45', 1, '697371337'),
(4, '1990-07-03', '05:14:33', '17:56:34', 15, '485508291'),
(5, '1912-08-20', '03:05:50', '14:46:11', 15, '877500697'),
(6, '1978-07-13', '01:32:12', '18:24:59', 4, '631415163'),
(7, '1988-07-26', '14:17:49', '20:13:14', 7, '334853542'),
(8, '1957-11-12', '22:58:33', '12:13:15', 10, '946225243');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipodocumento`
--

CREATE TABLE `tipodocumento` (
  `idTipoDocumeto` int(11) NOT NULL,
  `tipoDocumento` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tipodocumento`
--

INSERT INTO `tipodocumento` (`idTipoDocumeto`, `tipoDocumento`) VALUES
(1, 'C.C.'),
(2, 'T.I.'),
(3, 'C.E.'),
(4, 'P.E.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipoempleado`
--

CREATE TABLE `tipoempleado` (
  `idTipoEmpleado` int(11) NOT NULL,
  `tipoEmpleado` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tipoempleado`
--

INSERT INTO `tipoempleado` (`idTipoEmpleado`, `tipoEmpleado`) VALUES
(1, 'administracion'),
(2, 'recepcion');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`numeroDocumento`),
  ADD KEY `idTipoDocumento_FK` (`idTipoDocumento_FK`),
  ADD KEY `idTipoEmpleado_FK` (`idTipoEmpleado_FK`);

--
-- Indices de la tabla `registros`
--
ALTER TABLE `registros`
  ADD PRIMARY KEY (`registroID`);

--
-- Indices de la tabla `tipodocumento`
--
ALTER TABLE `tipodocumento`
  ADD PRIMARY KEY (`idTipoDocumeto`);

--
-- Indices de la tabla `tipoempleado`
--
ALTER TABLE `tipoempleado`
  ADD PRIMARY KEY (`idTipoEmpleado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `registros`
--
ALTER TABLE `registros`
  MODIFY `registroID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`idTipoDocumento_FK`) REFERENCES `tipodocumento` (`idTipoDocumeto`),
  ADD CONSTRAINT `empleados_ibfk_2` FOREIGN KEY (`idTipoEmpleado_FK`) REFERENCES `tipoempleado` (`idTipoEmpleado`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
