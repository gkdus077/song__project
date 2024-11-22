import streamlit as st
import sqlite3

st.header("관리자방🚫")

password = st.text_input("관리자 비밀번호를 입력하세요:", type="password")
btn = st.button("로그인")

    # 올바른 비밀번호 설정
ADMIN_PASSWORD = "aocjsqkdthd2024"  # 원하는 비밀번호로 설정하세요.

    # 비밀번호 검증
if btn:
    if password == ADMIN_PASSWORD:
        st.success("로그인 성공! 관리자 페이지에 접근합니다.")
        def get_requests():
            conn = sqlite3.connect("song_requests.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM song_requests")
            rows = cursor.fetchall()
            conn.close()
            return rows

        def update_status(request_id, status):
            conn = sqlite3.connect("song_requests.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE song_requests
                SET status = ?
                WHERE id = ?
            """, (status, request_id))
            conn.commit()
            conn.close()

        def add_request(title, artist):
            conn = sqlite3.connect("song_requests.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO song_requests (title, artist, status)
                VALUES (?, ?, '대기 중')
            """, (title, artist))
            conn.commit()
            conn.close()


        requests = get_requests()
        if requests:
             for req in requests:
                  st.write(f"ID: {req[0]}, 곡 제목: {req[1]}, 가수: {req[2]}, 상태: {req[3]}")
                  col1, col2 = st.columns(2)
                  with col1:
                    if st.button(f"승인 (ID: {req[0]})"):
                         update_status(req[0], "승인됨")
                    
                  with col2:
                    if st.button(f"거절 (ID: {req[0]})"):
                         update_status(req[0], "거절됨")
                    
        else:
            st.info("아직 신청곡이 없습니다.")
    else:
        st.warning("비밀번호를 다시 입력하세요.")