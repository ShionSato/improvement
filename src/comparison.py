import tcScan
from execution import Execution

# 実行結果比較メソッド
# 学生プログラムの実行結果と改善プログラムの実行結果を比較
def compare_text_files(student_output, gpt_output, i):
    text1 = student_output[i]
    text2 = gpt_output[i]
    if text1 == text2:
        return True
    else:
        return False
            
# テストケースの取得  
# 実行結果比較メソッドの呼び出し
def compare(class_name):
    check = True
    result = tcScan.testcase(str(class_name))
    if result is not None:
        command_line_args, standard_inputs, length = result
        student_output, gpt_output = Execution(class_name, command_line_args, standard_inputs, length)
        for i in range(length):
            if compare_text_files(student_output, gpt_output, i):
                print("testcase"+str(i+1)+"の内容は一致しています。")
            else:
                print("testcase"+str(i+1)+"の内容は一致していません。")
                check = False
        return check, length, student_output

if __name__ == "__main__":
    class_name = input("class:")
    compare(class_name) 