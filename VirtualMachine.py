from collections import deque

class VirtualMachine:
    def __init__(self, quads, funcs):
        self.quads = quads
        self.funcs = funcs
        self.memory = {}    #diccionario que simula la memoria de la máquina virtual
        self.IP = 0
        self.activation_record_count = 1
        self.current_func = "__main__"
        self.lastIPs = deque()
        self.lastFuncs = deque()

    def execute(self):
        running = True
        next_func = None
        new_activation_record = None
        self.memory[self.current_func] = {}
        while(running == True):
            quad = self.quads[self.IP]
            op, arg1, arg2, result = quad
            if(arg1 != None and not isinstance(arg1, int)):
                if (((arg1[0].isdigit() or (arg1[0]=='"') or (arg1[0]=='-')) == False) and arg1 not in self.memory[self.current_func] and arg1 not in self.funcs):
                    if(self.current_func == "__main__"):
                        self.memory[self.current_func][arg1] = 0
                    elif((arg1 not in self.memory["__main__"]) or (arg1[0] == 't' and arg1[-1].isdigit())):
                        self.memory[self.current_func][arg1] = 0
            if(arg2 != None and not isinstance(arg2, int)):
                if (((arg2[0].isdigit() or (arg2[0]=='"') or (arg2[0]=='-')) == False) and arg2 not in self.memory[self.current_func]):
                    if(self.current_func == "__main__"):
                        self.memory[self.current_func][arg2] = 0
                    elif((arg2 not in self.memory["__main__"]) or (arg2[0] == 't' and arg2[-1].isdigit())):
                        self.memory[self.current_func][arg2] = 0
            if(result != None and not isinstance(result, int)):
                if (((result[0].isdigit() or (result[0]=='"') or (result[0]=='-')) == False) and result not in self.memory[self.current_func]):
                    if(self.current_func == "__main__"):
                        self.memory[self.current_func][result] = 0
                    elif((result not in self.memory["__main__"]) or (result[0] == 't' and result[-1].isdigit())):
                        self.memory[self.current_func][result] = 0
            
            #OPERACIONES
            if op == "GoTo":
                self.IP = result - 1
            elif op == "=":
                if(result in self.memory[self.current_func]):
                    self.memory[self.current_func][result] = self.get_value(arg1)
                elif(result in self.memory["__main__"]):
                    self.memory["__main__"][result] = self.get_value(arg1)
            elif op in {"+", "-", "*", "/", "==", "!=", ">", "<"}:
                if(result in self.memory[self.current_func]):
                    self.memory[self.current_func][result] = self.perform_operation(op, arg1, arg2)
                elif(result in self.memory["__main__"]):
                    self.memory["__main__"][result] = self.perform_operation(op, arg1, arg2)
            elif op == "print":
                print(self.get_value(arg1))
            elif op == "GoToF":
                if self.get_value(arg1) == False:
                    self.IP = result - 1
            elif op == "ERA":
                next_func = arg1
                new_activation_record = f"{arg1}{self.activation_record_count}"
                self.memory[new_activation_record] = {}
                self.activation_record_count += 1
            elif op == "PARAMETER":
                param_name = list(self.funcs[next_func]['parametros'].keys())[arg2]
                self.memory[new_activation_record][param_name] = self.get_value(arg1)
            elif op == "GOSUB":
                self.lastFuncs.append(self.current_func)
                self.current_func = new_activation_record
                self.lastIPs.append(self.IP + 1)
                self.IP = self.funcs[next_func]['inicioQuad'] - 1
            elif op == "ENDFunc":
                self.current_func = self.lastFuncs.pop()
                self.IP = self.lastIPs.pop() - 1
            elif op == "END":
                running = False
            
            self.IP += 1
        
        print("\nMemory:")
        print(self.memory)


    def get_value(self, arg):
        if arg[0].isdigit() or arg[0] == "-":
            try:
                arg = int(arg)
            except:
                arg = float(arg)
        elif arg[0] == '"':
            arg = arg[1:-1]
        else:
            if(arg in self.memory[self.current_func]):
                arg = self.memory[self.current_func][arg]
            else:
                arg = self.memory["__main__"][arg]
        return arg

    def perform_operation(self, op, arg1, arg2):
        val1 = self.get_value(arg1)
        val2 = self.get_value(arg2)
        if op == "+":
            return val1 + val2
        elif op == "-":
            return val1 - val2
        elif op == "*":
            return val1 * val2
        elif op == "/":
            return val1 / val2
        elif op == "==":
            return val1 == val2
        elif op == "!=":
            return val1 != val2
        elif op == ">":
            return val1 > val2
        elif op == "<":
            return val1 < val2