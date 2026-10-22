import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(
    page_title="AI 맞춤형 여행지 추천",
    page_icon="✈️",
    layout="wide"
)

# 2. 샘플 여행지 데이터베이스
# 실제 서비스라면 CSV나 데이터베이스에서 불러올 수 있습니다.
travel_data = [
    {
        "name": "강원도 강릉",
        "category": "국내",
        "style": "힐링/자연",
        "budget": "보통",
        "desc": "푸른 동해바다와 안목해변의 커피 거리, 그리고 소나무숲이 어우러진 힐링 도시입니다.",
        "highlights": ["안목해변 커피거리", "정동진 바다부채길", "초당순두부마을"],
        "emoji": "🌊"
    },
    {
        "name": "제주도 서귀포",
        "category": "국내",
        "style": "액티비티/탐험",
        "budget": "여유",
        "desc": "환상적인 해안 절벽과 올레길, 스노클링을 즐길 수 있는 대한민국 최고의 휴양지입니다.",
        "highlights": ["성산일출봉", "중문 색달해변", "한라산 등반"],
        "emoji": "🍊"
    },
    {
        "name": "일본 오사카",
        "category": "해외",
        "style": "미식/쇼핑",
        "budget": "보통",
        "desc": "타코야키, 오코노미야키 등 길거리 음식의 천국이자 쇼핑의 성지입니다.",
        "highlights": ["도톤보리 글리코상", "오사카 성", "유니버설 스튜디오 재팬"],
        "emoji": "🐙"
    },
    {
        "name": "태국 방콕",
        "category": "해외",
        "style": "문화/역사",
        "budget": "알뜰",
        "desc": "화려한 왕궁과 이국적인 야시장, 가성비 최고의 미식과 마사지를 즐길 수 있는 곳입니다.",
        "highlights": ["왓 아룬 사원", "짜뚜짝 주말시장", "카오산 로드"],
        "emoji": "🛕"
    },
    {
        "name": "스위스 인터라켄",
        "category": "해외",
        "style": "액티비티/탐험",
        "budget": "럭셔리",
        "desc": "알프스의 대자연 속에서 스카이다이빙과 하이킹을 즐길 수 있는 액티비티의 성지입니다.",
        "highlights": ["융프라우요흐", "하더 쿨룸 전망대", "패러글라이딩"],
        "emoji": "🏔️"
    },
    {
        "name": "부산 광안리",
        "category": "국내",
        "style": "미식/쇼핑",
        "budget": "보통",
        "desc": "화려한 광안대교 야경과 바다를 보며 즐기는 맛있는 회와 해산물의 도시입니다.",
        "highlights": ["광안리 드론쇼", "민락수변공원", "해운대 블루라인파크"],
        "emoji": "🌉"
    }
]

df = pd.DataFrame(travel_data)

# 3. 메인 타이틀
st.title("✈️ AI 맞춤형 여행지 추천 시스템")
st.markdown("원하는 여행 스타일과 조건을 선택하시면 최적의 여행지를 골라드립니다!")
st.divider()

# 4. 사이드바 - 사용자 필터 입력
st.sidebar.header("🔍 여행 취향 설정")

selected_category = st.sidebar.radio(
    "1. 여행 지역 선택",
    ["전체", "국내", "해외"]
)

selected_style = st.sidebar.selectbox(
    "2. 선호하는 여행 스타일",
    ["전체", "힐링/자연", "액티비티/탐험", "미식/쇼핑", "문화/역사"]
)

selected_budget = st.sidebar.select_slider(
    "3. 예산 수준",
    options=["알뜰", "보통", "여유", "럭셔리"],
    value="보통"
)

# 5. 필터링 로직 구현
filtered_df = df.copy()

if selected_category != "전체":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

if selected_style != "전체":
    filtered_df = filtered_df[filtered_df["style"] == selected_style]

# 예산 필터 (선택한 예산과 같거나 그 이하인 항목 우선, 또는 일치 항목)
# 여기서는 예산 수준 매칭을 위해 간단히 필터링
budget_order = {"알뜰": 1, "보통": 2, "여유": 3, "럭셔리": 4}
filtered_df = filtered_df[
    filtered_df["budget"].map(budget_order) <= budget_order[selected_budget]
]

# 6. 결과 출력 영역
st.subheader(f"🎯 추천 결과 ({len(filtered_df)}건)")

if filtered_df.empty:
    st.warning("조건에 맞는 여행지가 없습니다. 필터를 조금 더 넓게 설정해 보세요!")
else:
    # 2열 그리드로 카드 배치
    cols = st.columns(2)
    for idx, row in filtered_df.reset_index().iterrows():
        col = cols[idx % 2]
        with col:
            with st.container(border=True):
                st.markdown(f"### {row['emoji']} {row['name']}")
                st.caption(f"카테고리: {row['category']} | 스타일: {row['style']} | 예산: {row['budget']}")
                st.write(row["desc"])
                
                st.markdown("**🌟 핵심 추천 코스**")
                for highlight in row["highlights"]:
                    st.markdown(f"- {highlight}")
                    
                if st.button(f"상세 일정 보기 ({row['name']})", key=f"btn_{idx}"):
                    st.success(f"🎉 [{row['name']}] 선택완료! 곧 상세 일정 플래너 기능이 업데이트됩니다.")

# 7. 푸터
st.divider()
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Travel Recommender App. Built with Streamlit.</p>", unsafe_allow_html=True)
