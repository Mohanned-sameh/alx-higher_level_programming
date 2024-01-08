#!/usr/bin/node
// prints the second argument passed to it
const { argv } = require('process');
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
