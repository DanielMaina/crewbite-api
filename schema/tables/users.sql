CREATE TABLE `Users` (
	`id` int NOT NULL AUTO_INCREMENT,
	`user_name` varchar(255) NOT NULL UNIQUE,
	`email_addr` tinytext,
	`phone_number` tinytext,
	`role_name` int NOT NULL,
	`is_member` bool NOT NULL,
	`created_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
	FOREIGN KEY (`role_name`) REFERENCES `Roles`(`role_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
