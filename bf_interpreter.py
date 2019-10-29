from typing import List
import sys

class Bf_interpreter:
    def __init__(self,inputs=""):
        self.memory_size: int = 10000   #メモリサイズ上限
        self.memory: List[int] = [0 for i in range(self.memory_size)]   #メモリ
        self.header: int = 0            #ヘッダーの位置
        self.inputs: str = inputs       #bfへの入力
        self.inputs_index: int = 0      #bfがどこまで読み込んだか
        self.outputs: str = ""          #bfの出力
        self.source: str = ""           #bfのソースコード
        self.matching_par: List[int]    #対応する括弧の座標(括弧でない場合は-1)
        self.source_index: int = 0      #ソースコードのどこにいるか
    
    def read_source(self):
        sources: List[str] = [line.rstrip() for line in sys.stdin]
        #self.source = "".join(sources)
        return "".join(sources)

    def set_source(self,source):
        self.source = source

    def parsing(self):
        self.matching_par = [-1 for i in range(len(self.source))]
        matching_stack: List[int] = []
        for i in range(len(self.source)):
            if self.source[i] == "[":
                matching_stack.append(i)
            elif self.source[i] == "]":
                if len(matching_stack) == 0:
                    #self.debug("There is no matching parenthesis.")
                    #sys.exit(1)
                    # 対応する括弧が存在しなくてもコンパイル時エラーにはせず、実行時に括弧の要件を満たした際に実行時エラーとなるようにした
                    self.matching_par[i] = -1
                else:
                    stack_top = matching_stack[-1]
                    matching_stack.pop()
                    self.matching_par[i] = stack_top
                    self.matching_par[stack_top] = i
        for v in matching_stack:
            self.matching_par[v]=len(self.source)
        """
        if len(matching_stack) != 0:
            self.debug("There is no matching parenthesis.")
            sys.exit(1)
        """

    def read(self) -> int:# ,
        if len(self.inputs)>self.inputs_index:
            res:int = ord(self.inputs[self.inputs_index])
            self.inputs_index += 1
            self.memory[self.header] = res
        else:
            self.memory[self.header] = 0

    def write(self):  # .
        self.outputs += chr(self.memory[self.header])

    def inc(self):  # +
        self.memory[self.header]+=1
        if self.memory[self.header]>255:
            self.memory[self.header] = 0
    
    def dec(self): # -
        self.memory[self.header] -= 1
        if self.memory[self.header] < 0:
            self.memory[self.header] = 255

    def debug(self,error_massage):
        print(f"error:{error_massage}", file=sys.stderr)
        print(f"header: {self.header}, outputs: {self.outputs}",
              file=sys.stderr)
        print(f"memory(~20): ", file=sys.stderr)
        for i in range(20):
            print(self.memory[i], end=" ", file=sys.stderr)
        print("",file=sys.stderr)

    def right(self): # >
        self.header += 1
        if self.memory_size <= self.header:
            self.debug("out of range(limit exceeded)")

    def left(self):  # <
        self.header -= 1
        if 0 > self.header:
            self.debug("out of range(limit below)")

    def right_parenthesis(self,index): # [
        if self.memory[self.header]==0:
            self.source_index = self.matching_par[index]
            if self.source_index==len(self.source):
                self.debug("out of range(limit exceeded due to right parenthesis)")
    
    def left_parenthesis(self,index): # ]
        if self.memory[self.header]!=0:
            self.source_index = self.matching_par[index]
            if self.source_index==-1:
                self.debug("out of range(limit below due to left parenthesis)")
    
    
    def interperter(self):
        while self.source_index < len(self.source):
            i = self.source_index
            if self.source[i] == ">":
                self.right()
            elif self.source[i] == "<":
                self.left()
            elif self.source[i] == "+":
                self.inc()
            elif self.source[i] == "-":
                self.dec()
            elif self.source[i] == ".":
                self.write()
            elif self.source[i] == ",":
                self.read()
            elif self.source[i] == "[":
                self.right_parenthesis(i)
            elif self.source[i] == "]":
                self.left_parenthesis(i)
            self.source_index += 1
            #self.debug("")

    def step_run(self):
        i = self.source_index
        if self.source[i] == ">":
            self.right()
        elif self.source[i] == "<":
            self.left()
        elif self.source[i] == "+":
            self.inc()
        elif self.source[i] == "-":
            self.dec()
        elif self.source[i] == ".":
            self.write()
        elif self.source[i] == ",":
            self.read()
        elif self.source[i] == "[":
            self.right_parenthesis(i)
        elif self.source[i] == "]":
            self.left_parenthesis(i)
        self.source_index += 1
    
if __name__ == "__main__":
    bf_ip = Bf_interpreter("2 5 ")
    bf_ip.set_source(bf_ip.read_source())
    bf_ip.parsing()
    
    bf_ip.debug("")
    bf_ip.interperter()
    bf_ip.debug("")
    print(bf_ip.outputs)