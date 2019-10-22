import sys
import os
import logic

class Brainfuck:
    """
    piv is memory number.
    length is len(variable)
    """
    variable = []
    piv = 0
    length = 0

args = sys.argv
#args[1] is file name
if __name__ == "__main__":
    brainfuck = Brainfuck()
    if len(args) != 2:
        print('Error: Invalid command', file=sys.stderr)
        sys.exit(1)
    with open(args[1]) as f:
        output = ""
        line = 1
        while True:

            s_line = f.readline()
            #EOF
            if not s_line:
                break
            s_line = s_line.replace('\n','').split(' ')
            #s_line[0] is command
            #Debug
            #print(s_line)
            if s_line[0] == "Var":
                for Text in s_line[1:]:
                    #used variable
                    if Text in brainfuck.variable:
                        print('File "' + args[1] + '", line ' + str(line) +'\nError: Variable "' + Text + '" is used.', file=sys.stderr)
                        sys.exit(1)
                    brainfuck.variable.append(Text)
                #Debug
                #print(brainfuck.variable)
                brainfuck.length = len(brainfuck.variable)
            elif s_line[0] == "Set":
                """
                hoge
                """
                input_dec = brainfuck.variable.index(s_line[1])
                output += logic.int_input(brainfuck, input_dec)
            elif s_line[0] == "Inc":
                """
                hoge
                """
            elif s_line[0] == "Print":
                input_dec = brainfuck.variable.index(s_line[1])
                output += logic.int_output(brainfuck, input_dec)
            #Debug
            #print(brainfuck.piv)

            line += 1
        
        print(output)