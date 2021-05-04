--THIS FILE IS FOR MAKING THE TABLES--

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema llbot
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema llbot
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `llbot` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `llbot` ;

-- -----------------------------------------------------
-- Table `llbot`.`lessons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `llbot`.`lessons` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `lessonDesc` VARCHAR(45) NULL DEFAULT NULL,
  `lessonCode` VARCHAR(45) NULL DEFAULT NULL,
  `preReq` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `llbot`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `llbot`.`students` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `studentName` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `llbot`.`scores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `llbot`.`scores` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `studentID` INT(11) NOT NULL,
  `lessonID` INT(11) NOT NULL,
  `score` INT(11) NULL DEFAULT NULL,
  `level` VARCHAR(45) NULL DEFAULT NULL,
  `status` INT(11) NULL DEFAULT NULL,
  `status_` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `studentID`, `lessonID`),
  INDEX `fk_student_id_idx` (`studentID` ASC) VISIBLE,
  INDEX `fk_lesson_id_idx` (`lessonID` ASC) VISIBLE,
  CONSTRAINT `fk_lesson_id`
    FOREIGN KEY (`lessonID`)
    REFERENCES `llbot`.`lessons` (`id`),
  CONSTRAINT `fk_student_id`
    FOREIGN KEY (`studentID`)
    REFERENCES `llbot`.`students` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `llbot`.`FoSBank`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `llbot`.`FoSBank` (
  `id` INT NOT NULL,
  `keyword` VARCHAR(45) NULL,
  `s_i` VARCHAR(45) NULL,
  `FoS` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
