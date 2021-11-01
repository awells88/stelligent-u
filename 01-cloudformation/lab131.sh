#!/bin/bash

echo $1

jq -c -r ".regions[]" regions.json | while read i; do
	echo "Creating bucket for region: $i"
	#aws cloudformation delete-stack --stack-name andrewwellsm01x131 --region $i &
	aws cloudformation create-stack --stack-name andrewwellsm01x131 --template-body file://template131.yml --parameters file://parameters131.json --region $i &
done

