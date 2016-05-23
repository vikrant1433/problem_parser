#!/usr/bin/env bash
url=${1}
site=`echo ${url} | cut -d'/' -f3 | rev | cut -d'.' -f2 | rev`

problem_code=${url##*\/}
echo "parsing problem ${problem_code} ...."
bash ~/PycharmProjects/hackerrank/${site}/parse_${site}_problem.sh "${url}"