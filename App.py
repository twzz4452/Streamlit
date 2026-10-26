import json
import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

# ==========================================
# 0. Streamlit 기본 페이지 설정
# ==========================================
st.set_page_config(layout="wide")

# 사이드바 발표자 정보
st.sidebar.title("📌 발표자 정보")
st.sidebar.markdown("""
- **발표자**: [20402 김태우]
- **분야**: [물리, 정보(컴퓨터 모델링)]
""")

# ==========================================
# 1. VPython 코드 원본 (스트림릿 파싱 오류 방지를 위한 정제된 문자열)
# ==========================================
VPYTHON_CODE = r'''
# ==========================================
# 1. 3D 카메라 및 클로즈업 뷰 설정
# ==========================================
scene = canvas(
    title="<b>⚽ SON 7 프리미엄 프리킥 & 오른쪽 상단 골인 시뮬레이션</b>",
    width=1050, height=650,
    center=vec(18, 2.2, 0),
    background=vec(0.02, 0.05, 0.12)
)

# 카메라를 선수와 공 바로 측후면에 가깝게 배치
scene.camera.pos = vec(-5, 2.0, 4)
scene.camera.axis = vec(25, -0.2, -4)

# 축구장 바닥 (잔디)
ground = box(pos=vec(25, -0.11, 0), size=vec(100, 0.2, 50), color=vec(0.08, 0.4, 0.15))

# ==========================================
# 2. 골대 및 구조물 제작 (X = 35m 지점)
# =
