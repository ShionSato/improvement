# テキスト入力を行うパターン

from flask import Flask, render_template, request
import improvement.NGquiz2 as NGquiz2
import sys
import os
sys.path.append('./src')
sys.path.append('./openai_env')
import antlr
import AI_exe
current_dir = os.path.dirname(os.path.abspath(__file__))
gpt_path = os.path.join(current_dir,'src','gpt.java')
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("index2.html")

@app.route("/templates", methods=["GET"])
def index():
    return render_template("index2.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        selected_number = request.form['selected_number']
        code_input = request.form['code_input']
        code_file_path = os.path.join(current_dir, 'input.java')
        if code_input:
            with open(code_file_path, 'w') as file:
                file.write(code_input)
        else:
            return render_template('index2.html', ng_message="プログラムを入力してください")
        class_name = antlr.get_className(code_file_path)
        if class_name in NGquiz2.random_quiz:
            return render_template('index2.html', ng_message="乱数を使用するプログラムは入力できません")
        if class_name in NGquiz2.double_quiz:
                return render_template('index2.html', ng_message="浮動小数点を使用するプログラムは入力できません")
        temp_file_path = os.path.join(current_dir, str(class_name)+'.java')
        with open(temp_file_path, 'w') as file:
                file.write(code_input)
        success = AI_exe.improvement(class_name,temp_file_path,gpt_path,selected_number)
        if(success):
            with open(gpt_path, 'r') as file:
                result_text = file.read()
            return render_template('result.html', student=code_input,result=result_text)
        else:
            result_text = "生成回数オーバーによる改善失敗"
            return render_template('result.html', student=code_input, result=result_text)
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
