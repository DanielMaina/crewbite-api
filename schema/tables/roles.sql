CREATE TABLE `Roles` (
	`id` int NOT NULL AUTO_INCREMENT,
	`role_name` varchar(255) NOT NULL,
	`description` TEXT NOT NULL,
	`user_name` varchar(255) NOT NULL,
	`created_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
	FOREIGN KEY (`user_name`) REFERENCES `Users`(`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;