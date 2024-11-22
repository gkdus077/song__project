import streamlit as st
import sqlite3


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


def add_request(title, artist):
    conn = sqlite3.connect("song_requests.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO song_requests (title, artist, status)
        VALUES (?, ?, '대기 중')
    """, (title, artist))
    conn.commit()
    conn.close()


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

# 데이터 가져오기 함수
def get_requests():
    conn = sqlite3.connect("song_requests.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM song_requests")
    rows = cursor.fetchall()
    conn.close()
    return rows


init_db()

if "logged_in" not in st.session_state:
     st.session_state.logged_in = False

    
if not st.session_state.logged_in:
    st.warning("로그인을 하지 않을 시 곡 신청 승인이 불가합니다.로그인을 하고 와주세요")
    

st.title("신청방")
st.warning("19금 노래는 피해주세요🔞")
st.warning("5분 이상인 노래는 피해주세요.")

with st.form("song_request_form"):
        st.subheader("신청곡 입력")
        title = st.text_input("곡 제목", "")
        artist = st.text_input("가수 이름", "")
        submit = st.form_submit_button("신청하기")

if submit:
            if not title or not artist:
                st.error("곡 제목과 가수 이름을 모두 입력해주세요.")
            else:
                add_request(title, artist)
                st.success(f"신청곡 '{title}'이(가) 접수되었습니다!")



