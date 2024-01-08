#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);
const fact = (n) => {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * fact(n - 1);
};

console.log(fact(num));
