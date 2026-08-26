const express = require('express');
const server = express();
server.get("/" , (req, res) => {
    res.send("hello user")
});
server.listen(3000,() => {console.log('server is on')})