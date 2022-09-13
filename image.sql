-- images Table definition

CREATE TABLE `images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `image_url` longtext NOT NULL,
  `is_hidden` tinyint(1) NOT NULL DEFAULT '0',
  `status` enum('yet_to_upload','uploaded','deleted','replaced') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'yet_to_upload',
  `created_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `images_UN` (`image_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;