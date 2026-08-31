import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="모동숲 주민 추천기 🍃",
    page_icon="🏕️",
    layout="centered"
)

# MBTI별 동물의 숲 주민 데이터 (이미지 URL 추가)
# 인터넷에 있는 동물들의 실제 이미지 주소(URL)를 넣었습니다.
mbti_villagers = {
    "INTJ": {"name": "로보", "image": "https://dodo.ac/np/images/4/44/Lobo_NH.png", "desc": "무뚝뚝해 보이지만 속은 따뜻하고 계획적인 늑대! 📚"},
    "INTP": {"name": "잭슨", "image": "https://dodo.ac/np/images/2/2a/Raymond_NH.png", "desc": "똑똑하고 논리적이며 시크한 매력의 고양이! 💻"},
    "ENTJ": {"name": "아폴로", "image": "https://dodo.ac/np/images/2/28/Apollo_NH.png", "desc": "카리스마 넘치고 리더십이 뛰어난 독수리! 👑"},
    "ENTP": {"name": "쭈니", "image": "https://dodo.ac/np/images/c/c5/Marshal_NH.png", "desc": "재치 만점! 자신감 넘치고 말도 잘하는 다람쥐! 💡"},
    "INFJ": {"name": "사이다", "image": "https://dodo.ac/np/images/1/15/Lolly_NH.png", "desc": "다정하고 배려심 깊은 고양이! 깊은 공감을 해준답니다. 🎵"},
    "INFP": {"name": "패치", "image": "https://dodo.ac/np/images/c/cf/Stitches_NH.png", "desc": "상상력이 풍부하고 감수성이 예민한 아기곰! 🎨"},
    "ENFJ": {"name": "솔미", "image": "https://dodo.ac/np/images/c/c4/Fauna_NH.png", "desc": "친절하고 헌신적인 사슴! 앞장서서 챙겨주는 따뜻한 친구예요. 🌻"},
    "ENFP": {"name": "애플", "image": "https://dodo.ac/np/images/5/57/Apple_NH.png", "desc": "에너지가 넘치고 발랄한 햄스터! 언제나 마을의 분위기 메이커랍니다. 🌟"},
    "ISTJ": {"name": "시베리아", "image": "https://dodo.ac/np/images/1/18/Fang_NH.png", "desc": "규칙을 잘 지키고 책임감 강한 늑대! 끝까지 의리를 지켜요. 🛡️"},
    "ISFJ": {"name": "티나", "image": "https://dodo.ac/np/images/1/1a/Tia_NH.png", "desc": "섬세하고 따뜻한 마음을 가진 코끼리! 따뜻한 차 한 잔의 위로를 줘요. 🍵"},
    "ESTJ": {"name": "대장", "image": "https://dodo.ac/np/images/0/05/Chief_NH.png", "desc": "현실적이고 추진력이 강한 늑대! 맡은 일은 확실하게 해내요. 🏗️"},
    "ESTP": {"name": "차둘", "image": "https://dodo.ac/np/images/8/87/Dom_NH.png", "desc": "활동적이고 스포티한 양! 언제나 에너지가 넘치고 도전을 두려워하지 않아요. ⚽"},
    "ISTP": {"name": "철깍", "image": "https://dodo.ac/np/images/1/1b/Ribbot_NH.png", "desc": "손재주가 좋고 쿨한 성격의 로봇 개구리! 묵묵히 관심사에 집중해요. 🛠️"},
    "ISFP": {"name": "피터", "image": "https://dodo.ac/np/images/d/d4/Beau_NH.png", "desc": "평화롭고 느긋한 성격의 사슴! 자연을 사랑하는 예술가형이에요. 🦋"},
    "ESFJ": {"name": "미첼", "image": "https://dodo.ac/np/images/f/f6/Sasha_NH.png", "desc": "사교적이고 친절함이 뚝뚝 묻어나는 토끼! 챙겨주는 걸 좋아해요. 🎈"},
    "ESFP": {"name": "모니카", "image": "https://dodo.ac/np/images/1/1b/Audie_NH.png", "desc": "스타성 최고! 활발하고 긍정적인 아이돌 지망생 늑대! 🎤"}
}

# 결과를 화면에 예쁘게 출력해주는 함수 (코드 중복을 방지하기 위해 만듭니다)
def show_result(mbti_result):
    result_data = mbti_villagers[mbti_result]
    st.write("---")
    st.subheader(f"🎉 당신과 어울리는 주민은... **{result_data['name']}**! ({mbti_result})")
    
    # st.image를 사용하여 웹상의 이미지를 불러옵니다.
    st.image(result_data["image"], width=250)
    
    st.info(f"**{result_data['name']}**는(은) {result_data['desc']}")
    st.balloons()
    st.success("당곡고 친구들에게 내 검사 결과를 공유해 보세요! 🥰")

# --- 화면 구성 시작 ---
st.title("🏕️ 모여봐요 동물의 숲 주민 추천기 🍃")
st.write("나의 MBTI를 알아보거나 선택해서, 찰떡궁합인 주민을 찾아보세요! ✈️🏝️")

# st.tabs를 이용해 두 개의 탭(화면)을 만듭니다.
tab1, tab2 = st.tabs(["📝 간단 MBTI 검사", "🔍 MBTI 직접 선택"])

with tab1:
    st.markdown("### 🧐 나에게 어울리는 주민 찾기 테스트")
    
    # 4가지 질문 생성 (E/I, S/N, T/F, J/P)
    q1 = st.radio("1. 주말에 에너지를 충전하는 방법은?", ["(선택 안함)", "밖에서 친구들과 신나게 놀기 🏃‍♂️", "집에서 뒹굴거리며 혼자 쉬기 🛌"])
    q2 = st.radio("2. 문제를 해결할 때 나는?", ["(선택 안함)", "현실적이고 실용적인 방법을 찾는다 🔍", "창의적이고 새로운 아이디어를 떠올린다 💡"])
    q3 = st.radio("3. 친구가 고민을 털어놓을 때 나는?", ["(선택 안함)", "문제의 원인을 분석하고 해결책을 제시한다 🛠️", "친구의 감정에 먼저 공감하고 위로해준다 💖"])
    q4 = st.radio("4. 여행을 갈 때 나는?", ["(선택 안함)", "철저하게 일정을 계획하고 움직인다 📅", "발길이 닿는 대로 즉흥적인 여행을 즐긴다 🚶‍♂️"])

    if st.button("결과 보기! 🎁", key="test_btn"):
        # 모든 질문에 답했는지 확인
        if "(선택 안함)" in [q1, q2, q3, q4]:
            st.warning("앗! 모든 질문에 답을 골라주세요. 😅")
        else:
            # 사용자의 선택에 따라 MBTI 알파벳 조합하기
            mbti_str = ""
            mbti_str += "E" if "밖에서" in q1 else "I"
            mbti_str += "S" if "현실적이고" in q2 else "N"
            mbti_str += "T" if "원인을 분석하고" in q3 else "F"
            mbti_str += "J" if "철저하게" in q4 else "P"
            
            # 결과 출력 함수 호출
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
