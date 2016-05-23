#!/usr/bin/env bash
problem_code=${1}
num_tests=${2}
sed "s/file_name/${problem_code}/g" ~/PycharmProjects/hackerrank/templates/makefile_template  > makefile_tmp
bash ~/PycharmProjects/hackerrank/make.sh ${problem_code} ${num_tests}
