'use strict';
Object.defineProperty(exports, "__esModule", {value: true});
const express = require("express");
const http = require("http");
const bodyParser = require("body-parser");
const sockjs = require("sockjs");

// App
const app = express();
app.use(bodyParser.json({limit: '5mb'}));
app.use(bodyParser.urlencoded({extended = false}));
app.use(function (req, res, next) {
  let err = new Error('Page not found');
  err.status = 404;
  next(err);
});

app.get('/url', (req, res, next) => {
  res.send('Hello World');
});



// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
