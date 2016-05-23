#!/usr/bin/env bash
url=${1}
site=`echo ${url} | cut -d'/' -f3 | rev | cut -d'.' -f2 | rev`

link_file="links"
#echo "site = ${site}"

/home/vikrant/.py_envs/env_scrapping/bin/python3.4 ~/PycharmProjects/hackerrank/${site}/parse_${site}_contest.py "${url}" > "${link_file}"

while IFS='' read -r line || [[ -n "$line" ]]; do
    bash ~/PycharmProjects/hackerrank/parse_problem.sh "${line}"
done < "${link_file}"
rm "${link_file}"

