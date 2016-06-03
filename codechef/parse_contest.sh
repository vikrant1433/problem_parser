#!/usr/bin/env bash
url=${1}
contest_folder=`echo ${url} | rev | cut -d'/' -f1 | rev`
echo "parsing ${contest_folder} please wait..."
mkdir -p ${contest_folder}
cd ${contest_folder}
problem_link_file="problem_links"
/home/vikrant/.py_envs/env_scrapping/bin/python3.4 /home/vikrant/PycharmProjects/hackerrank/codechef/parse_codechef_contest.py "${url}" > ${problem_link_file}

while IFS='' read -r problem_link || [[ -n "${problem_link}" ]]; do
    bash /home/vikrant/PycharmProjects/hackerrank/codechef/parse_codechef_problem.sh "${problem_link}"
done < "${problem_link_file}"

rm -f "${problem_link_file}"