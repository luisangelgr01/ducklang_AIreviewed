from ducklangListener import ducklangListener
from ducklangParser import ducklangParser

func_dir = {}

# Symbol table structure
tabla_simbolos = {
    'global': {},  #'Global'scope dictionary for variables
    'local': {}    # Local scope dictionary for variables (e.g., within functions)
}

# Example of a semantic cube for type compatibility with operators
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
        self.scope = 'global'  # Default scope is'global'
        self.current_ids = []
        self.current_func = None
        self.current_func_params = []
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
        # Check if the variable has already been declared in the current scope
        for nombre in nombres:
            if nombre in tabla_simbolos[scope]:
                raise Exception(f"Error semántico: Variable '{nombre}' se volvió a declarar en el scope {scope}.")
            # If not, add the variable to the symbol table with its type
            tabla_simbolos[scope][nombre] = tipo

    def enterFuncs(self, ctx: ducklangParser.FuncsContext):
        self.scope = 'local'
        self.current_func = ctx.getChild(1).getText()
        self.current_func_params = []
    
    def exitTipo(self, ctx: ducklangParser.TipoContext):
        self.current_func_var_tipo = ctx.getChild(0).getText()
    
    def exitFid(self, ctx: ducklangParser.FidContext):
        self.current_func_params.append((ctx.getChild(0).getText(), self.current_func_var_tipo))
    
    def exitFidtipo(self, ctx: ducklangParser.FidtipoContext):
        func_dir[self.current_func] = {
            'parameters': self.current_func_params
        }
    
    def exitFuncs(self, ctx: ducklangParser.FuncsContext):
        self.current_func = None
        self.current_func_params = []
        self.current_func_var_tipo = None
        tabla_simbolos['local'] = {}
    
    def exitPrograma(self, ctx: ducklangParser.ProgramaContext):
        print('\nDirectorio de funciones al finalizar programa:')
        print(func_dir)
        print('\nTabla de símbolos al finalizar programa:')
        print(tabla_simbolos)