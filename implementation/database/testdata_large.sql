INSERT INTO CITIES VALUES 
    (1, "Seattle", "WA", 98101),
    (2, "Chicago", "IL", 60606),
    (3, "New Orleans", "LA", 70130),
    (4, "Portland", "OR", 97210),
    (5, "Houston", "TX", 77070),
    (6, "Miami", "FL", 33162),
    (7, "Bellevue", "WA", 98006),
    (8, "New York", "NY", 11385),
    (9, "Los Angeles", "CA", 91331),
    (10, "San Francisco", "CA", 94565);

INSERT INTO THEATERS VALUES
    (1, "Cinemark Theaters", 1),
    (2, "Lincoln Memorial Theater", 1),
    (3, "Chelsea Theater Group", 1),
    (4, "Regal Cinemas", 1),
    (5, "Neptune Theaters", 1),
    (6, "Cineplex Entertainment", 2),
    (7, "Lincoln Memorial Theater", 2),
    (8, "Chelsea Theater Group", 2),
    (9, "Compass Players", 2),
    (10, "The Factory Theaters", 2),
    (11, "Cinemark Theaters", 3),
    (12, "The Diggers", 3),
    (13, "Focus Group", 3),
    (14, "Bad Dog Theater Company", 3),
    (15, "Neptune Theaters", 3),
    (16, "Whole World Theater", 4),
    (17, "Under the Gun Theater", 4),
    (18, "Chelsea Theater Group", 4),
    (19, "Regal Cinemas", 4),
    (20, "Wing-It Productions", 4),
    (21, "Cinemark Theaters", 5),
    (22, "Lincoln Memorial Theater", 5),
    (23, "Chelsea Theater Group", 5),
    (24, "Regal Cinemas", 5),
    (25, "Neptune Theaters", 5),
    (26, "Virago Theaters", 6),
    (27, "The National Comedy Theater", 6),
    (28, "Paramount Center", 6),
    (29, "Neptune Cinemas", 6),
    (30, "The School of Night", 6),
    (31, "Cinemark Theaters", 7),
    (32, "Bad Dog Theater Company", 7),
    (33, "Chelsea Theater Group", 7),
    (34, "Cineplex Entertainment", 7),
    (35, "Neptune Theaters", 7),
    (36, "Cinemark Theaters", 8),
    (37, "Bad Dog Theater Company", 8),
    (38, "Chelsea Theater Group", 8),
    (39, "Regal Cinemas", 8),
    (40, "Wing-It Productions", 8),
    (41, "Cinemark Theaters", 9),
    (42, "Focus Group", 9),
    (43, "Chelsea Theater Group", 9),
    (44, "Regal Cinemas", 9),
    (45, "Neptune Theaters", 9),
    (46, "Compass Players", 10),
    (47, "Focus Group", 10),
    (48, "Chelsea Theater Group", 10),
    (49, "Regal Cinemas", 10),
    (50, "The National Comedy Theater", 10);

-- insert values into THEATER_ROOMS
DROP PROCEDURE IF EXISTS insert_THEATER_ROOMS;
DELIMITER //
CREATE PROCEDURE insert_THEATER_ROOMS()
BEGIN
DECLARE i INT DEFAULT 1; 
DECLARE j INT DEFAULT 1;
WHILE (i <= 200) DO
    INSERT INTO `THEATER_ROOMS` VALUES (i, "Screen Room A", j, 48);
    SET i = i + 1;
    INSERT INTO `THEATER_ROOMS` VALUES (i, "Screen Room B", j, 48);
    SET i = i + 1;
    INSERT INTO `THEATER_ROOMS` VALUES (i, "Screen Room C", j, 48);
    SET i = i + 1;
    INSERT INTO `THEATER_ROOMS` VALUES (i, "Screen Room D", j, 48);
    SET i = i + 1;
    SET j = j + 1;
END WHILE;
END;
//
DELIMITER ;

-- insert values into THEATER_SEATS
DROP PROCEDURE IF EXISTS insert_THEATER_SEATS;
DELIMITER //
CREATE PROCEDURE insert_THEATER_SEATS()
BEGIN
DECLARE i INT DEFAULT 0; 
DECLARE j INT DEFAULT 1;
DECLARE s INT DEFAULT 1;
WHILE (j <= 200) 
DO
    WHILE (s <= 48) 
    DO
        IF (s <= 8) THEN
            INSERT INTO `THEATER_SEATS` VALUE (i, j, "A", s, "Premium");
        ELSEIF (s > 8 AND s <= 16) THEN
            INSERT INTO `THEATER_SEATS` VALUE (i, j, "B", s, "Premium");
        ELSEIF (s <= 24) THEN
            INSERT INTO `THEATER_SEATS` VALUE (i, j, "C", s, "Premium");
        ELSEIF (s <= 32) THEN
            INSERT INTO `THEATER_SEATS` VALUE (i, j, "D", s, "Premium");
        ELSEIF (s <= 40) THEN
            INSERT INTO `THEATER_SEATS` VALUE (i, j, "E", s, "Premium");
        ELSEIF (s <= 48) THEN
            INSERT INTO `THEATER_SEATS` VALUE (i, j, "F", s, "Premium");
        END IF;
        SET i = i + 1;
        SET s = s + 1;
    END WHILE;
    SET s = 1;
    SET j = j + 1;
END WHILE;
END;
//
DELIMITER ;

-- insert values into FOODBEVERAGES
DROP PROCEDURE IF EXISTS insert_FOODBEVERAGES;
DELIMITER //
CREATE PROCEDURE insert_FOODBEVERAGES()
BEGIN
DECLARE i INT DEFAULT 0; 
DECLARE j INT DEFAULT 1;
WHILE (j <= 50) 
DO
    INSERT INTO `FOODBEVERAGES` VALUES 
        (i+1, "Small Butter Popcorn", 5, j),
        (i+2, "Medium Butter Popcorn", 10, j),
        (i+3, "Large Butter Popcorn", 15, j),
        (i+4, "Medium Curly Fries", 10, j),
        (i+5, "Large Curly Fries", 15, j),
        (i+6, "Small Fountain Drink", 5, j),
        (i+7, "Medium Fountain Drink", 8, j),
        (i+8, "Large Fountain Drink", 10, j),
        (i+9, "M & M Candy", 5, j),
        (i+10, "Sour Patch Kids", 3, j);
    SET i = i + 10;
    SET j = j + 1;
END WHILE;
END;
//
DELIMITER ;

INSERT INTO MOVIES VALUES 
    (1, "Top Gun: Maverick", 
    "After more than 30 years of service as one of the Navy's top aviators, Pete Maverick Mitchell is 
    where he belongs, pushing the envelope as a courageous test pilot and dodging the advancement in rank 
    that would ground him. Training a detachment of graduates for a special assignment, Maverick must 
    confront the ghosts of his past and his deepest fears, culminating in a mission that demands the 
    ultimate sacrifice from those who choose to fly it.",
    "image", "trailer", "Action", "PG-13", "English", '01:50:00', 7, 80),
    (2, "Pushpa: The Rise - Part 1", 
    "Violence erupts between red sandalwood smugglers and the police charged with bringing down their 
    organisation in the Seshachalam forests of South India.",
    "image", "trailer", "Adventure/Romance", "NC-17", "Telugu", '02:59:00', 9, 75);
    
-- insert values into SHOWS
DROP PROCEDURE IF EXISTS insert_SHOWS;
DELIMITER //
CREATE PROCEDURE insert_SHOWS()
BEGIN
DECLARE i INT DEFAULT 0; 
DECLARE j INT DEFAULT 1;
WHILE (j <= 50) 
DO
    INSERT INTO `SHOWS` VALUES 
        (i+1, '2022-06-01', '12:30:00', '14:20:00', 48, ((4*j)-2), j, 1),
        (i+2, '2022-06-01', '12:30:00', '15:29:00', 48, ((4*j)-3), j, 2),
        (i+3, '2022-06-02', '12:30:00', '14:20:00', 48, ((4*j)-2), j, 1),
        (i+4, '2022-06-02', '12:30:00', '15:29:00', 48, ((4*j)-3), j, 2),
        (i+5, '2022-06-03', '12:30:00', '14:20:00', 48, ((4*j)-2), j, 1),
        (i+6, '2022-06-03', '12:30:00', '15:29:00', 48, ((4*j)-3), j, 2),
        (i+7, '2022-06-01', '15:45:00', '17:35:00', 48, ((4*j)-2), j, 1),
        (i+8, '2022-06-01', '17:00:00', '20:59:00', 48, ((4*j)-3), j, 2),
        (i+9, '2022-06-02', '15:45:00', '17:35:00', 48, ((4*j)-2), j, 1),
        (i+10, '2022-06-02', '17:00:00', '20:59:00', 48, ((4*j)-3), j, 2),
        (i+11, '2022-06-03', '15:45:00', '17:35:00', 48, ((4*j)-2), j, 1),
        (i+12, '2022-06-03', '17:00:00', '20:59:00', 48, ((4*j)-3), j, 2),
        (i+13, '2022-06-01', '20:00:00', '21:50:00', 48, ((4*j)-2), j, 1),
        (i+14, '2022-06-02', '12:30:00', '17:35:00', 48, ((4*j)-2), j, 1),
        (i+15, '2022-06-03', '12:30:00', '14:20:00', 48, ((4*j)-2), j, 1);
    SET i = i + 15;
    SET j = j + 1;
END WHILE;
END;
//
DELIMITER ;

INSERT INTO USERS VALUES 
    (-1, "Dummy", "Dummy2", "dummy.dummy2@dummy.com", 0100100011, 1);

INSERT INTO BOOKINGS VALUES (-1, 0, 0, 0, -1, 1);

-- insert values into SEATS_FOR_SHOWS
DROP PROCEDURE IF EXISTS insert_SEATS_FOR_SHOWS;
DELIMITER //
CREATE PROCEDURE insert_SEATS_FOR_SHOWS()
BEGIN
DECLARE i INT DEFAULT 0; 
DECLARE j INT DEFAULT 1;
DECLARE s INT DEFAULT 1;
WHILE (j <= 750) 
DO
    WHILE (s <= 48) 
    DO
        INSERT INTO `SEATS_FOR_SHOW` VALUES 
            (i, 1, 25, s, s, j, -1);
        SET s = s + 1;
        SET i = i + 1;
    END WHILE;
    SET j = j + 1;
    SET s = 0;
END WHILE;
END;
//
DELIMITER ;



