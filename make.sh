#!/usr/bin/env bash
cat makefile_tmp > makefile
rm makefile_tmp
num_tests=$2
#echo "num_tests = $num_tests"
problem_code=$1
function write_test {
text=`cat << EOM
test${1}: all
\t@./${problem_code} < input${1}.txt > out_ref
\t-@diff -wy --suppress-blank-empty output${1}.txt out_ref >/dev/null ;\\\\\\\\
\tif [ \\$\\$? -eq 0 ] ; then \\\\\\\\
\t\techo "\\${green}TEST CASE#${1} PASS\\${reset}" ;\\\\\\\\
\telse \\\\\\\\
\t\techo "\\${red}TEST CASE#${1} FAILED\\${reset}" ;\\\\\\\\
\t\techo "input:" ;\\\\\\\\
\t\thead input${1}.txt ;\\\\\\\\
\t\techo ;\\\\\\\\
\t\techo "expected output" ;\\\\\\\\
\t\tcat output${1}.txt ;\\\\\\\\
\t\techo ;\\\\\\\\
\t\techo "your output" ;\\\\\\\\
\t\tcat out_ref ;\\\\\\\\
\t\techo;\\\\\\\\
\tfi
EOM
`
echo -e "$text" >> makefile
}
if [ ${num_tests} -ne 0 ]; then
    test_all="testall: all "
    for (( i = 1; i <= ${num_tests}; i++ )); do
        test_all="${test_all}test${i} "
    done
    echo "$test_all" >> makefile
fi

#echo "	@echo \"testing all test cases\"" >> makefile
for (( i = 1; i <= ${num_tests}; i++ )); do
	write_test ${i}
done
clean_text=`cat << EOM
clean:
\trm *o ${problem_code} out_ref 2>/dev/null || true
EOM
`
echo -e "$clean_text" >> makefile