import main

def int_input(bf,input_dec):
    """
    piv is the number Memory address to point
    input_dec is Sequence number of input destination
    """
    output = ""
    bf.len = bf.len * 2
    input_dec = input_dec * 2
    if bf.len > bf.piv:
        for i in range(bf.len-bf.piv):
            output += '>'
    elif bf.len < bf.piv:
        for i in range(bf.len-bf.piv):
            output += '<'
    output += ">+[[-]>,----------[<++++[>-----<-]>--[<++++[>----<-]>>[<++++++++++>-]<[>+<-]<+>]]<]>>[<<<+>>>-]<<<["
    for i in range(bf.len - input_dec):
        output += '<'
    output += '+'
    for i in range(bf.len - input_dec):
        output += '>'
    output += '-]'
    bf.piv = input_dec
    return output
