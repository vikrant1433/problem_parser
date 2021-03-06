#!/usr/bin/env bash
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
echo ${complete_url}
if [ -n "$problem_code" ]; then
#	if [[ "$current_folder" != "$contest_folder" ]]; then
#		mkdir -p ${contest_folder}
#    	cd ${contest_folder}
#	fi
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
    #parse testcases from website
#    echo "$url/${suffix}"
    wget ${complete_url} > /dev/null 2>&1
    #extract downloaded test cases
    unzip "${zip_testcase_folder_name}" > /dev/null 2>&1
    #calculate number of test cases
    num_tests=`ls -l input | wc -l`
    ((num_tests--))
    # creat c++ makefile
    bash ~/PycharmProjects/hackerrank/create_makefile.sh "${problem_code}" "${num_tests}"
    rm ${zip_testcase_folder_name}
    mv input/* .; rm input -r
    mv output/* .; rm output -r
else
    echo "usage: bash parse_problem_hackerrank.sh <url>"
fi

function rename_with_suffix {
cnt=0
file_pattern="${1}"
for file in ${file_pattern}; do
  # new=$(printf "%02d.jpg" "$a") #04 pad to length of 4
  ext="${file##*.}"
  base="${file%%[0-9]*}"
  ((cnt++))
  mv -- "$file" "${base}${cnt}.${ext}"
done
}


rename_with_suffix "input*.txt"
rename_with_suffix "output*.txt"