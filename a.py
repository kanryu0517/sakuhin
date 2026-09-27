# import streamlit as st

# # タイトル
# st.title("英単語クイズ")

# # 初期化
# if "q" not in st.session_state:
#     st.session_state.q = 0
# if "answered" not in st.session_state:
#     st.session_state.answered = False
# if "result" not in st.session_state:
#     st.session_state.result = ""

# # 問題を用意する
# questions = [
#     {"word": "apple", "answer": "りんご", "choices": ["りんご", "みかん", "ねこ", "車"]},
#     {"word": "cat", "answer": "ねこ", "choices": ["いぬ", "ねこ", "とり", "さかな"]},
# ]

# # クリア判定
# if st.session_state.q >= len(questions):
#     st.balloons()
#     st.write("クリア！")
# else:
#     # 今の問題
#     q = questions[st.session_state.q]
#     st.write(f"Q. {q['word']} の意味は？")

#     # まだ答えていないときだけ選択肢を出す
#     if not st.session_state.answered:
#         for choice in q["choices"]:
#             if st.button(choice):
#                 if choice == q["answer"]:
#                     st.session_state.result = "正解"
#                 else:
#                     st.session_state.result = "不正解"
#                 st.session_state.answered = True
#                 st.rerun()

#     # 答えたあとに結果を表示
#     if st.session_state.answered:
#         if st.session_state.result == "正解":
#             st.success("正解！")
#         else:
#             st.error("不正解")

#         # 次へボタン
#         if st.button("次へ"):
#             st.session_state.q += 1
#             st.session_state.answered = False
#             st.session_state.result = ""


import streamlit as st
st.title("英単語クイズ")

if "q" not in st.session_state:
    st.session_state.q = 0

if "answerd" not in st.session_state:
    st.session_state.answerd=False

if "result" not in st.session_state:
    st.session_state.result=""

questions = [
    {"word": "external", "answer": "外部の", "choices": ["過激", "交換", "永遠の", "外部の"]},
    {"word": "broom", "answer": "箒", "choices": ["吹く", "咲く", "箒", "血"]},
]

if st.session_state.q >= len(questions):
    st.balloons()
    st.write("クリア！")
else:
    q = questions[st.session_state.q]
    st.write(f"Q. {q['word']} の意味は？")

    if not st.session_state.answerd:
        for choice in q["choices"]:
            if st.button(choice):
                if choice == q["answer"]:
                    st.session_state.result = "正解！"
                else:
                    st.session_state.result = "不正解"

                st.session_state.answered = True
                st.rerun()

    if st.session_state.answerd:
        if st.session_state.result == "正解":
            st.success("正解！")
        else:
            st.error("不正解")

        if st.button("次へ"):
            st.session_state.q += 1
            st.session_state.answered = False
            st.session_state.result = ""
            st.rerun()