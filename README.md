# ducklang_AIreviewed

[Documentation (Spanish)](https://docs.google.com/document/d/10ikBZkRi_IMPekerjUT-cDc6o7W0vfb0DKV0LHtO4fQ/edit?usp=sharing)

## Prerequisites
- Python 3
- Java 11

## Installation and execution
1. Create a Python virtual environment
```
python3 -m venv venv
```
2. Activate virtual environment
```
source venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
````
4. (If needed) Make changes to the lexer and parser in the "ducklang.g4" file, then run this command to generate the necessary Python module files
```
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 ducklang.g4
```
5. (If needed) Make changes to the input file where the ducklang code is ("input_ducklang_code.txt")
6. (If needed) Make changes to the Python files (main, lexer, parser, listeners, visitors)
7. Execute the parser
```
python main.py
```
8. Deactivate virtual environment
```
deactivate venv
```


### Created by Luis Ángel González Romo, using Python with ANTLR4 with BSD License
