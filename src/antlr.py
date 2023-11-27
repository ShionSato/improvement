from antlr4 import *
from Java8Lexer import Java8Lexer
from Java8Parser import Java8Parser
from Java_listener import Java8Listener
import JavaRule
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
        javarule = JavaRule.javaRule1
    elif(int(i)==3):
        javarule = JavaRule.javaRule2
    elif(int(i)==4):
        javarule = JavaRule.javaRule3
    elif(int(i)==5):
        javarule = JavaRule.javaRule4
    elif(int(i)==6 or int(i)==7 or int(i)==8):
        javarule = JavaRule.javaRule5
    elif(int(i)==9 or int(i)==10):
        javarule = JavaRule.javaRule6
    elif(int(i)==11 or int(i)==12 or int(i)==13):
        javarule = JavaRule.javaRule7
    return javarule

if __name__ == "__main__":
    print(get_NotJavaRule('/Users/satoushion/improvement/src/gpt.java',11))
    

