import streamlit as st
from openai import OpenAI

api_key = st.text_input("OpenAI API Key", type="password")
question = st.text_input("질문을 입력하세요:")

if st.button("질문하기"):
    if api_key and question:
        client = OpenAI(api_key=api_key)
        with st.spinner("GPT에게 물어보는 중..."):
            response = client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "user", "content": question}]
            )
            st.success("응답 완료!")
            st.write(response.choices[0].message.content)
    else:
        st.warning("API Key와 질문을 모두 입력하세요.")
