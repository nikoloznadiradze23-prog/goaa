const express = require("express");
const app = express();

function logRequest(req, res, next) {
    console.log("request resived");
    res.send("Main Data");
}

app.use(logRequest);

app.get("/info", (req, res) => {
    console.log("request resived");
    res.send("Information");
});

app.get("/", (req, res) => {
    res.send("Main Data");
});

app.listen(3000);

app.get("/", (req, res) => {
    console.log("request ")
    res.send("Main Data")
})

app.get("/info", (req, res, next) => {
    console.log("information")
})

app.get("/info/:id", (req, res) => {
    res.send(`information ${req.params.id}`)
})

function checkadmin (req, res, next) {
    if (req.query.user === "user") {
        res.admin = true
        next()
    } else {
        res.send("not authorised")
    }
}

app.listen(3000, () => console.log("running"))
