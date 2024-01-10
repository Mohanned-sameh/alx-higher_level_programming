#!/usr/bin/node
const fs = require('fs').promises;
const argv = require('process').argv;
const file = argv[2];
const content = argv[3];
fs.writeFile(file, content).catch((err) => console.log(err));
