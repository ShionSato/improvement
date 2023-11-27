# プログラムの実行を行う

import subprocess
import tcScan
import antlr
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
upper_dir = os.path.dirname(current_dir)
gpt_path = os.path.join(current_dir,'gpt.java')
output_gpt_path = os.path.join(current_dir,'output_gfile.java')
output_student_path = os.path.join(current_dir,'output_sfile.java')

# 改善プログラムの文字の置き換え
def convert_java_gfile(file_name):   
    with open(gpt_path, "r") as file:
        input_text = file.read()
    new_string = input_text.replace("System.console().readLine", "MySystem.console().readLine")
    new_string = new_string.replace(str(antlr.get_className(gpt_path)), "output_gfile")
    with open(output_gpt_path, "w") as file:
        file.write(new_string)

# 学生プログラムの文字の置き換え
def convert_java_sfile(file_name):
    with open(upper_dir+"/"+str(file_name)+".java", "r") as file:
        input_text = file.read()
    new_string = input_text.replace("System.console().readLine", "MySystem.console().readLine")
    new_string = new_string.replace(str(file_name), "output_sfile")
    with open(output_student_path, "w") as file:
        file.write(new_string)

# プログラムの実行処理
def Execution(file_name, command_line_args, standard_inputs, length):
    convert_java_gfile(file_name)
    convert_java_sfile(file_name)
    subprocess.run(['javac','output_gfile.java'], cwd=current_dir)
    subprocess.run(['javac','output_sfile.java'], cwd=current_dir)
    java_cmd = ['java','output_gfile']
    java_scmd = ['java','output_sfile']

    student_result = []
    gpt_result = []
    
    # コマンドライン引数のみの問題
    if len(command_line_args) != 0 and len(standard_inputs) == 0:
        for i in range(len(command_line_args)):
            for row in command_line_args[i]:
                java_cmd.append(row)
                java_scmd.append(row) 

            result = subprocess.run(java_scmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, cwd=current_dir)
            output = result.stdout
            error_output = result.stderr
            student_result.append(output)
            if error_output:
                print("エラーメッセージ:")
                print(error_output)
            
            result = subprocess.run(java_cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, cwd=current_dir)
            output = result.stdout
            error_output = result.stderr
            gpt_result.append(output)
            if error_output:
                print("エラーメッセージ:")
                print(error_output)

        return student_result, gpt_result
    
    # 標準入力のみの問題
    elif len(standard_inputs) != 0 and len(command_line_args) == 0:
        standard_inputs_joined =([ "\n".join(row) for row in standard_inputs])
        for i in range(len(standard_inputs_joined)):
            input_text = standard_inputs_joined[i]
            input_text = input_text + "\n"

            result = subprocess.run(java_scmd, input=input_text, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, cwd=current_dir)
            output = result.stdout
            error_output = result.stderr
            student_result.append(output)
            if error_output:
                print("エラーメッセージ:")
                print(error_output)

            result = subprocess.run(java_cmd, input=input_text, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, cwd=current_dir)
            output = result.stdout
            error_output = result.stderr
            gpt_result.append(output)
            if error_output:
                print("エラーメッセージ:")
                print(error_output)

        return student_result, gpt_result
    
    # コマンドライン引数と標準入力が両方ある問題
    elif len(command_line_args) != 0 and len(standard_inputs) != 0:
        standard_inputs_joined =([ "\n".join(row) for row in standard_inputs])
        for i in range(length):
            java_cmd = ['java','output_gfile']
            java_scmd = ['java','output_sfile']
            for row in command_line_args[i]:
                java_cmd.append(row)
                java_scmd.append(row) 
            input_text = standard_inputs_joined[i]
            input_text = input_text + "\n"

            result = subprocess.run(java_scmd, input=input_text, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, cwd=current_dir)
            output = result.stdout
            error_output = result.stderr
            student_result.append(output)
            if error_output:
                print("エラーメッセージ:")
                print(error_output)

            result = subprocess.run(java_cmd, input=input_text, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, cwd=current_dir)
            output = result.stdout
            error_output = result.stderr
            gpt_result.append(output)
            if error_output:
                print("エラーメッセージ:")
                print(error_output)

        return student_result, gpt_result

    # 入力がない問題
    else:
        for i in range(length):
            result = subprocess.run(java_scmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, cwd=current_dir)
            output = result.stdout
            error_output = result.stderr
            student_result.append(output)
            if error_output:
                print("エラーメッセージ:")
                print(error_output)

            result = subprocess.run(java_cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, cwd=current_dir)
            output = result.stdout
            error_output = result.stderr
            gpt_result.append(output)
            if error_output:
                print("エラーメッセージ:")
                print(error_output)

        return student_result, gpt_result

if __name__ == "__main__":
    file_name = input("プログラム名を入力:")
    result = tcScan.testcase(str(file_name))
    if result is not None:
        command_line_args, standard_inputs, length = result
        Execution(file_name, command_line_args, standard_inputs, length)