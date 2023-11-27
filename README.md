# 改善プログラムの説明

改善システムの処理に関わるプログラムは以下。それぞれの右側の括弧内はファイルが入っているフォルダ(improvementからの相対)

* main.py
* antlr.py (src)
* tcScan.py (src)
* execution.py (src)
* comparison.py (src)
* pro1_syntax.py (ai_generate)
* AI_exe.py (ai_generate)

## main.py
リストボックスで受講済みの授業回を入力、テキストでプログラムを入力するindex.htmlを表示するプログラム。

このプログラムをターミナルで実行すると[プログラムを入力するwebサイト](http://127.0.0.1:5000)が動く。

入力されたテキストを一度構文解析し、クラス名を取得。取得したクラス名のJavaファイルとして保存。

取得したクラス名が、乱数を使用する課題リストか浮動小数点を使用する課題リストの中にある場合入力できない旨のメッセージを表示。

保存したJavaファイルを元にAIによる改善システムを呼び出す。

実行後に結果を返すresult.htmlを表示。

改善に成功したらresult.htmlに改善後のプログラムを表示、改善に失敗したら改善失敗を表示する。

## antlr.py
ANTLRによる構文解析を行うプログラム。

index.htmlで入力された授業回を元にリストを切り替えてホワイトリスト判断を行う。

クラス名を取得するメソッドやホワイトリストで弾かれた構文を取得するメソッド、サイクロマティック複雑度を取得するメソッドなどがある。

##　tcScan.py
PLATEから保存したtestcase.tsvから各問題のテストケースを取得するプログラム。

## execution.py
tcScan.pyで取得したテストケースを元に、学生が入力したプログラムとAIによって改善されたプログラムを実行するプログラム。

Javaプログラムに含まれるSystem.console()をMySystem.console()に置き換える処理を行う。

subprocessを用いてjavacコマンドとjavaコマンドを実行する。

## comparison.py
execution.pyで実行した両プログラムの実行結果を比較するプログラム。

実行結果が一致したならTrueを、実行結果が不一致ならFalseを返す。

## pro1_syntax.py
index.htmlで入力された授業回を元に、AIへ指示する使用可能構文を返すプログラム。

## AI_exe.py
OpenAIによって学生のプログラムを改善するプログラム。

AIが行うことを記したsystem.txtと冗長の定義を記したredundancy.txt、pro1_syntax.pyから返された使用可能構文、学生のプログラムを最初の指示として改善を実行。

antlr.pyによって構文解析を行いホワイトリスト判断で弾かれなければサイクロマティック複雑度と行数による改善判断を行う。

その後、comparison.pyによる実行結果の比較を行う。

各チェックで弾かれた場合には生成されたプログラム、それぞれに対応した指示文を新たに追加して再帰的に生成を行わせる。