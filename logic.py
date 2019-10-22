import main
import math

def input(bf,input_dec,char=None):
    """
    input_dec is Sequence number of input destination
    """
    output = ""
    if char:
        return char_input(bf,input_dec)
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

def char_input(bf,input_dec):
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


def output(bf,input_dec,char=None):
    """
    input_dec is Sequence number of input destination
    """
    output = ""
    if char:
        return char_output(bf,input_dec)
    length = bf.length * 2
    input_dec = input_dec * 2
    if input_dec > bf.piv:
        for i in range(input_dec-bf.piv):
            output += '>'
    elif input_dec < bf.piv:
        for i in range(bf.piv-input_dec):
            output += '<'
    output += "[>+"
    for i in range(length - input_dec-1):
        output += '>'
    output += '+'
    for i in range(length - input_dec):
        output += '<'
    output += "-]>[<+>-]"
    for i in range(length - input_dec-1):
        output += '>'
    output += ">+<[>[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<[>+<-]<[>+<-]>>[<<+>>-]<[>+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<[>+<-]<[>+<-]>>[<<+>>-]<[>+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<[<+>-]++++++++[<++++++>-]<.[-]]++++++++[<++++++>-]<.[-]]++++++++[<++++++>-]<.[-]]>[+++++++[>++++++<-]>.[-]<]"
    bf.piv = length
    return output

def char_output(bf,input_dec):
    """
    input_dec is Sequence number of input destination
    """
    output = ""
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


def make_add_num(number):
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


def add_num(bf,input_dec):
    """
    """