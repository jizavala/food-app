CREATE DATABASE `foodDB`;

CREATE TABLE `foodDB`.`foods`
(
  `id`           BIGINT        NOT NULL AUTO_INCREMENT COMMENT 'Primary key of the table, it serves to identify the id of the food',
  `protein`      DECIMAL(12,2) NOT NULL DEFAULT 0.00   COMMENT 'The quantity of protein the food contains',
  `fat`          DECIMAL(12,2) NOT NULL DEFAULT 0.00   COMMENT 'The quantity of fat the food contains',
  `carbohydrate` DECIMAL(12,2) NOT NULL DEFAULT 0.00   COMMENT 'The quantity of carbohydrate the food contains',
  `calories`     DECIMAL(12,2) NOT NULL DEFAULT 0.00   COMMENT 'The quantity of calories the food contains',
  PRIMARY KEY  (`id`),
  UNIQUE INDEX id_UNIQUE (`id` ASC)
);

CREATE TABLE `foodDB`.`log_date` (
  `id`         INTEGER PRIMARY KEY AUTO_INCREMENT,
  `entry_date` TIMESTAMP    NOT NULL    DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `foodDB`.`food_date` (
  `food_id`     INTEGER NOT NULL,
  `log_date_id` INTEGER NOT NULL,
  PRIMARY KEY   (`food_id`, `log_date_id`)
);