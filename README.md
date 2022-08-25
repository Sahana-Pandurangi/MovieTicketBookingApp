# MOVIE TICKET BOOKING SYSTEM

Sahana Pandurangi Raghavendra, Megana Reddy Boddam    
CSS 533: Distributed Computing
University of Washington

# INTRODUCTION

Our movie ticket booking system will be a distributed online website application. Its main purpose is to allow a customer to access the following features. 
* A catalog of movies playing in our affiliated theaters
* Each movie is displayed with all relevant details: genre, rating, language, description, trailer
* A mechanism to search, sort, and filter the movie tickets based on the movie details (language, genre, rating, etc.), the locations of the theaters and the movie showtimes in theaters. 
* Book tickets for an available movie
* Receive relevant communication about the booked ticket
* Allow an administrative user to monitor and analyze the entire process

The following are the problems our web app aims to solve.
* Once arriving at a theater, waiting in line for a movie ticket takes time and it is not enjoyable. This online system provides a fast and convenient method to obtain the ticket ahead of time.
* At theaters, there sometimes are not enough staff to assist consumers in a timely manner. Automating this process online reduces the need for an individual to be present, supervising the ticket booking process. 
* The customer would be unable to view all the movie descriptions and their trailers while choosing the movie to watch in-person in a theater.
* Similarly, in a theater, the customer would be able to sort and/or filter the available movies to choose between them
* In a theater, a customer would be unable to know which movies have available tickets until reaching the ticketing counter and asking the theater representative.

Below is a schematic diagram (Figure 1) of the high-level processes we plan to use to create our web app. It will mainly use Amazon Web Services and JAVA language. For our front-end/client-tier, we plan to create JAVA scripts with CLI. We will request and get responses through the Amazon API Gateway. The APIs that we will create in AWS will use REST Architecture. Our middle-tier will comprise of these programming interfaces. We will have a set of APIs running on the “search movies” lambda service, another set on the “ticket booking” lambda service, and the last set on the “payment processing” lambda service as shown in figure 1. These services will be implemented using JAVA and Node JavaScript. For our data-tier, we will be using Amazon’s Dynamo Database for a caching system. We have a read-intensive application (movies, locations, trailers, descriptions, etc.), so we prefer to be as efficient as possible in responding to the client when the data requested is generally frequently used. Secondly, we plan to use Amazon Relational Database Service (RDS) to store all our data points in tabular format: movies, theater locations, movie show timings, booking information, and more. 

![High level Architectural Schemata](https://github.com/Sahana-Pandurangi/MovieTicketBookingApp/blob/main/figures/high%20level%20architechture.jpg)
Figure 1: High level Architectural Schemata

# SYSTEM DESIGN CONSIDERATIONS

The following considerations were made while designing the system:
* We assume that the clients of our services do not require authentication through their email account username and password. All the authorized users inherently have an API key generated by the Amazon API gateway, and they access the services through this key and the gateway.
* The clients of the system are assumed to book at least one movie ticket; so, all the three services in the system are sequentially traversed.
* To throttle any malicious use of our system, potentially through a denial-of-service attack, we restrict the number of seats a user can book to twenty seats. 
* We plan to use Amazon DynamoDB, as well as hash maps in the middle-tier, to cache any frequently used information. 
* The system is implemented from the perspective of user role only. 

# DESCRIPTION OF COMPONENTS

## Back-End or Data-Tier:

Amazon Relational Database Service
* PostgreSQL instance in RDS is our preference. We plan to use complex data types such as text, images and videos. It is also an atomic, consistent, isolated, and durable (ACID compliant) storage engine.
* Data is pulled from here and temporarily stored in the DynamoDB for further use as requested.
* To update the RDS, new data is accessed from DynamoDB and stored in RDS in tabular format as shown in figure 2.
* In figure 2, each table is represented by a box and its name is at the top of the table, highlighted in blue. The variable names in each row of each box are the column headers in that respective table. The data type names refer to the data types in that column. Bolded variable names are primary keys. The lines between boxes show the relationship between the tables. For example, the “city_code” in USERS is a foreign key and references the “city_code” primary key in CITIES. 
* If time permits, we plan to pull data from RDS to create our analytics services for business interests.
* We plan to have a replicated database to increase the availability of the data in case of system failures/crashes.
Amazon Dynamo Database 
* Because of the low latency and flexibility of this NoSQL database, we plan to use it to implement a caching system. Our APIs in the middle tier will call this database.

![Database](/figures/"database.JPG")
Figure 2: Schemata of tables in database [Final].

## Middle-Tier: 

We plan to implement our middle tier using the AWS infrastructure to make our system reliable, highly available and horizontally scalable. We will create HTTP REST APIs, communicate with the client-tier using the Amazon API gateway, and communicate with the back-end databases using API endpoints and AWS lambda.

Amazon API Gateway: This component routes HTTP API requests from the client to appropriate lambda functions hosted on the AWS server. It also routes the API responses from the lambda functions back to the client. The API gateway provides tools to securely access APIs with appropriate authentication and authorization controls by providing an ability to create API keys for a particular API endpoint.

AWS Lambda functions: These functions are organizational blocks for our various APIs. They will receive inputs from the API Gateway and provide output responses to the Gateway as well. They will take inputs and provide updates to our data-tier as well. We have three lambda functions which will implement a set of APIs each: search movies lambda, ticket booking lambda and payment processing lambda. 

Implementation of APIs: Below are the details of the APIs and their functionalities. All the APIs mentioned below have a mandatory API key parameter that will be generated using Amazon API gateway. The parameter api_key (string) will be used to allow only registered users to access the system. Exception handling will be implemented in all methods of each API. Successful REST API calls/requests will return a status code of 200.  Errors will display appropriate HTTP status code based on the type of exception and appropriate error message will be returned to the client to display to the user. Example: A 400 status code will be returned for client errors.

1.	Search movies lambda function: The search movies lambda function provides a set of APIs that allows the user to search a suitable movie they want to book based on their desired city, theater and movies. Below is the list of REST API endpoints we will implement in this component. 

a.	API → GetListOfCities(user_id):  This API will provide a list of cities where theaters are available as registered in the database.  It will implement a GET method  to communicate between the client and  search movies lambda function on AWS which internally implements logic to fetch a set of cities from the Amazon Relational Database Service using a JDBC connection.  

b.	API → GetSelectedCityCode(user_id, city_code) → This API will be used by the client to select the city from the list of cities displayed. 

c.	API → GetListOfTheatersByCity(user_id, city_code) - This api will return a list of theaters based on the city selected by the user.

d.	API→ GetSelectedTheaterCode(user_id, theater_id) : This api will be used by the client to select a theater from the list of theaters displayed in a particular city.

e.	API → GetListOfMoviesByTheater(user_id, theater_room_id): This api will return a list of  movies that will be displayed in a theater.

f.	API → PostSelectedMovie(show_id, room_id): This api will be used by the client to select a movie from the list, displayed in a particular theater. This detail will be stored in the backend server and would be used later for printing ticket details and during payment processing

2.	Ticket booking lambda function: The ticket booking lambda function provides REST API endpoints to clients to reserve seats based on the show selected by the user. We assume that the client will complete the booking and that there will be no partial bookings or cancellations. So, we will be updating the database with the details of the bookings the user makes their show/seat selections. We also need to make sure that no two users are able to reserve the same seat. To handle the issues that arise from concurrent requests, we plan to utilize transaction isolation levels in PostgreSQL to lock the specific show in the theater using show_id and booking_id before we update the database.
 
a.	API → GetDateOfMovie(user_id, show_id, room_id) : This API will display a list of dates the selected movie is displayed in the theater.

b.	API → PostSelectedDate(user_id, show_id, room_id) : This api will be used by the client to select a date the user wants to watch the movie. This detail will be stored in the backend server and would be used later for printing ticket details and during payment processing.

c.	API → GetTimeForSelectedDate(user_id, show_id, room_id, start_time) : This API will display a list of  showtimes for the selected movie on a particular date.

d.	API → PostSelectedTime(user_id, show_id): This API will be used by the client to select a time on a particular date to watch the  movie. This detail will be stored in the backend server and would be used later for printing ticket details and during payment processing.

e.	API → GetSeatDetails(user_id, show_seat_id, show_id, room_id): This API  will display a list of available seats by using the seat_row and seat_type to describe them.

f.	API → PostSelectedSeat(show_id, seat_id, booking_id): This API updates SEATS_FOR_SHOW with booking_id for each of the seats selected by the client.

3.	Food and Beverages lambda function: This lambda function provides a set of APIs that allows the user to book various available refreshments in the theater of choice. They will also be asked to select from a n available set of refreshment pick-up times that will be before the selected movie starts on the same day. We assume that once the user selects that they would like food and/or beverages, they will not change their mind in the middle of the selection process. We also assume that there is unlimited amount of food/beverage for sale at any particular theater on all days. To prevent malicious use of this service, we limit the maximum amount of food/beverage items selected to 40.
	
a.	API → GetFoodAvailable(user_id, theater_id) : This API will display a list of food and beverage items available at the theater. 

b.	API → PostSelectedFood(user_id, booking_id, food_id, quantity): This API collects the selected food/beverage items and their quantities and stores them in the backend database.

c.	API → GetPickUpTimings(user_id, booking_id): This API displays a list of food/beverage pick-up timings for the customer before the start of their show.

d.	API → PostFoodPickUpTime(user_id, booking_id, pickup): This API will e used by the client to select a time on  the date of the movie to pick up food. This detail will be saved in the backend server and the re-used when printing the final ticket.  

4.	Payment processing lambda function: The payment processing lambda function provides a set of APIs that allows the user to see the total cost of their movie ticket(s) booking, access the tickets in CLI, and receive communication (email) with the tickets.

a.	API → PostBookingCost(booking_id) : This API will access the booked seats associated with the provided booking_id in the SEATS_FOR_SHOW table in figure 2. It will also access the booked food and/or beverages in the FOOD_FOR_BOOKING table. Prices associated with each booked seat and cost associated with each booked food item in the tables allow this API to the  calculateion theof total cost of booking, which must be stored in BOOKINGS. 

b.	API → GetBookingCost(booking_id) : This API will access the cost of the booking from the data-tier and display it to the client.

c.	API → GetListOfTickets(booking_id) : Using the stored data of the client’s seat  selections and booking_id, display to the client their name, the movie, the theater name, theater location, theater room name, seat row and number. Display multiple sets of this information as needed for each movie theater seat that was booked in the booking_id. Lastly, using the stored data in the FOOD_FOR_BOOKING table, display a food/beverages ticket for the user that displays the client’s name, booking_id, food/beverage items (and their quantity) booked, total cost of food/beverages, and the pickup date and time. 

Lastly, if time permits, we plan to implement APIs for an admin role and add a user authentication step to our website. We would consider this to be our last priority as our focus is set up an initial working system for the average user role using API keys for authorization.

## Front-End: 
* We plan to create a command line interface (CLI) script to access APIs from the middleware and to interact with the customer. It will be stateless. The CLI will be implemented in JAVA and thus is platform independent and can run on windows, linux or MAC OS.
* We plan to use Postman to interact with the APIs described above and perform systematic integration tests. 
* If time permits, we plan to use Amazon CloudFront and REACT JS to build user-friendly client facing website pages. 

