const express = require("express");
const app = express();
const port = 80;

app.get("/api/hello", (request, response) => {
  const name = request.query["name"];
  response.send(`Hello ${name}`);
});

app.listen(port, () => {
  console.log(`Express.js greeting app listening on port ${port}`);
});
