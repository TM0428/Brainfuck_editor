import main
import math


def copy_to_cal(bf,input_dec,number=0):
    """
    this outputs the code that the number copies to cal memory 0
    """
    length = bf.length * 2
    output = ""
    if input_dec > bf.piv:
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
    """
    input_dec is Sequence number of input destination
    """
    output = ""
    if input_dec > bf.piv:
        for i in range(input_dec-bf.piv):
            output += '>'
    elif input_dec < bf.piv:
        for i in range(bf.piv-input_dec):
            output += '<'
    output += ','
    bf.piv = input_dec
    return output

def input_int(bf,input_dec):
    output = ""
    length = bf.length * 2
    input_dec = input_dec * 2
    if length > bf.piv:
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


def output(bf,input_dec,char=None):
    """
    input_dec is Sequence number of input destination
    """
    #go to char ver.
    if char:
        return output_char(bf,input_dec)
    else:
        return output_int(bf,input_dec)

def output_char(bf,input_dec,string=None):
    """
    input_dec is Sequence number of input destination
    """
    output = ""
    if string:
        """
        output string
        command:\n
        """
        
    length = bf.length * 2
    input_dec = input_dec * 2
    if input_dec > bf.piv:
        for i in range(input_dec-bf.piv):
            output += '>'
    elif input_dec < bf.piv:
        for i in range(bf.piv-input_dec):
            output += '<'
    output += '.'
    bf.piv = input_dec
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
    it takes another 1 memory
    """
    output = ""
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


def add_num(bf,input_dec,input_dec1,number=None):
    """
    """
    length = bf.length * 2
    input_dec = input_dec * 2
    input_dec1 = input_dec1 * 2
    output = ""
    output += copy_to_cal(bf,input_dec)
    if number:
        output += make_add_num(number)
    else:
        output += copy_to_cal(bf,input_dec1)

    for i in range(length):
        output += '<'
    output += "[-]"
    for i in range(length):
        output += '>'
    output += '['
    for i in range(length):
        output += '<'
    output += '+'
    for i in range(length):
        output += '>'
    output += "-]"
    bf.piv = length
    return output


def mul_num(bf,input_dec,number):
    """
    """
    length = bf.length * 2
    input_dec = input_dec * 2
    output = ""
    output += copy_to_cal(bf,input_dec)
    output += "[->"
    output += make_add_num(number)
    output += "<]>[<+>-]<"
    for i in range(length):
        output += '<'
    output += "[-]"
    for i in range(length):
        output += '>'
    output += '['
    for i in range(length):
        output += '<'
    output += '+'
    for i in range(length):
        output += '>'
    output += "-]"
    bf.piv = length
    return output