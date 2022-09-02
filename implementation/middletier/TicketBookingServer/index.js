// Function to connect to the database
var mysql = require('mysql');
var config = require('./config.json');

const SQL_CONNECTION_POOL  = mysql.createPool({
    host     : config.dbhost,
    user     : config.dbuser,
    password : config.dbpassword,
    database : config.dbname
  });
  
// API endppoints 
const QUERY_DATABASE_PATH = '/query';
const LIST_OF_SHOW_DATES_PATH = '/listofshowdates';
const LIST_OF_SHOWS_PATH = '/listofshows';
const LIST_OF_SHOW_SEATS_PATH = '/listofshowseats';
const ADD_SHOW_SEATS_PATH = '/addshowseats'

// Routing requests to appropriate endpoints
exports.handler = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;

  console.log('Request event: ', event);
  switch(true) {
    case event.httpMethod === 'GET' && event.path === LIST_OF_SHOW_DATES_PATH:
      console.log('Getting dates for the movie');
      getDatesForMovie(event, callback);
      break;
      
    case event.httpMethod === 'GET' && event.path === LIST_OF_SHOWS_PATH:
      console.log('Getting shows');
      getShows(event, callback);
      break;
      
    case event.httpMethod === 'GET' && event.path === LIST_OF_SHOW_SEATS_PATH:
      console.log('Getting seats for show');
      getSeats(event, callback);
      break;
    
    case event.httpMethod === 'POST' && event.path === ADD_SHOW_SEATS_PATH:
      console.log('Posting seat details for show');
      postSeats(event, callback);
      break;
      
    case event.httpMethod === 'GET' && event.path === QUERY_DATABASE_PATH:
      console.log('Querying database: ' + event.queryStringParameters.query);
      queryDatabaseOverload(event, callback);
      break;
      
    default:
      console.log('Could not find path: ', event.path);
      callback(null, buildResponse(404, { "message": "API path: '" + event.path + "' not found" }));
  }
};

// Function to post seat details and block the seats for the user so that no two users select the same seat
function postSeats(event, callback){
  if (event.queryStringParameters == null || typeof event.queryStringParameters.show_id === 'undefined') 
  {
    console.log("User input : " + event + " is incomplete, returning...");
    callback(null, buildResponse(400, { "message": "Invalid Input" }));
    return;
  }

    var booking_id = parseInt(Math.floor(Math.random() * 10000)) // Generate here
    var user_id = event.queryStringParameters.user_id
    var show_id = event.queryStringParameters.show_id
    var number_of_seats = event.queryStringParameters.number_of_seats
    var seats_remaining = event.queryStringParameters.seats_remaining
    var theater_room_id = event.queryStringParameters.theater_room_id
    var selected_seat_numbers = event.body
    var total_cost = (parseInt(10)) * (parseInt(number_of_seats, 10));
    
    // Processing the request body
    var array_selected_seat_id = selected_seat_numbers.split(":");
    array_selected_seat_id = array_selected_seat_id[1].split("}")
    array_selected_seat_id = array_selected_seat_id[0].split("[")
    array_selected_seat_id = array_selected_seat_id[1].split("]")
    array_selected_seat_id =  array_selected_seat_id[0].split(",")
    console.log(array_selected_seat_id)
    
    // generate a booking id and save the ticket cost into the database
    var query = "INSERT into BOOKINGS (booking_id,number_of_seats,total_cost,booking_complete,user_id,show_id) values ('"+booking_id+"','"+number_of_seats+"','"+total_cost+"',0,'"+user_id+"','"+show_id+"');"
    console.log(query)
    queryDatabase(query, function(queryResults) {
      var body = {message: "Sucessfully added booking details to the database",
      total_booking_cost: total_cost,
      booking_id: booking_id
      }
    callback(null, buildResponse(200, body));
    })
    
    //Updating the number available seats after the user has booked the seats 
    var query1 = "UPDATE SHOWS SET available_seats='"+seats_remaining+"' WHERE show_id='"+show_id+"';"  
    queryDatabase(query1, function(queryResults) {
      var body = {message: "Sucessfully updated seat details in the database",
      available_seats: seats_remaining}
      console.log(body)
    })
    
    // Blocking the booked seat 
    var query2 = "UPDATE SEATS_FOR_SHOW set available=0 WHERE seat_number IN (";
            var seat_ids = "";
            for (let i = 0; i < array_selected_seat_id.length; i++) {
              if (i != 0) {
                seat_ids += ", ";
              }
              seat_ids += array_selected_seat_id[i];
            }
            query2 = query2 + seat_ids+ ")" + "AND show_id=" + "'"+show_id+"'" + ";"
            console.log(query2)
            queryDatabase(query2, function(queryResults) {
            var body = {results: queryResults}
            console.log(body)})
    
    // Updating the booked seat with the respective booking id
    var query3 = "UPDATE SEATS_FOR_SHOW SET booking_id='"+booking_id+"' WHERE seat_number IN (";
            var seat_ids = "";
            for (let i = 0; i < array_selected_seat_id.length; i++) {
              if (i != 0) {
                seat_ids += ", ";
              }
              seat_ids += array_selected_seat_id[i];
            }
            query3 = query3 + seat_ids+ ")" + "AND show_id=" + "'"+show_id+"'" + ";" ;
            console.log(query3)
      queryDatabase(query3, function(queryResults) {
      var body = {message: "Sucessfully updated booking_id details in the database with seat number",
      results: queryResults}
      console.log(body)
    })
}

// Function to get list of available seats
function getSeats(event, callback) {
  if (event.queryStringParameters == null || typeof event.queryStringParameters.show_id === 'undefined') {
    console.log("User input : " + event + " is incomplete, returning...");
    callback(null, buildResponse(400, { "message": "Invalid Input" }));
    return;
  }
  
    var input = {
    "show_id": event.queryStringParameters.show_id
  };
  console.log("Received request: " + input + " for getting the list of seats.");
  
  const GET_SEATS_QUERY = "SELECT seatsforshow.show_seat_id, seatsforshow.price, theaterseats.seat_row, theaterseats.seat_number, theaterseats.seat_type"
    + " FROM SEATS_FOR_SHOW seatsforshow INNER JOIN THEATER_SEATS theaterseats ON seatsforshow.seat_id = theaterseats.seat_id"
    + " WHERE seatsforshow.available=1"
    + " AND seatsforshow.show_id = " + input.show_id
    + " ORDER BY theaterseats.seat_row, theaterseats.seat_number;";
    
  console.log("Final query to fetch seats for show: " + GET_SEATS_QUERY);
  queryDatabase(GET_SEATS_QUERY, function(queryResults) {
    console.log("Successfully queried for seats.");  
    var seats = [];
    for (var i = 0; i < queryResults.length; i++) {
      console.log("Adding '" + JSON.stringify(queryResults[i]) + "' to results.");
      
      var row = {
        "show_seat_id": queryResults[i].show_seat_id,
        "price": queryResults[i].price,
        "seat_row": queryResults[i].seat_row,
        "seat_number": queryResults[i].seat_number,
        "seat_type": queryResults[i].seat_type
      };
      
      seats.push(row);
    }
    
    callback(null, buildResponse(200, { "seats": seats }));
  });
}

// Function to get the show times on the selected date
function getShows(event, callback) {
  if (event.queryStringParameters == null || typeof event.queryStringParameters.movie_id === 'undefined' || typeof event.queryStringParameters.theater_id === 'undefined' || typeof event.queryStringParameters.show_date === 'undefined') {
    console.log("User input : " + event + " is incomplete, returning...");
    callback(null, buildResponse(400, { "message": "Invalid Input" }));
    return;
  }
  
  var input = {
    "movie_id": event.queryStringParameters.movie_id,
    "theater_id": event.queryStringParameters.theater_id,
    "show_date": event.queryStringParameters.show_date
  };
  console.log("Received request: " + input + " for getting the list of shows.");
  
  const GET_SHOWS_QUERY = "SELECT s.show_id, s.start_time, s.end_time, s.available_seats, t.room_id, t.room_name FROM SHOWS s INNER JOIN THEATER_ROOMS t ON s.theater_room_id = t.room_id"
    + " WHERE s.movie_id = " + input.movie_id
    + " AND s.theater_id = " + input.theater_id
    + " AND s.show_date = '" + input.show_date + "'";
    + " ORDER BY s.start_time;";
  
  console.log("Final query to fetch shows for movie: " + GET_SHOWS_QUERY);
  queryDatabase(GET_SHOWS_QUERY, function(queryResults) {
    console.log("Successfully queried for shows.");  
    var shows = [];
    for (var i = 0; i < queryResults.length; i++) {
      console.log("Adding '" + JSON.stringify(queryResults[i]) + "' to results.");
      
      var row = {
        "show_id": queryResults[i].show_id,
        "start_time": queryResults[i].start_time,
        "end_time": queryResults[i].end_time,
        "available_seats": queryResults[i].available_seats,
        "room_id": queryResults[i].room_id,
        "room_name": queryResults[i].room_name,
      };
      
      shows.push(row);
    }
    callback(null, buildResponse(200, { "shows": shows }));
  });
  
}

//Function to get the available date the movie is being displayed
function getDatesForMovie(event, callback) {
  if (event.queryStringParameters == null || typeof event.queryStringParameters.movie_id === 'undefined' || typeof event.queryStringParameters.theater_id === 'undefined') {
    console.log("User input : " + event + " is incomplete, returning...");
    callback(null, buildResponse(400, { "message": "Invalid Input" }));
    return;
  }
  
  var input = {
    "movie_id": event.queryStringParameters.movie_id,
    "theater_id": event.queryStringParameters.theater_id
  };
  console.log("Received request: " + input + " for getting the list of dates.");
  
  const GET_DATES_FOR_MOVIE_QUERY = "SELECT DISTINCT(show_date) AS unique_show_dates FROM SHOWS"
    + " WHERE movie_id = " + input.movie_id
    + " AND theater_id = " + input.theater_id
    + " ORDER BY unique_show_dates;";
  
  console.log("Final query to fetch dates for movie: " + GET_DATES_FOR_MOVIE_QUERY);
  queryDatabase(GET_DATES_FOR_MOVIE_QUERY, function(queryResults) {
    console.log("Successfully queried for dates.");  
    var dates = [];
    for (var i = 0; i < queryResults.length; i++) {
      console.log("Adding '" + queryResults[i].unique_show_dates + "' to results.");
      dates.push(JSON.stringify(queryResults[i].unique_show_dates).substring(1,11));
    }
    callback(null, buildResponse(200, { "date": dates }));
  });
}

// This function is used only for testing purpose to check updates in databse.
function queryDatabaseOverload(event, callback) {
  var query = event.queryStringParameters.query;
  
  queryDatabase(query, function(queryResults) {
      queryResults = { "queryResults": queryResults }
      console.log("Successfully queried database: " + JSON.stringify(queryResults));
      callback(null, buildResponse(200, queryResults));
  });
}

// Querying the databse and getting the response
function queryDatabase(query, callback) {
  SQL_CONNECTION_POOL.getConnection(function(err, connection) {
    if (err) {
      throw Error("Failed to connect to database.", err);
    }
    
    console.log("Successfully connected to database.");

    connection.query(query, function (error, results) {
      connection.release();
      if (error) {
        throw Error("Failed to query database for query: " + query + " | Error: ", error);
      }
      callback(results);
    });
  });
}

// Function to build response body
function buildResponse(statusCode, body) {
  return {
    statusCode: statusCode,
    headers: {
      'Content-Type': 'application/json'
    },
    body:JSON.stringify(body)
  };
}