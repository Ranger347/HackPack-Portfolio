#!/bin/bash

filename=$1

rm -r tmp
mkdir tmp

cp $filename tmp

cd tmp

file $filename

while [ 1 ]
do

	file $filename | grep "gzip"
	if [ "$?" -eq "0" ]
	then
		echo "This is a gzip file"
		mv $filename $filename.gz
		gzip -d $filename.gz	
		filename=$(ls *)
	fi

	file $filename | grep "bzip2"
	if [ "$?" -eq "0" ]
	then
		echo "This is a bzip2 file"
		mv $filename $filename.bz2
		bzip2 -d $filename.bz2
		filename=$(ls *)
	fi

	file $filename | grep "tar"
	if [ "$?" -eq "0" ]
	then
		echo "This is a tar file"
		tar -xf $filename
		rm $filename
		filename=$(ls *)
	fi

	file $filename | grep "ASCII"
	if [ "$?" -eq "0" ]
	then
		echo "This is a text file"
		mv $filename flag.txt
		break
	fi
done

