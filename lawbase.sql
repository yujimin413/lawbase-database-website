CREATE DATABASE  IF NOT EXISTS `lawbase` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `lawbase`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: lawbase
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cases`
--

DROP TABLE IF EXISTS `cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cases` (
  `case_ID` int NOT NULL AUTO_INCREMENT,
  `client_ID` int NOT NULL,
  `title` varchar(40) NOT NULL,
  `department` varchar(20) NOT NULL,
  `open_date` varchar(20) NOT NULL,
  `close_date` varchar(20) NOT NULL,
  PRIMARY KEY (`case_ID`,`client_ID`),
  KEY `client_ID_idx` (`client_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cases`
--

LOCK TABLES `cases` WRITE;
/*!40000 ALTER TABLE `cases` DISABLE KEYS */;
INSERT INTO `cases` VALUES (1,1,'Trial Case','Criminal','2024-08-03','Not Closed'),(2,2,'State vs. Michael Clark','Criminal','01-02-2024','10-03-2024'),(3,3,'Walker v. XYZ Corporation','Corporate','20-01-2024','Not Closed'),(4,4,'Hill v. Hill','Family','10-02-2024','05-04-2024'),(5,5,'Hayes Asylum Petition','Immigration','15-02-2024','Not Closed'),(6,6,'Wright Labor Dispute','Labor','01-03-2024','15-04-2024'),(7,7,'Turner Real Estate Dispute','Real Estate','30-01-2024','Not Closed'),(8,8,'Scott Tax Evasion Case','Tax','20-02-2024','01-04-2024'),(9,9,'Parker v. Former Employer','Civil','25-02-2024','Not Closed'),(10,10,'Evans Criminal Defense','Criminal','05-03-2024','01-05-2024'),(11,11,'Cook Corporate Litigation','Corporate','10-03-2024','15-05-2024'),(12,12,'Hughes Family Law Matter','Family','15-03-2024','01-06-2024'),(13,13,'Bennett Immigration Case','Immigration','20-03-2024','30-04-2024'),(14,14,'Phillips Labor Dispute','Labor','01-04-2024','20-05-2024'),(15,15,'Kim Real Estate Transaction','Real Estate','10-04-2024','15-06-2024'),(16,16,'trial 2 case','Real Estate','2024-08-03','Not Closed'),(17,1,'2nd trial','Real Estate','2024-08-03','Not Closed');
/*!40000 ALTER TABLE `cases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `client_ID` int NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `contact_no` varchar(50) NOT NULL,
  `specialization` varchar(30) NOT NULL,
  PRIMARY KEY (`client_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'Andrew','Tate','123-456-7820','Criminal'),(2,'Shubhankar','Mishra','123-456-7890','Criminal'),(3,'Sophia','Walker	','789-012-3456','Corporate'),(4,'Alexander','Hill','234-567-8901','Family'),(5,'Olivia','Hayes','567-890-1234','Immigration'),(6,'Benjamin','Wright','890-123-4567','Labor'),(7,'Isabella','Turner','345-678-9012','Real Estate'),(8,'Ethan','Scott','678-901-2345','Tax'),(9,'Mia','Parker','901-234-5678','Civil'),(10,'Charlotte','Evans','432-109-8765','Criminal'),(11,'Noah','Evans','109-876-5432','Corporate'),(12,'Amelia','Hughes','876-543-2109','Family'),(13,'Elijah','Bennett	','321-098-7654','Immigration'),(14,'Harper','Phillips','654-321-0987','Labor'),(15,'Michael','Kim','987-654-3210','Real Estate'),(16,'Shubhankar','Mishra','123-456-7890','Real Estate');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `court`
--

DROP TABLE IF EXISTS `court`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `court` (
  `court_ID` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `court_type` text NOT NULL,
  `location` text NOT NULL,
  PRIMARY KEY (`court_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `court`
--

LOCK TABLES `court` WRITE;
/*!40000 ALTER TABLE `court` DISABLE KEYS */;
INSERT INTO `court` VALUES (1,'Roosevelt Court','Supreme','Washington, D.C.'),(2,'Swiss County','Trial','Swiss'),(3,'Liberty Court','Circuit','New York City'),(4,'Magnolia Court','Superior','Los Angeles'),(5,'Harborview Court','County','Seattle'),(6,'Cypress Court','Municipal','Miami'),(7,'Summit Court','Appellate','Denver'),(8,'Oakwood Court','Federal','Atlanta'),(9,'Riverside Court','Appeals','Boston'),(10,'Maplewood Court','Juvenile','San Francisco'),(11,'Sycamore Court','Probate','Dallas'),(12,'Pinehurst Court','Family','Houston'),(13,'Evergreen Court','Traffic','Portland'),(14,'Cedarwood Court','Bankruptcy','Philadelphia'),(15,'Swiss County','Criminal','IIT');
/*!40000 ALTER TABLE `court` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document`
--

DROP TABLE IF EXISTS `document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `document` (
  `document_ID` int NOT NULL AUTO_INCREMENT,
  `document_type` text NOT NULL,
  `document_content` text NOT NULL,
  PRIMARY KEY (`document_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document`
--

LOCK TABLES `document` WRITE;
/*!40000 ALTER TABLE `document` DISABLE KEYS */;
INSERT INTO `document` VALUES (1,'Trial','This is just a trial for the web app...'),(2,'Case Memo','Regarding the criminal case of Michael Clark, we propose a plea deal to reduce the charges...'),(3,'Contract','Contract between Sophia Walker and XYZ Corporation for the provision of legal services...'),(4,'Affidavit','Affidavit of Alexander Hill in the family court case against his ex-spouse...'),(5,'Petition','Petition filed by Olivia Hayes for asylum due to persecution in her home country...'),(6,'Legal Opinion','Legal opinion on labor laws provided to Benjamin Wright\'s company regarding employee rights...'),(7,'Settlement','Settlement agreement between Isabella Turner and the real estate developer...'),(8,'Tax Return','Tax return filing prepared by Emily Scott for Ethan Taylor...'),(9,'Lawsuit','Mia Parker\'s lawsuit against her former employer for wrongful termination...'),(10,'Property Deed','Deed for a property purchased by Charlotte Evans...'),(11,'Witness Statement','Witness statement of Noah Cook in a family court matter...'),(12,'Immigration Petition','Immigration petition submitted by Amelia Hughes for her spouse...'),(13,'Labor Agreement','Labor agreement negotiated by Elijah Bennett\'s union...'),(14,'Court Order','Court order granting custody to Harper Phillips in a family law case...'),(15,'Trial','this is another trial');
/*!40000 ALTER TABLE `document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lawyer`
--

DROP TABLE IF EXISTS `lawyer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lawyer` (
  `lawyer_ID` int NOT NULL AUTO_INCREMENT,
  `first_name` text NOT NULL,
  `last_name` text NOT NULL,
  `contact_no` text NOT NULL,
  `department` text NOT NULL,
  PRIMARY KEY (`lawyer_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lawyer`
--

LOCK TABLES `lawyer` WRITE;
/*!40000 ALTER TABLE `lawyer` DISABLE KEYS */;
INSERT INTO `lawyer` VALUES (1,'Shubhankar','Mishra','123-456-7890','Criminal'),(2,'Alice','Johnson','456-789-0123','Criminal'),(3,'Robert','Brown','789-012-3456','Corporate'),(4,'Emily','Davis','234-567-8901','Family'),(5,'Michael','Wilson','567-890-1234','Immigration'),(6,'Sarah','Martinez','890-123-4567','Labor'),(7,'David','Anderson','345-678-9012','Real Estate'),(8,'Jennifer','Taylor','678-901-2345','Tax'),(9,'James','Garcia','901-234-5678','Civil'),(10,'Jessica','Rodriguez','432-109-8765','Criminal'),(11,'Matthew','Lee','109-876-5432','Corporate'),(12,'Amanda','White','876-543-2109','Family'),(13,'Daniel','Perez','321-098-7654','Immigration'),(14,'Samantha','Nguyen','654-321-0987','Labor'),(15,'Shubhankar','Mishra','123-456-7890','Criminal');
/*!40000 ALTER TABLE `lawyer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `participates`
--

DROP TABLE IF EXISTS `participates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `participates` (
  `case_ID` int NOT NULL,
  `client_ID` int NOT NULL,
  PRIMARY KEY (`case_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participates`
--

LOCK TABLES `participates` WRITE;
/*!40000 ALTER TABLE `participates` DISABLE KEYS */;
/*!40000 ALTER TABLE `participates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_ID` int NOT NULL AUTO_INCREMENT,
  `First_name` text NOT NULL,
  `last_name` text NOT NULL,
  `email` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  PRIMARY KEY (`user_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Shubhankar','Mishra','mishrashubhankar8@gmail.com',' smishra23','#shubhi8'),(2,'Susan','Vass','Susan_Vass9057@avn7d.store','Vass Susan','	#FFC0CB'),(3,'Liam','Roberts','Liam_Roberts2744@dvqq2.space','Roberts Liam','#468c89'),(4,'Irene','Power','Irene_Power8752@bqkv0.site','Power Irene','	#FFA500'),(5,'Scarlett','Tait','Scarlett_Tait5321@c2nyu.media','Tait Scarlett','	#C0C0C0'),(6,'Cadence','Goodman','Cadence_Goodman4334@lyvnc.website','Goodman Cadence','#468748'),(7,'Erick','Adams','Erick_Adams7292@chkzl.auction','Adams Erick','#e5c427'),(8,'Daron','Rowe','Daron_Rowe1962@3wbkp.site','Rowe Daron','	#00FFFF'),(9,'Julius','Gregory','Julius_Gregory1180@chkzl.net','Gregory Julius','#468748'),(10,'Maxwell','Gavin','Maxwell_Gavin5232@lyvnc.center','Gavin Maxwell','#7d8ca3'),(11,'Logan','Thomson','Logan_Thomson3475@dbxli.ca','Thomson Logan','#144187'),(12,'Bryce','Nobbs','Bryce_Nobbs1734@mpibr.shop','Nobbs Bryce','#468c89'),(13,'Roger','Russel','Roger_Russel3047@6ijur.pro','Russel Roger','#9e0806'),(14,'Johnny','Hope','Johnny_Hope2539@iaart.name','Hope Johnny','	#FFC0CB'),(15,'Shubhankar','Mishra','mishrashubhankar8@gmail.com',' smishra23','#FDCSGA');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-21  8:16:34
