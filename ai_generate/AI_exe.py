from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# OpenAIのAPIKeyを取得する
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    client = OpenAI(api_key=api_key)
else:
    print("APIキーが見つかりませんでした。")
    
# ファイルのパスを取得
current_dir = os.path.dirname(os.path.abspath(__file__))
system_path = os.path.join(current_dir,'system.txt')
redundancy_path = os.path.join(current_dir,'redundancy.txt')

import sys
sys.path.append('../src')
import antlr
import comparison
import pro1_syntax

prior_input = []
after_input = []
count = 0
success = False
studentCCN = 0

# 改善システムのメインプログラム
# 各変数の初期化と生成メソッドの呼び出し
def improvement(className,input_file_path,output_file_path,number):
    global count,studentCCN
    count = 0
    prior_input.clear()
    after_input.clear()
    java_syntax = pro1_syntax.Syntax(number)
    with open(input_file_path, 'r') as file:
      file_content = file.read()
    syntax_string = '\n'.join(map(str, java_syntax))
    syntax_string = "\"available syntax\"\n"+syntax_string

    with open(system_path, 'r') as system_file:
        system_message_content = system_file.read()

    with open(redundancy_path, 'r') as redundancy_file:
        redundancy_content = redundancy_file.read()

    prior_input.append({"role": "user", "content": system_message_content})
    prior_input.append({"role": "user", "content": syntax_string})
    prior_input.append({"role": "user", "content": redundancy_content})
    prior_input.append({"role": "user", "content": file_content})
    studentCCN = antlr.get_Cyclomatic(input_file_path)
    generate(className,input_file_path,output_file_path,syntax_string,number)
    return success

# 生成メソッド
# 生成プログラムをログ追加
# 生成回数のカウント処理
def generate(className,input_file_path,output_file_path,syntax_string,number):
    global count,success
    count += 1
    print(count)
    if count >= 6:
      success = False
      return success
    response = chat()
    after_input.append({"role": "assistant", "content": response})
    with open(output_file_path, 'w') as file:
        file.write(str(response))
    
    NgCheck1(className,input_file_path,output_file_path,syntax_string,number)

# AIによる改善プログラム生成
def chat():
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=prior_input+after_input
  )
  return completion.choices[0].message.content

# サイクロマティック複雑度と行数の比較
def CyclomaticCheck(input_file_path,output_file_path):
   gptCCN = antlr.get_Cyclomatic(output_file_path)
   if(gptCCN > studentCCN):
      count1 = count_lines(output_file_path)
      count2 = count_lines(input_file_path)
      print(gptCCN,studentCCN)
      if count1 >= count2:
        after_input.append({"role": "user", "content": "Generate with low cyclomatic complexity and fewer rows.\nPlease return only the improved program."})
        return False
   else:
      return True

# 行数の取得
def count_lines(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        return len(lines)

# ホワイトリスト判断
def NgCheck1(className,input_file_path,output_file_path,syntax_string,number):
  ng = antlr.get_NotJavaRule(output_file_path,number)
  if len(ng) > 0:
    print(ng)
    NG_syntax = "\n".join(ng)
    after_input.append({"role": "user", "content": NG_syntax+"\nParsing found these syntaxes that we do not want you to use. Please check the ”available syntax” again and improve it!\n"})
    after_input.append({"role": "user", "content": syntax_string+"\nSend only the program without any extra explanation!"})
    generate(className,input_file_path,output_file_path,syntax_string,number)
  else:
    if CyclomaticCheck(input_file_path,output_file_path):
      NgCheck2(className,input_file_path,output_file_path,syntax_string,number)
    else:
      print("Cyclomatic error")
      generate(className,input_file_path,output_file_path,syntax_string,number)

# 実行結果比較
def NgCheck2(className,input_file_path,output_file_path,syntax_string,number):
  global success
  result = comparison.compare(className)
  student_result = ""
  check, length , student_output= result
  print(check)
  if check == False:
      for i in range(length):
          student_result = student_result + "Execution"+str(i)+"\n" +student_output[i] + "\n"
      after_input.append({"role": "user", "content": student_result+"\nModify the program so that the result looks like this.\nSend only the program without any extra explanation!"})
      generate(className,input_file_path,output_file_path,syntax_string,number)
  else:
    success = True

if __name__ == "__main__":
   improvement()

   