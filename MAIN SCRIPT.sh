#!/bin/bash

#Put this script in your crontabs according to the time interval you want the prices to be updated


python AirTIckethacksscript.py

for value in $(cat values.txt)
    min= $value
    
for values in $(cat value.txt)    
    if [ $values le $min ]
        min= $values
    fi
echo " found ticket worth - INR $values" | mail  yourmailaddress@abc.com
    fi    
    
exit



