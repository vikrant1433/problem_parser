#!/usr/bin/env bash
url="$1"
problem_code=${url##*\/}
#url="codeforces.com/contest/675/problem/A"
#echo "url = $url"
site=`echo ${url} | cut -d'/' -f3 | cut -d'.' -f2`
#echo "site = $site"

contest_folder=`echo $url | rev | cut -d'/' -f3 | rev`
current_folder=`basename "$PWD"`
if [ -n "$problem_code" ]; then
	if [[ "$current_folder" != "$contest_folder" ]]; then
		mkdir -p ${contest_folder}
    	cd ${contest_folder}
	fi
    mkdir -p ${problem_code}
    cd ${problem_code}
#    touch $problem_code.cpp
    cat ~/PycharmProjects/hackerrank/c++_template > ${problem_code}.cpp
    if [[ ${site} == "codechef" ]]; then
#        echo "codechef running"
        /home/vikrant/.py_envs/env_scrapping/bin/python3.4 ~/PycharmProjects/hackerrank/codechef.py ${url}
    elif [[ ${site} == "codeforces" ]]; then
        /home/vikrant/.py_envs/env_scrapping/bin/python3.4 ~/PycharmProjects/hackerrank/codeforces.py ${url}
    else
        echo "else is running"
    fi 
    sed "s/file_name/${problem_code}/g" ~/PycharmProjects/hackerrank/makefile_template  > makefile_tmp
    num_tests=`cat num_tests`
    bash ~/PycharmProjects/hackerrank/make.sh ${problem_code} ${num_tests}
    rm num_tests
#    cd $problem_code
    subl .
else
    echo "usage: bash create.sh <program name>"
fi