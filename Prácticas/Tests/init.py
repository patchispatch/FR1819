import sqlite3
conn = sqlite3.connect('formulario.db')

c = conn.cursor()

c.execute('''
-- MySQL Script generated by MySQL Workbench
-- mié 19 dic 2018 19:34:20 CET
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema formularios
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema formularios
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `formularios` DEFAULT CHARACTER SET utf8 ;
USE `formularios` ;

-- -----------------------------------------------------
-- Table `formularios`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `formularios`.`Usuarios` (
  `user` VARCHAR(45) NOT NULL,
  `password` TINYTEXT NOT NULL,
  `is_admin` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`user`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `formularios`.`Formularios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `formularios`.`Formularios` (
  `nombre` VARCHAR(45) NOT NULL,
  `pregunta` TINYTEXT NULL,
  `respuesta1` TINYTEXT NULL,
  `respuesta2` TINYTEXT NULL,
  `respuesta3` TINYTEXT NULL,
  `respuesta4` TINYTEXT NULL,
  PRIMARY KEY (`nombre`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
''')

conn.commit()
conn.close()
