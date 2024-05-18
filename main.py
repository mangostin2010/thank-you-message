import streamlit as st
from deta import Deta

code = """
<style>
.st-emotion-cache-bm2z3a {
    background: linear-gradient(135deg, #cefcff 0%, #a5cbff 100%);
}    
.st-emotion-cache-18ni7ap.ezrtsby2 {
    display: none;
}
.css-m70y {display:none}

.st-emotion-cache-eczf16 {
    display: none;
}

[data-testid="InputInstructions"] { display:None }

.st-b1, .st-b7 {
    background-color: transparent;
}

.st-b0, .st-az, .st-ay, .st-ax, .st-b6, .st-b5, .st-b4, .st-b3 {
    border-color: rgba(49, 51, 63, 0.2);
}

.st-emotion-cache-7ym5gk {
    background: #d3f4ff;
}

@media (max-width: 808px) {
  .st-emotion-cache-gh2jqd {
    max-width: calc(-2.5rem + 100vw);
  }
}

@media (max-width: 50.5rem) {
  .st-emotion-cache-13ln4jf {
    max-width: unset
  }
}

</style>
"""
st.html(code)


with st.form('스승의 날'):
    '## Thank You Message'
    name = st.text_input('이름을 작성하세요.')
    content = st.text_area('선생님에게 스승의 날 편지를 작성하세요.')
    if st.form_submit_button('제출'):
        DETA_KEY = 'c0vbyabfec4_HZTUNwCr9UgVMtBHRvFDPXcWUdh1Sa5R' # c0vbyabfec4_HZTUNwCr9UgVMtBHRvFDPXcWUdh1Sa5R
        deta = Deta(DETA_KEY)
        db = deta.Base("Messages")
        db.put({"key": name, "content": content})
        st.success('선생님에게 메시지가 전달되었습니다.')
