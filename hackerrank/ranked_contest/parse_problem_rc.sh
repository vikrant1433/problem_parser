#!/usr/bin/env bash
source ~/PycharmProjects/hackerrank/hackerrank/ranked_contest/helper_functions.sh
url="$1"
#url="https://www.hackerrank.com/contests/code-cpp-4/challenges/prettyprint"
#url="https://www.hackerrank.com/contests/mtech-cse-2016-practice-test-2/challenges/coin-change"

problem_code=${url##*\/}
echo "parsing ${problem_code}..."
contest_folder=`echo $url | rev | cut -d'/' -f3 | rev`
current_folder=`basename "$PWD"`
if [ ${contest_folder} != "www.hackerrank.com" ] && [ ${current_folder} != ${contest_folder} ]; then
    mkdir -p ${contest_folder}
    cd ${contest_folder}
fi

fourth=`echo $url | cut -d'/' -f4`

if [[ "$fourth" == "challenges" ]] ; then
    middle="rest/contests/master"
elif [[ "$fourth" == "contests" ]] ; then
    middle="rest"
else 
    echo "invalid url"
fi

first=`echo ${url} | cut -d'/' -f1-3`
second=`echo ${url} | cut -d'/' -f4-`
suffix="download_testcases"
complete_url="${first}/${middle}/${second}/${suffix}"
#echo ${complete_url}
if [ -n "$problem_code" ]; then
#	if [[ "$current_folder" != "$contest_folder" ]]; then
#		mkdir -p ${contest_folder}
#    	cd ${contest_folder}
#	fi
    mkdir -p ${problem_code}
    cd ${problem_code}
    #remove all previous test cases if already present

    remove_input_output


    #create c++ template
    if [ ! -f "${problem_code}.cpp" ]; then
        create_cpp_template
    fi
    #parse testcases from website
#    echo "$url/${suffix}"
#    wget ${complete_url} > /dev/null 2>&1
    # if download zip file is present in /tmp/ director then move it , extract it, create makefile, remove zip file, remove extracted contents
    zip_testcase_folder_name="${problem_code}-testcases.zip"
    if [[ -f  "/tmp/${zip_testcase_folder_name}" ]]; then

        cp /tmp/${zip_testcase_folder_name} "${PWD}/"
        #extract downloaded test cases
        unzip "${zip_testcase_folder_name}" > /dev/null 2>&1
        #calculate number of test cases
        num_tests=`ls -l input | wc -l`
        ((num_tests--))
        # creat c++ makefile
        bash ~/PycharmProjects/hackerrank/create_makefile.sh "${problem_code}" "${num_tests}"
        delete_folder ${zip_testcase_folder_name}
        mv input/* .;
        mv output/* .;
        remove_input_output
        rename_files "input*txt"
        rename_files "output*txt"
        rename_with_suffix "_input*.txt"
        rename_with_suffix "_output*.txt"
    else
        touch "input1.txt" "output1.txt"
        bash ~/PycharmProjects/hackerrank/create_makefile.sh "${problem_code}" 1
    fi
else
    echo "usage: bash parse_problem_hackerrank.sh <url>"
fi

