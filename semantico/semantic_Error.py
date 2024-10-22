
import sys

from semantico.error_log import ErrorLog
import analizador_sintactico as parser

def identificar_error(codigo_error, linea_error):

    if codigo_error == 0:
        error_message = "ERROR SEMANTICO: EL PROCEDIMIENTO REQUIERE DE CUERPO" + str(linea_error)
        parser.semantic_err = True
        return error_message

    if codigo_error == 1:
        parser.symbol_table.clear()
        error_message = "ERROR SEMANTICO: NO EXITE EL PROCEDIMIENTO MAIN DECLARADO"
        parser.semantic_err = True
        return error_message

    if codigo_error == 2:
        parser.symbol_table.clear()
        error_message = "ERROR SEMANTICO: EXISTEN MULTIPLES PROCEDIMIENTOS MAIN DECLARADOS"
        parser.semantic_err = True
        return error_message
    
    if codigo_error == 3:
        error_message = "ERROR SEMANTICO EN LINEA " + str(linea_error) + ": LA VARIABLE YA HA SIDO DECLARADA"
        parser.semantic_err = True
        return error_message
    
    if codigo_error == 4:
        error_message = "ERROR SEMANTICO EN lINEA " + str(linea_error) + ": NO EXISTE DICHA VARIABLE DE TIPO INT"
        parser.semantic_err = True
        return error_message
    
    if codigo_error == 5:
        error_message = "ERROR SEMANTICO EN lINEA " + str(linea_error) + ": NO EXISTE DICHA VARIABLE DE TIPO BOOL"
        parser.semantic_err = True
        return error_message

    if codigo_error == 6:
        error_message = "ERROR SEMANTICO EN lINEA " + str(linea_error) + ": LA VARIABLE NO EXISTE"
        parser.semantic_err = True
        return error_message
    
    if codigo_error == 7:
        error_message = "ERROR SEMANTICO EN lINEA " + str(linea_error) + ": GLOBAL VARIABLE DOES NOT EXIST"
        parser.semantic_err = True
        return error_message
    
    if codigo_error == 8:
        error_message = "ERROR SEMANTICO EN lINEA " + str(linea_error) + ": NO ES POSIBLE MODIFCAR UN PARAMETRO DE UN PROCEDIMIENTO"
        parser.semantic_err = True
        return error_message
    
    if codigo_error == 9:
        parser.symbol_table.clear()
        error_message = "ERROR SEMANTICO" + ": FIRMA DE PROCEDIMIENTO DUPLICADA"
        parser.semantic_err = True
        return error_message

    if codigo_error == 10:
        parser.symbol_table.clear()
        error_message = "ERROR SEMANTICO: EL VALOR MÁXIMO DEBE SER MAYOR AL VALOR MINIMO: " + str(linea_error)
        parser.semantic_err = True
        return error_message

    if codigo_error == 11:
        parser.symbol_table.clear()
        error_message = "ERROR SEMANTICO: LOS VALORES NO SON DEL MISMO TIPO: " + str(linea_error)
        parser.semantic_err = True
        return error_message

    if codigo_error == 12:
        parser.symbol_table.clear()
        error_message = "ERROR SEMANTICO: NUMERO DE PARAMETROS NO COINCIDE CON EL ESPERADO: " + str(linea_error)
        parser.semantic_err = True
        return error_message 

    if codigo_error == 13:
        parser.symbol_table.clear()
        error_message = "ERROR SEMANTICO: NO SE HA DECLARADO LA FUNCION: " + str(linea_error)
        parser.semantic_err = True
        return error_message

    if codigo_error == 14:
        parser.symbol_table.clear()
        error_message = "ERROR SEMANTICO: PARÁMETRO DE PROCEDIMIENTO NO PUEDE SER DECLARADO: " + str(linea_error)
        parser.semantic_err = True
        return error_message              