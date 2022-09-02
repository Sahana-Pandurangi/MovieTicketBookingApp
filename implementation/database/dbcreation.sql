Create Table CITIES (
  `city_code` INT PRIMARY KEY,
  `city_name` VARCHAR(100), 
  `state_name` VARCHAR(50), 
  `zip_code` INT
);

Create Table USERS (
  `user_id` int Primary Key,
  `first_name` varchar(500),
  `second_name` varchar(500),
  `email` varchar(1000),
  `phone` int,
  `city_code` int, 
  FOREIGN KEY (`city_code`) REFERENCES `CITIES`(`city_code`) 
);

Create Table THEATERS (
  `theater_id` int Primary Key,
  `theater_name` varchar(1000),
  `city_code` int, 
  Foreign Key (`city_code`) References `CITIES`(`city_code`)
);

Create Table THEATER_ROOMS (
  `room_id` int Primary Key,
  `room_name` varchar(40),
  `theater_id` int,
  `total_seats` int,
  Foreign Key (`theater_id`) References `THEATERS`(`theater_id`)
);

Create Table THEATER_SEATS (
  `seat_id` int Primary Key,
  `room_id` int,
  `seat_row` varchar(10),
  `seat_number` int,
  `seat_type` varchar(20),
  Foreign Key (`room_id`) References `THEATER_ROOMS`(`room_id`)
);

Create Table FOODBEVERAGES (
  `food_id` int Primary Key,
  `food_name` varchar(80),
  `food_price` double,
  `theater_id` int, 
  Foreign Key (`theater_id`) References `THEATERS`(`theater_id`)
);

Create Table MOVIES (
  `movie_id` int Primary Key,
  `name` varchar(150),
  `description` text,
  `image` text,
  `trailer` text,
  `genre` varchar(80),
  `audience_rating_level` varchar(80),
  `language` varchar(80),
  `duration` time,
  `imdb_rating` double,
  `rotten_tomatoes_rating` int
);

Create Table SHOWS (
  `show_id` int Primary Key,
  `show_date` date,
  `start_time` time,
  `end_time` time,
  `available_seats` int,
  `theater_room_id` int, 
  Foreign Key (`theater_room_id`) References `THEATER_ROOMS`(`room_id`),
  `theater_id` int,
  Foreign Key (`theater_id`) References `THEATERS`(`theater_id`),
  `movie_id` int, 
  Foreign Key (`movie_id`) References `MOVIES`(`movie_id`)
);

Create Table BOOKINGS (
  `booking_id` int Primary Key,
  `number_of_seats` int,
  `total_cost` double,
  `booking_complete` bit,
  `user_id` int, 
  Foreign Key (`user_id`) References `USERS`(`user_id`),
  `show_id` int, 
  Foreign Key (`show_id`) References `SHOWS`(`show_id`)
);

Create Table SEATS_FOR_SHOW (
  `show_seat_id` int Primary Key,
  `available` bit,
  `price` double,
  `seat_id` int,
  Foreign Key (`seat_id`) References `THEATER_SEATS`(`seat_id`),
  `seat_number` int,
  `show_id` int, 
  Foreign Key (`show_id`) References `SHOWS`(`show_id`),
  `booking_id` int,
  Foreign Key (`booking_id`) References `BOOKINGS`(`booking_id`)
);

Create Table FOOD_FOR_BOOKING (
  `food_id` int, 
  Foreign Key (`food_id`) References `FOODBEVERAGES`(`food_id`),
  `quantity` int,
  `cost` double,
  `booking_id` int, 
  Foreign Key (`booking_id`) References `BOOKINGS`(`booking_id`)
);
