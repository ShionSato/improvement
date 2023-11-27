# ファイル入力を行うパターン

from flask import Flask, render_template, request
import improvement.NGquiz as NGquiz
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
    return render_template("index.html")

@app.route("/templates", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['fileInput']
        selected_number = request.form['selected_number']

        if uploaded_file.filename != '':
            if uploaded_file.filename in NGquiz.random_quiz:
                return render_template('index.html', ng_message="乱数を使用するプログラムは入力できません")
            if uploaded_file.filename in NGquiz.double_quiz:
                return render_template('index.html', ng_message="浮動小数点を使用するプログラムは入力できません")
            temp_file_path = os.path.join(current_dir, uploaded_file.filename)
            with open(temp_file_path, 'r') as file:
                    student_file = file.read() 
            uploaded_file.save(temp_file_path)
            class_name = antlr.get_className(temp_file_path)
            success = AI_exe.improvement(class_name,temp_file_path,gpt_path,selected_number)
            if(success):
                with open(gpt_path, 'r') as file:
                    result_text = file.read()
                return render_template('result.html', student=student_file,result=result_text)
            else:
                result_text = "生成回数オーバーによる改善失敗"
                return render_template('result.html', student=student_file, result=result_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
