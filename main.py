import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

# MBTI별 포켓몬 데이터 (각 MBTI마다 여러 마리!)
mbti_pokemon = {
    "INTJ": [
        {"pokemon": "뮤츠", "emoji": "🧬", "type": "에스퍼", "desc": "천재적인 두뇌와 강력한 정신력! 당신은 타고난 전략가예요.", "traits": "🧠 천재성 | 🎯 목표지향 | 🔮 직관력"},
        {"pokemon": "갸라도스", "emoji": "🐉", "type": "물/비행", "desc": "조용하지만 한번 폭발하면 무서운 카리스마! 깊이 있는 당신이에요.", "traits": "💪 카리스마 | 🌊 인내심 | ⚡ 폭발력"},
        {"pokemon": "메타그로스", "emoji": "🤖", "type": "강철/에스퍼", "desc": "슈퍼컴퓨터급 두뇌! 논리와 계산이 완벽한 당신과 닮았어요.", "traits": "💻 분석력 | 🔧 체계성 | 🎯 정확성"},
        {"pokemon": "다크라이", "emoji": "🌑", "type": "악", "desc": "신비롭고 고독한 매력! 깊은 사고를 즐기는 당신이에요.", "traits": "🌙 신비로움 | 🧠 통찰력 | 🎭 독립성"},
    ],
    "INTP": [
        {"pokemon": "폴리곤", "emoji": "🔷", "type": "노말", "desc": "데이터와 이론을 사랑하는 당신! 끝없는 탐구심을 가졌어요.", "traits": "💻 논리적 | 🔍 탐구심 | 📊 분석력"},
        {"pokemon": "알라카잠", "emoji": "🥄", "type": "에스퍼", "desc": "IQ 5000의 천재! 호기심 많고 지적인 당신과 똑 닮았어요.", "traits": "🧠 천재성 | 📚 지식욕 | 💡 통찰력"},
        {"pokemon": "로토무", "emoji": "💡", "type": "전기/고스트", "desc": "다양한 형태로 변신하는 호기심쟁이! 당신의 다재다능함과 닮았어요.", "traits": "🔌 호기심 | 🎨 다재다능 | 🌀 자유로움"},
        {"pokemon": "포리고2", "emoji": "🔶", "type": "노말", "desc": "업그레이드된 지능! 끊임없이 발전하는 당신이에요.", "traits": "📈 성장형 | 🔬 연구심 | 💫 진화"},
    ],
    "ENTJ": [
        {"pokemon": "리자몽", "emoji": "🔥", "type": "불꽃/비행", "desc": "정상을 향해 날아오르는 강력한 리더! 당신의 카리스마와 닮았어요.", "traits": "👑 리더십 | 🚀 야망 | 💪 추진력"},
        {"pokemon": "가이오가", "emoji": "🌊", "type": "물", "desc": "바다를 지배하는 전설! 압도적 존재감의 당신이에요.", "traits": "🌊 카리스마 | 👑 지배력 | ⚡ 영향력"},
        {"pokemon": "삼삼드래", "emoji": "🐲", "type": "악/드래곤", "desc": "세 개의 머리로 모든 걸 지휘! 강력한 통솔력의 소유자예요.", "traits": "🎯 통솔력 | 🔥 결단력 | 💼 야망"},
        {"pokemon": "솔가레오", "emoji": "☀️", "type": "에스퍼/강철", "desc": "태양처럼 빛나는 리더! 당당하고 위풍당당한 당신이에요.", "traits": "☀️ 카리스마 | 👑 위엄 | 🦁 용맹"},
    ],
    "ENTP": [
        {"pokemon": "겟핸보숭", "emoji": "🐵", "type": "노말", "desc": "끊임없는 아이디어와 장난기! 활발한 당신의 영혼이에요.", "traits": "💡 창의력 | 🎪 재치 | 🌈 호기심"},
        {"pokemon": "조로아크", "emoji": "🦊", "type": "악", "desc": "환영을 만드는 트릭스터! 기발한 발상의 천재예요.", "traits": "🎭 기발함 | 🎨 창의성 | 🃏 재치"},
        {"pokemon": "마릴리", "emoji": "🎈", "type": "전기/페어리", "desc": "통통 튀는 에너지! 어디로 튈지 모르는 매력의 소유자예요.", "traits": "⚡ 활발함 | 🎢 즉흥성 | ✨ 매력"},
        {"pokemon": "님피아", "emoji": "🎀", "type": "페어리", "desc": "리본으로 사로잡는 매력! 토론과 설득의 달인이에요.", "traits": "💬 설득력 | 🌸 매력 | 🎯 표현력"},
    ],
    "INFJ": [
        {"pokemon": "루카리오", "emoji": "🌀", "type": "격투/강철", "desc": "파동을 읽어내는 통찰력! 깊은 공감 능력의 당신이에요.", "traits": "✨ 통찰력 | 💙 공감능력 | 🛡️ 정의감"},
        {"pokemon": "가데보아르", "emoji": "💃", "type": "에스퍼/페어리", "desc": "미래를 보는 우아한 보호자! 헌신적인 당신과 닮았어요.", "traits": "🔮 직관력 | 💖 헌신 | 🌟 우아함"},
        {"pokemon": "샤로다", "emoji": "🐍", "type": "풀", "desc": "고귀하고 우아한 카리스마! 신비로운 분위기의 소유자예요.", "traits": "👑 고귀함 | 🌿 신비로움 | 💚 깊이"},
        {"pokemon": "크레세리아", "emoji": "🌙", "type": "에스퍼", "desc": "달빛처럼 부드럽게 치유하는 존재! 당신은 모두의 안식처예요.", "traits": "🌙 치유력 | 💫 평온함 | 🕊️ 보호"},
    ],
    "INFP": [
        {"pokemon": "이브이", "emoji": "🦊", "type": "노말", "desc": "무한한 가능성을 품은 순수한 영혼! 당신의 다채로움과 닮았어요.", "traits": "💖 순수함 | 🌸 감수성 | 🎨 상상력"},
        {"pokemon": "님피아", "emoji": "🎀", "type": "페어리", "desc": "사랑의 에너지로 가득! 따뜻한 마음의 소유자예요.", "traits": "💕 사랑 | 🌷 다정함 | ✨ 순수"},
        {"pokemon": "뮤", "emoji": "🌟", "type": "에스퍼", "desc": "모든 포켓몬의 조상! 신비롭고 순수한 당신의 영혼이에요.", "traits": "🌈 신비로움 | 💫 순수함 | 🎨 창의력"},
        {"pokemon": "라프라스", "emoji": "🌊", "type": "물/얼음", "desc": "온화하고 사람을 좋아하는 마음! 다정한 당신이에요.", "traits": "💙 온화함 | 🎵 감성 | 🛟 다정함"},
    ],
    "ENFJ": [
        {"pokemon": "픽시", "emoji": "🧚", "type": "페어리", "desc": "달빛 아래 모두를 이끄는 매력! 사랑받는 리더예요.", "traits": "🌟 카리스마 | 💝 따뜻함 | 🤝 친화력"},
        {"pokemon": "행복', '해피너스", "emoji": "🥚", "type": "노말", "desc": "행복을 나누는 천사! 모두에게 사랑을 베푸는 당신이에요.", "traits": "💕 헌신 | 🌸 친절 | 🎊 사교성"},
        {"pokemon": "블래키", "emoji": "🌑", "type": "악", "desc": "신뢰로 진화하는 충성스러운 친구! 깊은 인연을 소중히 해요.", "traits": "🤝 충성심 | 💖 신뢰 | 🌙 헌신"},
        {"pokemon": "토게키스", "emoji": "🕊️", "type": "페어리/비행", "desc": "평화와 행복의 사도! 모두를 화합시키는 능력자예요.", "traits": "🕊️ 평화 | ✨ 화합 | 💝 자애"},
    ],
    "ENFP": [
        {"pokemon": "피카츄", "emoji": "⚡", "type": "전기", "desc": "에너지 넘치는 사랑둥이! 당신의 밝은 매력과 똑 닮았어요.", "traits": "✨ 활발함 | 😄 긍정성 | 🎉 사교성"},
        {"pokemon": "이브이", "emoji": "🦊", "type": "노말", "desc": "가능성이 무한한 자유로운 영혼! 당신과 닮았어요.", "traits": "🌈 다재다능 | 💖 사랑스러움 | 🎨 가능성"},
        {"pokemon": "또가스", "emoji": "💨", "type": "독", "desc": "어디로 튈지 모르는 자유로움! 통통 튀는 매력이에요.", "traits": "🎈 자유로움 | 🎪 유쾌함 | 🌟 매력"},
        {"pokemon": "마릴", "emoji": "💧", "type": "물/페어리", "desc": "발랄하고 사랑스러운 매력! 누구나 좋아하는 당신이에요.", "traits": "💧 발랄함 | 💕 사랑스러움 | 🎵 즐거움"},
    ],
    "ISTJ": [
        {"pokemon": "거북왕", "emoji": "🐢", "type": "물", "desc": "묵직하고 든든한 책임감! 신뢰의 상징인 당신이에요.", "traits": "🛡️ 책임감 | 📚 성실함 | ⚖️ 원칙주의"},
        {"pokemon": "메타그로스", "emoji": "🤖", "type": "강철/에스퍼", "desc": "정확하고 체계적인 두뇌! 완벽주의자 당신이에요.", "traits": "📐 체계성 | 🎯 정확함 | 💼 신뢰성"},
        {"pokemon": "강철톤", "emoji": "🚂", "type": "강철/땅", "desc": "단단하고 흔들리지 않는 의지! 든든한 기둥 같아요.", "traits": "⚙️ 견고함 | 🏔️ 안정성 | 🛡️ 강인함"},
        {"pokemon": "딱구리", "emoji": "🗿", "type": "바위/땅", "desc": "변함없이 한결같은 모습! 우직한 매력의 소유자예요.", "traits": "🪨 우직함 | 📋 원칙 | 💪 끈기"},
    ],
    "ISFJ": [
        {"pokemon": "이상해씨", "emoji": "🌱", "type": "풀/독", "desc": "친구를 지키는 따뜻한 보호자! 헌신적인 당신이에요.", "traits": "🌿 헌신 | 🤗 다정함 | 🏡 안정감"},
        {"pokemon": "럭키", "emoji": "🥚", "type": "노말", "desc": "행운과 치유의 천사! 모두를 보살피는 당신이에요.", "traits": "💕 보살핌 | 🌸 친절 | ✨ 행운"},
        {"pokemon": "이브이", "emoji": "🦊", "type": "노말", "desc": "곁에 있는 것만으로 위로가 되는 존재! 따뜻한 당신이에요.", "traits": "🤗 위로 | 💖 충성 | 🏠 안정"},
        {"pokemon": "치코리타", "emoji": "🌿", "type": "풀", "desc": "은은한 향기로 치유하는 존재! 부드러운 매력이에요.", "traits": "🌱 치유 | 💚 다정함 | 🌸 부드러움"},
    ],
    "ESTJ": [
        {"pokemon": "딱구리", "emoji": "🗿", "type": "바위/땅", "desc": "강하고 단단한 추진력! 체계적인 리더예요.", "traits": "📋 체계적 | 💼 실용적 | 🏆 성취욕"},
        {"pokemon": "괴력몬", "emoji": "💪", "type": "격투", "desc": "강력한 힘과 추진력! 행동으로 보여주는 당신이에요.", "traits": "💪 추진력 | 🏋️ 강인함 | 🎯 실행력"},
        {"pokemon": "한카리아스", "emoji": "🦈", "type": "드래곤/땅", "desc": "강력한 카리스마와 결단력! 압도적인 리더예요.", "traits": "👑 카리스마 | ⚡ 결단력 | 🏆 성취"},
        {"pokemon": "코뿌리", "emoji": "🦏", "type": "땅/바위", "desc": "한번 정한 길은 끝까지 돌진! 추진력 만렙이에요.", "traits": "🏃 추진력 | 🛡️ 강인함 | 🎯 의지"},
    ],
    "ESFJ": [
        {"pokemon": "해피너스", "emoji": "🥚", "type": "노말", "desc": "행복을 나누는 사랑의 화신! 따뜻한 당신이에요.", "traits": "💕 배려심 | 🌸 친절함 | 🎊 사교성"},
        {"pokemon": "푸쿠린", "emoji": "🎀", "type": "노말/페어리", "desc": "포근하고 다정한 매력! 모두에게 사랑받아요.", "traits": "🤗 포근함 | 💝 다정함 | 🌷 사교성"},
        {"pokemon": "이브이", "emoji": "🦊", "type": "노말", "desc": "어디서나 사랑받는 매력덩어리! 당신과 닮았어요.", "traits": "💖 사랑스러움 | 🤝 친화력 | ✨ 매력"},
        {"pokemon": "치라치노", "emoji": "🐭", "type": "노말", "desc": "깔끔하고 우아한 매력! 모두를 챙기는 당신이에요.", "traits": "🌸 우아함 | 💕 배려 | ✨ 깔끔함"},
    ],
    "ISTP": [
        {"pokemon": "갸라도스", "emoji": "🐉", "type": "물/비행", "desc": "조용하지만 폭발적인 매력! 쿨한 당신이에요.", "traits": "🔧 손재주 | 🌊 침착함 | ⚡ 폭발력"},
        {"pokemon": "루카리오", "emoji": "🥋", "type": "격투/강철", "desc": "냉정하고 정확한 판단력! 실력으로 보여주는 당신이에요.", "traits": "🎯 정확함 | 💪 실력 | 🧊 냉정함"},
        {"pokemon": "팬텀", "emoji": "👻", "type": "고스트/독", "desc": "신비롭고 쿨한 매력! 종잡을 수 없는 당신이에요.", "traits": "🌙 신비로움 | 🃏 자유로움 | 🎭 독립성"},
        {"pokemon": "포푸니라", "emoji": "🗡️", "type": "악/강철", "desc": "날카로운 분석과 실행력! 쿨한 실력자예요.", "traits": "⚔️ 예리함 | 🎯 실행력 | 🧊 독립성"},
    ],
    "ISFP": [
        {"pokemon": "이상해꽃", "emoji": "🌺", "type": "풀/독", "desc": "아름다운 꽃을 피우는 평화로운 영혼! 감성적인 당신이에요.", "traits": "🎨 예술성 | 🕊️ 평화로움 | 🌷 감성적"},
        {"pokemon": "뮤", "emoji": "🌸", "type": "에스퍼", "desc": "신비롭고 순수한 자유로운 영혼! 당신과 닮았어요.", "traits": "🌈 신비로움 | ✨ 자유로움 | 💖 순수"},
        {"pokemon": "샤미드", "emoji": "💧", "type": "물", "desc": "달빛 아래 우아한 매력! 감성적이고 평온한 당신이에요.", "traits": "🌊 우아함 | 🌙 감성 | 💙 평온"},
        {"pokemon": "리피아", "emoji": "🌿", "type": "풀", "desc": "자연과 함께 호흡하는 평화로움! 순수한 영혼이에요.", "traits": "🌱 자연친화 | 🕊️ 평화 | 🎨 감성"},
    ],
    "ESTP": [
        {"pokemon": "팬텀", "emoji": "👻", "type": "고스트/독", "desc": "장난기 가득한 스릴 메이커! 행동력 넘치는 당신이에요.", "traits": "🎢 모험심 | 🃏 장난기 | 🏃 행동력"},
        {"pokemon": "괴력몬", "emoji": "💪", "type": "격투", "desc": "지금 당장 부딪치는 행동파! 에너지 넘치는 당신이에요.", "traits": "⚡ 행동력 | 🏋️ 도전 | 🔥 열정"},
        {"pokemon": "메가자드", "emoji": "🔥", "type": "불꽃", "desc": "화끈하고 멋진 매력! 시선을 사로잡는 당신이에요.", "traits": "🔥 카리스마 | ⚡ 스릴 | 💫 매력"},
        {"pokemon": "한카리아스", "emoji": "🦈", "type": "드래곤/땅", "desc": "거침없는 추진력과 도전 정신! 스릴을 즐기는 당신이에요.", "traits": "🏃 추진력 | ⚡ 모험 | 🎯 도전"},
    ],
    "ESFP": [
        {"pokemon": "푸린", "emoji": "🎤", "type": "노말/페어리", "desc": "노래로 모두를 매료시키는 엔터테이너! 사랑스러운 당신이에요.", "traits": "🎵 매력적 | 🎭 표현력 | 🌈 자유로움"},
        {"pokemon": "피카츄", "emoji": "⚡", "type": "전기", "desc": "어디서나 빛나는 스타! 모두의 사랑을 받는 당신이에요.", "traits": "✨ 인기 | 😄 발랄함 | 🎉 즐거움"},
        {"pokemon": "마임맨", "emoji": "🎭", "type": "에스퍼/페어리", "desc": "퍼포먼스의 달인! 시선 강탈 매력의 소유자예요.", "traits": "🎨 표현력 | 🎪 끼 | 💫 매력"},
        {"pokemon": "님피아", "emoji": "🎀", "type": "페어리", "desc": "사랑스러운 매력으로 분위기 메이커! 당신과 닮았어요.", "traits": "💕 사랑스러움 | 🌸 매력 | ✨ 화려함"},
    ]
}

# 타이틀
st.markdown("<h1 style='text-align: center;'>⚡ MBTI 포켓몬 추천기 🎮</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>당신의 MBTI에 어울리는 포켓몬은? 🔍✨</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>버튼을 누를 때마다 다른 포켓몬이 나와요! 🎲</p>", unsafe_allow_html=True)
st.markdown("---")

# MBTI 선택
st.markdown("### 🎯 당신의 MBTI를 선택해주세요!")

col1, col2 = st.columns(2)
with col1:
    ei = st.radio("🗣️ 에너지 방향", ["E (외향) 🎉", "I (내향) 🌙"])
    sn = st.radio("👀 인식 기능", ["S (감각) 🔍", "N (직관) 💫"])
with col2:
    tf = st.radio("🧠 판단 기능", ["T (사고) 🧊", "F (감정) 💖"])
    jp = st.radio("📅 생활 양식", ["J (판단) 📋", "P (인식) 🎲"])

mbti = ei[0] + sn[0] + tf[0] + jp[0]

st.markdown("---")

# 결과 보기 버튼
if st.button("🔮 나의 포켓몬 친구 만나기! 🎊", use_container_width=True):
    pokemon_list = mbti_pokemon[mbti]
    result = random.choice(pokemon_list)  # 랜덤 선택! 🎲
    
    st.balloons()
    
    st.markdown(f"<h2 style='text-align: center;'>✨ 당신의 MBTI는 <span style='color:#FF6B6B;'>{mbti}</span> ✨</h2>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #FFE5E5 0%, #FFD6E8 100%); 
                padding: 30px; border-radius: 20px; text-align: center; margin: 20px 0;'>
        <h1 style='font-size: 80px; margin: 0;'>{result['emoji']}</h1>
        <h2 style='color: #FF4757; margin: 10px 0;'>🎉 {result['pokemon']} 🎉</h2>
        <p style='font-size: 18px; color: #555;'>📌 타입: {result['type']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💌 당신에게 보내는 메시지")
    st.info(f"💬 {result['desc']}")
    
    st.markdown("### 🌟 당신의 매력 포인트")
    st.success(result['traits'])
    
    # 다른 추천 미리보기
    st.markdown("---")
    st.markdown("### 🎁 이 MBTI에 어울리는 다른 포켓몬들")
    other_pokemons = [p for p in pokemon_list if p['pokemon'] != result['pokemon']]
    cols = st.columns(len(other_pokemons))
    for i, p in enumerate(other_pokemons):
        with cols[i]:
            st.markdown(f"<div style='text-align:center;'><h2>{p['emoji']}</h2><p><b>{p['pokemon']}</b></p></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>🎲 다시 눌러서 또 다른 포켓몬을 만나보세요! 🎮</p>", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.markdown("## 📖 사용 방법")
    st.markdown("""
    1. 🎯 MBTI 4가지 항목 선택  
    2. 🔮 버튼 클릭!  
    3. 🎲 랜덤 포켓몬 등장!  
    4. 🔄 또 누르면 다른 포켓몬!
    """)
    st.markdown("---")
    st.markdown("### 💡 MBTI란?")
    st.markdown("성격 유형을 16가지로 분류하는 검사예요! 🧩")
    st.markdown("---")
    st.markdown("### 🎮 포켓몬 통계")
    total = sum(len(v) for v in mbti_pokemon.values())
    st.metric("총 포켓몬 수", f"{total}마리 🌟")
    st.metric("MBTI 유형", "16가지 🎨")
    st.markdown("---")
    st.markdown("Made with 💖 by 당곡고")
