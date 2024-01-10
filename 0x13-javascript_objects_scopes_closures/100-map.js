#!/usr/bin/node
const list = require('./100-data').list;
list.map((x, i) => (list[i] = x * i));
