from antlr4 import *
from Java8Lexer import Java8Lexer
from Java8Parser import Java8Parser
from Java_listener import Java8Listener
import javarule1
import javarule2
import javarule3
import javarule4
import javarule5
import javarule6
import javarule7
listener = Java8Listener()

# 構文解析を行う
def analysis(input_file):
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = Java8Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Java8Parser(token_stream)

    parser.addParseListener(listener)

    tree = parser.compilationUnit()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

# プログラムのクラス名を取得する
def get_className(input_file):
    analysis(input_file)
    if listener.get_class() is not None:
        return listener.get_class()
    else:
        print("Class Name not found")

# ホワイトリストで弾かれた構文を取得する
def get_NotJavaRule(input_file,i):
    javarule = get_javarule(i)
    analysis(input_file)
    NotJavarule = []
    for item in listener.foundInMethodBody:
        if item not in javarule:
            NotJavarule.append(item)
    
    return NotJavarule

# サイクロマティック複雑度を取得する
def get_Cyclomatic(input_file):
    analysis(input_file)
    Cyclomatic = listener.get_cyclomatic()
    CCN = Cyclomatic
    listener.Cyclomatic_clear()
    return CCN

# 各授業回ごとの構文のホワイトリストを取得
def get_javarule(i):
    if(int(i)==1 or int(i)==2):
        javarule = javarule1.javaRule
    elif(int(i)==3):
        javarule = javarule2.javaRule
    elif(int(i)==4):
        javarule = javarule3.javaRule
    elif(int(i)==5):
        javarule = javarule4.javaRule
    elif(int(i)==6 or int(i)==7 or int(i)==8):
        javarule = javarule5.javaRule
    elif(int(i)==9 or int(i)==10):
        javarule = javarule6.javaRule
    elif(int(i)==11 or int(i)==12 or int(i)==13):
        javarule = javarule7.javaRule
    return javarule

if __name__ == "__main__":
    print(get_NotJavaRule('/Users/satoushion/improvement/src/gpt.java',11))
    

