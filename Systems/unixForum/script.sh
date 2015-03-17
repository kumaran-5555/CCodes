logFile=$1

while [ 1 ]
do
	curr=`wc -l $logFile`
	if [ "$curr" != "$prev" ]
	then
		echo "Command to execute"
	fi
	prev=$curr
	sleep 1

done

