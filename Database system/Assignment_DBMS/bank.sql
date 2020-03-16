-- MySQL dump 10.16  Distrib 10.3.10-MariaDB, for osx10.14 (x86_64)
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	10.3.10-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ACCOUNT`
--

DROP TABLE IF EXISTS `ACCOUNT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ACCOUNT` (
  `Anumber` char(12) NOT NULL,
  `Balance` decimal(10,0) NOT NULL,
  `Term` date DEFAULT NULL,
  `Interest` decimal(3,2) DEFAULT NULL,
  `Ussn` char(9) NOT NULL,
  PRIMARY KEY (`Anumber`),
  KEY `Ussn` (`Ussn`),
  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`Ussn`) REFERENCES `USER` (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ACCOUNT`
--

LOCK TABLES `ACCOUNT` WRITE;
/*!40000 ALTER TABLE `ACCOUNT` DISABLE KEYS */;
INSERT INTO `ACCOUNT` VALUES ('216942137264',2430000,'2020-03-01',1.07,'333445555'),('273986092469',1250000,'2020-05-09',1.07,'987987987'),('366947237264',300000,NULL,NULL,'333445555'),('478347894945',1400000,'2020-09-01',1.13,'123456789'),('539134653046',4250000,'2020-02-05',1.04,'888665555'),('539608253046',380000,NULL,NULL,'888665555'),('578345624945',250000,NULL,NULL,'123456789'),('599168678006',3250000,'2020-05-01',1.03,'987654321'),('713682887887',1380000,'2020-02-13',1.20,'999887777'),('729641348006',400000,NULL,NULL,'987654321'),('850986092469',550000,NULL,NULL,'987987987'),('943110567309',1550000,'2020-01-04',1.12,'666884444'),('943113467309',250000,NULL,NULL,'666884444'),('948482887887',250000,NULL,NULL,'999887777'),('964189181156',1000000,'2020-05-14',1.07,'453453453'),('964462351156',430000,NULL,NULL,'453453453');
/*!40000 ALTER TABLE `ACCOUNT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEPOSIT`
--

DROP TABLE IF EXISTS `DEPOSIT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DEPOSIT` (
  `Dnumber` decimal(5,0) NOT NULL,
  `Damount` decimal(10,0) NOT NULL,
  `Daccount` char(12) NOT NULL,
  `Mssn` char(9) NOT NULL,
  PRIMARY KEY (`Dnumber`),
  KEY `Daccount` (`Daccount`),
  KEY `Mssn` (`Mssn`),
  CONSTRAINT `deposit_ibfk_2` FOREIGN KEY (`Mssn`) REFERENCES `MANAGER` (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPOSIT`
--

LOCK TABLES `DEPOSIT` WRITE;
/*!40000 ALTER TABLE `DEPOSIT` DISABLE KEYS */;
INSERT INTO `DEPOSIT` VALUES (1,100,'578345624945','234234234'),(2,100,'948482887887','222444888'),(3,100,'943113467309','222444888'),(4,200,'366947237264','222444888'),(5,300,'539608253046','222444888'),(6,400,'729641348006','666333111'),(7,300,'964462351156','666333111'),(8,300,'850986092469','222444888'),(9,300,'578345624945','234234234'),(10,300,'948482887887','234234234'),(11,400,'943113467309','234234234'),(12,400,'366947237264','234234234'),(13,400,'539608253046','234234234'),(14,400,'729641348006','234234234'),(15,400,'964462351156','234234234'),(16,200,'850986092469','666333111'),(17,200,'578345624945','666333111'),(18,200,'948482887887','222444888'),(19,100,'943113467309','666333111'),(20,100,'366947237264','666333111'),(21,100,'539608253046','666333111'),(22,200,'729641348006','234234234'),(23,300,'964462351156','234234234'),(24,400,'850986092469','222444888'),(25,300,'578345624945','666333111'),(26,300,'948482887887','222444888'),(27,300,'943113467309','666333111'),(28,300,'366947237264','666333111'),(29,400,'539608253046','666333111'),(30,400,'729641348006','222444888'),(31,400,'964462351156','222444888'),(32,400,'850986092469','222444888');
/*!40000 ALTER TABLE `DEPOSIT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LOAN`
--

DROP TABLE IF EXISTS `LOAN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LOAN` (
  `Lnumber` decimal(5,0) NOT NULL,
  `Lamount` decimal(10,0) NOT NULL,
  `Lterm` date NOT NULL,
  `Linterest` decimal(3,2) NOT NULL,
  `Laccount` char(12) NOT NULL,
  `Mssn` char(9) NOT NULL,
  PRIMARY KEY (`Lnumber`),
  KEY `Laccount` (`Laccount`),
  KEY `Mssn` (`Mssn`),
  CONSTRAINT `loan_ibfk_2` FOREIGN KEY (`Mssn`) REFERENCES `MANAGER` (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LOAN`
--

LOCK TABLES `LOAN` WRITE;
/*!40000 ALTER TABLE `LOAN` DISABLE KEYS */;
INSERT INTO `LOAN` VALUES (1,300000,'2023-04-01',1.19,'964462351156','222444888'),(2,530000,'2022-06-09',1.29,'539608253046','666333111'),(3,123000,'2021-08-27',1.17,'366947237264','666333111'),(4,240000,'2023-10-03',1.25,'948482887887','222444888'),(5,500000,'2020-12-13',1.20,'578345624945','234234234');
/*!40000 ALTER TABLE `LOAN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MANAGER`
--

DROP TABLE IF EXISTS `MANAGER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MANAGER` (
  `Name` varchar(15) NOT NULL,
  `Ssn` char(9) NOT NULL,
  `Sex` char(1) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Bdate` date DEFAULT NULL,
  `Salary` decimal(8,0) DEFAULT NULL,
  PRIMARY KEY (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MANAGER`
--

LOCK TABLES `MANAGER` WRITE;
/*!40000 ALTER TABLE `MANAGER` DISABLE KEYS */;
INSERT INTO `MANAGER` VALUES ('George','222444888','M','1121 Castle, Spring, TX','1960-11-11',40000),('David','234234234','M','713 Fondren, Houston, TX','1951-12-15',50000),('Fred','666333111','F','1455 Voss, Houston, TX','1995-08-13',15000);
/*!40000 ALTER TABLE `MANAGER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REMITTANCE`
--

DROP TABLE IF EXISTS `REMITTANCE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `REMITTANCE` (
  `Rnumber` decimal(5,0) NOT NULL,
  `Ramount` decimal(10,0) NOT NULL,
  `Getting_account` char(12) NOT NULL,
  `Raccount` char(12) NOT NULL,
  `Mssn` char(9) NOT NULL,
  PRIMARY KEY (`Rnumber`),
  KEY `Raccount` (`Raccount`),
  KEY `Mssn` (`Mssn`),
  CONSTRAINT `remittance_ibfk_2` FOREIGN KEY (`Mssn`) REFERENCES `MANAGER` (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REMITTANCE`
--

LOCK TABLES `REMITTANCE` WRITE;
/*!40000 ALTER TABLE `REMITTANCE` DISABLE KEYS */;
INSERT INTO `REMITTANCE` VALUES (1,25,'964462351156','850986092469','222444888'),(2,25,'964462351156','850986092469','666333111'),(3,25,'539608253046','964462351156','222444888'),(4,125,'943113467309','964462351156','234234234'),(5,225,'964462351156','729641348006','222444888'),(6,325,'964462351156','729641348006','234234234'),(7,225,'578345624945','539608253046','666333111'),(8,225,'943113467309','539608253046','234234234'),(9,225,'539608253046','366947237264','666333111'),(10,225,'578345624945','366947237264','234234234'),(11,325,'578345624945','943113467309','666333111'),(12,325,'539608253046','943113467309','234234234'),(13,325,'943113467309','948482887887','222444888'),(14,325,'539608253046','948482887887','234234234'),(15,325,'539608253046','578345624945','666333111'),(16,125,'943113467309','578345624945','234234234'),(17,125,'539608253046','850986092469','222444888'),(18,125,'943113467309','850986092469','222444888'),(19,25,'578345624945','964462351156','234234234'),(20,25,'850986092469','964462351156','666333111'),(21,25,'539608253046','729641348006','234234234'),(22,125,'943113467309','729641348006','666333111'),(23,225,'850986092469','539608253046','666333111'),(24,325,'729641348006','539608253046','222444888'),(25,225,'850986092469','366947237264','666333111'),(26,225,'943113467309','366947237264','222444888'),(27,225,'578345624945','943113467309','666333111'),(28,225,'729641348006','943113467309','222444888'),(29,325,'729641348006','948482887887','222444888'),(30,325,'578345624945','948482887887','222444888'),(31,325,'539608253046','578345624945','666333111'),(32,325,'729641348006','578345624945','234234234');
/*!40000 ALTER TABLE `REMITTANCE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USER` (
  `Name` varchar(15) NOT NULL,
  `Ssn` char(9) NOT NULL,
  `Sex` char(1) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Bdate` date DEFAULT NULL,
  `Salary` decimal(8,0) DEFAULT NULL,
  PRIMARY KEY (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER`
--

LOCK TABLES `USER` WRITE;
/*!40000 ALTER TABLE `USER` DISABLE KEYS */;
INSERT INTO `USER` VALUES ('John','123456789','M','731 Fondren, Houston, TX','1965-01-09',30000),('Franklin','333445555','M','638 Voss, Houston, TX','1955-12-08',40000),('Joyce','453453453','F','5631 Rice, Houston, TX','1972-07-31',25000),('Ramesh','666884444','M','975 Fire Oak, Humble, TX','1962-09-15',38000),('James','888665555','M','450 Stone, Houston, TX','1937-11-10',55000),('Jennifer','987654321','F','291 Berry, Bellaire, TX','1941-06-20',43000),('Ahmad','987987987','M','980 Dallas, Houston, TX','1969-03-29',25000),('Alicia','999887777','F','3321 Castle, Spring, TX','1968-01-19',25000);
/*!40000 ALTER TABLE `USER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WITHDRAW`
--

DROP TABLE IF EXISTS `WITHDRAW`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WITHDRAW` (
  `Wnumber` decimal(5,0) NOT NULL,
  `Wamount` decimal(10,0) NOT NULL,
  `Waccount` char(12) NOT NULL,
  `Mssn` char(9) NOT NULL,
  PRIMARY KEY (`Wnumber`),
  KEY `Waccount` (`Waccount`),
  KEY `Mssn` (`Mssn`),
  CONSTRAINT `withdraw_ibfk_2` FOREIGN KEY (`Mssn`) REFERENCES `MANAGER` (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WITHDRAW`
--

LOCK TABLES `WITHDRAW` WRITE;
/*!40000 ALTER TABLE `WITHDRAW` DISABLE KEYS */;
INSERT INTO `WITHDRAW` VALUES (1,50,'850986092469','222444888'),(2,50,'964462351156','222444888'),(3,50,'729641348006','222444888'),(4,250,'539608253046','666333111'),(5,450,'366947237264','666333111'),(6,650,'943113467309','666333111'),(7,450,'948482887887','222444888'),(8,450,'578345624945','666333111'),(9,450,'850986092469','222444888'),(10,450,'964462351156','234234234'),(11,650,'729641348006','234234234'),(12,650,'539608253046','666333111'),(13,650,'366947237264','666333111'),(14,650,'943113467309','666333111'),(15,650,'948482887887','222444888'),(16,250,'578345624945','666333111'),(17,250,'850986092469','666333111'),(18,250,'964462351156','234234234'),(19,50,'729641348006','234234234'),(20,50,'539608253046','234234234'),(21,50,'366947237264','234234234'),(22,250,'943113467309','234234234'),(23,450,'948482887887','234234234'),(24,650,'578345624945','234234234'),(25,450,'850986092469','222444888'),(26,450,'964462351156','666333111'),(27,450,'729641348006','666333111'),(28,450,'539608253046','222444888'),(29,650,'366947237264','222444888'),(30,650,'943113467309','222444888'),(31,650,'948482887887','222444888'),(32,650,'578345624945','234234234');
/*!40000 ALTER TABLE `WITHDRAW` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-07 12:57:36
