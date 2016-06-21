#!/bin/bash

echo "What is the minimum price you expect"
read min

for values in $(cat value.txt)
    if [ $values le $min ]
        then  echo " found - INR $values"
    fi
    
