#!/bin/bash
cd test
for file in *
do
if [ ${file: -4} == ".csv" ]
then
	echo "test/${file}"
fi
done

