//Code that routes to appropriate html pages once requests comes in
const fs = require('fs');

exports.handler = (event, context, callback) => {
    var page = './' + event.path.substring(7) + '.html';
    
    console.log("Fetching '" + page + "'");
    fs.readFile(page, 'utf8', (err, data) => {
        if (err) { 
            console.log(err);
            callback(null, buildResponse(404, "Page not found."));
            return;
        }
        
        console.log("Found page");
        callback(null, buildResponse(200, data));
    });
};

function buildResponse(statusCode, body) {
    return {
        statusCode: statusCode,
        headers: { 'Content-Type': 'text/html' },
        body: body
    };
}
