#!/usr/bin/env bash
url=${1}
site=`echo ${url} | cut -d'/' -f3 | rev | cut -d'.' -f2 | rev`
link_file="links"
#echo $site
if [ ${site} == "codechef" ]; then
#    echo "running chef"
    /home/vikrant/.py_envs/env_scrapping/bin/python3.4 ~/PycharmProjects/hackerrank/parse_codechef_contest.py ${url} > "${link_file}"
elif [ ${site} == "codeforces" ]; then
#    echo "running forces"
    /home/vikrant/.py_envs/env_scrapping/bin/python3.4 ~/PycharmProjects/hackerrank/parse_codeforces_contest.py ${url} > "${link_file}"
else
    :
fi

while IFS='' read -r line || [[ -n "$line" ]]; do
    bash ~/PycharmProjects/hackerrank/parse_problem.sh ${line}
done < "${link_file}"


#echo "hecat llo"