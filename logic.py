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



def copy_to_cal(bf,input_dec,number=0):
    """
    this function output the code that input_dec copies to cal memory (number)\n
    number: default is 0\n
    header move to (bf.length*2)
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
    output = ""
    if bf.piv < input_dec:
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
        return output
        

    if bf.piv < input_dec:
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
    it takes another 1 next memory
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
    This function use max 2 calc memory
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


def mul_num(bf,input_dec,input_dec1,number=None):
    """
    This function use max 3 calc memory
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
    else:
        """
        this is not implementation
        """
    bf.piv = length
    return output


def comparison(bf,com,input_dec,input_dec1,number=None):
    """
    this library is comparison
    >,<,>=,<=,==,!=
    The memory "bf.length * 2" is 1 or 0
    this function use max 3 calc memory
    """
    length = bf.length * 2
    input_dec = input_dec * 2
    input_dec1 = input_dec1 * 2
    output = ""
    output += copy_to_cal(bf,input_dec)
    if number:
        output += '>'
        output += make_add_num(number)
    else:
        output += copy_to_cal(bf,input_dec1,1)
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

    bf.piv = length
    return output