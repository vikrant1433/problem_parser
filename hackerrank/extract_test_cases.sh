#!/usr/bin/env bash
function run {
	i=1
	for file in *; do
		newfilename=`echo $file | sed -r "s/[0-9]+//"`
		ext=${newfilename##*.}
		base=${newfilename%%.*}
		newfilename=$base${i}.$ext
		mv $file $newfilename
		printf '\n' >> $newfilename
		((i++))
	done

}
file_to_extract=`ls *.zip`
# echo $file_to_extract
unzip $file_to_extract
cd output
run
cd ../input
run