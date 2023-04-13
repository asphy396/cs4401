i=0
while true
do
	echo "attempt $i"
	let i++
	./brute < expl 2>/dev/null
done
