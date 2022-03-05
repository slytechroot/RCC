#!/bin/bash
# Bash script example for if, while, for, until, etc. 
# Created by Attila Kun for the CIS-21A-45405 Linux Class
 
# Make Directory for ping.txt results
mkdir ~/Desktop/syslog

# Ping Google DNS IP to check Internet connectivity
ping -c4 8.8.8.8 > ~/Desktop/syslog/ping.txt

# Sleep option to test manual delete of ping file to test if condition for exit breakout
#sleep 10

# Check for ping file 
if [ -e ~/Desktop/syslog/ping.txt ]
then
	echo "Permissions are working. Ping file will exist." | tr 'a-z' 'A-Z'
else
	echo "Permissions failed. Ping file will NOT exist. Exiting..."
	exit
fi

# Print successful ping header
for file in ~/Desktop/syslog/ping.txt 
do
	head -n 2 $file
done

# Check if ping.txt exists. Check condition. 
echo "You MUST  delete ping.txt manually to test this while condition and output echo result..."
echo "You have 10 seconds..."
sleep 10
while [ ! -f "$file" ]
do
	echo "The ping.txt file has been manually deleted. "
	break
done

# Echo task ended. 
echo Tasks Completed!!!













