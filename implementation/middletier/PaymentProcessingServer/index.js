//function to connect to the databse
var mysql = require('mysql');
var config = require('./config.json');

const SQL_CONNECTION_POOL  = mysql.createPool({
    host     : config.dbhost,
    user     : config.dbuser,
    password : config.dbpassword,
    database : config.dbname
  });

//API end points 
const BOOKING_COST_PATH = '/bookingcost';
const LIST_OF_TICKETS_PATH = '/listoftickets';
const INVALID_INPUT = buildResponse(400, {message: 'Invalid Input'});

//function to route request to appropriate end point
exports.handler = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;

  console.log('Request event: ', event);
  switch(true) {
    case event.httpMethod === 'GET' && event.path === BOOKING_COST_PATH:
      console.log('Getting the booking cost for food and movie tickets.');
      calculateBookingCost(event, callback);
      break;
      
    case event.httpMethod === 'POST' && event.path === BOOKING_COST_PATH:
      console.log('Updating the database');
      postBookingCost(event, callback);
      break;
    
    case event.httpMethod === 'GET' && event.path === LIST_OF_TICKETS_PATH:
      console.log('Getting your ticket ');
      displayTickets(event, callback);
      break;
  
    default:
      console.log('Could not find path: ', event.path);
      callback(Error('API path', event.path, ' not found'));
  }
};

//function to calculate total booking cost (ticket cost + food cost) 
function calculateBookingCost(event, callback) {
  if (event.queryStringParameters == null || 
    !("booking_id" in event.queryStringParameters)) {
      return callback(null, INVALID_INPUT);
  } 
  var booking_id = event.queryStringParameters.booking_id;
  if (isBookingIdValid(booking_id)) {
    let query1 = "SELECT cost FROM FOOD_FOR_BOOKING WHERE booking_id = '" + booking_id + "'";
    queryDatabase(query1, function(queryResults1) {
      var food_cost = 0;
      for(var i = 0; i < queryResults1.length; i++) {
        food_cost = food_cost + queryResults1[i]["cost"];
      }
      let query2 = "SELECT total_cost FROM BOOKINGS WHERE booking_id = '" + booking_id + "'";
      queryDatabase(query2, function(queryResults2) {
        var seat_cost = 0;
        for(var i = 0; i < queryResults2.length; i++) {
          seat_cost = seat_cost + queryResults2[i]["total_cost"];
        }
        var total_cost = food_cost + seat_cost;
        let query3 = "UPDATE BOOKINGS SET total_cost = '" + total_cost + "' WHERE booking_id = '" + booking_id + "'";
        queryDatabase(query3, function(queryResults3) {
          var body = {
            ["food_cost"]: food_cost,
            ["seat_cost"]: seat_cost,
            ["total_cost"]: total_cost
          };
          return callback(null, buildResponse(200, body));
        });
      });
    });
  } else {
    return callback(null, INVALID_INPUT);
  }
}

//function to complete booking after the user has paid for the tickets and food
function postBookingCost(event, callback) {
  if (event.queryStringParameters == null || 
    !("booking_id" in event.queryStringParameters)) {
    return callback(null, INVALID_INPUT);
  }
  var booking_id = event.queryStringParameters.booking_id;
  if (isBookingIdValid(booking_id)) {
    let query1 = "UPDATE BOOKINGS SET booking_complete = 1 WHERE booking_id = '" + booking_id + "'";
    queryDatabase(query1, function(queryResults1) {
      let query2 = "SELECT total_cost FROM BOOKINGS WHERE booking_id = '" + booking_id + "'";
      queryDatabase(query2, function(queryResults2) {
        var body = {
          ["total_cost"]: queryResults2[0]["total_cost"]
        };
        
        callback(null, buildResponse(200, body));
      });
    });
  } else {
    return callback(null, INVALID_INPUT);
  }
}

//function to display tickets
function displayTickets(event, callback) {
  if (event.queryStringParameters == null || 
    !("booking_id" in event.queryStringParameters)) {
    return callback(null, INVALID_INPUT);
  }
  var booking_id = event.queryStringParameters.booking_id;
  if (isBookingIdValid(booking_id)) {
    let query1 = "SELECT * from BOOKINGS where booking_id='" + booking_id + "'";
    console.log(query1);
    queryDatabase(query1, function(queryResults1) {
      var cost = queryResults1[0]["total_cost"];
      let query2 = "SELECT city_code FROM USERS WHERE user_id = '" + queryResults1[0]["user_id"] + "'";
      queryDatabase(query2, function(queryResults2) {
        let query3 = "SELECT city_name FROM CITIES WHERE city_code = '" + queryResults2[0]["city_code"] + "'";
        queryDatabase(query3, function(queryResults3) {
          var city_name = queryResults3[0]["city_name"];
          let query4 = "SELECT * FROM SHOWS WHERE show_id = '" + queryResults1[0]["show_id"] + "'";
          queryDatabase(query4, function(queryResults4) {
            var show_date = queryResults4[0]["show_date"].toString().substring(0, 10);
            var start_time = queryResults4[0]["start_time"];
            var end_time = queryResults4[0]["end_time"];
            let query5 = "SELECT theater_name FROM THEATERS WHERE theater_id = '" + queryResults4[0]["theater_id"] + "'";
            queryDatabase(query5, function(queryResults5) {
              var theater_name = queryResults5[0]["theater_name"];
              let query6 = "SELECT name FROM MOVIES WHERE movie_id = '" + queryResults4[0]["movie_id"] + "'";
              queryDatabase(query6, function(queryResults6) {
                var movie_name = queryResults6[0]["name"];
                let query7 = "SELECT room_name FROM THEATER_ROOMS WHERE room_id = '" + queryResults4[0]["theater_room_id"] + "'";
                queryDatabase(query7, function(queryResults7) {
                  var room_name = queryResults7[0]["room_name"];
                  var body = {
                    ["city_name"]: city_name,
                    ["theater_name"]: theater_name,
                    ["movie_name"]: movie_name,
                    ["show_date"]: show_date,
                    ["start_time"]: start_time,
                    ["end_time"]: end_time,
                    ["room_name"]: room_name,
                    ["cost"]: cost
                  };
                  callback(null, buildResponse(200, body));
                    
                });
              });
            });
          });
        });
      });
    });
  } else {
    return callback(null, INVALID_INPUT);
  }
} 

//function to check for valid booking id
function isBookingIdValid(booking_id) {
  if (isNaN(booking_id) || parseInt(booking_id, 10) < 1 || 
      parseInt(booking_id, 10) > 100000) {
    return false;
  } else {
    return true;
  }
}

// inputs: query
// outputs: result of database query into callback
//          OR inability to connect to database error message
//          OR inability to query database error message
function queryDatabase(query, callback) {
  SQL_CONNECTION_POOL.getConnection(function(err, connection) {
    if (err) {
      throw Error("Failed to connect to database.", err);
    }
    connection.query(query, function (error, results) {
      connection.release();
      if (error) {
        throw Error("Failed to query the database.", err);
      }
      //console.log(results);
      callback(results);
    });
  });
}

//function to build API response
function buildResponse(statusCode, body) {
  return {
    statusCode: statusCode,
    headers: {'Content-Type': 'application/json'},
    body:JSON.stringify(body)
  };
}

