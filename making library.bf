com

[
    >[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<+<[>-<[-]]>[>>>+<<<-]>+>]<<<
]


a sml b big is 1(not eq)
a b tmpb
[
    >[
        <->-[>+<-]
    ]
    >>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<
]>[<+>[-]]<
opti:
[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]>[<+>[-]]<

a big b sml is 1(include eq)
opti:
[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]<

a big b sml is 1(not eq)
[>>+<<-]>[<+>-]>[<+>-]<<
[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]>[<+>[-]]<

a sml b big is 1(include eq)
[>>+<<-]>[<+>-]>[<+>-]<<
[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]<

a nep b is 1
[>-<-]>[<+>[-]]<

a eq b is 1
[>-<-]+>[<->[-]]<


"""
while(a){
    while(b){
        a--;
        b--;
        tmpb = b;
        b = 0;
    }
    jud = 1;
    while(tmpb){
        jud = 0;
        b = tmpb;
        tmpb = 0;
    }
    while(jud){
        jud = 0;
        a = 0;
    }
}




A/B

int x = 1;
int ans1 = 0;
while(b){
    x++;
    tmpb = b;
    b = 0;
}
x--;
while(x){
    if(a>=b){
        ans1++;
        while(b){
            a--;
            tmpb++;
            b--;
        }
        while(tmpb){
            tmpb--;
            b++;
        }
    }
    else{
        b = a;
        a = 0;
        x = 0;
    }
}
a = 0;
a = ans1;


division

(a)(b)(x)(ac)(bc)(tmp)()(ans1)

>>>+<<[>>+<<
    [>+<-]
]
>[<+>-]>[<+>-]<-
[
    <<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<<
    [>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]<
    >+<[->-<
        >>>>+<<<<<<[<->>>+<<-]>>[<<+>>-]
    ]
    >[-
        <<-<[-]<[>+<-]>>>>
    ]
    <<
]<<[-]>>
>>>>>[<<<<<<<+>>>>>>>-]<<<<<<<

opti:
>>>+<<[>>+<<[>+<-]]>[<+>-]>[<+>-]<-[<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<<<[<->>>+<<-]>>[<<+>>-]]>[-<<-<[-]<[>+<-]>>>>]<<]<<[-]>>>>>>>[<<<<<<<+>>>>>>>-]<<<<<<<

division
(\10)
(a)(x)(ac)(ac)(tmp)()(ans1)
>+[
    <[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<
    [>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]<
    >+<[->-<
        >>>>+<<<<++++++++++[<<->>-]
    ]
    >[-
        <<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<
    ]
    <<
]<
>>[<+>-]<<
opti:
>+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<<

print(int)

>+<[>-<
    >+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<
    [>+<-]<[>+<-]>>[<<+>>-]<
    [
        >+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<
        [>+<-]<[>+<-]>>[<<+>>-]<
        [
            >+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<
            [<+>-]++++++++[<++++++>-]<.[-]
        ]
        ++++++++[<++++++>-]<.[-]
    ]
    ++++++++[<++++++>-]<.[-]
]
>[++++++++[>++++++<-]>.[-]<]
opti:
>+<[>[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<[>+<-]<[>+<-]>>[<<+>>-]<[>+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<[>+<-]<[>+<-]>>[<<+>>-]<[>+[<[>>+>+<<<-]>>>[<<<+>>>-]++++++++++<[>[<->-[>+<-]]>>+<[>-<[<+>-]]>[-<<<[-]>>>]<<<]+>[<->[-]]+<[->->>>+<<<<++++++++++[<<->>-]]>[-<<-<[>>+<<-]>>>>>>[<<<<<<+>>>>>>-]<<<]<<]>[<+>-]<[<+>-]++++++++[<++++++>-]<.[-]]++++++++[<++++++>-]<.[-]]++++++++[<++++++>-]<.[-]]>[+++++++[>++++++<-]>.[-]<]