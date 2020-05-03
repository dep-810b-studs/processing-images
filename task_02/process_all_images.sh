#!/bin/bash

for filename in ./training/*.tif; do
	echo "file $filename processed"
	python ./task_02.py "-i" "$filename"
done