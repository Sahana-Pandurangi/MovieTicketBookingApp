// Code to connect to the database
var mysql = require('mysql');
var config = require('./config.json');

const SQL_CONNECTION_POOL  = mysql.createPool({
    host     : config.dbhost,
    user     : config.dbuser,
    password : config.dbpassword,
    database : config.dbname
  });
  
const LIST_OF_CITIES_PATH = '/listofcities';
const ADD_NEW_USER_PATH = '/addnewuser';
const LIST_OF_THEATERS_PATH = '/listoftheaters';
const LIST_OF_MOVIES_PATH = '/listofmovies';
const GET_USER_PATH = '/getuser';

//Code to direct requests to an endpoint
exports.handler = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;

  console.log('Request event: ', event);
  switch(true) {
    case event.httpMethod === 'POST' && event.path === ADD_NEW_USER_PATH:
      console.log('Adding a new user to the database');
      addNewUser(event, callback);
      break;
    
    case event.httpMethod === 'GET' && event.path === LIST_OF_CITIES_PATH:
      console.log('Getting list of citites.');
      displayCity(event, callback);
      break;
      
    case event.httpMethod === 'POST' && event.path === LIST_OF_CITIES_PATH:
      console.log('Updating the database with the selected city');
      selectCity(event, callback);
      break;
    
    case event.httpMethod === 'GET' && event.path === LIST_OF_THEATERS_PATH:
      console.log('Getting list of theaters by cities.');
      displayTheatersInCity(event, callback);
      break;
    
    case event.httpMethod === 'POST' && event.path === LIST_OF_THEATERS_PATH:
      console.log('Updating the database with the selected theater');
      selectTheaters(event, callback);
      break;
    
    case event.httpMethod === 'GET' && event.path === LIST_OF_MOVIES_PATH:
      console.log('Getting list of movies now showing the selected theater');
      displayMoviesInTheater(event, callback);
      break;
      
    case event.httpMethod === 'GET' && event.path === GET_USER_PATH:
      console.log('Getting user details.');
      getUser(event, callback);
      break;
  
    default:
      console.log('Could not find path: ', event.path);
      callback(Error('API path', event.path, ' not found'));
  }
};

// function to get the user details from the database
function getUser(event, callback) {
  if (event.queryStringParameters == null || typeof event.queryStringParameters.user_id === 'undefined') {
    console.log("User input : " + event + " is incomplete, returning...");
    callback(null, buildResponse(400, { "message": "Invalid Input" }));
    return;
  }
  
  var user_id = event.queryStringParameters.user_id
  console.log("Received request to get user: " + user_id);
  
  const GET_USER = "SELECT * FROM USERS WHERE user_id = " + user_id;
  console.log("Final query to fetch user: " + GET_USER);
  queryDatabase(GET_USER, function(queryResults) {
    console.log("Successfully queried for user.");  
    
    var user = {};
    if (queryResults.length > 0) {
      user = {
        "user_id": queryResults[0].user_id,
        "first_name": queryResults[0].first_name,
        "second_name": queryResults[0].second_name,
        "email": queryResults[0].email,
        "phone": queryResults[0].phone,
        "created_at": queryResults[0].created_at,
        "city_code": queryResults[0].city_code
      };
    }
    callback(null, buildResponse(200, { "user": user }));
  });
}

//Function to register/add a new user
function addNewUser(event, callback) 
{
  var customer_user_id ,first_name, second_name,email, phone = null
  if (event.queryStringParameters != null)
    {
      getUserId(function (queryResults) 
      {
        customer_user_id = parseInt(queryResults[0].user_id) + 1
        first_name = event.queryStringParameters.first_name
        second_name = event.queryStringParameters.second_name
        email = event.queryStringParameters.email
        phone = parseInt(event.queryStringParameters.phone)
        console.log("the phone number is:")
        console.log(phone)
        var query = "INSERT into USERS (user_id,first_name,second_name,phone,email) values ('"+customer_user_id+"','"+first_name+"','"+second_name+"','"+phone+"','"+email+"');"
        console.log("the query is: " + query)
        queryDatabase(query, function(queryResults) {
          var body = {message: "Sucessfully added the user to the database",
            user_id: customer_user_id
          }
          callback(null, buildResponse(200, body));
        });
      });
    }
  else
  {
    const body = {message: 'Invalid Input'}
    return callback(null, buildResponse(400, body));
  }
}

// Function to get userid
function getUserId(callback) {
  queryDatabase("SELECT MAX(user_id) as user_id FROM USERS;", function(queryResults) {
    callback(queryResults);
  });
}
// function to display cities
function displayCity(event,  callback)
{
  if (event.queryStringParameters != null)
  {
    let user_id
    if (("user_id" in event.queryStringParameters) == true)  
      {
        user_id = event.queryStringParameters.user_id
        if (isUserIdValid(user_id) == true)
        {
          console.log(user_id)
          let query = 'SELECT * from CITIES'
          var type = "city"
          queryDatabase(query, function(queryResults) {
          var body = {[type]: queryResults}
          callback(null, buildResponse(200, body));});
        }
        else
        {
          const body = {
            message: 'Invalid Input'}
          return callback(null, buildResponse(400, body));
        }
      }
  }
  else
  {
    const body =
    {
      message: 'Invalid Input'
    }
    return callback(null, buildResponse(400, body));
  }
}

// function to select cities
function selectCity(event,callback)
{
  if (event.queryStringParameters != null)
  {
    let user_id, city_code
    if (("user_id" in event.queryStringParameters) == true && ("city_code" in event.queryStringParameters) == true)  
      {
        user_id = event.queryStringParameters.user_id
        city_code = event.queryStringParameters.city_code
        if (isUserIdValid(user_id) == true && isCityCodeValid(city_code) == true)
        {
          let query = "UPDATE USERS SET city_code = '"+city_code+"' WHERE user_id = '"+user_id+"'"
          var type = "city"
          queryDatabase(query, function(queryResults) {
            console.log("The query results for the database")
            console.log(queryResults)
          });
          query = "SELECT * FROM CITIES WHERE city_code = '"+city_code+"'"
          queryDatabase(query, function(queryResults) {
            var body = {[type]: queryResults}
            callback(null, buildResponse(200, body));
          });
        }
        else
        {
          const body = {
            message: 'Invalid Input'}
          return callback(null, buildResponse(400, body));
        }
      }
  }
  else
  {
    const body =
    {
      message: 'Invalid Input'
    }
    return callback(null, buildResponse(400, body));
  }
}

// function to display theaters in the selected city
function displayTheatersInCity(event,callback)
{
  if (event.queryStringParameters != null)
  {
    let user_id, city_code
    if (("user_id" in event.queryStringParameters) == true && ("city_code" in event.queryStringParameters) == true)  
      {
        user_id = event.queryStringParameters.user_id
        city_code = event.queryStringParameters.city_code
        if (isUserIdValid(user_id) == true && isCityCodeValid(city_code) == true)
        {
          
          let query = "SELECT * FROM THEATERS WHERE city_code = '"+city_code+"'"
          var type = "theater"
          queryDatabase(query, function(queryResults) {
            console.log("The query results for the database")
            console.log(queryResults)
            var body = {[type]: queryResults}
            callback(null, buildResponse(200, body));
          });
        }
        else
        {
          const body = {
            message: 'Invalid Input'}
          return callback(null, buildResponse(400, body));
        }
      }
  }
  else
  {
    const body =
    {
      message: 'Invalid Input'
    }
    return callback(null, buildResponse(400, body));
  }
  
}

// function to select theater
function selectTheaters(event, callback){
  if (event.queryStringParameters != null)
  {
    let user_id, theater_id
    if (("user_id" in event.queryStringParameters) == true && ("theater_id" in event.queryStringParameters) == true)  
      {
        user_id = event.queryStringParameters.user_id
        theater_id = event.queryStringParameters.theater_id
        if (isUserIdValid(user_id) == true && isTheaterIdValid(theater_id) == true)
        {
          let query = "SELECT * FROM THEATERS WHERE theater_id = '"+theater_id+"'"
          var type = "theater"
          queryDatabase(query, function(queryResults) {
            console.log("The selected movies are:")
            console.log(queryResults)
            var body = {[type]: queryResults}
            callback(null, buildResponse(200, body));
          });
        }
        else
        {
          const body = {
            message: 'Invalid Input'}
          return callback(null, buildResponse(400, body));
        }
      }
  }
  else
  {
    const body =
    {
      message: 'Invalid Input'
    }
    return callback(null, buildResponse(400, body));
  }
  
}

// function to display movies in the selected theater
function displayMoviesInTheater(event, callback){
  if (event.queryStringParameters != null)
  {
    let user_id,theater_id
    if (("user_id" in event.queryStringParameters) == true && ("theater_id" in event.queryStringParameters) == true)  
      {
        user_id = event.queryStringParameters.user_id
        theater_id = event.queryStringParameters.theater_id
        if (isUserIdValid(user_id) == true  && isTheaterIdValid(theater_id) == true)
        {
          let query = "SELECT DISTINCT movie_id FROM SHOWS WHERE theater_id = '"+theater_id+"'"
          var type = "movie"
          var list_movies = []
          queryDatabase(query, function(queryResults) {
            var movies_query = "SELECT * FROM MOVIES WHERE movie_id IN (";
            var movie_ids = "";
            for (let i = 0; i < queryResults.length; i++) {
              if (i != 0) {
                movie_ids += ", ";
              }
              movie_ids += queryResults[i].movie_id;
            }
            movies_query = movies_query + movie_ids+ ")";
            queryDatabase(movies_query, function(queryResults) {
            var body = {[type]: queryResults}
            callback(null, buildResponse(200, body));
          });
          });
        }
        else
        {
          const body = {
            message: 'Invalid Input'}
          return callback(null, buildResponse(400, body));
        }
      }
  }
  else
  {
    const body =
    {
      message: 'Invalid Input'
    }
    return callback(null, buildResponse(400, body));
  }
}


// Function to validate theater id
function isTheaterIdValid(theater_id){
  if ((isNaN(theater_id)) || (parseInt(theater_id) > 5)) {
    return false
  }
  return true
}

// function to validate city code
function isCityCodeValid(city_code){
  if ((isNaN(city_code)) || (parseInt(city_code) > 10)) {
    return false
  }
  return true
}

//function to validate userid
function isUserIdValid(user_id){
  //The isNaN() outputs as True for a NaN value and 
  //returns False for a valid numeric value.
  if ((isNaN(user_id)) || (parseInt(user_id) > 100000)) {
    return false
  }
  return true
}

// function to query database
function queryDatabase(query, callback) {
  SQL_CONNECTION_POOL.getConnection(function(err, connection) {
    if (err) {
      throw Error("Failed to connect to database.", err);
    }

    connection.query(query, function (error, results) {
      connection.release();
      if (error) {
        throw Error("Failed to query database.", error);
      }
      callback(results);
    });
  });
}

// function to build response
function buildResponse(statusCode, body) {
  return {
    statusCode: statusCode,
    headers: {
      'Content-Type': 'application/json'
    },
    body:JSON.stringify(body)
  };
}