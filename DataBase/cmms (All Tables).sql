-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: cmms
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `name` varchar(45) NOT NULL,
  `floor` int NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('Catheter',3),('Clinics',2),('Dialysis Unit',0),('Emergency',0),('ICU',3),('Labs',2),('Operations',1),('Radiology',0),('Recovery',1),('Sterilization Unit',2);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engineer`
--

DROP TABLE IF EXISTS `engineer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engineer` (
  `ssn` varchar(45) NOT NULL,
  `eng_name` varchar(45) NOT NULL,
  `eng_phone` varchar(45) NOT NULL,
  `eng_email` varchar(45) NOT NULL,
  `equip_sn` varchar(45) NOT NULL,
  `v_ssn` varchar(45) NOT NULL,
  PRIMARY KEY (`ssn`),
  UNIQUE KEY `ssn_UNIQUE` (`ssn`),
  KEY `equip_sn_idx` (`equip_sn`),
  KEY `v_ssn_idx` (`v_ssn`),
  CONSTRAINT `equip_sn` FOREIGN KEY (`equip_sn`) REFERENCES `equipment` (`serial_number`),
  CONSTRAINT `v_ssn` FOREIGN KEY (`v_ssn`) REFERENCES `vendor` (`vendor_ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engineer`
--

LOCK TABLES `engineer` WRITE;
/*!40000 ALTER TABLE `engineer` DISABLE KEYS */;
INSERT INTO `engineer` VALUES ('28701300103669','Emam','1023242901','engemam30@gmail.com','E7','29012010102837'),('28801249012345','Mohamed','1023864012','engmohamed24@gmail.com','E10','28809200100348'),('28811220100094','Hadeer','1090923902','enghadeer22@gmail.com','E2','29012010102837'),('28903230103673','Eslam','1123486201','engeslam23@gmail.com','E12','28904280109832'),('28904261876372','Ahmed','1092347182','engahmed26@gmail.com','E0','28705300103679'),('28905160102436','Ibrahem','1004932817','engibrahem16@gmail.com','E19','28910220103842'),('28907120100273','Adham','1123409577','engadham12@gmail.com','E2','29009150101208'),('28910010102223','Ghidaa','1029122234','engghidaa01@gmail.com','E1','29009150101208'),('29002150107284','Sayed','1093840213','engsayed15@gmail.com','E17','28906230100899'),('29003140109442','Hanaa','1124293014','enghanaa14@gmail.com','E14','29103120102938'),('29009110101208','Khaled','1220203945','engkhaled11@gmail.com','E6','29103120102938'),('29103250100362','Mostafa','1229831724','engmostafa25@gmail.com','E20','28908160101836');
/*!40000 ALTER TABLE `engineer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `serial_number` varchar(45) NOT NULL,
  `equipment_name` varchar(45) NOT NULL,
  `equipment_code` varchar(45) NOT NULL,
  `portable` varchar(45) NOT NULL,
  `work_time` datetime NOT NULL,
  `insurance` datetime NOT NULL,
  `maintenance` datetime NOT NULL,
  `price` int NOT NULL,
  `cat_name` varchar(45) NOT NULL,
  PRIMARY KEY (`serial_number`),
  UNIQUE KEY `serial number_UNIQUE` (`serial_number`),
  KEY `cat name_idx` (`cat_name`),
  CONSTRAINT `cat_name` FOREIGN KEY (`cat_name`) REFERENCES `category` (`name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES ('E0','Anesthesia Machine','0000','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',50000,'Recovery'),('E00','Anesthesia Machine','0000','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',55000,'Recovery'),('E1','Monitors','0001','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',10000,'Recovery'),('E10','Beds','0010','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',2000,'Recovery'),('E1010','Beds','0010','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',2500,'Recovery'),('E11','Anesthesia Machine','0000','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',50000,'Operations'),('E1111','Anesthesia Machine','0000','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',55000,'Operations'),('E12','Monitors','0001','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',10000,'Operations'),('E13','Electric Suction','0010','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',1000,'Operations'),('E14','Operation Table','0011','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',200,'Operations'),('E15','Surgical Lights','0003','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',250,'Operations'),('E16','Tourniquet','0012','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',50,'Operations'),('E17','Syringe Pump','0013','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',5000,'Operations'),('E1717','Syringe Pump','0013','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',6000,'Operations'),('E18','C Arm','0014','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',30000,'Operations'),('E19','Defibrillators','0004','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',80000,'Operations'),('E2','Ultrasound Equipment','0002','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',100000,'Recovery'),('E20','Hemodialysis','0014','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',85000,'Dialysis Unit'),('E2020','Hemodialysis','0014','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',90000,'Dialysis Unit'),('E21','Beds','0010','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',2000,'ICU'),('E2121','Beds','0010','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',2500,'ICU'),('E22','Monitors','0001','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',10000,'ICU'),('E23','Ventiltors','0007','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',85000,'ICU'),('E24','Endotracheal Tube','0015','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',500,'ICU'),('E25','Intravenous Infusion Pump','0016','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',5500,'ICU'),('E26','Syringe Pump','0013','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',5000,'ICU'),('E2626','Syringe Pump','0013','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',6000,'ICU'),('E27','Nasogastric Tubes','0017','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',500,'ICU'),('E28','Indwelling Urinary Catheter','0018','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',3000,'ICU'),('E29','Pulse Oximeter','0019','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',1000,'ICU'),('E3','Surgical Lights','0003','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',250,'Recovery'),('E30','Ultrasonography Machine','0020','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',150000,'Radiology'),('E31','X Ray','0021','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',200000,'Radiology'),('E32','Echocardiography Machine','0022','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',150000,'Radiology'),('E33','CT Scan','0023','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',150000,'Radiology'),('E34','MRI','0024','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',200000,'Radiology'),('E35','Linear Accelerator','0025','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',100000,'Radiology'),('E36','PET Scan','0026','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',120000,'Radiology'),('E37','Interventional Radiology','0027','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',145000,'Radiology'),('E38','Lead Shielding','0028','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',10000,'Radiology'),('E39','Autoclave','0029','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',5000,'Labs'),('E4','Defibrillators','0004','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',80000,'Recovery'),('E40','Microscope','0030','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',2000,'Labs'),('E41','Centrifuges','0031','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',3000,'Labs'),('E42','Thermal cyclers (PCR)','0032','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',300,'Labs'),('E43','Refrigerators and Freezers','0033','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',30000,'Labs'),('E44','Humidifier','0034','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',15000,'Labs'),('E45','Incubators','0035','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',150000,'Operations'),('E46','Incubators','0035','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',150000,'ICU'),('E47','Defibrillators','0004','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',80000,'Emergency'),('E48','ECG','0036','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',50000,'Emergency'),('E49','Diathermy','0037','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',70000,'Emergency'),('E5','Endoscopy Equipment','0005','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',90000,'Recovery'),('E6','EKG Machines','0006','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',45000,'Recovery'),('E7','Ventilators','0007','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',80000,'Recovery'),('E77','Ventilators','0007','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',85000,'Recovery'),('E8','Sterilizers','0008','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',5000,'Recovery'),('E88','Sterilizers','0008','Yes','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',5000,'Recovery'),('E9','Stretchers','0009','No','2020-03-23 08:30:00','2020-09-30 12:00:00','2020-04-23 04:00:00',150,'Recovery');
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment_installation`
--

DROP TABLE IF EXISTS `equipment_installation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment_installation` (
  `Equ_SN` varchar(45) NOT NULL,
  `Equ_Name` varchar(45) NOT NULL,
  `Equ_Code` varchar(45) NOT NULL,
  `catName` varchar(45) NOT NULL,
  `techName` varchar(45) NOT NULL,
  `installation_time` datetime NOT NULL,
  `equipment_model` varchar(45) NOT NULL,
  PRIMARY KEY (`Equ_SN`),
  UNIQUE KEY `Equ_SN_UNIQUE` (`Equ_SN`),
  KEY `catName_idx` (`catName`),
  CONSTRAINT `catName` FOREIGN KEY (`catName`) REFERENCES `category` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment_installation`
--

LOCK TABLES `equipment_installation` WRITE;
/*!40000 ALTER TABLE `equipment_installation` DISABLE KEYS */;
INSERT INTO `equipment_installation` VALUES ('E0','Anesthesia Machine','0000','Recovery','Kholod','2020-03-23 10:00:00','Philips'),('E00','Anesthesia Machine','0000','Recovery','Toaa','2020-03-23 10:00:00','Philips'),('E1','Monitors','0001','Recovery','Gaser','2020-03-23 10:00:00','GE'),('E10','Beds','0010','Recovery','Fathy','2020-03-23 10:00:00','3A'),('E30','Ultrasonography Machine','0020','Radiology','Belal','2020-03-23 10:00:00','Siemens'),('E31','X Ray','0021','Radiology','Renad','2020-03-23 10:00:00','Siemens'),('E32','Echocardiography Machine','0022','Radiology','Dina','2020-03-23 10:00:00','Physio-Control'),('E33','CT Scan','0023','Radiology','Nour','2020-03-23 10:00:00','Siemens'),('E34','MRI','0024','Radiology','Wael','2020-03-23 10:00:00','Siemens'),('E36','PET Scan','0026','Radiology','Ester','2020-03-23 10:00:00','Philips'),('E39','Autoclave','0029','Labs','Anas','2020-03-23 10:00:00','Fresenius Vial'),('E40','Microscope','0030','Labs','Omar','2020-03-23 10:00:00','Fresenius Vial'),('E41','Centrifuges','0031','Labs','Mario','2020-03-23 10:00:00','Fresenius Vial'),('E43','Refrigerators and Freezers','0033','Labs','Hashim','2020-03-23 10:00:00','Fresenius Vial'),('E44','Humidifier','0034','Labs','Mohamed','2020-03-23 10:00:00','H003-A');
/*!40000 ALTER TABLE `equipment_installation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment_ppm`
--

DROP TABLE IF EXISTS `equipment_ppm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment_ppm` (
  `EQU_SN` varchar(45) NOT NULL,
  `EQU_NAME` varchar(45) NOT NULL,
  `EQU_CODE` varchar(45) NOT NULL,
  `CATEGORY` varchar(45) NOT NULL,
  `technician_name` varchar(45) NOT NULL,
  `ppm_time` datetime NOT NULL,
  `ppm_year` int NOT NULL,
  `ERROR` varchar(45) NOT NULL,
  PRIMARY KEY (`EQU_SN`),
  UNIQUE KEY `EQU_SN_UNIQUE` (`EQU_SN`),
  KEY `category_idx` (`CATEGORY`),
  CONSTRAINT `category` FOREIGN KEY (`CATEGORY`) REFERENCES `category` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment_ppm`
--

LOCK TABLES `equipment_ppm` WRITE;
/*!40000 ALTER TABLE `equipment_ppm` DISABLE KEYS */;
INSERT INTO `equipment_ppm` VALUES ('E0','Anesthesia Machine','0000','Recovery','Yehia','2020-05-05 03:30:00',20,'None'),('E1','Monitors','0001','Operations','Adel','2020-05-06 03:30:00',21,'Power Cable Failure'),('E10','Beds','0010','Recovery','Farouk','2020-05-10 01:30:00',10,'Automatic Not Response'),('E20','Hemodialysis','0014','Dialysis Unit','Emad','2020-06-01 03:30:00',10,'Filter'),('E21','Beds','0010','ICU','Marwa','2020-05-10 01:30:00',12,'None'),('E2121','Beds','0010','ICU','Nagham','2020-05-10 02:30:00',12,'None'),('E22','Monitors','0001','ICU','Menna','2020-05-11 02:30:00',17,'None'),('E23','Ventiltors','0007','ICU','Ismael','2020-06-11 02:30:00',19,'Tube Error'),('E24','Endotracheal Tube','0015','ICU','Sally','2020-05-18 05:30:00',15,'None'),('E25','Intravenous Infusion Pump','0016','ICU','Mahdy','2020-05-20 12:30:00',22,'None'),('E26','Syringe Pump','0013','ICU','Tamer','2020-06-02 03:30:00',12,'Leakage'),('E2626','Syringe Pump','0013','ICU','Galal','2020-05-08 12:30:00',25,'None'),('E27','Nasogastric Tubes','0017','ICU','Omar','2020-06-08 12:30:00',10,'None'),('E28','Indwelling Urinary Catheter','0018','ICU','Salma','2020-06-01 10:30:00',16,'None'),('E29','Pulse Oximeter','0019','ICU','Hesham','2020-05-12 11:30:00',8,'Sensor Failure'),('E31','X Ray','0021','Radiology','Mona','2020-05-30 03:30:00',18,'None'),('E7','Ventilators','0007','Recovery','Ghada','2020-06-07 03:30:00',22,'Reading'),('E9','Stretchers','0009','Recovery','Beshoy','2020-05-07 03:30:00',15,'None');
/*!40000 ALTER TABLE `equipment_ppm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment_repair`
--

DROP TABLE IF EXISTS `equipment_repair`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment_repair` (
  `equip_serial` varchar(45) NOT NULL,
  `equip_name` varchar(45) NOT NULL,
  `equip_code` varchar(45) NOT NULL,
  `Categ_Name` varchar(45) NOT NULL,
  `error` varchar(45) NOT NULL,
  `fixed` varchar(45) NOT NULL,
  `technician_name` varchar(45) NOT NULL,
  `repair_time` datetime NOT NULL,
  `repair_type` varchar(45) NOT NULL,
  `cost` int NOT NULL,
  PRIMARY KEY (`equip_serial`),
  UNIQUE KEY `equip_sn_UNIQUE` (`equip_serial`),
  KEY `cat_name_idx` (`Categ_Name`),
  CONSTRAINT `Categ_Name` FOREIGN KEY (`Categ_Name`) REFERENCES `category` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment_repair`
--

LOCK TABLES `equipment_repair` WRITE;
/*!40000 ALTER TABLE `equipment_repair` DISABLE KEYS */;
INSERT INTO `equipment_repair` VALUES ('E1','Monitors','0001','Operations','Power Cable Failure','Yes','Esraa','2020-05-07 10:00:00','Change of Power Cable',100),('E10','Beds','0010','Recovery','Automatic Not Response','Yes','Mina','2020-05-11 10:00:00','Change Automatic System',250),('E20','Hemodialysis','0014','Dialysis Unit','Filter','Yes','Amany','2020-06-02 10:00:00','Replace Filter',150),('E23','Ventiltors','0007','ICU','Tube Error','Yes','Ebram','2020-06-12 10:00:00','Change Tube',50),('E26','Syringe Pump','0013','ICU','Leakage','Yes','Mourad','2020-06-03 10:00:00','New Syringe',150),('E29','Pulse Oximeter','0019','ICU','Sensor Failure','Yes','Tasneem','2020-05-13 10:00:00','New Sensor',50),('E7','Ventiltors','0007','Recovery','Reading','No','Martina','2020-06-08 10:00:00','Replacement',80000);
/*!40000 ALTER TABLE `equipment_repair` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `installation_save`
--

DROP TABLE IF EXISTS `installation_save`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `installation_save` (
  `E_SN` varchar(45) NOT NULL,
  `E_Name` varchar(45) NOT NULL,
  `E_Code` varchar(45) NOT NULL,
  `C_Name` varchar(45) NOT NULL,
  `T_Name` varchar(45) NOT NULL,
  `I_Time` datetime NOT NULL,
  `E_Model` varchar(45) NOT NULL,
  PRIMARY KEY (`E_SN`),
  UNIQUE KEY `E_SN_UNIQUE` (`E_SN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `installation_save`
--

LOCK TABLES `installation_save` WRITE;
/*!40000 ALTER TABLE `installation_save` DISABLE KEYS */;
/*!40000 ALTER TABLE `installation_save` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ppm_save`
--

DROP TABLE IF EXISTS `ppm_save`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ppm_save` (
  `EquipmentSN` varchar(45) NOT NULL,
  `EquipmentName` varchar(45) NOT NULL,
  `EquipmentCode` varchar(45) NOT NULL,
  `CatName` varchar(45) NOT NULL,
  `TechName` varchar(45) NOT NULL,
  `ppmTime` datetime NOT NULL,
  `ppmYear` int NOT NULL,
  `ppmError` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ppm_save`
--

LOCK TABLES `ppm_save` WRITE;
/*!40000 ALTER TABLE `ppm_save` DISABLE KEYS */;
/*!40000 ALTER TABLE `ppm_save` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair_save`
--

DROP TABLE IF EXISTS `repair_save`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_save` (
  `Equipment_SN` varchar(45) NOT NULL,
  `Equipment_Name` varchar(45) NOT NULL,
  `Equipment_Code` varchar(45) NOT NULL,
  `Cat_Name` varchar(45) NOT NULL,
  `Equ_Error` varchar(45) NOT NULL,
  `Fixed/Not` varchar(45) NOT NULL,
  `Tech_Name` varchar(45) NOT NULL,
  `Reapir_Time` datetime NOT NULL,
  `Repair_Type` varchar(45) NOT NULL,
  `Repair_Cost` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_save`
--

LOCK TABLES `repair_save` WRITE;
/*!40000 ALTER TABLE `repair_save` DISABLE KEYS */;
/*!40000 ALTER TABLE `repair_save` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idusers_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'mostafa','mustafayehia4@gmail.com','MUSTAFA!'),(2,'ibrahem','ibrahemelsayed4@gmail.com','DARSH1999'),(3,'ahmed','ahmed4@gmail.com','mou23');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor`
--

DROP TABLE IF EXISTS `vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendor` (
  `vendor_ssn` varchar(45) NOT NULL,
  `vendor_name` varchar(45) NOT NULL,
  `vendor_phone` varchar(45) NOT NULL,
  `vendor_email` varchar(45) NOT NULL,
  PRIMARY KEY (`vendor_ssn`),
  UNIQUE KEY `v ssn_UNIQUE` (`vendor_ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor`
--

LOCK TABLES `vendor` WRITE;
/*!40000 ALTER TABLE `vendor` DISABLE KEYS */;
INSERT INTO `vendor` VALUES ('28705300103679','Ghaly','1098974632','engghaly30@gmail.com'),('28804260102384','Gehad','1020723528','enggehad26@gmail.com'),('28809200100348','Inas','1123975162','enginas20@gmail.com'),('28904280109832','Eman','1225767429','engeman28@gmail.com'),('28905270102847','Youssef','1099392012','engyoussef27@gmail.com'),('28906230100899','Kamal','1220908043','engkamal23@gmail.com'),('28908160101836','Bassam','1112309466','engbassam16@gmail.com'),('28910220103842','Karem','1029093475','engkarem22@gmail.com'),('29001180103480','Samar','1118363524','engsamar18@gmail.com'),('29009150101208','Gamel','1142837490','enggamel15@gmail.com'),('29012010102837','Abdullah','1009836428','engabdullah01@gmail.com'),('29103120102938','Shymaa','1000923129','engshymaa12@gmail.com');
/*!40000 ALTER TABLE `vendor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-10 16:55:57
