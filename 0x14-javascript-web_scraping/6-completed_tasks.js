#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const tasks = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (tasks[task.userId] === undefined) {
          tasks[task.userId] = 1;
        } else {
          tasks[task.userId]++;
        }
      }
    }
    console.log(tasks);
  }
});
