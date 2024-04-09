#!/usr/bin/node
const argnum = process.argv.length - 2
if (argnum === 0)
{
	console.log('No argument');
}
else if (argnum === 1)
{
	console.log('Argument found');
}
else if (argnum > 1)
{
	console.log('Arguments found');
}
