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
# 1. VPython 코드 (리스트 조인 방식으로 따옴표/줄바꿈 에러 원천 차단)
# ==========================================
VPYTHON_CODE = "\n".join([
    "GlowScript 3.2 VPython",
    "scene = canvas(",
    "    title='<b>⚽ SON 7 프리미엄 프리킥 & 오른쪽 상단 골인 시뮬레이션</b>',",
    "    width=1050, height=650,",
    "    center=vec(18, 2.2, 0),",
    "    background=vec(0.02, 0.05, 0.12)",
    ")",
    "scene.camera.pos = vec(-5, 2.0, 4)",
    "scene.camera.axis = vec(25, -0.2, -4)",
    "ground = box(pos=vec(25, -0.11, 0), size=vec(100, 0.2, 50), color=vec(0.08, 0.4, 0.15))",
    "goal_x = 35.0",
    "goal_w = 7.32",
    "goal_h = 2.44",
    "goal_d = 2.0",
    "post_left = cylinder(pos=vec(goal_x, 0, -goal_w/2), axis=vec(0, goal_h, 0), radius=0.08, color=color.white)",
    "post_right = cylinder(pos=vec(goal_x, 0, goal_w/2), axis=vec(0, goal_h, 0), radius=0.08, color=color.white)",
    "crossbar = cylinder(pos=vec(goal_x, goal_h, -goal_w/2), axis=vec(0, 0, goal_w), radius=0.08, color=color.white)",
    "net_box = box(pos=vec(goal_x + goal_d/2, goal_h/2, 0), size=vec(goal_d, goal_h, goal_w), color=vec(0.9, 0.9, 0.9), opacity=0.15)",
    "p_head = sphere(pos=vec(-1.5, 1.7, -0.4), radius=0.18, color=vec(0.9, 0.7, 0.6))",
    "p_hair = ellipsoid(pos=vec(-1.5, 1.82, -0.4), size=vec(0.32, 0.15, 0.32), color=color.black)",
    "p_torso = cylinder(pos=vec(-1.5, 0.9, -0.4), axis=vec(0, 0.7, 0), radius=0.22, color=color.red)",
    "p_stripe = box(pos=vec(-1.5, 0.9, -0.4), size=vec(0.05, 0.68, 0.46), color=color.white)",
    "num_7 = text(text='7', pos=vec(-1.76, 1.0, -0.55), axis=vec(0, 0, -1), height=0.22, depth=0.02, color=color.white)",
    "p_short = cylinder(pos=vec(-1.5, 0.2, -0.4), axis=vec(0, 0.6, 0), radius=0.13, color=color.blue)",
    "p_boot_l = box(pos=vec(-1.5, -0.1, -0.4), size=vec(0.15, 0.08, 0.28), color=color.black)",
    "p_leg_r = cylinder(pos=vec(-1.4, 0.8, -0.2), axis=vec(0.1, -0.8, 0.2), radius=0.09, color=color.white)",
    "p_boot_r = box(pos=vec(-1.3, -0.05, 0.0), size=vec(0.15, 0.08, 0.28), color=color.black)",
    "R =
