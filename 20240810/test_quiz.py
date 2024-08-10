import random

# クイズの質問と選択肢を定義
quiz = [
    {
        "question": "Pythonの開発者は誰ですか？",
        "choices": ["Guido van Rossum", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Pythonの最新バージョンは何ですか？（2024年現在）",
        "choices": ["3.8", "3.9", "3.10", "3.11"],
        "answer": "3.11"
    },
    {
        "question": "Pythonのデータ型に含まれないものはどれですか？",
        "choices": ["list", "tuple", "dictionary", "array"],
        "answer": "array"
    },
    {
        "question": "Pythonで無限ループを作成するにはどの構文を使いますか？",
        "choices": ["for", "while", "if", "def"],
        "answer": "while"
    }
]

# クイズをランダムに選択
def random_quiz(quiz):
    question = random.choice(quiz)
    print("質問: " + question["question"])
    for i, choice in enumerate(question["choices"], 1):
        print(f"{i}. {choice}")
    return question

# ユーザーの回答をチェック
def check_answer(question, user_answer):
    correct_answer = question["answer"]
    if question["choices"][user_answer - 1] == correct_answer:
        print("正解！")
    else:
        print(f"不正解。正解は {correct_answer} です。")

# クイズを実行
selected_question = random_quiz(quiz)
user_answer = int(input("答えを選んでください（1-4）: "))
check_answer(selected_question, user_answer)
