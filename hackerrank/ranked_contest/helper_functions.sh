#!/usr/bin/env bash



function rename_files {
cnt=0
file_pattern="${1}"
for file in ${file_pattern}; do
  mv -- "$file" "_${file}"
done
}


function rename_with_suffix {
cnt=0
file_pattern="${1}"
for file in ${file_pattern}; do
  # new=$(printf "%02d.jpg" "$a") #04 pad to length of 4
  ext="${file##*.}"
  base="${file%%[0-9]*}"
  base=${base#_}
  ((cnt++))
  mv -- "$file" "${base}${cnt}.${ext}"
#  echo "renaming file _$file to ${base}${cnt}.${ext}"
done
}


function remove_input_output {
    rm input -rf
    rm output -rf
}

function create_cpp_template {
    echo "// ${url}" > ${problem_code}.cpp
    cat ~/PycharmProjects/hackerrank/templates/c++_template >> ${problem_code}.cpp
}

function delete_file {
    rm ${1} -f
}
function delete_folder {
    rm ${1} -fr
}