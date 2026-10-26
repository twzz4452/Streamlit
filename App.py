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
# 1. VPython 코드 원본
# ==========================================
VPYTHON_CODE = """GlowScript 3.2 VPython

scene = canvas(
    title="<b>⚽ SON 7 프리미엄 프리킥 & 오른쪽 상단 골인 시뮬레이션</b>",
    width=1050, height=650,
    center=vec(18, 2.2, 0),
    background=vec(0.02, 0.05, 0.12)
)

scene.camera.pos = vec(-5, 2.0, 4)
scene.camera.axis = vec(25, -0.2, -4)

ground = box(pos=vec(25, -0.11, 0), size=vec(100, 0.2, 50), color=vec(0.08, 0.4, 0.15))

goal_x = 35.0
goal_w = 7.32
goal_h = 2.44
goal_d = 2.0

post_left = cylinder(pos=vec(goal_x, 0, -goal_w/2), axis=vec(0, goal_h, 0), radius=0.08, color=color.white)
post_right = cylinder(pos=vec(goal_x, 0, goal_w/2), axis=vec(0, goal_h, 0), radius=0.08, color=color.white)
crossbar = cylinder(pos=vec(goal_x, goal_h, -goal_w/2), axis=vec(0, 0, goal_w), radius=0.08, color=color.white)
net_box = box(pos=vec(goal_x + goal_d/2, goal_h/2, 0), size=vec(goal_d, goal_h, goal_w), color=vec(0.9, 0.9, 0.9), opacity=0.15)

p_head = sphere(pos=vec(-1.5, 1.7, -0.4), radius=0.18, color=vec(0.9, 0.7, 0.6))
p_hair = ellipsoid(pos=vec(-1.5, 1.82, -0.4), size=vec(0.32, 0.15, 0.32), color=color.black)

p_torso = cylinder(pos=vec(-1.5, 0.9, -0.4), axis=vec(0, 0.7, 0), radius=0.22, color=color.red)
p_stripe = box(pos=vec(-1.5, 0.9, -0.4), size=vec(0.05, 0.68, 0.46), color=color.white)
num_7 = text(text="7", pos=vec(-1.76, 1.0, -0.55), axis=vec(0, 0, -1), height=0.22, depth=0.02, color=color.white)

p_short = cylinder(pos=vec(-1.5, 0.2, -0.4), axis=vec(0, 0.6, 0), radius=0.13, color=color.blue)
p_boot_l = box(pos=vec(-1.5, -0.1, -0.4), size=vec(0.15, 0.08, 0.28), color=color.black)

p_leg_r = cylinder(pos=vec(-1.4, 0.8, -0.2), axis=vec(0.1, -0.8, 0.2), radius=0.09, color=color.white)
p_boot_r = box(pos=vec(-1.3, -0.05, 0.0), size=vec(0.15, 0.08, 0.28), color=color.black)

R = 0.11
m = 0.43
g = vec(0, -9.81, 0)
rho = 1.225
Cd = 0.24
Cm = 0.26
A = pi * R**2

ball = sphere(
    pos=vec(0, R, 0),
    radius=R,
    color=color.white,
    make_trail=True,
    trail_color=vec(1, 0.8, 0),
    trail_radius=0.035
)

v0 = 29.0
angle_elevation = 18.5
angle_azimuth = 3.0

rad_elev = radians(angle_elevation)
rad_azim = radians(angle_azimuth)

vx = v0 * cos(rad_elev) * cos(rad_azim)
vy = v0 * sin(rad_elev)
vz = v0 * cos(rad_elev) * sin(rad_azim)
ball.v = vec(vx, vy, vz)

omega = vec(0, -25, 0)

for _ in range(12):
    rate(35)
    p_leg_r.axis = vec(0.3, -0.6, -0.3)

dt = 0.002
t = 0.0
goal_scored = False

while t < 3.5:
    rate(1/dt)
    if not goal_scored:
        v_mag = mag(ball.v)
        v_hat = hat(ball.v)
        F_net = (m * g) + (-0.5 * rho * Cd * A * (v_mag**2) * v_hat) + (0.5 * rho * Cm * A * R * cross(omega, ball.v))
        a = F_net / m
        ball.v = ball.v + a * dt
        ball.pos = ball.pos + ball.v * dt
        if ball.pos.x >= goal_x and (1.8 <= ball.pos.y <= 2.4) and (1.0 <= ball.pos.z <= 3.4):
            goal_scored = True
            ball.color = vec(1, 0.5, 0
