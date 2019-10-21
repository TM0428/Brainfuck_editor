import sys
import os

variable = set()

args = sys.argv
#args[1] is file name

if len(args) != 2:
    print('Error: Invalid command', file=sys.stderr)
    sys.exit(1)

with open(args[1]) as f:
    while True:
        s_line = f.readline()
        #EOF
        if not s_line:
            break
        s_line = s_line.replace('\n','').split(' ')
        #s_line[0] is command
        #CAUTION:
        #s_line[len(s_line)-1] is include '\n'
        print(s_line)
        if s_line[0] == "Var":
            for Text in s_line[1:]:
                variable.add(Text)
            print(variable)