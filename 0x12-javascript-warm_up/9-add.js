#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2]) && isNaN(argv[3])) {
  console.log('NaN');
} else {
  console.log(parseInt(argv[2]) + parseInt(argv[3]));
}
