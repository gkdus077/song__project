import streamlit as st
import sqlite3

conn=sqlite3.connect('db.db')
cursor=conn.cursor()

st.title("회원가입")
id= st.text_input("이름",placeholder='이름을 입력하세요')
pw= st.text_input("비밀번호",placeholder='비밀번호를 입력하세요',type='password')
pw_check=st.text_input("비밀번호 확인",placeholder='비밀번호를 재입력하세요',type='password')
gender=st.radio("성별을 선택하세요",['male','female'])


btn=st.button("회원가입")
if btn:
        if pw==pw_check:
            sql = f"""
insert into users(username,password,gender)
values('{id}','{pw}','{gender}')"""
            cursor.execute(sql)
            conn.commit()
            st.success("회원가입 성공")
        else:
            st.error("비밀번호가 일치하지 않습니다.")


    