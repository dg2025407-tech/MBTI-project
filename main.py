import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="모동숲 주민 추천기 🍃",
    page_icon="🏕️",
    layout="centered"
)

# MBTI별 동물의 숲 주민 데이터 (이미지와 여러 명의 캐릭터 포함)
mbti_villagers = {
    "INTJ": [
        {"name": "로보", "image": "https://dodo.ac/np/images/4/44/Lobo_NH.png", "desc": "무뚝뚝해 보이지만 속은 따뜻하고 계획적인 늑대! 📚"},
        {"name": "시베리아", "image": "https://dodo.ac/np/images/1/18/Fang_NH.png", "desc": "규칙을 잘 지키고 쿨한 매력의 늑대! 혼자만의 시간을 소중히 해요. ❄️"}
    ],
    "INTP": [
        {"name": "잭슨", "image": "https://dodo.ac/np/images/2/2a/Raymond_NH.png", "desc": "똑똑하고 논리적이며 시크한 매력의 고양이! 지적 호기심이 넘쳐요. 💻"},
        {"name": "스파크", "image": "https://dodo.ac/np/images/c/c2/Static_NH.png", "desc": "까칠하지만 호기심 많은 다람쥐! 관심 분야에는 엄청난 집중력을 보여요. ⚡"}
    ],
    "ENTJ": [
        {"name": "아폴로", "image": "https://dodo.ac/np/images/2/28/Apollo_NH.png", "desc": "카리스마 넘치고 리더십이 뛰어난 독수리! 목표를 향해 거침없이 나아가요. 👑"},
        {"name": "비앙카", "image": "https://dodo.ac/np/images/6/6f/Whitney_NH.png", "desc": "기품 있고 주도적인 늑대! 어른스럽고 상황을 잘 이끌어가요. 💎"}
    ],
    "ENTP": [
        {"name": "쭈니", "image": "https://dodo.ac/np/images/c/c5/Marshal_NH.png", "desc": "재치 만점! 자신감 넘치고 말도 잘하는 다람쥐! 💡"},
        {"name": "리카르도", "image": "https://dodo.ac/np/images/a/a9/Kyle_NH.png", "desc": "자유로운 영혼의 능글맞은 늑대! 틀에 갇히지 않는 걸 좋아해요. 🎸"}
    ],
    "INFJ": [
        {"name": "사이다", "image": "https://dodo.ac/np/images/1/15/Lolly_NH.png", "desc": "다정하고 배려심 깊은 고양이! 친구들의 이야기에 깊게 공감해준답니다. 🎵"},
        {"name": "다람", "image": "https://dodo.ac/np/images/8/87/Sylvana_NH.png", "desc": "순둥하고 섬세한 다람쥐! 진정성 있는 관계를 중요하게 생각해요. 🌰"}
    ],
    "INFP": [
        {"name": "패치", "image": "https://dodo.ac/np/images/c/cf/Stitches_NH.png", "desc": "상상력이 풍부하고 감수성이 예민한 아기곰! 🎨"},
        {"name": "미애", "image": "https://dodo.ac/np/images/9/91/Judy_NH.png", "desc": "밤하늘을 담은 눈동자의 아기곰! 독특한 예술적 감각을 가졌어요. 🌌"}
    ],
    "ENFJ": [
        {"name": "솔미", "image": "https://dodo.ac/np/images/c/c4/Fauna_NH.png", "desc": "친절하고 헌신적인 사슴! 앞장서서 챙겨주는 따뜻한 친구예요. 🌻"},
        {"name": "나탈리", "image": "https://dodo.ac/np/images/f/f6/Diana_NH.png", "desc": "아름답고 우아한 사슴! 주변에 긍정적인 영향력을 주는 멘토 같아요. 🌟"}
    ],
    "ENFP": [
        {"name": "애플", "image": "https://dodo.ac/np/images/5/57/Apple_NH.png", "desc": "에너지가 넘치고 발랄한 햄스터! 언제나 마을의 분위기 메이커랍니다. 🍎"},
        {"name": "부케", "image": "https://dodo.ac/np/images/1/1a/Rosie_NH.png", "desc": "언제나 텐션이 높은 고양이! 사람을 너무너무 좋아해요. 🎀"}
    ],
    "ISTJ": [
        {"name": "늑태", "image": "https://dodo.ac/np/images/f/f4/Dobie_NH.png", "desc": "규칙을 잘 지키고 책임감 강한 늑대! 겉은 무뚝뚝해도 의리가 엄청나요. 📋"},
        {"name": "켄", "image": "https://dodo.ac/np/images/9/93/Ken_NH.png", "desc": "묵묵히 자기 할 일을 하는 닭! 전통과 예의를 중요하게 생각해요. 🥋"}
    ],
    "ISFJ": [
        {"name": "티나", "image": "https://dodo.ac/np/images/1/1a/Tia_NH.png", "desc": "섬세하고 따뜻한 마음을 가진 코끼리! 따뜻한 차 한 잔의 위로를 줘요. 🍵"},
        {"name": "마리아", "image": "https://dodo.ac/np/images/0/0c/Marcie_NH.png", "desc": "가족처럼 친구를 돌보는 캥거루! 사소한 것도 다 기억해 준답니다. 🍼"}
    ],
    "ESTJ": [
        {"name": "대장", "image": "https://dodo.ac/np/images/0/05/Chief_NH.png", "desc": "현실적이고 추진력이 강한 늑대! 맡은 일은 확실하게 해내요. 🏗️"},
        {"name": "호랭이", "image": "https://dodo.ac/np/images/5/50/Rowan_NH.png", "desc": "파이팅 넘치는 호랑이! 체계적으로 계획을 짜고 부지런하게 움직여요. 🏆"}
    ],
    "ESTP": [
        {"name": "차둘", "image": "https://dodo.ac/np/images/8/87/Dom_NH.png", "desc": "활동적이고 스포티한 양! 언제나 에너지가 넘치고 도전을 두려워하지 않아요. ⚽"},
        {"name": "1호", "image": "https://dodo.ac/np/images/4/47/Kid_Cat_NH.png", "desc": "히어로 헬멧을 쓴 고양이! 위기 상황에서 가장 먼저 몸을 던져요. 🦸‍♂️"}
    ],
    "ISTP": [
        {"name": "철깍", "image": "https://dodo.ac/np/images/1/1b/Ribbot_NH.png", "desc": "손재주가 좋고 쿨한 성격의 로봇 개구리! 묵묵히 관심사에 집중해요. 🛠️"},
        {"name": "뚝심", "image": "https://dodo.ac/np/images/0/09/Curt_NH.png", "desc": "과묵한 곰! 말보다는 행동으로 보여주는 츤데레 매력이 있어요. 🪓"}
    ],
    "ISFP": [
        {"name": "피터", "image": "https://dodo.ac/np/images/d/d4/Beau_NH.png", "desc": "평화롭고 느긋한 성격의 사슴! 자연을 사랑하는 예술가형이에요. 🦋"},
        {"name": "빙티", "image": "https://dodo.ac/np/images/7/7b/Bob_NH.png", "desc": "여유로운 고양이! 맛있는 간식을 먹으며 소소한 행복을 즐길 줄 알아요. 🥪"}
    ],
    "ESFJ": [
        {"name": "미첼", "image": "https://dodo.ac/np/images/f/f6/Sasha_NH.png", "desc": "사교적이고 친절함이 뚝뚝 묻어나는 토끼! 챙겨주는 걸 좋아해요. 🎈"},
        {"name": "첼시", "image": "https://dodo.ac/np/images/3/30/Chelsea_NH.png", "desc": "밝고 상냥한 사슴! 조화로운 분위기를 좋아해서 갈등을 잘 풀어줘요. 🍮"}
    ],
    "ESFP": [
        {"name": "모니카", "image": "https://dodo.ac/np/images/1/1b/Audie_NH.png", "desc": "스타성 최고! 활발하고 긍정적인 아이돌 지망생 늑대! 🎤"},
        {"name": "백프로", "image": "https://dodo.ac/np/images/b/b2/Tangy_NH.png", "desc": "상큼한 귤 헬멧을 쓴 고양이! 주변까지 신나게 만드는 텐션 100% 캐릭터예요. 🍊"}
    ]
}

# 랜덤으로 결과를 화면에 출력해주는 함수
def show_result(mbti_result):
    # 선택된 MBTI의 캐릭터 리스트를 가져옵니다.
    villager_list = mbti_villagers[mbti_result]
    
    # 리스트 중에서 랜덤으로 1명을 뽑습니다!
    result_data = random.choice(villager_list)
    
    st.write("---")
    st.subheader(f"🎉 당신과 찰떡궁합인 주민은... **{result_data['name']}**! ({mbti_result})")
    
    # 인터넷 URL을 사용해 이미지를 출력합니다.
    st.image(result_data["image"], width=250)
    
    st.info(f"**{result_data['name']}**는(은) {result_data['desc']}")
    st.balloons()
    st.success("팁💡: 같은 MBTI라도 다시 버튼을 누르면 다른 친구가 나올 수 있어요!")

# --- 화면 구성 시작 ---
st.title("🏕️ 모여봐요 동물의 숲 주민 추천기 🍃")
st.write("나의 MBTI를 알아보거나 선택해서, 나에게 맞는 주민을 찾아보세요! ✈️🏝️")

# 탭 기능 생성
tab1, tab2 = st.tabs(["📝 간단 MBTI 검사", "🔍 MBTI 직접 선택"])

with tab1:
    st.markdown("### 🧐 나에게 어울리는 주민 찾기 테스트")
    
    q1 = st.radio("1. 주말에 에너지를 충전하는 방법은?", ["(선택 안함)", "밖에서 친구들과 신나게 놀기 🏃‍♂️", "집에서 뒹굴거리며 혼자 쉬기 🛌"])
    q2 = st.radio("2. 문제를 해결할 때 나는?", ["(선택 안함)", "현실적이고 실용적인 방법을 찾는다 🔍", "창의적이고 새로운 아이디어를 떠올린다 💡"])
    q3 = st.radio("3. 친구가 고민을 털어놓을 때 나는?", ["(선택 안함)", "문제의 원인을 분석하고 해결책을 제시한다 🛠️", "친구의 감정에 먼저 공감하고 위로해준다 💖"])
    q4 = st.radio("4. 여행을 갈 때 나는?", ["(선택 안함)", "철저하게 일정을 계획하고 움직인다 📅", "발길이 닿는 대로 즉흥적인 여행을 즐긴다 🚶‍♂️"])

    if st.button("검사 결과 보기! 🎁", key="test_btn"):
        if "(선택 안함)" in [q1, q2, q3, q4]:
            st.warning("앗! 모든 질문에 답을 골라주세요. 😅")
        else:
            mbti_str = ""
            mbti_str += "E" if "밖에서" in q1 else "I"
            mbti_str += "S" if "현실적이고" in q2 else "N"
            mbti_str += "T" if "원인을 분석하고" in q3 else "F"
            mbti_str += "J" if "철저하게" in q4 else "P"
            
            show_result(mbti_str)

with tab2:
    st.markdown("### 🔍 이미 내 MBTI를 알고 있다면?")
    mbti_list = list(mbti_villagers.keys())
    selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", ["선택해주세요!"] + mbti_list)

    if st.button("바로 결과 확인하기! 🎲", key="select_btn"):
        if selected_mbti == "선택해주세요!":
            st.warning("앗! MBTI를 먼저 선택해주세요. 😅")
        else:
            show_result(selected_mbti)
