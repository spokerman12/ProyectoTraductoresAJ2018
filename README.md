# Titulo: RealPars

Descripcion: Interpretador del lenguaje BasicTran
			 Analizador lexicografico sintactico y de contexto. 
             Fase 4 del proyecto de CI3725 - Traductores e Interpretadores

Autores:
Daniel Francis     12-10863
Javier Vivas       12-11067 

Fecha: 13/07/2018.

## Instrucciones

1. En linux, correr el comando "chmod +x RealPars" en el directorio donde se encuentra RealPars.
2. Ejecutar "./RealPars <Nombre de archivo>" donde el archivo es un documento de codigo de BasicTran



## ¿Cómo se interpreta el lenguaje?

Se hace un análisis léxico, luego sintáctico siguiendo la gramática definida. Al seguir la gramática, se forma un árbol, decorado con las instrucciones y operaciones pertinentes.

Las llamadas "operaciones" tienen un "resultado", dependiente del alcance. (Véase clase Operacion)
Las "instrucciones" tienen una "ejecución", también dependiente del contexto. (Incluye If's, For's y demás)

Se recorre el árbol y se ejecutan las operaciones e instrucciones pertinentes.

## Referencias

Aho - Compilers, Principles, Techniques and Tools.
