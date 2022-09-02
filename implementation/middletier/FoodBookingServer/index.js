var mysql = require('mysql');
var config = require('./config.json');

const SQL_CONNECTION_POOL  = mysql.createPool({
    host     : config.dbhost,
    user     : config.dbuser,
    password : config.dbpassword,
    database : config.dbname
  });
  
const LIST_OF_FOOD_PATH = '/listoffood';
const INVALID_INPUT = buildResponse(400, {message: 'Invalid Input'});

exports.handler = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  switch(true) {
    case event.httpMethod === 'GET' && event.path === LIST_OF_FOOD_PATH:
      displayFood(event, callback);
      break;
      
    case event.httpMethod === 'POST' && event.path === LIST_OF_FOOD_PATH:
      selectFood(event, callback);
      break;
    
    default:
      callback(Error('API path', event.path, ' not found'));
  }
};

// inputs: user_id and theater_id
// outputs: list of food items available in the particular theater
//          OR INVALID_INPUTS error message
//          OR inability to connect to database error message
//          OR inability to query database error message
// function to get the list of available food items and their cost
function displayFood(event, callback) {
  if (event.queryStringParameters == null || 
    !("user_id" in event.queryStringParameters) || 
    !("theater_id" in event.queryStringParameters)) {
      return callback(null, INVALID_INPUT);
  } 
  var user_id = event.queryStringParameters.user_id;
  var theater_id = event.queryStringParameters.theater_id;
  if (isUserIdValid(user_id) && isTheaterIdValid(theater_id)) {
    let query = "SELECT * FROM FOODBEVERAGES WHERE theater_id = '" + theater_id + "'";
    var type = "food";
    console.log("query:"+ query)
    queryDatabase(query, function(queryResults) {
      var body = {[type]: queryResults};
      console.log(body)
      callback(null, buildResponse(200, body));
    });
  } else {
    return callback(null, INVALID_INPUT);
  }
}



//function to save the selected food item in the database 
function selectFood(event, callback) {
  if (event.queryStringParameters == null || 
    !("booking_id" in event.queryStringParameters) || 
    !("food_id" in event.queryStringParameters) ||
    !("quantity" in event.queryStringParameters)) {
      return callback(null, INVALID_INPUT);
  }
  var booking_id = parseInt(event.queryStringParameters.booking_id)
  var food_id = parseInt(event.queryStringParameters.food_id)
  var quantity = parseInt(event.queryStringParameters.quantity)
  var food_price = parseInt(event.queryStringParameters.food_price)
  if (isBookingIdValid(booking_id) && isFoodIdValid(food_id)) {
    console.log("Price of the food is" + food_price)
    var cost = (parseInt(food_price, 10)) * (parseInt(quantity, 10));
    console.log("Cost of the food is" + cost)
    console.log("food_id"+ food_id)
    console.log("quantity"+quantity)
    console.log("food_price" + food_price)
    
    let query="INSERT into FOOD_FOR_BOOKING (booking_id,food_id,quantity,cost) values ('"+booking_id+"','"+food_id+"','"+quantity+"','"+cost+"');"
    console.log(query)
    queryDatabase(query, function(queryResults) {
          var body = {message: "Sucess",
          cost: cost
          }
          callback(null, buildResponse(200, body));
        });
    
  } else {
    return callback(null, INVALID_INPUT);
  }
}

// function displayPickUpTimes(event, callback) {
//   if (event.queryStringParameters == null || 
//     !("show_id" in event.queryStringParameters) || 
//     !("booking_id" in event.queryStringParameters)) {
//       return callback(null, INVALID_INPUT);
//   }
//   var show_id = event.queryStringParameters.show_id;
//   var booking_id = event.queryStringParameters.booking_id;
//   if (isUserIdValid(show_id) && isBookingIdValid(booking_id)) {
//     let query = "SELECT show_id FROM BOOKINGS WHERE booking_id = '" + booking_id + "'";
//     queryDatabase(query, function(queryResults) {
//       var show_id = queryResults['show_id'];
//       let query2 = "SELECT start_time FROM SHOWS WHERE show_id = '" + show_id + "'";
//       queryDatabase(query2, function(queryResults) {
//         var start_time = queryResults["start_time"];
//         var body = {["pickup_time"]: start_time};
//         callback(null, buildResponse(200, body));
//       });
//     });
//   } else {
//     return callback(null, INVALID_INPUT);
//   }
// }

// function selectPickUpTimes(event, callback) {
//   if (event.queryStringParameters == null || 
//     !("booking_id" in event.queryStringParameters) || 
//     !("user_id" in event.queryStringParameters) ||
//     !("pickup_time" in event.queryStringParameters)) {
//       return callback(null, INVALID_INPUT);
//   }
//   var booking_id = event.queryStringParameters.booking_id;
//   //var user_id = event.queryStringParameters.user_id;
//   var pickup_time = event.queryStringParameters.pickup_time;
//   if (isBookingIdValid(booking_id)) {
//     let query = "UPDATE FOOD_FOR_BOOKING SET 'pickup_time'='" + pickup_time + "' WHERE booking_id='" + booking_id +"'";
//     var type = "pickup_time";
//     queryDatabase(query, function(queryResults) {
//       var body = {[type]: pickup_time};
//       callback(null, buildResponse(200, body));
//     });
//   } else {
//     return callback(null, INVALID_INPUT);
//   }
// }

// function to validate user id
function isUserIdValid(user_id) {
  if (isNaN(user_id) || parseInt(user_id, 10) < 1 || 
      parseInt(user_id, 10) > 100000) {
    return false;
  } else {
    return true;
  }
}

// function to validate theater id
function isTheaterIdValid(theater_id) {
  if (isNaN(theater_id) || parseInt(theater_id, 10) < 1 || 
      parseInt(theater_id, 10) > 100000) {
    return false;
  } else {
    return true;
  }
}

//function to validate booking id
function isBookingIdValid(booking_id) {
  if (isNaN(booking_id) || parseInt(booking_id, 10) < 1 || 
      parseInt(booking_id, 10) > 100000) {
    return false;
  } else {
    return true;
  }
}

//function to validate food_id
function isFoodIdValid(food_id) {
  if (isNaN(food_id) || parseInt(food_id, 10) < 1 || 
      parseInt(food_id, 10) > 100000) {
    return false;
  } else {
    return true;
  }
}

// inputs: query
// outputs: result of database query into callback
//          OR inability to connect to database error message
//          OR inability to query database error message
// function to connect and query the databse
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

// function to return response
function buildResponse(statusCode, body) {
  return {
    statusCode: statusCode,
    headers: {'Content-Type': 'application/json'},
    body:JSON.stringify(body)
  };
}


/*
function isTheaterIdValid(theater_id){
  
  if (isNaN(theater_id)) {
    return false;
  } else {
    let query = "SELECT * FROM THEATERS WHERE theater_id = " + theater_id + ";";
    console.log(query);
    return queryDatabase(query, function(queryResults) {
      console.log("is theater_id valid query results: ", queryResults);
      if (JSON.stringify(queryResults) == "[]") {
        console.log("entered invalid theater_id");
        return false;
      } else {
        console.log("entered valid theater_id");
        return true;
      }
      
      
    });
    
    
    
  }
}
*/
/*
function isUserIdValid(user_id){
  //The isNaN() outputs as True for a NaN value and 
  //returns False for a valid numeric value.
  
  if (isNaN(user_id)) {
    return false;
  } else {
    let query = "SELECT * FROM USERS WHERE user_id = " + user_id + ";";
    console.log(query);
    return queryDatabase(query, function(queryResults) {
      console.log("is userid valid query results: ", queryResults);
      if (JSON.stringify(queryResults) == "[]") {
        console.log("entered invalid user_id");
        return false;
      } else {
        console.log("entered valid user_id");
        return true;
      }
      
      
    });
  }
}
*/


