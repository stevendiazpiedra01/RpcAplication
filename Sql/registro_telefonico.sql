-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 23, 2020 at 10:42 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE DATABASE IF NOT EXISTS `registro_telefonico` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `registro_telefonico`;

--
-- Database: `registro_telefonico`
--

-- --------------------------------------------------------

--
-- Table structure for table `registros`
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
-- Dumping data for table `registros`
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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registros`
--
ALTER TABLE `registros`
  ADD PRIMARY KEY (`registroID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `registros`
--
ALTER TABLE `registros`
  MODIFY `registroID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
