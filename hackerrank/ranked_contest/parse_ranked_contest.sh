#!/usr/bin/env bash
contest_url=${1}
problem_link_file="problem_links"
echo "parsing contest please wait..."
#https://www.hackerrank.com/domains/algorithms/graph-theory
#https://www.hackerrank.com/contests/code-cpp-4/challenges
#https://www.hackerrank.com/contests/mtech-cse-2016-practice-test-1/challenges
url_without_challenge=${contest_url%/challenges}
path=`echo ${url_without_challenge} | cut -d'/' -f5-6`
mkdir -p ${path}
cd ${path}
/home/vikrant/.py_envs/env_scrapping/bin/python3.4 ~/PycharmProjects/hackerrank/hackerrank/ranked_contest/hackerrank_rc.py "${contest_url}" > ${problem_link_file}
while IFS='' read -r problem_link || [[ -n "${problem_link}" ]]; do
    bash /home/vikrant/PycharmProjects/hackerrank/hackerrank/ranked_contest/parse_problem_rc.sh "${problem_link}"
done < "${problem_link_file}"

rm -f "${problem_link_file}"
rm -f ghostdriver.log
