#!/usr/bin/node
// reverse a list
exports.eserver = function (list) {
  list.reduceRight((a, b) => {
    a.push(b);
    return a;
  });
};
