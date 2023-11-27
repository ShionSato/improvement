import pandas as pd
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
testcase_path = os.path.join(current_dir,'testcase.tsv')

# testcase.tsvから問題ごとのテストケースの取得
def testcase(quiz_id):
    command_line_args = []
    standard_inputs = []
    length = 0
    df = pd.read_csv(testcase_path, sep='\t')
    filtered_df = df[df['QUIZ_ID'] == quiz_id]

    for index, row in filtered_df.iterrows():
        if not pd.isna(row['COMMANDLINEARGS']):
            command_line_args.append(row['COMMANDLINEARGS'].split())
            length = len(filtered_df)
        else:
            length = len(filtered_df)

    for index, row in filtered_df.iterrows():
        if not pd.isna(row['STANDARDINPUTS']):
            standard_inputs.append(row['STANDARDINPUTS'].split())
            length = len(filtered_df)
        else:
            length = len(filtered_df)

    return command_line_args, standard_inputs, length

if __name__ == "__main__":
    quiz_id = input("クイズ名を入力")
    command_line_args, standard_inputs, length = testcase(quiz_id)
    print(command_line_args)
    print(standard_inputs)
    print(length)