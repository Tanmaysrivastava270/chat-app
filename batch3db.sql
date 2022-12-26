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
-- Database: `batch3db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `email` varchar(34) NOT NULL,
  `password` varchar(44) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `password`) VALUES
(1, 'admin@gmail.com', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `id` int(11) NOT NULL,
  `sendermessage` varchar(100) NOT NULL,
  `receivermessage` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`id`, `sendermessage`, `receivermessage`) VALUES
(49, 'hello user', ''),
(50, '', 'hi I am fine'),
(51, 'helllo saumya ji', ''),
(52, '', 'hello raman ji'),
(53, 'hi', ''),
(54, 'hi saurabh', ''),
(55, 'hi shubham', ''),
(56, 'hi vibho', ''),
(57, 'kaie ho tum ', ''),
(58, 'mast rhoo', ''),
(59, 'hello bhaiya', ''),
(60, 'kaie ho tum ', ''),
(61, 'introduction', ''),
(62, '', 'kya hua'),
(63, '', 'shubham  the great'),
(64, 'mashgfywjrg', ''),
(65, '', 'jhyf');

-- --------------------------------------------------------

--
-- Table structure for table `ppassword`
--

CREATE TABLE `ppassword` (
  `id` int(11) NOT NULL,
  `email` varchar(34) NOT NULL,
  `password` varchar(44) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `usertbp`
--

CREATE TABLE `usertbp` (
  `id` int(11) NOT NULL,
  `Name` varchar(34) NOT NULL,
  `Email` varchar(44) NOT NULL,
  `Password` varchar(33) NOT NULL,
  `mobile` int(67) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertbp`
--

INSERT INTO `usertbp` (`id`, `Name`, `Email`, `Password`, `mobile`) VALUES
(23, 'user', 'user@gmail.com', 'qwerty', 12345678),
(24, 'TANMAY ', 'shyam@gmai.com', '123', 7415263);

-- --------------------------------------------------------

--
-- Table structure for table `usertbr`
--

CREATE TABLE `usertbr` (
  `id` int(11) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `password` varchar(44) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertbr`
--

INSERT INTO `usertbr` (`id`, `Email`, `password`) VALUES
(23, 'user@gmail.com', 'user'),
(24, 'shyam@gmai.com', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ppassword`
--
ALTER TABLE `ppassword`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usertbp`
--
ALTER TABLE `usertbp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usertbr`
--
ALTER TABLE `usertbr`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `ppassword`
--
ALTER TABLE `ppassword`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usertbp`
--
ALTER TABLE `usertbp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `usertbr`
--
ALTER TABLE `usertbr`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
