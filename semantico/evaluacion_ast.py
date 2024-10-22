
from analizador_sintactico import symbol_table
from analizador_sintactico import current_scope
from semantico.aritmeticas import *
from semantico.condicionales_logicas import *
from semantico.movimiento import *
from semantico.procedimientos_declaraciones import *
from semantico.ciclos import *

# Almacena todos los procedimientos que hayan para tener sus referencias cuando sean llamados
lista_procedimientos_temp = []

class evaluacion_ast:

    def __init__(self, ast):
        self.ast = ast

    def evaluar_ast(self, elemento):

        if isinstance(elemento, Programa):
           proc_compuesto = elemento.proc_compuesto
           self.evaluacion_ast(proc_compuesto)
           return None

        if isinstance(elemento, ProcCompuesto):
            
            # se verifica la función main
            funcion_main = elemento.inicio
            self.evaluar_ast(funcion_main)

            # se verifian el resto de funciones
            lista_funciones = elemento.set_proc
            for funcion in lista_funciones:
                self.evaluar_ast(funcion)
            return None
            
        # LISTO
        if isinstance(elemento,Funcion):
            lista_procedimientos_temp.insert(elemento)  # se almacena el objeto de la función en la lista temporal de procedimientos
            def_funcion_exito = elemento.calculate()
            if (def_funcion_exito == True):
                parser.current_scope = elemento.nombre  # se actualiza el ambito a la función actual, pues se estará verificando el cuuerpo
                lista_expresiones_funcion = elemento.cuerpo.expresiones
                for expresion in lista_expresiones_funcion:
                    self.evaluar_ast(expresion)
            return None
            # No se deben verificar aquellas expresiones que dependan de un parámetro

        # LISTO
        if isinstance(elemento,Def_variable): # no ocupa de parámetros del procedimiento
            def_variable_exito = elemento.calculate()
            
            if(def_variable_exito):
                if isinstance(elemento.valor, int) or isinstance(elemento,bool):
                    return None  # cuando el valor dado a la variable es un int o bool
                else:
                    # cuando el valor de dado a la variable es una operación aritmética que retorna valor (objeto)
                    self.evaluar_ast(elemento.valor)
            
            return None
        
        # LISTO
        if isinstance(elemento,Put): # no ocupa de parámetros del procedimiento
            def_variable_exito = elemento.calculate()
            
            if(def_variable_exito):
                if isinstance(elemento.valor, int) or isinstance(elemento.valor,bool):
                    return None  # cuando el valor dado a la variable es un int o bool
                else:
                    # cuando el valor de dado a la variable es una operación aritmética que retorna valor
                    self.evaluar_ast(elemento.valor)
            
            return None

        #LISTO
        if isinstance(elemento, Llamada_funcion):
            llamada_funcion_exito = elemento.calculate()

            if(llamada_funcion_exito):
                # Se guarda el scope actual como temporal antes de cambiar el scope del parser
                temp_scope_actual = parser.current_scope

                # Se cambia el scope del parser pues se verificará la función con los parámetros
                parser.current_scope = elemento.nombre

                lista_expresiones_funcion = []
                for procedimiento in lista_procedimientos_temp:
                    if(procedimiento.nombre == elemento.nombre):
                        # Se obtiene el cuerpo (expresion) del procedimiento para verificarlo ahora con los parámetros
                        lista_expresiones_funcion = procedimiento.cuerpo.expresiones
                        break;
            
                for expresion in lista_expresiones_funcion:
                    self.evaluar_ast(expresion)

                # se restaura el scope del parser al actual
                parser.current_scope = temp_scope_actual

            return None
        
        # LISTO, se debe verificar que no se tome un parámetro para modificar
        if isinstance(elemento,AddOne):
            elemento.calculate()
            return None

        #LISTO
        if isinstance(elemento,AddVar):
            elemento.calculate()
            return None

        if isinstance(element, WritingIf):
            solve = element.calculate()
            self.evaluate(solve)
            print(parser.symbol_table)

        if isinstance(element, WritingIfElse):
            solve = element.calculate()
            self.evaluate(solve)
            print(parser.symbol_table)

        if isinstance(element, WritingWhile):
            solve = element.calculate()
            if isinstance(solve, Sequence):
                self.evaluate(solve)
                self.evaluate(element)

        if isinstance(element, Repeat):
            solve = element.calculate()
            if isinstance(solve, Sequence):
                self.evaluate(solve)
                self.evaluate(element)

        if isinstance(element, Run):
            solve = element.calculate()
            if solve:
                self.evaluate(solve)

        if isinstance(element, ContinueUp):
            solve = element.calculate()

        if isinstance(element, ContinueDown):
            solve = element.calculate()

        if isinstance(element, ContinueLeft):
            solve = element.calculate()

        if isinstance(element, ContinueRight):
            solve = element.calculate()

        if isinstance(element, Pos):
            solve = element.calculate()

        if isinstance(element, PosX):
            solve = element.calculate()

        if isinstance(element, PosY):
            solve = element.calculate()

        if isinstance(element, Up):
            solve = element.calculate()

        if isinstance(element, Down):
            solve = element.calculate()

        if isinstance(element, Begin):
            solve = element.calculate()

        if isinstance(element, Speed):
            solve = element.calculate()


