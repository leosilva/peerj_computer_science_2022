-- MySQL dump 10.13  Distrib 8.0.31, for macos12.6 (x86_64)
--
-- Host: 127.0.0.1    Database: TwitterDataMining
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BigFiveResult`
--

DROP TABLE IF EXISTS `BigFiveResult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BigFiveResult` (
  `id` int NOT NULL AUTO_INCREMENT,
  `o_score` int NOT NULL,
  `c_score` int NOT NULL,
  `e_score` int NOT NULL,
  `a_score` int NOT NULL,
  `n_score` int DEFAULT NULL,
  `id_user` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `BigFiveResult_User_id_fk` (`id_user`),
  CONSTRAINT `BigFiveResult_User_id_fk` FOREIGN KEY (`id_user`) REFERENCES `User` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Tweet`
--

DROP TABLE IF EXISTS `Tweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tweet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_str_twitter` varchar(255) NOT NULL,
  `text` longtext NOT NULL,
  `created_at` datetime NOT NULL,
  `favorite_count` int NOT NULL,
  `retweet_count` int NOT NULL,
  `lang` varchar(10) NOT NULL,
  `id_user` int DEFAULT NULL,
  `vader_sentiment_analysis_score` float DEFAULT NULL,
  `vader_sentiment_analysis_polarity` text,
  `vader_sentiment_analysis_polarity_5_cat` text,
  `oplexicon_sentiment_analysis_score` float DEFAULT NULL,
  `oplexicon_sentiment_analysis_polarity` text,
  `oplexicon_sentiment_analysis_polarity_5_cat` text,
  `sentistrength_sentiment_analysis_score` float DEFAULT NULL,
  `sentistrength_sentiment_analysis_polarity` text,
  `sentistrength_sentiment_analysis_polarity_5_cat` text,
  `sentilexpt_sentiment_analysis_score` float DEFAULT NULL,
  `sentilexpt_sentiment_analysis_polarity` text,
  `sentilexpt_sentiment_analysis_polarity_5_cat` text,
  `liwc_sentiment_analysis_score` float DEFAULT NULL,
  `liwc_sentiment_analysis_polarity` text,
  `liwc_sentiment_analysis_polarity_5_cat` text,
  `final_score` float DEFAULT NULL,
  `final_score_ensemble` float DEFAULT NULL,
  `final_polarity` text,
  `final_polarity_ensemble` text,
  `text_updated` tinyint(1) DEFAULT '0',
  `is_retweet` tinyint(1) NOT NULL DEFAULT '0',
  `retweet_updated` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Tweet_id_str_twitter_uindex` (`id_str_twitter`),
  KEY `Tweet_User_id_fk` (`id_user`),
  CONSTRAINT `Tweet_User_id_fk` FOREIGN KEY (`id_user`) REFERENCES `User` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=229951 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_str_twitter` varchar(255) NOT NULL,
  `participant_id` int DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `screen_name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_id_twitter_account_uindex` (`id_str_twitter`),
  UNIQUE KEY `User_screen_name_uindex` (`screen_name`),
  UNIQUE KEY `User_participant_id_uindex` (`participant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-11 20:48:45
