#!/usr/bin/env bash
url="$1"
problem_code=${url##*\/}
#echo "url = $url"
echo "parsing ${problem_code} ..."
contest_folder=`echo $url | rev | cut -d'/' -f3 | rev`
current_folder=`basename "$PWD"`
#echo "contest_folder = $contest_folder"
#echo "current_folder = ${current_folder}"
if [ -n "$problem_code" ]; then
	if [[ "$current_folder" != "$contest_folder" ]]; then
		mkdir -p ${contest_folder}
    	cd ${contest_folder}
	fi
    mkdir -p ${problem_code}
    cd ${problem_code}

    #remove all previous test cases if already present
    rm input* -f
    rm output* -f

    #create c++ template
    if [ ! -f "${problem_code}.cpp" ]; then
        echo "// ${url}" > ${problem_code}.cpp
        cat ~/PycharmProjects/hackerrank/templates/c++_template >> ${problem_code}.cpp
    fi

#
#    #create c++ template
#    echo "// ${url}" > ${problem_code}.cpp
#    cat ~/PycharmProjects/hackerrank/templates/c++_template > ${problem_code}.cpp

    #parse testcases from website
    /home/vikrant/.py_envs/env_scrapping/bin/python3.4 ~/PycharmProjects/hackerrank/codeforces/codeforces.py "${url}"
    # creat c++ makefile
    num_tests=`cat num_tests`
    bash ~/PycharmProjects/hackerrank/create_makefile.sh ${problem_code} ${num_tests}
    rm num_tests
else
    echo "usage: bash parse_problem_codechef.sh <url>"
fi