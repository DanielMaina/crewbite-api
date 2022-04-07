CREATE TABLE `User_Profiles` (
	`id` int NOT NULL AUTO_INCREMENT,
	`user_name` varchar(255) NOT NULL UNIQUE,
	`first_name` TEXT NOT NULL,
	`last_name` TEXT NOT NULL,
	`location` smallint NOT NULL,
	`about_you` varchar(255) NOT NULL,
	`union_member` bool NOT NULL,
	`volunteer_work` bool NOT NULL,
	`covid_vaccinated` bool NOT NULL,
	`demo_reel` varchar(255),
	`imdb_profile` varchar(255),
	`instagram` varchar(255),
	`event_name` tinytext,
	`created_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
	FOREIGN KEY (`user_name`) REFERENCES `Users`(`user_name`)
	FOREIGN KEY (`event_name`) REFERENCES `User_Calendar`(`event_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;