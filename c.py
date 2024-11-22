import streamlit as st
import sqlite3
conn=sqlite3.connect('db.db')
cursor= conn.cursor()



def init_db():
    conn = sqlite3.connect("song_requests.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS song_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT '대기 중'  -- 기본 상태: 대기 중
        )
    """)
    conn.commit()
    conn.close()

init_db()

if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

if st.session_state.logged_in:
        st.success("이미 로그인 상태입니다.")
        st.info("다른 페이지로 이동하세요.")
else:
     id=st.text_input("이름",placeholder='이름을 입력하세요')
     pw=st.text_input("비밀번호",placeholder='비밀번호를 입력하세요')
     btn=st.button("로그인")

     if btn:
          cursor.execute(f"SELECT *FROM users WHERE username='{id}'")
          row=cursor.fetchone()
          if row:
               db_id=row[1]
               db_pw=row[2]
          else:
               db_id=''
               db_pw=''

          if db_pw==pw:
               st.write(f"{id}님 환영합니다")
               
          else:
               st.error("비밀번호 혹은 아이디가 일치하지 않습니다.")


