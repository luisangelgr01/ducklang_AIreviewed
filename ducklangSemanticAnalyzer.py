from ducklangListener import ducklangListener
from ducklangParser import ducklangParser
from antlr4 import *
from collections import deque

#estructuras para generar cuadruplos
POper = deque()
PilaO = deque()
PTypes = deque()
Quad = deque()
availTemp = deque([f't{i}' for i in range(1000, 0, -1)])
contTemps = 0
maxTemps = 0
PJumps = deque()

#funcion de apoyo para determinar el tipo de nodo del hijo (muestra el nombre de la regla gramatical o el nombre de token)
def child_type(ctx: ParserRuleContext, indice: int):
    if(indice<0 or indice>=ctx.getChildCount()):
        return None

    child = ctx.getChild(indice)
    if(isinstance(child, ParserRuleContext)):
        rule_index = child.getRuleIndex()
        rule_name = ctx.parser.ruleNames[rule_index]
        return rule_name
    elif(isinstance(child, TerminalNode)):
        token = child.getSymbol()
        token_type = token.type
        token_name = ctx.parser.symbolicNames[token_type]
        return token_name
    else:
        return type(child).__name__

#funcion de apoyo para obtener el siguiente temporal disponible
def getNextAvailTemp():
    global availTemp, contTemps, maxTemps
    if not availTemp:
        raise Exception("Error: Stack Overflow. Se acabaron los temporales disponibles.")
    contTemps = contTemps + 1
    maxTemps = max(maxTemps, contTemps)
    return availTemp.pop()

#función de apoyo para generar cuádruplo de expresión
def generateQuadExpression():
    global availTemp, contTemps
    right_operand = PilaO.pop() if len(PilaO) > 0 else None
    right_type = PTypes.pop() if len(PTypes) > 0 else None
    left_operand = PilaO.pop() if len(PilaO) > 0 else None
    left_type = PTypes.pop() if len(PTypes) > 0 else None
    operator = POper.pop() if len(POper) > 0 else None
    if(left_type == None or right_type == None or operator == None):
        raise Exception(f"Error semántico: No se pudo generar cuádruplo de expresión. Pila(s) vacía(s).")
    result_type = cubo_semantico[left_type][right_type][operator]
    if(result_type != None):
        result_temp = getNextAvailTemp()
        Quad.append([operator, left_operand, right_operand, result_temp])
        PilaO.append(result_temp)
        PTypes.append(result_type)
        if(right_operand[0] == 't' and right_operand[-1].isdigit()):
            availTemp.append(right_operand)
            contTemps = contTemps - 1
        if(left_operand[0] == 't' and left_operand[-1].isdigit()):
            availTemp.append(left_operand)
            contTemps = contTemps - 1
    else:
        raise Exception(f"Error semántico: Type mismatch. Operandos {left_operand} {left_type} y {right_operand} {right_type} no son compatibles con el operador {operator}.")

#estructuras de datos de apoyo para el análisis semántico
func_dir = {}

tabla_simbolos = {
    'global': {},
    'local': {}
}

cubo_semantico = {
    'entero': {
        'entero': {'+': 'entero', '-': 'entero', '*': 'entero', '/': 'flotante', '>': 'booleano', '<': 'booleano', '!=': 'booleano', '==': 'booleano'},
        'flotante': {'+': 'flotante', '-': 'flotante', '*': 'flotante', '/': 'flotante', '>': 'booleano', '<': 'booleano', '!=': 'booleano', '==': 'booleano'},
        'booleano': {'+': None, '-': None, '*': None, '/': None, '>': None, '<': None, '!=': None, '==': None}
    },
    'flotante': {
        'entero': {'+': 'flotante', '-': 'flotante', '*': 'flotante', '/': 'flotante', '>': 'booleano', '<': 'booleano', '!=': 'booleano', '==': 'booleano'},
        'flotante': {'+': 'flotante', '-': 'flotante', '*': 'flotante', '/': 'flotante', '>': 'booleano', '<': 'booleano', '!=': 'booleano', '==': 'booleano'},
        'booleano': {'+': None, '-': None, '*': None, '/': None, '>': None, '<': None, '!=': None, '==': None}
    },
    'booleano': {
        'entero': {'+': None, '-': None, '*': None, '/': None, '>': None, '<': None, '!=': None, '==': None},
        'flotante': {'+': None, '-': None, '*': None, '/': None, '>': None, '<': None, '!=': None, '==': None},
        'booleano': {'+': None, '-': None, '*': None, '/': None, '>': None, '<': None, '!=': None, '==': None}
    }
}

class ducklangSemanticAnalyzer(ducklangListener):
    def __init__(self):
        #variables de apoyo, manejan valores actuales al salir/entrar a una regla sintáctica, serán utilizadas en otro paso del recorrido del árbol
        self.scope = 'global' #se inicializa en global el scope
        self.current_ids = []
        self.current_func = None
        self.current_func_params = {}
        self.current_func_var_tipo = None
        self.current_fsign = ''
        self.isExpCondicion = False
        self.current_llamada = None
        self.k = 0
        self.ovejota_quads = None
        self.ovejota_funcs = None
    
    def enterVid(self, ctx: ducklangParser.VidContext):
        self.current_ids.append(ctx.getChild(0).getText())
    
    def enterVtipo(self, ctx: ducklangParser.VtipoContext):
        self.current_ids = []

    def exitVtipo(self, ctx: ducklangParser.VtipoContext):
        var_nombres = self.current_ids
        var_tipo = ctx.getChild(2).getText()

        self.declarar_variables(var_nombres, var_tipo, self.scope)

    def declarar_variables(self, nombres, tipo, scope):
        for nombre in nombres:
            if(nombre in tabla_simbolos[scope] or nombre in tabla_simbolos['global']):
                raise Exception(f"Error semántico: Variable '{nombre}' se volvió a declarar en el scope {scope}.")
            tabla_simbolos[scope][nombre] = tipo

    def enterFuncs(self, ctx: ducklangParser.FuncsContext):
        self.scope = 'local'
        self.current_func = ctx.getChild(1).getText()
        if(self.current_func in func_dir):
            raise Exception(f"Error semántico: Función '{self.current_func}' se volvió a declarar.")
        self.current_func_params = {}
    
    def exitFid(self, ctx: ducklangParser.FidContext):
        self.current_func_var_tipo = ctx.getChild(2).getChild(0).getText()
        var_nombre = ctx.getChild(0).getText()
        if(var_nombre in self.current_func_params):
            raise Exception(f"Error semántico: Parámetro '{var_nombre}' se volvió a declarar en la función '{self.current_func}'.")
        self.current_func_params[var_nombre] = self.current_func_var_tipo
    
    def exitFidtipo(self, ctx: ducklangParser.FidtipoContext):
        cont = len(Quad) if len(Quad) > 0 else 0
        func_dir[self.current_func] = {
            'parametros': self.current_func_params,
            'numParams': len(self.current_func_params),
            'inicioQuad': cont
        }
        for variable in self.current_func_params:
            tabla_simbolos['local'][variable] = self.current_func_params[variable]
    
    def exitFuncs(self, ctx: ducklangParser.FuncsContext):
        global contTemps, maxTemps
        func_dir[self.current_func].update({
            'numVars': len(tabla_simbolos['local']),
            'numTemps': maxTemps,
        })
        Quad.append(['ENDFunc', None, None, None])
        self.current_func = None
        self.current_func_params = {}
        self.current_func_var_tipo = None
        tabla_simbolos['local'] = {}
        contTemps = 0
        maxTemps = 0
    
    def exitPrograma(self, ctx: ducklangParser.ProgramaContext):
        global contTemps, maxTemps
        Quad.append(['END', None, None, None])
        func_dir['__main__'] = {
            'numVars': len(tabla_simbolos['global']),
            'numTemps': maxTemps,
        }
        print('\nDirectorio de funciones al finalizar programa:')
        print(func_dir)
        print('\nCuádruplos generados:')
        for i, quad in enumerate(Quad):
            print(f'{i}: {quad}')
        print('\n\n')
        self.ovejota_quads = Quad
        self.ovejota_funcs = func_dir
    
    def enterFaid(self, ctx: ducklangParser.FaidContext):
        factor = child_type(ctx, 0)
        if(factor == 'ID'):
            id = ctx.getChild(0).getText()
            if(id in tabla_simbolos['global']):
                tipo = tabla_simbolos['global'][id]
            elif(id in tabla_simbolos['local']):
                tipo = tabla_simbolos['local'][id]
            else:
                raise Exception(f"Error semántico: Variable '{id}' no declarada en el scope global.")
            PilaO.append(self.current_fsign + id)
            PTypes.append(tipo)
        elif(factor == 'cte'):
            cte = ctx.getChild(0)
            tipo = 'entero' if child_type(cte, 0) == 'CTE_ENT' else 'flotante' if child_type(cte, 0) == 'CTE_FLOT' else None
            PilaO.append(self.current_fsign + cte.getText())
            PTypes.append(tipo)
        else:
            raise Exception(f"Error semántico: Factor '{factor}' no reconocido.")
    
    def enterOp(self, ctx: ducklangParser.OpContext):
        POper.append(ctx.getChild(0).getText())
    
    def enterSign(self, ctx: ducklangParser.SignContext):
        POper.append(ctx.getChild(0).getText())
    
    def exitFsign(self, ctx: ducklangParser.FsignContext):
        if(ctx.getChildCount() > 0):
            POper.pop()
    
    def exitTermino(self, ctx: ducklangParser.TerminoContext):
        if(len(POper) > 0):
            if(POper[-1] == '+' or POper[-1] == '-'):
                generateQuadExpression()
    
    def exitFactor(self, ctx: ducklangParser.FactorContext):
        if(len(POper) > 0):
            if(POper[-1] == '*' or POper[-1] == '/'):
                generateQuadExpression()
    
    def enterFactor(self, ctx: ducklangParser.FactorContext):
        if(ctx.getChild(0).getText() == '('):
            POper.append('(')
            self.current_fsign = ''
        elif(ctx.getChild(0).getChildCount() > 0):
            self.current_fsign = '-' if ctx.getChild(0).getChild(0).getText() == '-' else ''
        else:
            self.current_fsign = ''
    
    def exitExpresion(self, ctx: ducklangParser.ExpresionContext):
        if(len(POper) > 0):
            if(POper[-1] == '('):
                POper.pop()
    
    def enterComp(self, ctx: ducklangParser.CompContext):
        POper.append(ctx.getChild(0).getText())
    
    def exitEexp(self, ctx: ducklangParser.EexpContext):
        if(len(POper) > 0):
            comparativas = ['>', '<', '!=', '==']
            if(POper[-1] in comparativas):
                generateQuadExpression()
    
    def exitCont(self, ctx: ducklangParser.ContContext):
        global availTemp, contTemps
        print_param = child_type(ctx, 0)
        if(print_param == 'LETRERO'):
            print_text = ctx.getChild(0).getText()
            Quad.append(['print', print_text, None, None])
        elif(print_param == 'expresion'):
            print_exp = PilaO.pop()
            print_type = PTypes.pop()
            Quad.append(['print', print_exp, None, None])
            if(print_exp[0] == 't' and print_exp[-1].isdigit()):
                availTemp.append(print_exp)
                contTemps = contTemps - 1
    
    def exitAsigna(self, ctx: ducklangParser.AsignaContext):
        global availTemp, contTemps
        variable = ctx.getChild(0).getText()
        variable_type = tabla_simbolos['global'][variable] if variable in tabla_simbolos['global'] else tabla_simbolos['local'][variable] if variable in tabla_simbolos['local'] else None
        resultado = PilaO.pop()
        resultado_type = PTypes.pop()
        if(variable_type == None):
            raise Exception(f"Error semántico: Variable '{variable}' no declarada.")
        if(variable_type != resultado_type):
            raise Exception(f"Error semántico: Type mismatch. Variable '{variable}' no se le puede asinar resultado de tipo {resultado_type}.")
        Quad.append(['=', resultado, None, variable])
        if(resultado[0] == 't' and resultado[-1].isdigit()):
            availTemp.append(resultado)
            contTemps = contTemps - 1
    
    def enterCondicion(self, ctx: ducklangParser.CondicionContext):
        self.isExpCondicion = True
    
    def enterCuerpo(self, ctx: ducklangParser.CuerpoContext):
        global availTemp, contTemps
        if(self.isExpCondicion and len(PTypes) > 0):
            exp_type = PTypes.pop()
            if(exp_type != 'booleano'):
                raise Exception(f"Error semántico: Type mismatch. Expresión de condición no es de tipo booleano.")
            else:
                resultado = PilaO.pop()
                Quad.append(['GoToF', resultado, None])
                if(resultado[0] == 't' and resultado[-1].isdigit()):
                    availTemp.append(resultado)
                    contTemps = contTemps - 1
                PJumps.append(len(Quad)-1)
        self.isExpCondicion = False
    
    def exitCondicion(self, ctx: ducklangParser.CondicionContext):
        if(len(PJumps) > 0):
            posicion_end = PJumps.pop()
            Quad[posicion_end].append(len(Quad))
    
    def enterCsino(self, ctx: ducklangParser.CsinoContext):
        Quad.append(['GoTo', None, None])
        false = PJumps.pop()
        PJumps.append(len(Quad)-1)
        Quad[false].append(len(Quad))
    
    def enterCiclo(self, ctx: ducklangParser.CicloContext):
        PJumps.append(len(Quad))
        self.isExpCondicion = True
    
    def exitCiclo(self, ctx: ducklangParser.CicloContext):
        if(len(PJumps) > 0):
            posicion_end = PJumps.pop()
            posicion_return = PJumps.pop()
            Quad.append(['GoTo', None, None, posicion_return])
            Quad[posicion_end].append(len(Quad))
    
    def enterLlamada(self, ctx: ducklangParser.LlamadaContext):
        self.current_llamada = ctx.getChild(0).getText()
        if(self.current_llamada not in func_dir):
            raise Exception(f"Error semántico: Función '{self.current_llamada}' no declarada.")
        Quad.append(['ERA', self.current_llamada, None, None])
        self.k = 0
    
    def exitLexpresion(self, ctx: ducklangParser.LexpresionContext):
        global availTemp, contTemps
        argumento = PilaO.pop()
        argumento_tipo = PTypes.pop()
        parametro_tipo = list(func_dir[self.current_llamada]['parametros'].values())[self.k]
        if(parametro_tipo != argumento_tipo):
            raise Exception(f"Error semántico: Type mismatch. Argumento en posición {self.k+1} de llamada a función '{self.current_llamada}' no coincide con la firma de la función.")
        Quad.append(['PARAMETER', argumento, self.k, None])
        if(argumento[0] == 't' and argumento[-1].isdigit()):
            availTemp.append(argumento)
            contTemps = contTemps - 1
        self.k = self.k + 1
    
    def exitLlamada(self, ctx: ducklangParser.LlamadaContext):
        if(self.k != func_dir[self.current_llamada]['numParams']):
            raise Exception(f"Error semántico: Número de argumentos incorrecto en llamada a función '{self.current_llamada}'.")
        Quad.append(['GOSUB', self.current_llamada, None, None])
    
    def enterPrograma(self, ctx: ducklangParser.ProgramaContext):
        Quad.append(['GoTo', None, None])
    
    def exitPpfuncs(self, ctx: ducklangParser.PpfuncsContext):
        if(len(Quad[0]) == 3):
            Quad[0].append(len(Quad))