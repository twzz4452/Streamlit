GlowScript 3.2 VPython

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
# ==========================================
goal_x = 35.0
goal_w = 7.32
goal_h = 2.44
goal_d = 2.0

# 골대 프레임
post_left = cylinder(pos=vec(goal_x, 0, -goal_w/2), axis=vec(0, goal_h, 0), radius=0.08, color=color.white)
post_right = cylinder(pos=vec(goal_x, 0, goal_w/2), axis=vec(0, goal_h, 0), radius=0.08, color=color.white)
crossbar = cylinder(pos=vec(goal_x, goal_h, -goal_w/2), axis=vec(0, 0, goal_w), radius=0.08, color=color.white)

# 골망 영역 시각화
net_box = box(pos=vec(goal_x + goal_d/2, goal_h/2, 0), size=vec(goal_d, goal_h, goal_w), color=vec(0.9, 0.9, 0.9), opacity=0.15)

# ==========================================
# 3. 손흥민 스타일 선수 모델 (7번 유니폼 & 축구화)
# ==========================================
p_head = sphere(pos=vec(-1.5, 1.7, -0.4), radius=0.18, color=vec(0.9, 0.7, 0.6))
p_hair = ellipsoid(pos=vec(-1.5, 1.82, -0.4), size=vec(0.32, 0.15, 0.32), color=color.black)

p_torso = cylinder(pos=vec(-1.5, 0.9, -0.4), axis=vec(0, 0.7, 0), radius=0.22, color=color.red)
p_stripe = box(pos=vec(-1.5, 0.9, -0.4), size=vec(0.05, 0.68, 0.46), color=color.white)

# 유니폼 등번호 '7'번 마킹
num_7 = text(text="7", pos=vec(-1.76, 1.0, -0.55), axis=vec(0, 0, -1), height=0.22, depth=0.02, color=color.white)

p_short = cylinder(pos=vec(-1.5, 0.2, -0.4), axis=vec(0, 0.6, 0), radius=0.13, color=color.blue)
p_boot_l = box(pos=vec(-1.5, -0.1, -0.4), size=vec(0.15, 0.08, 0.28), color=color.black)

p_leg_r = cylinder(pos=vec(-1.4, 0.8, -0.2), axis=vec(0.1, -0.8, 0.2), radius=0.09, color=color.white)
p_boot_r = box(pos=vec(-1.3, -0.05, 0.0), size=vec(0.15, 0.08, 0.28), color=color.black)

# ==========================================
# 4. 축구공 물리 매개변수 및 생성
# ==========================================
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

# ==========================================
# 5. [수정됨] 오른쪽 상단 골인을 위한 향상된 슈팅 초기 조건
# ==========================================
v0 = 29.0               # 초기 속도를 높여서 공이 힘 있게 날아가도록 수정
angle_elevation = 18.5  # 발사 각도를 높여 공이 위로 솟구치며 골대 상단을 향하도록 수정
angle_azimuth = 3.0     # 오른쪽 방향각

rad_elev = radians(angle_elevation)
rad_azim = radians(angle_azimuth)

vx = v0 * cos(rad_elev) * cos(rad_azim)
vy = v0 * sin(rad_elev)
vz = v0 * cos(rad_elev) * sin(rad_azim)
ball.v = vec(vx, vy, vz)

omega = vec(0, -25, 0)

print("🔥 SON 7 프리킥! 우측 상단 골인 슈팅 시작!")

# ==========================================
# 6. 킥 모션 애니메이션
# ==========================================
for _ in range(12):
    rate(35)
    p_leg_r.axis = vec(0.3, -0.6, -0.3)

# ==========================================
# 7. 물리 시뮬레이션 루프
# ==========================================
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
        
        # 골대 오른쪽 상단 통과 판정 (범위를 골대 상단 높이에 맞게 조정)
        if ball.pos.x >= goal_x and (1.8 <= ball.pos.y <= 2.4) and (1.0 <= ball.pos.z <= 3.4):
            goal_scored = True
            print("🎉 GOAL IN!! 오른쪽 상단 구석 명중!")
            ball.color = vec(1, 0.5, 0)
            
        if ball.pos.y <= R:
            ball.pos.y = R
            break
    else:
        ball.v = ball.v * 0.82
        ball.pos = ball.pos + ball.v * dt
        if ball.pos.x >= goal_x + 1.5:
            ball.pos.x = goal_x + 1.5
            ball.v = vec(0, 0, 0)
            
    t = t + dt
