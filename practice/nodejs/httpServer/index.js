#!/usr/bin/node

const http = require("node:http")

const server = http.createServer((req, res) => {
    res.writeHead(200, {"content-Type": "text/plain"})
    res.end("<h1>i hear you :)<h1>")
});
server.listen(3000, () => {
    console.log("I'm listening...");
})
