import streamlit as st

# タイトル
st.title("英単語クイズ")

# 初期化
if "q" not in st.session_state:
    st.session_state.q = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "result" not in st.session_state:
    st.session_state.result = ""
if "score" not in st.session_state:
    st.session_state.score = 0

# 問題を用意する
questions = [
    {"word": "上げる", "answer": "raise", "choices": ["rise", "raise"]},
    {"word": "潰す", "answer": "crush", "choices": ["crush","crash"]},
    {"word": "箒", "answer": "broom", "choices": ["bloom", "broom"]},
    {"word": "犯罪", "answer": "crime", "choices": ["clime","crime"]},
    {"word": "違反", "answer": "breach", "choices": ["breach", "bleach"]},
    {"word": "恐れ", "answer": "fear", "choices": ["fare", "fear"]},
    {"word": "採用する", "answer": "adopt", "choices": ["adapt", "adopt"]},
    {"word": "考案する", "answer": "devise", "choices": ["device", "devise"]},
    {"word": "議会", "answer": "council", "choices": ["council","counsel"]},
    {"word": "適合する", "answer": "conform", "choices": ["conform", "confirm"]},
    {"word": "粗末な", "answer": "coarse", "choices": ["coerce", "coarse"]},
    {"word": "立てる", "answer": "erect", "choices": ["erect", "elect"]},
    {"word": "企業の", "answer": "corporate", "choices": ["corporate","cooperate"]},
    {"word": "定量化する", "answer": "quantify", "choices": ["quantity", "quantify"]},
    {"word": "世辞", "answer": "compliment", "choices": ["complement","compliment"]},
    {"word": "外部の", "answer": "external", "choices": ["extreme", "exchange", "eternal", "external"]},
    {"word": "詰め込む", "answer": "cram", "choices": ["clam", "clamp", "calm", "cram","cramp"]},
]

# クリア判定
if st.session_state.q >= len(questions):
    st.balloons()
    st.header("クリア！")
    st.write(f"正解数：{st.session_state.score} / {len(questions)}")
else:
    # 今の問題
    q = questions[st.session_state.q]
    st.write(f"Q. {q['word']} の意味は？")

    # まだ答えていないときだけ選択肢を出す
    if not st.session_state.answered:
        for choice in q["choices"]:
            if st.button(choice):
                if choice == q["answer"]:
                    st.session_state.result = "正解"
                    st.session_state.score += 1  # 正解したら1点増やす
                else:
                    st.session_state.result = "不正解"

                st.session_state.answered = True
                st.rerun()

    # 答えたあとに結果を表示
    if st.session_state.answered:
        if st.session_state.result == "正解":
            st.success("正解！")
        else:
            st.error("不正解")

        # 次へボタン
        if st.button("次へ"):
            st.session_state.q += 1
            st.session_state.answered = False
            st.session_state.result = ""
    