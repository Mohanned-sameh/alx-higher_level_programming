#!/usr/bin/node
exports.logMe = function (item) {
  for (const element in item) {
    console.log(element + ': ' + item[element]);
  }
};
