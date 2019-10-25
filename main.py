import sys
import os
import logic

class Brainfuck:
    """
    piv is memory header.
    length is len(variable)
    """
    variable = ["Res"]
    piv = 0
    length = 1
    output = ""
    in_else = 0

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def judge(bf, s_line, line):
    if s_line[0] == "Var":
        """
        This is declaring variables
        >Var a b c
        """
        for Text in s_line[1:]:
            #used variable
            if Text in bf.variable:
                print('File "' + args[1] + '", line ' + str(line) +'\nError: Variable "' + Text + '" is used.', file=sys.stderr)
                sys.exit(1)
            bf.variable.append(Text)
        bf.length = len(bf.variable)
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
        input_dec = bf.variable.index(s_line[1])
        if is_integer(s_line[2]):
            bf.output += logic.add_num(bf, input_dec,-1,int(s_line[2]))
        else:
            input_dec1 = bf.variable.index(s_line[2])
            bf.output += logic.add_num(bf,input_dec,input_dec1,None)
    elif s_line[0] == "Mul":
        """
        This is mul function
        >Add a b c
        >Add a 10
        its mean "c=a+b", but 'c' doesn't have to write. 
        if you don't write, the value is in the variable "Res"
        """
        input_dec = bf.variable.index(s_line[1])
        if is_integer(s_line[2]):
            bf.output += logic.mul_num(bf, input_dec, -1, int(s_line[2]))
        else:
            input_dec1 = bf.variable.index(s_line[2])
            bf.output += logic.mul_num(bf, input_dec, input_dec1, None)
    elif s_line[0] == "Scan":
        """
        This is scan function
        >Scan Int a
        >Scan Char a
        this function has two mode(int or char).
        """
        if s_line[1] == "Int":
            input_dec = bf.variable.index(s_line[2])
            bf.output += logic.input(bf, input_dec)
        else:
            input_dec = bf.variable.index(s_line[2])
            bf.output += logic.input(bf, input_dec,1)
    elif s_line[0] == "Print":
        """
        This is print function
        >Print Int a
        >Print Char a
        this function has two mode(int or char).
        """
        if s_line[1] == "Int":
            input_dec = bf.variable.index(s_line[2])
            bf.output += logic.output(bf, input_dec)
        elif s_line[1] == "String":
            string = s_line[2]
            bf.output += logic.output(bf, -1, None, string)
        else:
            input_dec = bf.variable.index(s_line[2])
            bf.output += logic.output(bf, input_dec,1)
    elif s_line[0] == "if":
        """
        """
        input_dec = bf.variable.index(s_line[1])
        if is_integer(s_line[3]):
            bf.output += logic.if_output(bf, s_line[2], input_dec, -1, int(s_line[3]))
        else:
            input_dec1 = bf.variable.index(s_line[3])
            bf.output += logic.if_output(bf, s_line[2], input_dec, input_dec1)
    elif s_line[0] == "elif":
        """
        """
        bf.in_else += 2
        input_dec = bf.variable.index(s_line[1])
        if is_integer(s_line[3]):
            bf.output += logic.elif_output(bf, s_line[2], input_dec, -1, int(s_line[3]))
        else:
            input_dec1 = bf.variable.index(s_line[3])
            bf.output += logic.elif_output(bf, s_line[2], input_dec, input_dec1)
    elif s_line[0] == "else":
        """
        """
        bf.in_else += 1
        bf.output += logic.else_output(bf)
    elif s_line[0] == "endif":
        """
        """
        bf.output += logic.endif_output(bf)
        bf.in_else = 0
    elif s_line[0] == "//":
        pass


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
            judge(brainfuck,s_line,line)
            #Debug
            #print(brainfuck.piv)

            line += 1
        print(brainfuck.output)