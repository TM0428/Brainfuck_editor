import main

def int_input(bf,input_dec):
    """
    input_dec is Sequence number of input destination
    """
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

def int_output(bf,input_dec):
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




