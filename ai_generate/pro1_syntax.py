syntax =[]

# 各回の使用可能構文の設定
def Syntax(number):
    if(int(number)>=11):
        syntax = ["クラス宣言",
                  "メインメソッド",
                  "System.out.print",
                  "\\n, \\t",
                  "変数宣言",
                  "System.console().readLine",
                  "Integer.parseInt",
                  "Math.random()",
                  "Math.sqrt()",
                  "Math.pow()",
                  "キャストによる型変換",
                  "Double.parseDouble",
                  "if文",
                  "if-else文",
                  "for文",
                  "配列",
                  "コマンドライン引数"]
        return syntax
    
    elif(int(number)>=9):
        syntax = ["クラス宣言",
                  "メインメソッド",
                  "System.out.print",
                  "\\n, \\t",
                  "変数宣言",
                  "System.console().readLine",
                  "Integer.parseInt",
                  "Math.random()",
                  "Math.sqrt()",
                  "Math.pow()",
                  "キャストによる型変換",
                  "Double.parseDouble",
                  "if文",
                  "if-else文",
                  "for文"]
        return syntax
    elif(int(number)>=6):
        syntax = ["クラス宣言",
                  "メインメソッド",
                  "System.out.print",
                  "\\n, \\t",
                  "変数宣言",
                  "System.console().readLine",
                  "Integer.parseInt",
                  "Math.random()",
                  "Math.sqrt()",
                  "Math.pow()",
                  "キャストによる型変換",
                  "Double.parseDouble",
                  "if文",
                  "if-else文"]
        return syntax
    elif(int(number)>=5):
        syntax = ["クラス宣言",
                  "メインメソッド",
                  "System.out.print",
                  "\\n, \\t",
                  "変数宣言",
                  "System.console().readLine",
                  "Integer.parseInt",
                  "Math.random()",
                  "Math.sqrt()",
                  "Math.pow()",
                  "キャストによる型変換",
                  "Double.parseDouble"]
        return syntax
    elif(int(number)>=4):
        syntax = ["クラス宣言",
                  "メインメソッド",
                  "System.out.print",
                  "\\n, \\t",
                  "変数宣言",
                  "System.console().readLine",
                  "Integer.parseInt",
                  "Math.random()",
                  "Math.sqrt()",
                  "Math.pow()"]
        return syntax
    elif(int(number)>=3):
        syntax = ["クラス宣言",
                  "メインメソッド",
                  "System.out.print",
                  "\\n,\\t",
                  "変数宣言"]
        return syntax
    elif(int(number)>=1):
        syntax = ["クラス宣言",
                  "メインメソッド",
                  "System.out.print",
                  "\\n, \\t"]
        return syntax
        
if __name__ == "__main__":
    syntax = []
    syntax = Syntax(input("class:"))
    print(syntax)