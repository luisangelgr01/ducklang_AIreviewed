from ducklangListener import ducklangListener
from ducklangParser import ducklangParser

#estructuras de datos de apoyo para el análisis semántico
func_dir = {}

tabla_simbolos = {
    'global': {},
    'local': {}
}

cubo_semantico = {
    'entero': {
        'entero': {'+': 'entero', '-': 'entero', '*': 'entero', '/': 'flotante'},
        'flotante': {'+': 'flotante', '-': 'flotante', '*': 'flotante', '/': 'flotante'}
    },
    'flotante': {
        'entero': {'+': 'flotante', '-': 'flotante', '*': 'flotante', '/': 'flotante'},
        'flotante': {'+': 'flotante', '-': 'flotante', '*': 'flotante', '/': 'flotante'}
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
            if nombre in tabla_simbolos[scope] or nombre in tabla_simbolos['global']:
                raise Exception(f"Error semántico: Variable '{nombre}' se volvió a declarar en el scope {scope}.")
            tabla_simbolos[scope][nombre] = tipo

    def enterFuncs(self, ctx: ducklangParser.FuncsContext):
        self.scope = 'local'
        self.current_func = ctx.getChild(1).getText()
        if self.current_func in func_dir:
            raise Exception(f"Error semántico: Función '{self.current_func}' se volvió a declarar.")
        self.current_func_params = {}
    
    def exitTipo(self, ctx: ducklangParser.TipoContext):
        self.current_func_var_tipo = ctx.getChild(0).getText()
    
    def exitFid(self, ctx: ducklangParser.FidContext):
        var_nombre = ctx.getChild(0).getText()
        if var_nombre in self.current_func_params:
            raise Exception(f"Error semántico: Parámetro '{var_nombre}' se volvió a declarar en la función '{self.current_func}'.")
        self.current_func_params[var_nombre] = self.current_func_var_tipo
    
    def exitFidtipo(self, ctx: ducklangParser.FidtipoContext):
        func_dir[self.current_func] = {
            'parametros': self.current_func_params
        }
    
    def exitFuncs(self, ctx: ducklangParser.FuncsContext):
        self.current_func = None
        self.current_func_params = {}
        self.current_func_var_tipo = None
        tabla_simbolos['local'] = {}
    
    def exitPrograma(self, ctx: ducklangParser.ProgramaContext):
        print('\nDirectorio de funciones al finalizar programa:')
        print(func_dir)
        print('\nTabla de símbolos al finalizar programa:')
        print(tabla_simbolos)