INSERT INTO CITIES VALUES 
    (1, "Seattle", "WA", 98101),
    (2, "Universal City", "FL", 12436),
    (3, "Kirkland", "WA", 98083),
    (5, "Redmond", "WA", 98073);

INSERT INTO THEATERS VALUES
    (1, "Cinemark", 5),
    (2, "Cinemark", 1),
    (3, "Lincoln Memorial Theater", 1),
    (4, "Regal", 1),
    (5, "Neptune Theaters", 5),
    (6, "Cinemark", 2),
    (7, "Regal Cinemas", 2),
    (8, "Neptune", 3),
    (9, "Ariel Theaters", 2);

INSERT INTO THEATER_ROOMS VALUES
    (1, "Screen Room A", 2, 48),
    (2, "Screen Room B", 2, 48),
    (3, "Screen Room C", 2, 48);

INSERT INTO THEATER_SEATS VALUES
    (1, 3, "A", 1, "Premium"),
    (2, 3, "A", 2, "Premium"),
    (3, 3, "A", 3, "Premium"),
    (4, 3, "A", 4, "Premium"),
    (5, 3, "A", 5, "Premium"),
    (6, 3, "A", 6, "Premium"),
    (12, 3, "B", 14, "Premium"),
    (13, 3, "B", 13, "Premium");




-- insert values into FOODBEVERAGES

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

INSERT INTO USERS VALUES 
    (-1, "Dummy", "Dummy2", "dummy.dummy2@dummy.com", 0100100011, 1);

INSERT INTO BOOKINGS VALUES (-1, 0, 0, 0, -1, 1);

-- insert values into SEATS_FOR_SHOWS





