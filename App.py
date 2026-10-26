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
# 1. VPython 코드 (따옴표 에러 원천 차단형)
# ==========================================
VPYTHON_CODE = (
    "GlowScript 3.2 VPython\n"
    "scene = canvas(\n"
    "    title='<b>⚽ SON 7 프리미엄 프리킥 & 오른쪽 상단 골인 시뮬레이션</b>',\n"
    "    width=1050, height=650,\n"
    "    center=vec(18, 2.2, 0),\n"
    "    background=vec(0.02, 0.05, 0.12)\n"
    ")\n"
    "scene.camera.pos = vec(-5, 2.0, 4)\n"
    "scene.camera.axis = vec(25, -0.2, -4)\n"
    "ground = box(pos=vec(25, -0.11, 0), size=vec(100, 0.2, 50), color=vec(0.08, 0.4, 0.15))\n"
    "goal_x = 35.0\n"
    "goal_w = 7.32\n"
    "goal_h = 2.44\n"
    "goal_d = 2.0\n"
    "post_left = cylinder(pos=vec(goal_x, 0, -goal_w/2), axis=vec(0, goal_h, 0), radius=0.08, color=color.white)\n"
    "post_right = cylinder(pos=vec(goal_x, 0, goal_w/2), axis=vec(0, goal_h, 0), radius=0.08, color=color.white)\n"
    "crossbar = cylinder(pos=vec(goal_x, goal_h, -goal_w/2), axis=vec(0, 0, goal_w), radius=0.08, color=color.white)\n"
    "net_box = box(pos=vec(goal_x + goal_d/2, goal_h/2, 0), size=vec(goal_d, goal_h, goal_w), color=vec(0.9, 0.9, 0.9), opacity=0.15)\n"
    "p_head = sphere(pos=vec(-1.5, 1.7, -0.4), radius=0.18, color=vec(0.9, 0.7, 0.6))\n"
    "p_hair = ellipsoid(pos=vec(-1.5, 1.82, -0.4), size=vec(0.32, 0.15, 0.32), color=color.black)\n"
    "p_torso = cylinder(pos=vec(-1.5, 0.9, -0.4), axis=vec(0, 0.7, 0), radius=0.22, color=color.red)\n"
    "p_stripe = box(pos=vec(-1.5, 0.9, -0.4), size=vec(0.05, 0.68, 0.46), color=color.white)\n"
    "num_7 = text(text='7', pos=vec(-1.76, 1.0, -0.55), axis=vec(0, 0, -1), height=0.22, depth=0.02, color=color.white)\n"
    "p_short = cylinder(pos=vec(-1.5, 0.2, -0.4), axis=vec(0, 0.6, 0), radius=0.13, color=color.blue)\n"
    "p_boot_l = box(pos=vec(-1.5, -0.1, -0.4), size=vec(0.15, 0.08, 0.28), color=color.black)\n"
    "p_leg_r = cylinder(pos=vec(-1.4, 0.8, -0.2), axis=vec(0.1, -0.8, 0.2), radius=0.09, color=color.white)\n"
    "p_boot_r = box(pos=vec(-1.3, -0.05, 0.0), size=vec(0.15, 0.08, 0.28), color=color.black)\n"
    "R = 0.11\n"
    "m = 0.43\n"
    "g = vec(0, -9.81, 0)\n"
    "rho = 1.225\n"
    "Cd = 0.24\n"
    "Cm = 0.26\n"
    "A = pi * R**2\n"
    "ball = sphere(pos=vec(0, R, 0), radius=R, color=color.white, make_trail=True, trail_color=vec(1, 0.8, 0), trail_radius=0.035)\n"
    "v0 = 29.0\n"
    "angle_elevation = 18.5\n"
    "angle_azimuth = 3.0\n"
    "rad_elev = radians(angle_elevation)\n"
    "rad_azim = radians(angle_azimuth)\n"
    "vx = v0 * cos(rad_elev) * cos(rad_azim)\n"
    "vy = v0 * sin(rad_elev)\n"
    "vz = v0 * cos(rad_elev) * sin(rad_azim)\n"
    "ball.v = vec(vx, vy, vz)\n"
    "omega = vec(0, -25, 0)\n"
    "for _ in range(12):\n"
    "    rate(35)\n"
    "    p_leg_r.axis = vec(0.3, -0.6, -0.3)\n"
    "dt = 0.002\n"
    "t = 0.0\n"
    "goal_scored = False\n"
    "while t < 3.5:\n"
    "    rate(1/dt)\n"
    "    if not goal_scored:\n"
    "        v_mag = mag(ball.v)\n"
    "        v_hat = hat(ball.v)\n"
    "        F_net = (m * g) + (-0.5 * rho * Cd * A * (v_mag**2) * v_hat) + (0.5 * rho * Cm * A * R * cross(omega, ball.v))\n"
    "        a = F_net / m\n"
    "        ball.v = ball.v + a * dt\n"
    "        ball.pos = ball.pos + ball.v * dt\n"
    "        if ball.pos.x >= goal_x and (1.8 <= ball.pos.y <= 2.4) and (1.0 <= ball.pos.z <= 3.4):\n"
    "            goal_scored = True\n"
    "            ball.color = vec(1, 0.5, 0)\n"
    "        if ball.pos.y <= R:\n"
    "            ball.pos.y = R\n"
    "            break\n"
    "    else:\n"
    "        ball.v = ball.v * 0.82\n"
    "        ball.pos = ball.pos + ball.v * dt\n"
    "        if ball.pos.x >= goal_x + 1.5:\n"
    "            ball.pos.x = goal_x + 1.5\n"
    "            ball.v = vec(0, 0, 0)\n"
    "    t = t + dt\n"
)

# ==========================================
# 2. 시뮬레이션 표시 코드 (수정 금지)
# ==========================================
GLOWSCRIPT = "https://www.glowscript.org"

PAGE = """<!doctype html>
<html><head><meta charset="utf-8">
<link type="text/css" href="__GS__/css/redmond/2.1/jquery-ui.custom.css" rel="stylesheet" />
<link type="text/css" href="__GS__/css/ide.css" rel="stylesheet" />
<script src="__GS__/lib/jquery/2.1/jquery.min.js"></script>
<script src="__GS__/lib/jquery/2.1/jquery-ui.custom.min.js"></script>
<script src="__GS__/package/glow.3.2.min.js"></script>
<script src="__GS__/package/RScompiler.3.2.min.js"></script>
<script src="__GS__/package/RSrun.3.2.min.js"></script>
<style>
  body { background: white; margin: 0; padding: 8px; font-family: sans-serif; }
  #error { color: #c00; white-space: pre-wrap; font-family: monospace; }
</style>
</head><body>
<div id="error"></div>
<div id="glowscript" class="glowscript"></div>
<script>
function showError(msg) {
  document.getElementById("error").textContent = "시뮬레이션 오류: " + msg;
}
window.onerror = function (msg) { showError(msg); };
try {
  var source = __SOURCE__;
  var js = glowscript_compile(source, {lang: "vpython", version: "3.2"});
  window.__context = { glowscript_container: $("#glowscript").removeAttr("id") };
  (0, eval)(js + ";window.__main = __main__;");
  var result = window.__main();
  if (result && result.catch) result.catch(function (e) { showError(e); });
} catch (e) {
  showError(e);
}
</script>
</body></html>
"""


def show_vpython(code, height=800):
    source_js = json.dumps(code.strip()).replace("</", "<\\/")
    html = PAGE.replace("__GS__", GLOWSCRIPT).replace("__SOURCE__", source_js)
    components.html(html, height=height, scrolling=True)


# ==========================================
# 3. 6개 탭 구성 (발표 내용 기반)
# ==========================================
st.title("⚽ 과학 탐구 발표 웹앱")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "① 탐구 질문", 
    "② 시뮬레이션", 
    "③ 원리", 
    "④ 결과 분석", 
    "⑤ 결론과 한계", 
    "⑥ 퀴즈"
])

# 탭 ① 탐구 질문(가설 포함)
with tab1:
    st.subheader("주제 (탐구 질문)")
    st.info("축구 프리킥 시 공기 저항과 마그누스 효과는 공의 3차원 궤적과 골인 지점에 어떤 영향을 미칠까?")
    
    st.subheader("가설")
    st.success("초기 속도와 발사 각도가 고정되어 있더라도, 공의 회전(각속도 벡터)에 의한 마그누스 효과를 코드로 구현하면 공이 포물선 궤적에서 휘어져 골대 우측 상단 구석으로 정밀하게 명중할 것이다.")

# 탭 ② 시뮬레이션(사용 방법 한 줄 + show_vpython)
with tab2:
    st.subheader("시뮬레이션 구동")
    st.markdown("GlowScript 3.2 VPython 웹 에디터에 시뮬레이션 코드를 입력하고 실행(Run)하면, 손흥민 선수 모델의 다리 휘두르기 킥 모션과 동시에 공이 발사되어 35m 전방 골대 상단을 향해 날아가는 3D 애니메이션이 구동된다.")
    show_vpython(VPYTHON_CODE, height=900)

# 탭 ③ 원리(수식은 st.latex)
with tab3:
    st.subheader("원리와 관련 식")
    st.markdown("1. 중력:")
    st.latex(r"\vec{F}_g = m\vec{g} \text{ (연직 아래 방향)}")
    
    st.markdown("2. 공기 저항 (Drag Force):")
    st.latex(r"\vec{F}_d = -\frac{1}{2}\rho C_d A v^2 \hat{v} \text{ (속도의 제곱에 비례하는 저항)}")
    
    st.markdown("3. 마그누스 효과
