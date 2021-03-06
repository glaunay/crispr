#!/usr/bin/env python3
"""
Test for specific Gene script. Use the Blast output and the output of setCompare from the folder
test/data/sg
The total number of sgRNA is 28
"""

import os
import sys
import json
import difflib


if __name__ == '__main__':
    gi = "Enterobacter sp. 638 GCF_000016325.1&Candidatus Blochmannia vafer str. BVAF GCF_000185985.2"
    os.system("python -u bin/parse_blast.py -blast test/data/sg/blast.xml -gi \"" + gi + "\" -o test/parse_blast.p -ip 70")
    os.system("python -u bin/specific_gene.py -f test/data/sg/output_c.txt -sl 20 -pam \"NGG\" -gi \"" + gi + "\" -gni \"\" -r " + sys.argv[1] + "  -c 2000 --no-proxy -blast test/parse_blast.p")

    res = json.load(open("results.json", "r"))
    # Check if the total number of sgRNA is correct
    if len(res) != 28:
        sys.exit("Problem with Specific Gene test")

    # Check if found sequences are corect
    res = open("results.json", "r")
    ref = open("test/data/sg/results.json", "r")

    diff = difflib.ndiff(res.readlines(), ref.readlines())
    delta = ''.join(x[2:] for x in diff if x.startswith('- ') or x.startswith("+ "))

    if delta:
        sys.exit("Problem with Specific Gene test")
