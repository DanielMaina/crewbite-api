CREATE TABLE `User_Calendar` (
	`id` int NOT NULL AUTO_INCREMENT,
	`event_name` tinytext NOT NULL,
	`start_date` DATETIME NOT NULL,
	`end_date` DATETIME NOT NULL,
	`user_name` varchar(255) NOT NULL,
	`created_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
	FOREIGN KEY (`user_name`) REFERENCES `User_Profiles`(`user_name`);
) ENGINE=InnoDB DEFAULT CHARSET=utf8;