import streamlit as st
pages = {
    "회원" : [
        st.Page("./page/a.py", title="공지사항📣"),
        st.Page("./page/b.py", title="회원가입"),
        st.Page("./page/c.py", title="로그인")
    ],
    "곡 신청" : [
        st.Page("./page/d.py", title="신청방"),
        st.Page("./page/f.py", title="관리자방")
    ]
}
pg = st.navigation(pages)
pg.run()