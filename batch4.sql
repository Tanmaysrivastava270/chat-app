-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 02, 2022 at 06:21 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `batch4`
--

-- --------------------------------------------------------

--
-- Table structure for table `usertbc`
--

CREATE TABLE `usertbc` (
  `id` int(11) NOT NULL,
  `Name` varchar(34) NOT NULL,
  `email` varchar(44) NOT NULL,
  `mobile` varchar(33) NOT NULL,
  `feedback` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertbc`
--

INSERT INTO `usertbc` (`id`, `Name`, `email`, `mobile`, `feedback`) VALUES
(1, 'TANMAY ', 'Srivastavat300@gmail.com', '234', ''),
(2, 'TANMAY ', 'Srivastavat300@gmail.com', '234', ''),
(3, 'TANMAY ', 'Srivastavat300@gmail.com', '3456', ''),
(4, 'TANMAY ', 'Srivastavat300@gmail.com', '123456', ''),
(5, 'ram', 'ram@dfgh.com', '741852963', ''),
(6, 'ram', 'ram@dfgh.com', '741852963', ''),
(7, 'TANMAY ', 'kanand635@gmail.com', '12535', ''),
(8, 'TANMAY ', 'Srivastavat300@gmail.com', '741852', ''),
(9, 'ram', 'Srivastavat300@gmail.com', '85293', 'sdfghjk'),
(10, 'customer', 'customer@gmail.com', '123456789', 'outstanding'),
(11, 'user', 'user@gmail.com', '12345679', 'outstanding');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `usertbc`
--
ALTER TABLE `usertbc`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `usertbc`
--
ALTER TABLE `usertbc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
