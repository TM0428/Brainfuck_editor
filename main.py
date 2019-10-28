import sys
import os
import logic
import regex

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
    data_memory = 2

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def judge(bf, s_line, line, in_loop=False):
    if not in_loop:
        bf.output += logic.first_step(bf)
    s_line_list = s_line.replace('\n','').split(' ')
    if s_line_list[0] == "Var":
        """
        This is declaring variables
        >Var a b c
        """
        for Text in s_line_list[1:]:
            #used variable
            if Text in bf.variable:
                print('File "' + args[1] + '", line ' + str(line) +'\nError: Variable "' + Text + '" is used.', file=sys.stderr)
                sys.exit(1)
            bf.variable.append(Text)
        bf.length = len(bf.variable)

    elif s_line_list[0] == "Set":
        if s_line_list[2][0] == '{':
            re_pattern = r"(?<rec>{(?:[^{}]+|(?&rec))*})"
            re_text = regex.search(re_pattern, s_line)
            judge(bf,re_text.group('rec')[1:len(re_text.group('rec'))-1],line,True)
            bf.output += logic.set_data(bf,s_line_list[1],-1,1)
        else:
            bf.output += logic.set_data(bf,s_line_list[1],s_line_list[2])


    elif s_line_list[0] == "Inc":
        """
        hoge
        """
    elif s_line_list[0] == "Add":
        """
        This is add function
        >Add a b
        >Add a 10
        """
        if s_line_list[2][0] == '{':
            re_pattern = r"(?<rec>{(?:[^{}]+|(?&rec))*})"
            re_text = regex.search(re_pattern, s_line)
            judge(bf,re_text.group('rec')[1:len(re_text.group('rec'))-1],line,True)
            bf.output += logic.add_num(bf,s_line_list[1],s_line_list[2],1)
        else:
            bf.output += logic.add_num(bf,s_line_list[1],s_line_list[2])

    elif s_line_list[0] == "Sub":
        if s_line_list[2][0] == '{':
            re_pattern = r"(?<rec>{(?:[^{}]+|(?&rec))*})"
            re_text = regex.search(re_pattern, s_line)
            judge(bf,re_text.group('rec')[1:len(re_text.group('rec'))-1],line,True)
            bf.output += logic.sub_num(bf,s_line_list[1],s_line_list[2],1)
        else:
            bf.output += logic.sub_num(bf,s_line_list[1],s_line_list[2])


    elif s_line_list[0] == "Mul":
        """
        This is mul function
        >Mul a b
        >Mul a 10
        if you don't write, the value is in the variable "Res"
        """
        input_dec = bf.variable.index(s_line_list[1])
        if is_integer(s_line_list[2]):
            bf.output += logic.mul_num(bf, input_dec, -1, int(s_line_list[2]))
        else:
            input_dec1 = bf.variable.index(s_line_list[2])
            bf.output += logic.mul_num(bf, input_dec, input_dec1, None)

    elif s_line_list[0] == "Div":
        if s_line_list[2][0] == '{':
            re_pattern = r"(?<rec>{(?:[^{}]+|(?&rec))*})"
            re_text = regex.search(re_pattern, s_line)
            judge(bf,re_text.group('rec')[1:len(re_text.group('rec'))-1],line,True)
            bf.output += logic.div_num(bf,s_line_list[1],s_line_list[2],1)
        else:
            bf.output += logic.div_num(bf,s_line_list[1],s_line_list[2])

    elif s_line_list[0] == "Mod":
        if s_line_list[2][0] == '{':
            re_pattern = r"(?<rec>{(?:[^{}]+|(?&rec))*})"
            re_text = regex.search(re_pattern, s_line)
            judge(bf,re_text.group('rec')[1:len(re_text.group('rec'))-1],line,True)
            bf.output += logic.mod_num(bf,s_line_list[1],s_line_list[2],1)
        else:
            bf.output += logic.mod_num(bf,s_line_list[1],s_line_list[2])

    elif s_line_list[0] == "Scan":
        """
        This is scan function
        >Scan Int a
        >Scan Char a
        this function has two mode(int or char).
        """
        if s_line_list[1] == "Int":
            input_dec = bf.variable.index(s_line_list[2])
            bf.output += logic.input(bf, input_dec)
        else:
            input_dec = bf.variable.index(s_line_list[2])
            bf.output += logic.input(bf, input_dec,1)

    elif s_line_list[0] == "Print":
        """
        This is print function
        >Print Int a
        >Print Char a
        this function has two mode(int or char).
        """
        if s_line_list[1] == "Int":
            input_dec = bf.variable.index(s_line_list[2])
            bf.output += logic.output(bf, input_dec)
        elif s_line_list[1] == "String":
            string = s_line_list[2]
            bf.output += logic.output(bf, -1, None, string)
        else:
            input_dec = bf.variable.index(s_line_list[2])
            bf.output += logic.output(bf, input_dec,1)

    elif s_line_list[0] == "if":
        """
        if is special format
        if a >= b
        if a != 2
        you can write only "x op y"
        op allows >,<,>=,<=,==,!=
        making:
        and,or
        """
        bf.output += logic.if_output(bf,s_line_list[1],s_line_list[3],s_line_list[2])

    elif s_line_list[0] == "elif":
        """
        if is special format
        if a >= b
        if a != 2
        you can write only "x op y"
        op allows >,<,>=,<=,==,!=
        making:
        and,or
        """
        bf.in_else += 2
        bf.output += logic.elif_output(bf,s_line_list[1],s_line_list[3],s_line_list[2])

    elif s_line_list[0] == "else":
        """
        """
        bf.in_else += 1
        bf.output += logic.else_output(bf)

    elif s_line_list[0] == "endif":
        """
        YOU SHOULD WRITE THE END OF "IF"
        """
        bf.output += logic.endif_output(bf)
        bf.in_else = 0

    elif s_line_list[0] == "//":
        pass

    elif s_line_list[0] == "Command":
        #Command is Debug.
        bf.output += s_line_list[1]
    
    elif s_line_list[0] == "And":
        input_dec = bf.variable.index(s_line_list[1])
        if is_integer(s_line_list[2]):
            bf.output += logic.logical_operation(bf,"and",input_dec,-1,int(s_line_list[2]))
        else:
            input_dec1 = bf.variable.index(s_line_list[2])
            bf.output += logic.logical_operation(bf,"and",input_dec,input_dec1,None)
    
    elif s_line_list[0] == "Or":
        input_dec = bf.variable.index(s_line_list[1])
        if is_integer(s_line_list[2]):
            bf.output += logic.logical_operation(bf,"or",input_dec,-1,int(s_line_list[2]))
        else:
            input_dec1 = bf.variable.index(s_line_list[2])
            bf.output += logic.logical_operation(bf,"or",input_dec,input_dec1,None)
    elif s_line_list[0] == "test":
        bf.output += logic.test(bf,s_line_list[2],s_line_list[1],s_line_list[3])



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
            #s_line[0] is command
            judge(brainfuck,s_line,line)
            #Debug
            #print(brainfuck.piv)

            line += 1
        print(brainfuck.output)