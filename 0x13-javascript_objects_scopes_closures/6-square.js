#!/usr/bin/node
const Square = require('5-square.js');
Class Square extends Square {
	constructor(size) {
		super(size, size)
	}
	charPrint(c) {
		for (i = 0; i < size; i++) {
			row = ''
			for (i = 0; i < size; i++) {
				row = row + 'C'
			}
			console.log(row)
		}
	}
}
