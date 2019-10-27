import main
import math

class cal:
    def __init__(self, bf: main.Brainfuck):
        self.set = set([i for i in range(bf.length, bf.length+100)])
    def borrow(self, num): #num個の計算用スペースのindexを借りる
        res = []
        for i in range(num):
            if len(self.set) <= 0: #要素が無くなったら追加
                self.set.add(
                    [j for j in range(max(self.set), max(self.set)+100)])
            temp = min(self.set) #最小を取り出す
            res.append(temp)
            self.set.remove(temp)
        return res
    def back(self, li): #borrowしたスペースを返却する。
        for v in li:
            self.set.add(v)

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


"""
function:
in return, bf.piv must go to bf.length*2 and result is in the bf.piv memory
"""

def first_step(bf):
    length = bf.length * 2
    output = ""
    output += move_header(bf,length)
    output += '['
    output += move_to_mem(bf,length,0)
    output += ']'
    bf.piv = length
    return output

##################### 
#        mem        #
#####################


def copy_to_cal(bf,input_dec,number=0):
    """
    this function output the code that input_dec copies to cal memory (number)\n
    number: default is 0\n
    header move to (bf.length*2)\n
    YOU SHOULD DOUBLED INPUT_DEC
    """
    length = bf.length * 2
    output = ""
    if bf.piv < input_dec:
        for i in range(input_dec-bf.piv):
            output += '>'
    elif input_dec < bf.piv:
        for i in range(bf.piv-input_dec):
            output += '<'
    output += "[>+"
    for i in range(length - input_dec-1+number):
        output += '>'
    output += '+'
    for i in range(length - input_dec+number):
        output += '<'
    output += "-]>[<+>-]"
    for i in range(length - input_dec-1):
        output += '>'
    bf.piv = length
    return output

def move_to_mem(bf,input_dec,copy_to_dec):
    """
    reset the copy_to_dec and move input_dec to copy_to_dec
    YOU SHOULD DOUBLED NUMBER
    """
    output = ""
    if bf.piv < copy_to_dec:
        for i in range(copy_to_dec-bf.piv):
            output += '>'
    elif copy_to_dec < bf.piv:
        for i in range(bf.piv-copy_to_dec):
            output += '<'
    output += "[-]"
    bf.piv = copy_to_dec

    if bf.piv < input_dec:
        for i in range(input_dec-bf.piv):
            output += '>'
    elif input_dec < bf.piv:
        for i in range(bf.piv-input_dec):
            output += '<'
    output += '['
    if input_dec < copy_to_dec:
        for i in range(copy_to_dec - input_dec):
            output += '>'
        output += '+'
        for i in range(copy_to_dec - input_dec):
            output += '<'
        output += "-]"

    elif copy_to_dec < input_dec:
        for i in range(input_dec - copy_to_dec):
            output += '<'
        output += '+'
        for i in range(input_dec - copy_to_dec):
            output += '>'
        output += "-]"
    bf.piv = input_dec
    return output


def set_data(bf,copy_to_dec,input_dec,number=None,after_cal=None):
    copy_to_dec = copy_to_dec * 2
    input_dec = input_dec * 2
    length = bf.length * 2
    output = ""
    if bf.piv < copy_to_dec:
        for i in range(copy_to_dec-bf.piv):
            output += '>'
    elif copy_to_dec < bf.piv:
        for i in range(bf.piv-copy_to_dec):
            output += '<'
    output += "[-]"
    bf.piv = copy_to_dec
    if after_cal:
        if bf.piv < length:
            for i in range(length-bf.piv):
                output += '>'
        elif length < bf.piv:
            for i in range(bf.piv-length):
                output += '<'
        output += '['
        bf.piv = length
        for i in range(bf.piv-copy_to_dec):
            output += '<'
        output += '+'
        for i in range(bf.piv-copy_to_dec):
            output += '>'
        output += "-]"
        bf.piv = length
        return output
    elif number:
        output += make_add_num(number)
        for i in range(length-bf.piv):
            output += '>'
        bf.piv = length
        return output
    else:
        if bf.piv < input_dec:
            for i in range(input_dec-bf.piv):
                output += '>'
        elif input_dec < bf.piv:
            for i in range(bf.piv-input_dec):
                output += '<'
        bf.piv = input_dec
        output += "[>+<"
        if bf.piv < copy_to_dec:
            for i in range(copy_to_dec-bf.piv):
                output += '>'
            output += '+'
            for i in range(copy_to_dec-bf.piv):
                output += '<'
        elif copy_to_dec < bf.piv:
            for i in range(bf.piv-copy_to_dec):
                output += '<'
            output += '+'
            for i in range(bf.piv-copy_to_dec):
                output += '>'
        output += "-]>[<+>-]<"
        bf.piv = length
        return output


def move_header(bf,input_to):
    output = ""
    if bf.piv < input_to:
        for i in range(input_to-bf.piv):
            output += '>'
    elif input_to < bf.piv:
        for i in range(bf.piv-input_to):
            output += '<'
    bf.piv = input_to
    return output

#################### 
#       ScPt       #
####################


def input(bf,input_dec,char=None):
    """
    input_dec is Sequence number of input destination
    """
    #go to char ver.
    if char:
        return input_char(bf,input_dec)
    else:
        return input_int(bf,input_dec)

def input_char(bf,input_dec):
    length = bf.length * 2
    input_dec = input_dec * 2
    output = ""
    output += move_header(bf, input_dec)
    output += ','
    bf.piv = input_dec
    output += move_header(bf,length)
    bf.piv = length
    return output

def input_int(bf,input_dec):
    output = ""
    length = bf.length * 2
    input_dec = input_dec * 2
    if bf.piv < length:
        for i in range(length-bf.piv):
            output += '>'
    elif length < bf.piv:
        for i in range(bf.piv-length):
            output += '<'
    output += ">+[[-]>,----------[<++++[>-----<-]>--[<++++[>----<-]>>[<++++++++++>-]<[>+<-]<+>]]<]>>[<<<+>>>-]<<<["
    for i in range(length - input_dec):
        output += '<'
    output += '+'
    for i in range(length - input_dec):
        output += '>'
    output += '-]'
    bf.piv = length
    return output


def output(bf,input_dec,char=None,string=None):
    """
    input_dec is Sequence number of input destination
    This function use about 8 calc memory(?)
    """
    #go to char ver.
    if char:
        return output_char(bf,input_dec,None)
    elif string:
        return output_char(bf,-1,string)
    else:
        return output_int(bf,input_dec)

def output_char(bf,input_dec,string=None):
    """
    input_dec is Sequence number of input destination
    """
    length = bf.length * 2
    input_dec = input_dec * 2
    output = ""
    if string:
        """
        output string
        command:\n
        """
        if bf.piv < length:
            for i in range(length-bf.piv):
                output += '>'
        elif length < bf.piv:
            for i in range(bf.piv-length):
                output += '<'
        char_list = list(string)
        command = False
        for i in range(len(string)):
            if command:
                if char_list[i] == 'n':
                    """
                    this is output '\n'
                    """
                    command = False
                    ascii = 10
                elif char_list[i] == '\\':
                    command = False
                    ascii = ord(char_list[i])
                else:
                    command = False
                    ascii = ord(char_list[i])
            elif char_list[i] == '\\':
                command = True
                continue
            else:
                ascii = ord(char_list[i])
            output += make_add_num(ascii)
            output += ".[-]"
        bf.piv = length
        return output
        

    if bf.piv < input_dec:
        for i in range(input_dec-bf.piv):
            output += '>'
    elif input_dec < bf.piv:
        for i in range(bf.piv-input_dec):
            output += '<'
    output += '.'
    if input_dec < length:
        for i in range(length-input_dec):
            output += '>'
    elif length < input_dec:
        for i in range(input_dec-length):
            output += '<'
    bf.piv = length
    return output

def output_int(bf,input_dec):
    output = ""
    length = bf.length * 2
    input_dec = input_dec * 2
    output += copy_to_cal(bf,input_dec)
    output += ">+<[>[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<[>+<-]<[>+<-]>>[<<+>>-]<[>+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<[>+<-]<[>+<-]>>[<<+>>-]<[>++++++++[<++++++>-]<.[-]]++++++++[<++++++>-]<.[-]]++++++++[<++++++>-]<.[-]]>[++++++++[>++++++<-]>.[-]<]<"
    bf.piv = length
    return output



def make_add_num(number):
    """
    this function is add the value of number.
    it takes another 1 next memory
    """
    output = ""
    if number < 16:
        for i in range(number):
            output += '+'
        return output
    sq1 = int(math.sqrt(number))
    sq2 = sq1 + 1
    num1 = abs(number - (sq1*sq1))
    num2 = abs(number - (sq2*sq2))
    if num1 > num2:
        sq = sq2
        output += '>'
        for i in range(sq):
            output += '+'
        output += "[<"
        for i in range(sq):
            output += '+'
        output += ">-]<"
        for i in range(num2):
            output += '-'
    else:
        sq = sq1
        output += '>'
        for i in range(sq):
            output += '+'
        output += "[<"
        for i in range(sq):
            output += '+'
        output += ">-]<"
        for i in range(num1):
            output += '+'
    return output


#################### 
#       +-*/       #
####################

def add_num(bf,input1,input2,after_cal=None):
    """
    This function use max 3 calc memory
    """
    length = bf.length * 2
    output = ""
    if after_cal:
        output += move_header(bf,length)
        output += "[>>+<<-]"
    if is_integer(input1):
        output += move_header(bf,length)
        output += make_add_num(int(input1))
    else:
        input_dec = bf.variable.index(input1) * 2
        output += copy_to_cal(bf,input_dec)
    #bf.piv = length
    if after_cal:
        output += ">>[<<+>>-]<<"
    elif is_integer(input2):
        output += make_add_num(int(input2))
    else:
        input_dec = bf.variable.index(input2) * 2
        output += copy_to_cal(bf,input_dec)
    bf.piv = length
    return output


def sub_num(bf,input1,input2,after_cal=None):
    """
    This function use max 3 calc memory
    """
    length = bf.length * 2
    output = ""
    if after_cal:
        output += move_header(bf,length)
        output += "[>>+<<-]"
    if is_integer(input1):
        output += move_header(bf,length)
        output += make_add_num(int(input1))
    else:
        input_dec = bf.variable.index(input1) * 2
        output += copy_to_cal(bf,input_dec)
    #bf.piv = length
    if after_cal:
        output += ">>[<<->>-]<<"
    elif is_integer(input2):
        output += '>'
        output += make_add_num(int(input2))
        output += "[<->-]<"
    else:
        input_dec = bf.variable.index(input2) * 2
        output += copy_to_cal(bf,input_dec,1)
        output += ">[<->-]<"
    bf.piv = length
    return output



def mul_num(bf,input_dec,input_dec1,number=None):
    """
    This function use max 4 calc memory
    """
    length = bf.length * 2
    input_dec = input_dec * 2
    input_dec1 = input_dec1 * 2
    output = ""
    output += copy_to_cal(bf,input_dec)

    if number:
        output += "[->"
        output += make_add_num(number)
        output += "<]>[<+>-]<"
    else:
        output += copy_to_cal(bf,input_dec1,1)
        output += "[->[>+>+<<-]>[<+>-]<<]>>>[<<<+>>>-]<<[-]<"
    bf.piv = length
    return output

def div_num(bf,input1,input2,after_cal=None):
    length = bf.length * bf.data_memory
    output = ""
    if after_cal:
        if bf.piv < length:
            for i in range(length-bf.piv):
                output += '>'
        elif length < bf.piv:
            for i in range(bf.piv-length):
                output += '<'
        output += "[>>+<<-]"
    if is_integer(input1):
        if bf.piv < length:
            for i in range(length-bf.piv):
                output += '>'
        elif length < bf.piv:
            for i in range(bf.piv-length):
                output += '<'
        output += make_add_num(int(input1))
    else:
        input_dec = bf.variable.index(input1) * 2
        output += copy_to_cal(bf,input_dec)
    #bf.piv = length
    if after_cal:
        output += ">>[<+>-]<<"
    elif is_integer(input2):
        output += '>'
        output += make_add_num(int(input2))
        output += '<'
    else:
        input_dec = bf.variable.index(input2) * 2
        output += copy_to_cal(bf,input_dec,1)
    #bf.piv = length
    output += ">>>+<<[>>+<<[>+<-]]>[<+>-]>[<+>-]<-[<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<<<[<->>>+<<-]>>[<<+>>-]]>[-<<-<[-]>>>]<<]<<[-]>>>>>>>[<<<<<<<+>>>>>>>-]<<<<<<<"
    bf.piv = length
    return output
    
def mod_num(bf,input1,input2,after_cal=None):
    length = bf.length * bf.data_memory
    output = ""
    if after_cal:
        if bf.piv < length:
            for i in range(length-bf.piv):
                output += '>'
        elif length < bf.piv:
            for i in range(bf.piv-length):
                output += '<'
        output += "[>>+<<-]"
    if is_integer(input1):
        if bf.piv < length:
            for i in range(length-bf.piv):
                output += '>'
        elif length < bf.piv:
            for i in range(bf.piv-length):
                output += '<'
        output += make_add_num(int(input1))
    else:
        input_dec = bf.variable.index(input1) * 2
        output += copy_to_cal(bf,input_dec)
    #bf.pit = length
    if after_cal:
        output += ">>[<+>-]<<"
    elif is_integer(input2):
        output += '>'
        output += make_add_num(int(input2))
        output += '<'
    else:
        input_dec = bf.variable.index(input2) * 2
        output += copy_to_cal(bf,input_dec,1)
    #bf.pit = length
    output += ">>>+<<[>>+<<[>+<-]]>[<+>-]>[<+>-]<-[<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->-<<<[<->>>+<<-]>>[<<+>>-]]>[-<<-<[-]>>>]<<]<<"
    bf.piv = length
    return output




#################### 
#        if        #
####################

def if_output(bf,input1,input2,com):
    length = bf.length * bf.data_memory
    output = ""

    if is_integer(input1):
        if bf.piv < length:
            for i in range(length-bf.piv):
                output += '>'
        elif length < bf.piv:
            for i in range(bf.piv-length):
                output += '<'
        output += make_add_num(int(input1))
    else:
        input_dec = bf.variable.index(input1) * 2
        output += copy_to_cal(bf,input_dec)
    #bf.pit = length
    if is_integer(input2):
        output += '>'
        output += make_add_num(int(input2))
        output += '<'
    else:
        input_dec = bf.variable.index(input2) * 2
        output += copy_to_cal(bf,input_dec,1)
    #bf.pit = length
    output += comparison(bf,com)
    output += ">+<[>-<-"
    bf.piv = length
    return output

def elif_output(bf,input1,input2,com):
    length = bf.length * bf.data_memory
    output = ""

    if bf.piv < length:
        for i in range(length-bf.piv):
            output += '>'
    elif length < bf.piv:
        for i in range(bf.piv-length):
            output += '<'
    output += "]>[-<"
    #bf.piv = length
    if is_integer(input1):
        output += make_add_num(int(input1))
    else:
        input_dec = bf.variable.index(input1) * 2
        output += copy_to_cal(bf,input_dec)
    #bf.pit = length
    if is_integer(input2):
        output += '>'
        output += make_add_num(int(input2))
        output += '<'
    else:
        input_dec = bf.variable.index(input2) * 2
        output += copy_to_cal(bf,input_dec,1)
    output += comparison(bf,com)
    output += ">+<[>-<-"
    bf.piv = length
    return output

def else_output(bf):
    """
    """
    length = bf.length * 2
    output = ""
    if bf.piv < length:
        for i in range(length-bf.piv):
            output += '>'
    elif length < bf.piv:
        for i in range(bf.piv-length):
            output += '<'
    output += "]>[-<"
    bf.piv = length
    return output

def endif_output(bf):
    """
    'elif' makes another bracket
    bf.in_else//2:the number of 'elif'
    bf.in_else!=0:include 'else' or 'elif'

    """
    length = bf.length * 2
    output = ""
    if bf.piv < length:
        for i in range(length-bf.piv):
            output += '>'
    elif length < bf.piv:
        for i in range(bf.piv-length):
            output += '<'
    if bf.in_else:
        if bf.in_else%2 == 1:
            output += ">]<"
        else:
            output += ']'
        for i in range(bf.in_else//2):
            output += '>]<]'
    else:
        output += "]>[-]<"
    bf.piv = length
    return output

    

def comparison(bf,com):
    """
    this library is comparison
    >,<,>=,<=,==,!=
    comparison bf.piv and (bf.piv+1)
    this function use max 3 calc memory
    """
    output = ""
    if com == '<':
        output += "[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]>[<+>[-]]<"
    elif com == '>':
        output += "[>>+<<-]>[<+>-]>[<+>-]<<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]>[<+>[-]]<"
    elif com == "<=":
        output += "[>>+<<-]>[<+>-]>[<+>-]<<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]<"
    elif com == ">=":
        output += "[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]<"
    elif com == "==":
        output += "[>-<-]+>[<->[-]]<"
    elif com == "!=":
        output += "[>-<-]>[<+>[-]]<"

    return output


def logical_operation(bf,op,input_dec,input_dec1,number=None):
    """
    this library is logical operation
    and or not nand nor xor
    op input_dec and (input_dec1 or number)
    this function use max 3 calc memory([bf.length,bf.length+2])
    """
    length = bf.length * 2
    input_dec = input_dec * 2
    input_dec1 = input_dec1 * 2
    output = ""
    piv = bf.piv
    if op == "and":
        #[flag]に2をセットして引数の値がnon 0なら[flag]から1を引く
        flag = length+2
        output += move_header(bf,flag)
        output += "++"

        output += copy_to_cal(bf,input_dec)
        output += move_header(bf,length)
        output += "["
        output += move_header(bf,flag)
        output += "-"
        output += move_header(bf,length)
        output+="[-]"
        output += "]"
        
        if number!=None:
            #set bf.length number(also use bf.length+1) 
            output += make_add_num(number)
            output += move_header(bf,length)
            output += "["
            output += move_header(bf,flag)
            output += "-"
            output += move_header(bf,length)
            output+="[-]"
            output += "]"
        else:
            output += copy_to_cal(bf,input_dec1)
            output += move_header(bf,length)
            output += "["
            output += move_header(bf,flag)
            output += "-"
            output += move_header(bf,length)
            output+="[-]"
            output += "]"
        
        output += move_header(bf,length)
        output += "+"
        output += move_header(bf,flag)
        output += "["
        output += move_header(bf,length)
        output += "[-]"
        output += move_header(bf,flag)
        output += "[-]"
        output += "]"
        #go to length
        output += move_header(bf,length)
    return output