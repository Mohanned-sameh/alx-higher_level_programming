#!/usr/bin/node
// script that searches the second biggest integer in the list of args
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
