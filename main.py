import sys
import os
import logic

class Brainfuck:
    """
    piv is memory number.
    length is len(variable)
    """
    variable = ["Res"]
    piv = 0
    length = 1

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


args = sys.argv
#args[1] is file name
if __name__ == "__main__":
    brainfuck = Brainfuck()
    #ERROR
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
                """
                This is declaring variables
                >Var a b c
                """
                for Text in s_line[1:]:
                    #used variable
                    if Text in brainfuck.variable:
                        print('File "' + args[1] + '", line ' + str(line) +'\nError: Variable "' + Text + '" is used.', file=sys.stderr)
                        sys.exit(1)
                    brainfuck.variable.append(Text)
                #Debug
                #print(brainfuck.variable)
                brainfuck.length = len(brainfuck.variable)
            elif s_line[0] == "Inc":
                """
                hoge
                """
            elif s_line[0] == "Add":
                """
                This is add function
                >Add a b c
                >Add a 10
                its mean "c=a+b", but 'c' doesn't have to write. 
                if you don't write, the value is in the variable "Res"
                """
                input_dec = brainfuck.variable.index(s_line[1])
                if is_integer(s_line[2]):
                    output += logic.add_num(brainfuck, input_dec,int(s_line[2]))
            elif s_line[0] == "Mul":
                """
                This is add function
                >Add a b c
                >Add a 10
                its mean "c=a+b", but 'c' doesn't have to write. 
                if you don't write, the value is in the variable "Res"
                """
                input_dec = brainfuck.variable.index(s_line[1])
                if is_integer(s_line[2]):
                    output += logic.mul_num(brainfuck, input_dec,int(s_line[2]))
            elif s_line[0] == "Scan":
                """
                This is scan function
                >Scan Int a
                >Scan Char a
                this function has two mode(int or char).
                """
                if s_line[1] == "Int":
                    input_dec = brainfuck.variable.index(s_line[2])
                    output += logic.input(brainfuck, input_dec)
                else:
                    input_dec = brainfuck.variable.index(s_line[2])
                    output += logic.input(brainfuck, input_dec,1)
            elif s_line[0] == "Print":
                """
                This is print function
                >Print Int a
                >Print Char a
                this function has two mode(int or char).
                """
                if s_line[1] == "Int":
                    input_dec = brainfuck.variable.index(s_line[2])
                    output += logic.output(brainfuck, input_dec)
                else:
                    input_dec = brainfuck.variable.index(s_line[2])
                    output += logic.output(brainfuck, input_dec,1)
            #Debug
            #print(brainfuck.piv)

            line += 1
        print(output)