#!/usr/bin/node
exports.logMe = function (item) {
  for (let i = 0; i < item; i++) {
    console.log(`${i}: ${arguments[i + 1]}`);
  }
};
