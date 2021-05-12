CREATE DATABASE  IF NOT EXISTS `llbot` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `llbot`;
-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: llbot
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `fosbank`
--

DROP TABLE IF EXISTS `fosbank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fosbank` (
  `id` int(11) NOT NULL,
  `keyword` varchar(45) DEFAULT NULL,
  `s_i` varchar(45) DEFAULT NULL,
  `FoS` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fosbank`
--

LOCK TABLES `fosbank` WRITE;
/*!40000 ALTER TABLE `fosbank` DISABLE KEYS */;
INSERT INTO `fosbank` VALUES (0,'beautiful','S','like a flower'),(1,'easy','I','piece of cake'),(2,'tough','S','as a tiger'),(3,'happy','I','on cloud nine'),(4,'fierce','S','as a tiger'),(5,'small','S','as a mouse'),(6,'depressed','I','down in the dumps'),(7,'leave','I','hit the road'),(8,'busy','S','as a bee'),(9,'smart','S','as a fox'),(10,'fight','S','like a lion'),(11,'clear','S','as a crystal'),(12,'hard','S','as a rock'),(13,'best','I','second to none'),(14,'innocent','S','as a lamb'),(15,'rich','I','born with a silver spoon'),(16,'cold (or cool)','S','as ice'),(17,'strong','S','as an ox (or a bull)'),(18,'sleep','I','hit the sack'),(19,'study','I','hit the books'),(20,'(very) happy  ecstatic','I','over the moon'),(21,'lazy','I','couch potato'),(22,'exercise','I','get in shape'),(23,'stupid','I','birdbrain'),(24,'quick','S','as lightning'),(25,'tall','S','as a giraffe'),(26,'wise','S','like an owl'),(27,'sad','I','with a heavy heart'),(28,'small','S','as an ant'),(29,'pretty','I','a dreamboat'),(30,'handsome','I','a dreamboat'),(31,'scared','I','chickened out'),(32,'unclear','I','a grey area'),(33,'playful','S','as a kitten'),(34,'quit','I','call it a day'),(35,'try','I','give it a shot'),(36,'eat','I','pig out'),(37,'expensive','I','cost an arm and leg'),(38,'agree','I','see eye to eye'),(39,'hot','S','as fire'),(40,'smooth','S','as porcelain'),(41,'sly','S','as a fox'),(42,'brave','S','as a lion'),(43,'deep','S','as the ocean'),(44,'ate','S','like a pig'),(45,'ignore','I','give a cold shoulder'),(46,'hard','S','as nails'),(47,'mad','S','as a hornet'),(48,'white','S','as snow'),(49,'blue','S','as the sea'),(50,'annoying','S','like a mosquito'),(51,'different','S','as night and day'),(52,'healthy','I','fit as a fiddle'),(53,'careful','I','throwing caution to the wind'),(54,'ruined','I','bombed'),(55,'hot','S','as the sun'),(56,'sharp','S','as a razor'),(57,'light','S','as a feather'),(58,'quiet','S','as a mouse'),(59,'cry','S','like a baby'),(60,'shiny','S','as gold'),(61,'dry','S','a bone'),(62,'red','S','as a ruby'),(63,'glad','I','tickled pink'),(64,'simple','I','not exactly rocket science'),(65,'amazed','I','bug-eyed'),(66,'warning','I','slap on the wrist'),(67,'listening','I','all-ears'),(68,'comfortable','I','bed of roses'),(69,'enjoy','I','have a blast'),(70,'bright','S','as a button'),(71,'sweet','S','as sugar'),(72,'raining hard','I','raining cats and dogs'),(73,'good luck','I','break a leg');
/*!40000 ALTER TABLE `fosbank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessonresponse`
--

DROP TABLE IF EXISTS `lessonresponse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lessonresponse` (
  `id` int(11) NOT NULL,
  `resp_type` longtext NOT NULL,
  `dialogue_template` varchar(500) NOT NULL,
  `dialogue_code` varchar(45) NOT NULL,
  `lessonID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `lessonId_idx` (`lessonID`),
  CONSTRAINT `lessonId` FOREIGN KEY (`lessonID`) REFERENCES `lessons` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessonresponse`
--

LOCK TABLES `lessonresponse` WRITE;
/*!40000 ALTER TABLE `lessonresponse` DISABLE KEYS */;
INSERT INTO `lessonresponse` VALUES (0,'intro_yes','That is great to know Now just to refresh your memory\r','GEN',NULL),(1,'intro_no','That’s okay! Let me tell you about it. \r \r \r First, let me define the terms for you.\r','GEN',NULL),(2,'intro_alittle','That’s okay! Let me refresh your memory:','GEN',NULL),(3,'term1','What is a Subject?','SVA',1),(4,'term1','A subject is the one being talked about in a Sentence','SVA',1),(5,'term2','What is a Verb?','SVA',1),(6,'term2','A verb is a word that talks about the subject','SVA',1),(7,'main','\"Since the terms are now clear,  let me talk about Subject-Verb Agreement (SVA).\n\nSVA says that subjects and verbs must AGREE with one another in number (singular or plural):\nif a subject is singular, its verb must also be singular; if a subject is plural, its verb must also be plural.\n\n\"','SVA',1),(8,'ex','\"If the subject is singular, the verb must be singular too.\nExample: She writes every day.\n\"','SVA',1),(9,'ex','\"If the subject is plural, the verb must also be plural.\nExample: They write every day.\n\"','SVA',1),(10,'ex','\"When the subject of the sentence is composed of two or more nouns or pronouns connected by and, use a plural verb.\nExample: The doctoral student and the committee members write every day.\n\n\"','SVA',1),(11,'ex','\"When there is one subject and more than one verb, the verbs throughout the sentence must agree with the subject.\nExample: Interviews are one way to collect data and allow researchers to gain an in-depth understanding of participants.\n\"','SVA',1),(12,'ex','\"When a phrase comes between the subject and the verb, remember that the verb still agrees with the subject, not the noun or pronoun in the phrase following the subject of the sentence.\nExample: The student, as well as the committee members, is excited.\n\"','SVA',1),(13,'ex','\"When two or more singular nouns or pronouns are connected by \"\"or\"\" or \"\"nor,\"\" use a singular verb.\nExample: The chairperson or the CEO approves the proposal before proceeding.\"','SVA',1),(14,'ex','\"When a compound subject contains both a singular and a plural noun or pronoun joined by \"\"or\"\" or \"\"nor,\"\" the verb should agree with the part of the subject that is closest to the verb. This is also called the rule of proximity.\nExample: The student or the committee members write every day.\nExample: The committee members or the student writes every day.\n\n\"','SVA',1),(15,'ex','\"The words and phrases \"\"each,\"\" \"\"each one,\"\" \"\"either,\"\" \"\"neither,\"\" \"\"everyone,\"\" \"\"everybody,\"\" \"\"anyone,\"\" \"\"anybody,\"\" \"\"nobody,\"\" \"\"somebody,\"\" \"\"someone,\"\" and \"\"no one\"\" are singular and require a singular verb.\nExample: Each of the participants was willing to be recorded.\nExample: Neither alternative hypothesis was accepted.\nExample: I will offer a $5 gift card to everybody who participates in the study.\nExample: No one was available to meet with me at the preferred times.\n\"','SVA',1),(16,'ex','\"Noncount nouns take a singular verb.\nExample: Education is the key to success.\nExample: Diabetes affects many people around the world.\nExample: The information obtained from the business owners was relevant to include in the study.\nExample: The research I found on the topic was limited.\n\"','SVA',1),(17,'ex','\" Some countable nouns in English such as earnings, goods, odds, surroundings, proceeds, contents, and valuables only have a plural form and take a plural verb.\nExample: The earnings for this quarter exceed expectations.\nExample: The proceeds from the sale go to support the homeless population in the city.\nExample: Locally produced goods have the advantage of shorter supply chains\n\"','SVA',1),(18,'ex','\"In sentences beginning with \"\"there is\"\" or \"\"there are,\"\" the subject follows the verb. Since \"\"there\"\" is not the subject, the verb agrees with what follows the verb.\nExample: There is little administrative support.\nExample: There are many factors affecting teacher retention.\n\"','SVA',1),(19,'ex','\"Collective nouns are words that imply more than one person but are considered singular and take a singular verb. Some examples are \"\"group,\"\" \"\"team,\"\" \"\"committee,\"\" \"\"family,\"\" and \"\"class.\"\"\nExample: The group meets every week.\nExample: The committee agrees on the quality of the writing.\n\"','SVA',1),(20,'term1','\"What is an order?\"','OOA',2),(21,'term1','An order is the arrangement of things','OOA',2),(22,'term2','What is an adjective?\r ','OOA',2),(23,'term2','An adjective is a word that describes nouns','OOA',2),(24,'main','\"Since the terms are now clear, let me talk about Order of Adjectives (OOA).\n\nOOA says that when more than one adjective comes before a noun, the adjectives are normally in a particular order. Adjectives which describe opinions or attitudes usually come first, before more neutral, factual ones. \nHere is a list of the most usual sequence of adjectives:\n\n1. QUANTITY   \n2. OPINION   \n3. SIZE           \n4. AGE         \n5. SHAPE       \n6. COLOR      \n7. ORIGIN      \n8. MATERIAL   \n\"','OOA',2),(25,'ex','\"I saw Kresta carrying a huge, orange, wooden bookshelf.\n- size -> color -> material\n\"','OOA',2),(26,'ex','\"There are five large rectangular paintings inside our house.\n- quantity -> size -> shape\n\"','OOA',2),(27,'ex','\"I want to give you a beautiful large yellow paper sunflower.\n- opinion -> size -> color -> material\n\"','OOA',2),(28,'ex','\"We cooked creamy heart-shaped yema candies in school.\n- opinion -> shape\n\"','OOA',2),(29,'ex','\"Georgee lives with her fat old brown cat named Pepe.\n- opinion -> age -> color\n\"','OOA',2),(30,'term1','\"What is a Degree?\"','DOA',3),(31,'term1','A degree is a level or how intense something is','DOA',3),(32,'term2','\"What is an adjective?\"','DOA',3),(33,'term2','An adjective is a word that describes nouns','DOA',3),(34,'main','\"DOA says that adjectives are compared in different ways: positive, comparative and superlative. Adjectives form their comparative by adding ‘er’ at the end of the word or adding ‘more’ before the adjective, and their superlative by adding ‘est’ at the end of the word or adding ‘most’ before the adjective. \n\"','DOA',3),(35,'ex','\"The king is happy. \nThe queen is happier than the king. \nThe prince is the happiest among the three royalties.\n\"','DOA',3),(36,'ex','\"The blue T- shirt is cheap. \nThe red T- shirt is cheaper than the blue shirt. \nThe white T- shirt is the cheapest among the three T- shirts.\n\"','DOA',3),(37,'ex','\"The forest is far. \nThe castle is farther than the forest. \nThe lake is the farthest among the three.\n\"','DOA',3),(38,'ex','\"Bianca is famous. \nJohn is more famous than Bianca.\nKevin is the most famous of them all.\n\"','DOA',3),(39,'ex','\"Sarah is anxious. \nMathilda is more anxious than Sarah. \nRoger is the most anxious among all the students.\n\"','DOA',3),(40,'ask_ID','Hello! I am LLBOT. Do you have a Student ID?','GEN',NULL),(41,'ask_yes','What is your ID?','GEN',NULL),(42,'ask_no','What is your Name?','GEN',NULL);
/*!40000 ALTER TABLE `lessonresponse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessons`
--

DROP TABLE IF EXISTS `lessons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lessons` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lessonDesc` varchar(45) DEFAULT NULL,
  `lessonCode` varchar(45) DEFAULT NULL,
  `preReq` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons`
--

LOCK TABLES `lessons` WRITE;
/*!40000 ALTER TABLE `lessons` DISABLE KEYS */;
INSERT INTO `lessons` VALUES (1,'Subject Verb Agreement','SVA',0),(2,'Order of Adjectives','OOA',1),(3,'Degree of Adjectives','DOA',2);
/*!40000 ALTER TABLE `lessons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scores`
--

DROP TABLE IF EXISTS `scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentID` int(11) NOT NULL,
  `lessonID` int(11) NOT NULL,
  `score` int(11) DEFAULT NULL,
  `level` varchar(45) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `status_` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`,`studentID`,`lessonID`),
  KEY `fk_student_id_idx` (`studentID`),
  KEY `fk_lesson_id_idx` (`lessonID`),
  CONSTRAINT `fk_lesson_id` FOREIGN KEY (`lessonID`) REFERENCES `lessons` (`id`),
  CONSTRAINT `fk_student_id` FOREIGN KEY (`studentID`) REFERENCES `students` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scores`
--

LOCK TABLES `scores` WRITE;
/*!40000 ALTER TABLE `scores` DISABLE KEYS */;
/*!40000 ALTER TABLE `scores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-12  3:19:15
