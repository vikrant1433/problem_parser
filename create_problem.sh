#!/usr/bin/env bash

problem_code=${1}
num_tests=${2}
mkdir -p ${problem_code}
cd ${problem_code}
#create c++ file
cat ~/PycharmProjects/hackerrank/templates/c++_template > ${problem_code}.cpp

#create input output files
for (( i = 1; i <= ${num_tests} ; i++)) ; do
    touch input${i}.txt output${i}.txt
done

#create make file
bash ~/PycharmProjects/hackerrank/create_makefile.sh ${problem_code} ${num_tests}

