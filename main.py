import streamlit as st
import random
import requests

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 월드",
    page_icon="⚡",
    layout="wide"
)

# ==================== MBTI별 포켓몬 데이터 ====================
mbti_pokemon = {
    "INTJ": [
        {"id": 150, "name_kr": "뮤츠", "type": "에스퍼",
         "desc": "천재적인 두뇌와 강력한 정신력! 당신은 타고난 전략가예요.",
         "detail": "뮤츠는 유전자 조작으로 탄생한 전설의 포켓몬이에요. 차갑고 이성적인 성격이 INTJ의 전략적 사고와 닮았답니다.",
         "traits": "🧠 천재성 | 🎯 목표지향 | 🔮 직관력"},
        {"id": 376, "name_kr": "메타그로스", "type": "강철/에스퍼",
         "desc": "슈퍼컴퓨터급 두뇌! 논리와 계산이 완벽한 당신이에요.",
         "detail": "4개의 뇌가 연결되어 슈퍼컴퓨터를 능가하는 연산 능력을 가졌어요.",
         "traits": "💻 분석력 | 🔧 체계성 | 🎯 정확성"},
        {"id": 491, "name_kr": "다크라이", "type": "악",
         "desc": "신비롭고 고독한 매력! 깊은 사고를 즐기는 당신이에요.",
         "detail": "악몽을 다루는 신비로운 포켓몬이에요. 혼자만의 시간을 즐기는 INTJ와 비슷해요.",
         "traits": "🌙 신비로움 | 🧠 통찰력 | 🎭 독립성"},
        {"id": 248, "name_kr": "마기라스", "type": "바위/악",
         "desc": "압도적인 카리스마와 강력한 힘! 위엄있는 리더예요.",
         "detail": "산을 무너뜨릴 만큼 강력한 포켓몬이에요. 침착하지만 강한 INTJ와 닮았어요.",
         "traits": "👑 위엄 | 💪 강인함 | 🎯 결단력"},
        {"id": 384, "name_kr": "레쿠쟈", "type": "드래곤/비행",
         "desc": "하늘을 지배하는 고독한 전설! 압도적 존재감의 당신이에요.",
         "detail": "오존층에 사는 전설의 포켓몬으로 고독을 즐기며 천공을 누벼요.",
         "traits": "🌌 독립성 | 👑 카리스마 | 🔮 신비"},
        {"id": 94, "name_kr": "팬텀", "type": "고스트/독",
         "desc": "그림자처럼 조용하지만 강력한 존재감! 신비로운 매력이에요.",
         "detail": "어둠 속에서 조용히 상대를 관찰하는 포켓몬이에요. 전략적인 INTJ와 닮았어요.",
         "traits": "🎭 신비 | 🧠 전략 | 🌙 관찰력"},
    ],
    "INTP": [
        {"id": 137, "name_kr": "폴리곤", "type": "노말",
         "desc": "데이터와 이론을 사랑하는 당신! 끝없는 탐구심을 가졌어요.",
         "detail": "세계 최초로 인공적으로 만들어진 포켓몬이에요. 사이버 공간을 누비는 모습이 INTP와 닮았어요.",
         "traits": "💻 논리적 | 🔍 탐구심 | 📊 분석력"},
        {"id": 65, "name_kr": "후딘", "type": "에스퍼",
         "desc": "IQ 5000의 천재! 호기심 많고 지적인 당신이에요.",
         "detail": "IQ가 5000이 넘는 포켓몬으로, 모든 일을 기억할 수 있어요.",
         "traits": "🧠 천재성 | 📚 지식욕 | 💡 통찰력"},
        {"id": 479, "name_kr": "로토무", "type": "전기/고스트",
         "desc": "다양한 형태로 변신하는 호기심쟁이! 당신의 다재다능함과 닮았어요.",
         "detail": "가전제품에 들어가 다양한 형태로 변신해요. 호기심 많은 INTP와 닮았어요!",
         "traits": "🔌 호기심 | 🎨 다재다능 | 🌀 자유로움"},
        {"id": 233, "name_kr": "폴리곤2", "type": "노말",
         "desc": "업그레이드된 지능! 끊임없이 발전하는 당신이에요.",
         "detail": "인공지능이 탑재되어 스스로 학습하고 진화해요.",
         "traits": "📈 성장형 | 🔬 연구심 | 💫 진화"},
        {"id": 386, "name_kr": "테오키스", "type": "에스퍼",
         "desc": "외계에서 온 천재! 독창적 사고를 즐기는 당신이에요.",
         "detail": "우주에서 온 DNA가 변이한 포켓몬이에요.",
         "traits": "🌌 독창성 | 🧠 천재 | 🔬 변화"},
        {"id": 196, "name_kr": "에브이", "type": "에스퍼",
         "desc": "지적이고 우아한 매력! 사색을 즐기는 당신이에요.",
         "detail": "햇빛처럼 밝은 에너지로 사고를 확장시키는 포켓몬이에요.",
         "traits": "✨ 지성 | 🌟 우아함 | 🧠 사색"},
    ],
    "ENTJ": [
        {"id": 6, "name_kr": "리자몽", "type": "불꽃/비행",
         "desc": "정상을 향해 날아오르는 강력한 리더! 당신의 카리스마와 닮았어요.",
         "detail": "불꽃을 뿜으며 하늘을 지배하는 포켓몬이에요.",
         "traits": "👑 리더십 | 🚀 야망 | 💪 추진력"},
        {"id": 382, "name_kr": "가이오가", "type": "물",
         "desc": "바다를 지배하는 전설! 압도적 존재감의 당신이에요.",
         "detail": "바다를 만들었다는 전설의 포켓몬이에요.",
         "traits": "🌊 카리스마 | 👑 지배력 | ⚡ 영향력"},
        {"id": 635, "name_kr": "삼삼드래", "type": "악/드래곤",
         "desc": "세 개의 머리로 모든 걸 지휘! 강력한 통솔력의 소유자예요.",
         "detail": "3개의 머리로 다양한 방향을 지휘해요.",
         "traits": "🎯 통솔력 | 🔥 결단력 | 💼 야망"},
        {"id": 791, "name_kr": "솔가레오", "type": "에스퍼/강철",
         "desc": "태양처럼 빛나는 리더! 당당하고 위풍당당한 당신이에요.",
         "detail": "태양을 삼키는 자라 불리는 전설의 포켓몬이에요.",
         "traits": "☀️ 카리스마 | 👑 위엄 | 🦁 용맹"},
        {"id": 445, "name_kr": "한카리아스", "type": "드래곤/땅",
         "desc": "거침없는 추진력과 결단력! 압도적인 리더예요.",
         "detail": "마하의 속도로 적을 제압하는 강력한 포켓몬이에요.",
         "traits": "⚡ 추진력 | 🎯 결단력 | 🏆 성취"},
        {"id": 644, "name_kr": "삼삼드래", "type": "전기/드래곤",
         "desc": "강력한 전류와 카리스마! 모두를 이끄는 리더예요.",
         "detail": "강력한 전류를 다루며 하늘을 지배하는 포켓몬이에요.",
         "traits": "⚡ 강력함 | 👑 리더십 | 🔥 카리스마"},
    ],
    "ENTP": [
        {"id": 424, "name_kr": "겟핸보숭", "type": "노말",
         "desc": "끊임없는 아이디어와 장난기! 활발한 당신의 영혼이에요.",
         "detail": "두 개의 꼬리로 다양한 트릭을 부려요.",
         "traits": "💡 창의력 | 🎪 재치 | 🌈 호기심"},
        {"id": 571, "name_kr": "조로아크", "type": "악",
         "desc": "환영을 만드는 트릭스터! 기발한 발상의 천재예요.",
         "detail": "환영을 만들어 상대를 속이는 영리한 포켓몬이에요.",
         "traits": "🎭 기발함 | 🎨 창의성 | 🃏 재치"},
        {"id": 196, "name_kr": "에브이", "type": "에스퍼",
         "desc": "빛나는 아이디어로 세상을 비추는 당신! 영감의 원천이에요.",
         "detail": "햇빛 같은 긍정 에너지로 주변을 밝게 해요.",
         "traits": "💡 영감 | 🌟 긍정 | 🎨 창의"},
        {"id": 700, "name_kr": "님피아", "type": "페어리",
         "desc": "리본으로 사로잡는 매력! 토론과 설득의 달인이에요.",
         "detail": "리본 같은 더듬이로 상대의 감정을 읽어요.",
         "traits": "💬 설득력 | 🌸 매력 | 🎯 표현력"},
        {"id": 65, "name_kr": "후딘", "type": "에스퍼",
         "desc": "천재적인 두뇌로 모든 걸 해결! 토론의 챔피언이에요.",
         "detail": "천재적인 두뇌로 새로운 가능성을 탐구해요.",
         "traits": "🧠 천재성 | 💡 발상 | 🎯 논리"},
        {"id": 405, "name_kr": "렌트라", "type": "전기",
         "desc": "번뜩이는 통찰력! 새로운 길을 개척하는 당신이에요.",
         "detail": "전기로 모든 것을 꿰뚫어볼 수 있어요.",
         "traits": "⚡ 통찰력 | 🔍 분석 | 🚀 도전"},
    ],
    "INFJ": [
        {"id": 448, "name_kr": "루카리오", "type": "격투/강철",
         "desc": "파동을 읽어내는 통찰력! 깊은 공감 능력의 당신이에요.",
         "detail": "'파동'을 읽어 상대의 감정과 미래까지 감지하는 포켓몬이에요.",
         "traits": "✨ 통찰력 | 💙 공감능력 | 🛡️ 정의감"},
        {"id": 282, "name_kr": "가디안", "type": "에스퍼/페어리",
         "desc": "미래를 보는 우아한 보호자! 헌신적인 당신이에요.",
         "detail": "트레이너를 위해 미래를 예측하고 헌신하는 포켓몬이에요.",
         "traits": "🔮 직관력 | 💖 헌신 | 🌟 우아함"},
        {"id": 497, "name_kr": "샤로다", "type": "풀",
         "desc": "고귀하고 우아한 카리스마! 신비로운 분위기의 소유자예요.",
         "detail": "귀족적인 분위기와 강한 자존심을 가진 포켓몬이에요.",
         "traits": "👑 고귀함 | 🌿 신비로움 | 💚 깊이"},
        {"id": 488, "name_kr": "크레세리아", "type": "에스퍼",
         "desc": "달빛처럼 부드럽게 치유하는 존재! 당신은 모두의 안식처예요.",
         "detail": "좋은 꿈을 선사하는 달의 화신이에요.",
         "traits": "🌙 치유력 | 💫 평온함 | 🕊️ 보호"},
        {"id": 251, "name_kr": "세레비", "type": "에스퍼/풀",
         "desc": "시간을 넘나드는 신비로운 영혼! 깊은 통찰력의 소유자예요.",
         "detail": "시간을 여행하며 숲을 지키는 신비로운 포켓몬이에요.",
         "traits": "🌿 신비 | ✨ 통찰력 | 💚 보호"},
        {"id": 481, "name_kr": "엠라이트", "type": "에스퍼",
         "desc": "감정의 화신! 깊이 공감하고 이해하는 당신이에요.",
         "detail": "'감정의 화신'으로 불리며 사람들의 마음을 이해해요.",
         "traits": "💖 공감 | 🌙 감성 | ✨ 이해"},
    ],
    "INFP": [
        {"id": 133, "name_kr": "이브이", "type": "노말",
         "desc": "무한한 가능성을 품은 순수한 영혼! 당신의 다채로움과 닮았어요.",
         "detail": "8가지 형태로 진화할 수 있는 무한한 가능성의 포켓몬이에요.",
         "traits": "💖 순수함 | 🌸 감수성 | 🎨 상상력"},
        {"id": 700, "name_kr": "님피아", "type": "페어리",
         "desc": "사랑의 에너지로 가득! 따뜻한 마음의 소유자예요.",
         "detail": "사랑의 감정을 에너지로 바꾸는 포켓몬이에요.",
         "traits": "💕 사랑 | 🌷 다정함 | ✨ 순수"},
        {"id": 151, "name_kr": "뮤", "type": "에스퍼",
         "desc": "모든 포켓몬의 조상! 신비롭고 순수한 당신의 영혼이에요.",
         "detail": "모든 포켓몬의 시조라고 알려진 신비한 포켓몬이에요.",
         "traits": "🌈 신비로움 | 💫 순수함 | 🎨 창의력"},
        {"id": 131, "name_kr": "라프라스", "type": "물/얼음",
         "desc": "온화하고 사람을 좋아하는 마음! 다정한 당신이에요.",
         "detail": "멸종 위기에 처한 온화한 포켓몬이에요.",
         "traits": "💙 온화함 | 🎵 감성 | 🛟 다정함"},
        {"id": 35, "name_kr": "삐삐", "type": "페어리",
         "desc": "달빛 아래 춤추는 순수한 영혼! 사랑스러운 당신이에요.",
         "detail": "보름달 밤에 함께 모여 춤추는 포켓몬이에요.",
         "traits": "🌟 순수 | 💫 감성 | 💕 사랑"},
        {"id": 173, "name_kr": "삐", "type": "페어리",
         "desc": "별처럼 빛나는 순수함! 꿈을 사랑하는 당신이에요.",
         "detail": "별빛을 받고 태어난 사랑스러운 포켓몬이에요.",
         "traits": "⭐ 꿈 | 💖 순수 | 🌙 사랑"},
    ],
    "ENFJ": [
        {"id": 36, "name_kr": "픽시", "type": "페어리",
         "desc": "달빛 아래 모두를 이끄는 매력! 사랑받는 리더예요.",
         "detail": "신비로운 매력으로 사람들을 끌어모으는 포켓몬이에요.",
         "traits": "🌟 카리스마 | 💝 따뜻함 | 🤝 친화력"},
        {"id": 242, "name_kr": "해피너스", "type": "노말",
         "desc": "행복을 나누는 천사! 모두에게 사랑을 베푸는 당신이에요.",
         "detail": "행복한 사람을 발견하면 그 행복을 나눠주는 포켓몬이에요.",
         "traits": "💕 헌신 | 🌸 친절 | 🎊 사교성"},
        {"id": 197, "name_kr": "블래키", "type": "악",
         "desc": "신뢰로 진화하는 충성스러운 친구! 깊은 인연을 소중히 해요.",
         "detail": "트레이너와의 강한 유대로 진화하는 포켓몬이에요.",
         "traits": "🤝 충성심 | 💖 신뢰 | 🌙 헌신"},
        {"id": 468, "name_kr": "토게키스", "type": "페어리/비행",
         "desc": "평화와 행복의 사도! 모두를 화합시키는 능력자예요.",
         "detail": "평화로운 세상에만 나타나는 행복의 포켓몬이에요.",
         "traits": "🕊️ 평화 | ✨ 화합 | 💝 자애"},
        {"id": 282, "name_kr": "가디안", "type": "에스퍼/페어리",
         "desc": "주변을 보호하는 따뜻한 수호자! 헌신적인 리더예요.",
         "detail": "트레이너를 위해 자신을 희생할 만큼 헌신적이에요.",
         "traits": "🛡️ 보호 | 💖 헌신 | 👑 리더십"},
        {"id": 350, "name_kr": "밀로틱", "type": "물",
         "desc": "아름다움으로 분쟁을 진정시키는 화합의 화신!",
         "detail": "그 아름다움으로 싸움을 멈추게 한다는 전설의 포켓몬이에요.",
         "traits": "💎 아름다움 | 🌊 화합 | ✨ 우아함"},
    ],
    "ENFP": [
        {"id": 25, "name_kr": "피카츄", "type": "전기",
         "desc": "에너지 넘치는 사랑둥이! 당신의 밝은 매력과 똑 닮았어요.",
         "detail": "활발하고 호기심 많은 인기 만점 포켓몬이에요.",
         "traits": "✨ 활발함 | 😄 긍정성 | 🎉 사교성"},
        {"id": 133, "name_kr": "이브이", "type": "노말",
         "desc": "가능성이 무한한 자유로운 영혼! 당신과 닮았어요.",
         "detail": "다양한 형태로 진화할 수 있는 가능성의 포켓몬이에요.",
         "traits": "🌈 다재다능 | 💖 사랑스러움 | 🎨 가능성"},
        {"id": 183, "name_kr": "마릴", "type": "물/페어리",
         "desc": "발랄하고 사랑스러운 매력! 누구나 좋아하는 당신이에요.",
         "detail": "통통 튀는 꼬리로 사람들을 즐겁게 해주는 포켓몬이에요.",
         "traits": "💧 발랄함 | 💕 사랑스러움 | 🎵 즐거움"},
        {"id": 39, "name_kr": "푸린", "type": "노말/페어리",
         "desc": "노래로 모두를 매료시키는 매력! 분위기 메이커예요.",
         "detail": "노래로 사람들을 잠들게 하는 매력의 포켓몬이에요.",
         "traits": "🎵 매력 | 🎭 끼 | ✨ 사랑스러움"},
        {"id": 700, "name_kr": "님피아", "type": "페어리",
         "desc": "사랑의 매력으로 세상을 밝히는 당신이에요!",
         "detail": "사랑의 감정을 에너지로 만드는 포켓몬이에요.",
         "traits": "💖 사랑 | 🌸 매력 | ✨ 긍정"},
        {"id": 778, "name_kr": "따라먹쥐", "type": "고스트/페어리",
         "desc": "예측 불가한 매력! 자유분방한 당신이에요.",
         "detail": "변신을 좋아하는 자유로운 포켓몬이에요.",
         "traits": "🎭 자유 | 🎪 유쾌함 | 🌟 매력"},
    ],
    "ISTJ": [
        {"id": 9, "name_kr": "거북왕", "type": "물",
         "desc": "묵직하고 든든한 책임감! 신뢰의 상징인 당신이에요.",
         "detail": "단단한 등껍질로 동료를 지키는 포켓몬이에요.",
         "traits": "🛡️ 책임감 | 📚 성실함 | ⚖️ 원칙주의"},
        {"id": 376, "name_kr": "메타그로스", "type": "강철/에스퍼",
         "desc": "정확하고 체계적인 두뇌! 완벽주의자 당신이에요.",
         "detail": "4개의 뇌로 슈퍼컴퓨터급 연산을 해요.",
         "traits": "📐 체계성 | 🎯 정확함 | 💼 신뢰성"},
        {"id": 208, "name_kr": "강철톤", "type": "강철/땅",
         "desc": "단단하고 흔들리지 않는 의지! 든든한 기둥 같아요.",
         "detail": "다이아몬드보다 단단한 몸을 가진 포켓몬이에요.",
         "traits": "⚙️ 견고함 | 🏔️ 안정성 | 🛡️ 강인함"},
        {"id": 95, "name_kr": "롱스톤", "type": "바위/땅",
         "desc": "변함없이 한결같은 모습! 우직한 매력의 소유자예요.",
         "detail": "바위로 이루어진 거대한 포켓몬이에요.",
         "traits": "🪨 우직함 | 📋 원칙 | 💪 끈기"},
        {"id": 365, "name_kr": "씨카이저", "type": "얼음/물",
         "desc": "차분하고 든든한 리더! 책임감 만렙이에요.",
         "detail": "무리를 이끄는 든든한 리더 포켓몬이에요.",
         "traits": "🛡️ 책임감 | ❄️ 차분함 | 👑 리더십"},
        {"id": 530, "name_kr": "몰드류", "type": "땅/강철",
         "desc": "묵묵히 자기 일을 해내는 성실함! 진정한 프로페셔널이에요.",
         "detail": "단단한 발톱으로 땅을 파내는 성실한 포켓몬이에요.",
         "traits": "⛏️ 성실 | 💼 프로 | 🎯 집중"},
    ],
    "ISFJ": [
        {"id": 1, "name_kr": "이상해씨", "type": "풀/독",
         "desc": "친구를 지키는 따뜻한 보호자! 헌신적인 당신이에요.",
         "detail": "등의 씨앗으로 영양을 모으는 포켓몬이에요.",
         "traits": "🌿 헌신 | 🤗 다정함 | 🏡 안정감"},
        {"id": 113, "name_kr": "럭키", "type": "노말",
         "desc": "행운과 치유의 천사! 모두를 보살피는 당신이에요.",
         "detail": "다친 사람들에게 알을 나눠주는 자상한 포켓몬이에요.",
         "traits": "💕 보살핌 | 🌸 친절 | ✨ 행운"},
        {"id": 39, "name_kr": "푸린", "type": "노말/페어리",
         "desc": "포근하고 다정한 매력! 모두에게 사랑받아요.",
         "detail": "노래로 사람들을 편안하게 해주는 포켓몬이에요.",
         "traits": "🎀 포근함 | 💝 다정함 | 🌷 사교성"},
        {"id": 152, "name_kr": "치코리타", "type": "풀",
         "desc": "은은한 향기로 치유하는 존재! 부드러운 매력이에요.",
         "detail": "머리 잎사귀에서 달콤한 향기를 내뿜는 포켓몬이에요.",
         "traits": "🌱 치유 | 💚 다정함 | 🌸 부드러움"},
        {"id": 241, "name_kr": "밀탱크", "type": "노말",
         "desc": "맛있는 우유로 모두를 돌보는 어머니 같은 존재예요!",
         "detail": "영양가 높은 우유로 아픈 사람들을 회복시켜요.",
         "traits": "🥛 돌봄 | 💕 헌신 | 🌸 자상함"},
        {"id": 184, "name_kr": "마릴리", "type": "물/페어리",
         "desc": "친구를 끝까지 챙기는 따뜻한 마음의 소유자예요!",
         "detail": "새끼들을 정성껏 돌보는 자상한 포켓몬이에요.",
         "traits": "💧 자상함 | 💖 보살핌 | 🌷 따뜻함"},
    ],
    "ESTJ": [
        {"id": 248, "name_kr": "마기라스", "type": "바위/악",
         "desc": "강하고 단단한 추진력! 체계적인 리더예요.",
         "detail": "산을 무너뜨릴 만큼 강력한 포켓몬이에요.",
         "traits": "📋 체계적 | 💼 실용적 | 🏆 성취욕"},
        {"id": 68, "name_kr": "괴력몬", "type": "격투",
         "desc": "강력한 힘과 추진력! 행동으로 보여주는 당신이에요.",
         "detail": "4개의 팔로 강력한 힘을 발휘하는 포켓몬이에요.",
         "traits": "💪 추진력 | 🏋️ 강인함 | 🎯 실행력"},
        {"id": 445, "name_kr": "한카리아스", "type": "드래곤/땅",
         "desc": "강력한 카리스마와 결단력! 압도적인 리더예요.",
         "detail": "마하의 속도로 목표를 향해 돌진하는 포켓몬이에요.",
         "traits": "👑 카리스마 | ⚡ 결단력 | 🏆 성취"},
        {"id": 112, "name_kr": "코뿌리", "type": "땅/바위",
         "desc": "한번 정한 길은 끝까지 돌진! 추진력 만렙이에요.",
         "detail": "한번 돌진하면 멈추지 않는 포켓몬이에요.",
         "traits": "🏃 추진력 | 🛡️ 강인함 | 🎯 의지"},
        {"id": 75, "name_kr": "데구리", "type": "바위",
         "desc": "흔들림 없는 의지! 원칙주의 리더예요.",
         "detail": "산에서 굴러내려오는 단단한 포켓몬이에요.",
         "traits": "🪨 원칙 | 💼 의지 | 🎯 결단"},
        {"id": 217, "name_kr": "링곰", "type": "노말",
         "desc": "강력한 힘과 듬직한 카리스마! 든든한 리더예요.",
         "detail": "강력한 발톱으로 나무를 베어내는 든든한 포켓몬이에요.",
         "traits": "💪 카리스마 | 🐻 듬직함 | 🏆 리더십"},
    ],
    "ESFJ": [
        {"id": 242, "name_kr": "해피너스", "type": "노말",
         "desc": "행복을 나누는 사랑의 화신! 따뜻한 당신이에요.",
         "detail": "행복을 나누면 더 큰 행복이 온다고 믿는 포켓몬이에요.",
         "traits": "💕 배려심 | 🌸 친절함 | 🎊 사교성"},
        {"id": 40, "name_kr": "푸크린", "type": "노말/페어리",
         "desc": "포근하고 다정한 매력! 모두에게 사랑받아요.",
         "detail": "큰 눈으로 상대를 매료시키는 포켓몬이에요.",
         "traits": "🤗 포근함 | 💝 다정함 | 🌷 사교성"},
        {"id": 184, "name_kr": "마릴리", "type": "물/페어리",
         "desc": "친구들을 챙기는 따뜻함! 모두의 친구예요.",
         "detail": "가족과 친구를 끔찍이 아끼는 포켓몬이에요.",
         "traits": "💧 따뜻함 | 💕 우정 | 🤝 친화력"},
        {"id": 573, "name_kr": "치라치노", "type": "노말",
         "desc": "깔끔하고 우아한 매력! 모두를 챙기는 당신이에요.",
         "detail": "깔끔한 성격으로 주변을 정리하는 포켓몬이에요.",
         "traits": "🌸 우아함 | 💕 배려 | ✨ 깔끔함"},
        {"id": 241, "name_kr": "밀탱크", "type": "노말",
         "desc": "푸근하고 자상한 어머니 같은 매력의 소유자예요!",
         "detail": "우유로 사람들을 건강하게 해주는 포켓몬이에요.",
         "traits": "🥛 자상함 | 💕 돌봄 | 🤗 따뜻함"},
        {"id": 700, "name_kr": "님피아", "type": "페어리",
         "desc": "사랑을 나누는 매력덩어리! 모두의 사랑이에요.",
         "detail": "사랑의 감정을 에너지로 바꾸는 포켓몬이에요.",
         "traits": "💖 사랑 | 🌸 매력 | ✨ 친절"},
    ],
    "ISTP": [
        {"id": 130, "name_kr": "갸라도스", "type": "물/비행",
         "desc": "조용하지만 폭발적인 매력! 쿨한 당신이에요.",
         "detail": "평소엔 조용하지만 화나면 무서운 포켓몬이에요.",
         "traits": "🔧 손재주 | 🌊 침착함 | ⚡ 폭발력"},
        {"id": 448, "name_kr": "루카리오", "type": "격투/강철",
         "desc": "냉정하고 정확한 판단력! 실력으로 보여주는 당신이에요.",
         "detail": "차분하지만 강력한 격투가예요.",
         "traits": "🎯 정확함 | 💪 실력 | 🧊 냉정함"},
        {"id": 94, "name_kr": "팬텀", "type": "고스트/독",
         "desc": "신비롭고 쿨한 매력! 종잡을 수 없는 당신이에요.",
         "detail": "그림자처럼 움직이는 신비한 포켓몬이에요.",
         "traits": "🌙 신비로움 | 🃏 자유로움 | 🎭 독립성"},
        {"id": 625, "name_kr": "절각참", "type": "악/강철",
         "desc": "날카로운 분석과 실행력! 쿨한 실력자예요.",
         "detail": "날카로운 칼날 같은 발톱으로 빠르게 움직이는 포켓몬이에요.",
         "traits": "⚔️ 예리함 | 🎯 실행력 | 🧊 독립성"},
        {"id": 197, "name_kr": "블래키", "type": "악",
         "desc": "조용하지만 강력한 카리스마! 쿨한 매력의 소유자예요.",
         "detail": "밤에 활동하는 신비로운 포켓몬이에요.",
         "traits": "🌙 쿨함 | 💪 강함 | 🎭 독립"},
        {"id": 472, "name_kr": "글라이온", "type": "땅/비행",
         "desc": "날렵하고 정확한 사냥꾼! 실력 있는 당신이에요.",
         "detail": "어둠 속에서 정확하게 사냥하는 포켓몬이에요.",
         "traits": "🎯 정확 | ⚡ 날렵함 | 💪 실력"},
    ],
    "ISFP": [
        {"id": 3, "name_kr": "이상해꽃", "type": "풀/독",
         "desc": "아름다운 꽃을 피우는 평화로운 영혼! 감성적인 당신이에요.",
         "detail": "등의 큰 꽃에서 달콤한 향기를 내는 포켓몬이에요.",
         "traits": "🎨 예술성 | 🕊️ 평화로움 | 🌷 감성적"},
        {"id": 151, "name_kr": "뮤", "type": "에스퍼",
         "desc": "신비롭고 순수한 자유로운 영혼! 당신과 닮았어요.",
         "detail": "자유롭게 하늘을 날아다니는 신비로운 포켓몬이에요.",
         "traits": "🌈 신비로움 | ✨ 자유로움 | 💖 순수"},
        {"id": 134, "name_kr": "샤미드", "type": "물",
         "desc": "달빛 아래 우아한 매력! 감성적이고 평온한 당신이에요.",
         "detail": "우아한 물의 정령 같은 포켓몬이에요.",
         "traits": "🌊 우아함 | 🌙 감성 | 💙 평온"},
        {"id": 470, "name_kr": "리피아", "type": "풀",
         "desc": "자연과 함께 호흡하는 평화로움! 순수한 영혼이에요.",
         "detail": "숲의 정령처럼 자연과 하나가 되는 포켓몬이에요.",
         "traits": "🌱 자연친화 | 🕊️ 평화 | 🎨 감성"},
        {"id": 350, "name_kr": "밀로틱", "type": "물",
         "desc": "세상에서 가장 아름다운 포켓몬! 우아한 감성의 소유자예요.",
         "detail": "가장 아름다운 포켓몬으로 불려요.",
         "traits": "💎 아름다움 | 🌊 우아함 | ✨ 감성"},
        {"id": 700, "name_kr": "님피아", "type": "페어리",
         "desc": "사랑을 표현하는 감성적 영혼! 부드러운 당신이에요.",
         "detail": "사랑의 감정을 리본으로 표현하는 포켓몬이에요.",
         "traits": "💕 감성 | 🌸 부드러움 | ✨ 매력"},
    ],
    "ESTP": [
        {"id": 94, "name_kr": "팬텀", "type": "고스트/독",
         "desc": "장난기 가득한 스릴 메이커! 행동력 넘치는 당신이에요.",
         "detail": "어둠 속에서 장난을 즐기는 포켓몬이에요.",
         "traits": "🎢 모험심 | 🃏 장난기 | 🏃 행동력"},
        {"id": 68, "name_kr": "괴력몬", "type": "격투",
         "desc": "지금 당장 부딪치는 행동파! 에너지 넘치는 당신이에요.",
         "detail": "4개의 팔로 즉시 행동하는 포켓몬이에요.",
         "traits": "⚡ 행동력 | 🏋️ 도전 | 🔥 열정"},
        {"id": 6, "name_kr": "리자몽", "type": "불꽃/비행",
         "desc": "화끈하고 멋진 매력! 시선을 사로잡는 당신이에요.",
         "detail": "강한 자존심과 화려한 매력의 포켓몬이에요.",
         "traits": "🔥 카리스마 | ⚡ 스릴 | 💫 매력"},
        {"id": 445, "name_kr": "한카리아스", "type": "드래곤/땅",
         "desc": "거침없는 추진력과 도전 정신! 스릴을 즐기는 당신이에요.",
         "detail": "마하의 속도로 돌진하는 포켓몬이에요.",
         "traits": "🏃 추진력 | ⚡ 모험 | 🎯 도전"},
        {"id": 257, "name_kr": "번치코", "type": "불꽃/격투",
         "desc": "빠른 발차기와 화끈한 매력! 액션 스타예요.",
         "detail": "강력한 다리로 빠르게 움직이는 포켓몬이에요.",
         "traits": "🦵 액션 | 🔥 열정 | ⚡ 스피드"},
        {"id": 308, "name_kr": "요가램", "type": "격투/에스퍼",
         "desc": "유연하고 빠른 액션! 즉흥적인 매력의 소유자예요.",
         "detail": "유연한 몸으로 빠르게 움직이는 포켓몬이에요.",
         "traits": "💫 유연함 | ⚡ 즉흥 | 🎯 액션"},
    ],
    "ESFP": [
        {"id": 39, "name_kr": "푸린", "type": "노말/페어리",
         "desc": "노래로 모두를 매료시키는 엔터테이너! 사랑스러운 당신이에요.",
         "detail": "노래로 사람들을 매료시키는 포켓몬이에요.",
         "traits": "🎵 매력적 | 🎭 표현력 | 🌈 자유로움"},
        {"id": 25, "name_kr": "피카츄", "type": "전기",
         "desc": "어디서나 빛나는 스타! 모두의 사랑을 받는 당신이에요.",
         "detail": "활발하고 사랑받는 포켓몬계의 슈퍼스타예요.",
         "traits": "✨ 인기 | 😄 발랄함 | 🎉 즐거움"},
        {"id": 122, "name_kr": "마임맨", "type": "에스퍼/페어리",
         "desc": "퍼포먼스의 달인! 시선 강탈 매력의 소유자예요.",
         "detail": "팬터마임으로 사람들을 즐겁게 하는 포켓몬이에요.",
         "traits": "🎨 표현력 | 🎪 끼 | 💫 매력"},
        {"id": 700, "name_kr": "님피아", "type": "페어리",
         "desc": "사랑스러운 매력으로 분위기 메이커! 당신과 닮았어요.",
         "detail": "사랑의 에너지로 분위기를 밝게 만드는 포켓몬이에요.",
         "traits": "💕 사랑스러움 | 🌸 매력 | ✨ 화려함"},
        {"id": 778, "name_kr": "따라먹쥐", "type": "고스트/페어리",
         "desc": "예측 불가한 깜짝 매력! 즐거움을 선사하는 당신이에요.",
         "detail": "변신을 즐기는 장난꾸러기 포켓몬이에요.",
         "traits": "🎭 즐거움 | 🎪 깜짝 | 🌟 매력"},
        {"id": 52, "name_kr": "나옹", "type": "노말",
         "desc": "귀엽고 영리한 매력! 어디서나 인기 만점이에요.",
         "detail": "반짝이는 것을 좋아하는 매력적인 포켓몬이에요.",
         "traits": "✨ 매력 | 😺 귀여움 | 🎉 인기"},
    ]
}

# ==================== MBTI 궁합 데이터 ====================
mbti_compatibility = [
    "INTJ": {"best": ["ENFP", "ENTP"], "good": ["INFJ", "INFP"], "desc": "지적인 자극을 주는 ENFP/ENTP와 환상의 케미! 🔥"},
    "INTP": {"best": ["ENTJ", "ESTJ"], "good": ["INFJ", "ENFJ"], "desc": "추진력 있는 ENTJ/ESTJ가 당신의 아이디어를 실현시켜줘요! 💡"},
    "ENTJ": {"best": ["INTP", "INFP"], "good": ["ENFP", "INTJ"], "desc": "당신의 비전을 이해해주는 INTP/INFP와 완벽한 콤비! 👑"},
    "ENTP": {"best": ["INFJ", "INTJ"], "good": ["ENFJ", "ENFP"], "desc": "깊이 있는 INFJ/INTJ가 당신의 영혼의 단짝이에요! 🎭"},
    "INFJ": {"best": ["ENTP", "ENFP"], "good": ["INTJ", "INFJ"], "desc": "활기찬 ENTP/ENFP와 마음의 균형을 이루는 관계! ✨"},
    "INFP": {"best": ["ENFJ", "ENTJ"], "good": ["INFJ", "ENFP"], "desc": "따뜻한 ENFJ/ENTJ가 당신의 꿈을 응원해줘요! 💖"},
    "ENFJ": {"best": ["INFP", "ISFP"], "good": ["ENFP", "INFJ"], "desc": "감성적인 INFP/ISFP를 이끌어주는 멋진 관계! 🌟"},
    "ENFP": {"best": ["INTJ", "INFJ"], "good": ["ENTP", "ENFJ"], "desc": "차분한 INTJ/INFJ와 환상의 균형을 이뤄요! 🎉"},
    "ISTJ": {"best": ["ESFP", "ESTP"], "good": ["ISFJ", "ESTJ"], "desc": "발랄한 ESFP/ESTP가 당신의 일상을 빛나게 해줘요! 🛡️"},
    "ISFJ": {"best": ["ESTP", "ESFP"], "good": ["ISTJ", "ENFJ"], "desc": "활발한 ESTP/ESFP와 따뜻한 조화를 이뤄요! 🌸"},
    "ESTJ": {"best": ["ISFP", "ISTP"], "good": ["ESFJ", "ENTJ"], "desc": "감성적인 ISFP/ISTP와 균형 있는 관계! 💼"},
    "ESFJ": {"best": ["ISFP", "ISTP"], "good": ["ESTJ", "ENFJ"], "desc": "조용한 ISFP/ISTP를 따뜻하게 챙겨주는 관계! 💕"},
    "ISTP": {"best": ["ESTJ", "ESFJ"], "good": ["ISFP", "ENTP"], "desc": "추진력 있는 ESTJ/ESFJ와 환상의 호흡! 🔧"},
    "ISFP": {"best": ["ENFJ", "ESFJ"], "good": ["ESTJ", "ISFP"], "desc": "리더십 있는 ENFJ/ESFJ가 당신을 빛나게 해요! 🌺"},
    "ESTP": {"best": ["ISTJ", "ISFJ"], "good": ["ESFP", "ESTP"], "desc": "차분한 ISTJ/ISFJ가 당신의 에너지를 안정시켜줘요! ⚡"},
    "ESFP": {"best": ["ISTJ", "ISFJ"], "good": ["ESFJ", "ENFP"], "desc": "신뢰감 있는 ISTJ/ISFJ와 완벽한 케미! 🎤"},
]

# ==================== MBTI 검사 질문 ====================
mbti_questions = [
    {"q": "1. 주말에 시간이 생기면?", "a": "🎉 친구들과 신나게 놀러간다!", "b": "🌙 집에서 혼자만의 시간을 즐긴다", "type": "EI"},
    {"q": "2. 새로운 사람을 만나면?", "a": "😄 먼저 다가가서 말을 건다", "b": "🙂 상대가 말 걸어주길 기다린다", "type": "EI"},
    {"q": "3. 에너지를 충전하는 방법은?", "a": "🎊 사람들과 어울리며", "b": "🧘 혼자만의 시간을 가지며", "type": "EI"},
    {"q": "4. 일을 할 때 나는?", "a": "🔍 현재의 사실과 데이터를 중시한다", "b": "💫 미래의 가능성과 아이디어를 중시한다", "type": "SN"},
    {"q": "5. 설명을 들을 때?", "a": "📋 구체적이고 실용적인 게 좋다", "b": "🎨 추상적이고 창의적인 게 좋다", "type": "SN"},
    {"q": "6. 책이나 영화를 볼 때?", "a": "📖 실제 일어난 이야기가 좋다", "b": "🌌 판타지나 SF가 좋다", "type": "SN"},
    {"q": "7. 결정을 내릴 때?", "a": "🧊 논리적으로 분석한다", "b": "💖 사람들의 감정을 고려한다", "type": "TF"},
    {"q": "8. 친구가 고민을 털어놓으면?", "a": "🎯 해결책을 제시해준다", "b": "🤗 공감하고 위로해준다", "type": "TF"},
    {"q": "9. 비판을 받았을 때?", "a": "💪 객관적으로 받아들인다", "b": "😢 마음에 상처를 받는다", "type": "TF"},
    {"q": "10. 계획을 세울 때?", "a": "📅 미리 철저하게 계획한다", "b": "🎲 그때그때 상황에 맞춰간다", "type": "JP"},
    {"q": "11. 책상이나 방은?", "a": "✨ 항상 정리정돈되어 있다"},
    {"q": "11. 책상이나 방은?", "a": "✨ 항상 정리정돈되어 있다", "b": "🎨 좀 어수선해도 괜찮다", "type": "JP"},
    {"q": "12. 여행을 갈 때?", "a": "🗺️ 일정을 꼼꼼히 짠다", "b": "🎒 즉흥적으로 떠난다", "type": "JP"},
]


# ==================== PokeAPI 이미지 가져오기 ====================
@st.cache_data
def get_pokemon_image(pokemon_id):
    """PokeAPI에서 포켓몬 공식 아트워크 이미지 URL 가져오기"""
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            img_url = data["sprites"]["other"]["official-artwork"]["front_default"]
            if not img_url:
                img_url = data["sprites"]["front_default"]
            return img_url
    except Exception:
        return None
    return None


# ==================== 사이드바 메뉴 ====================
with st.sidebar:
    st.markdown("# ⚡ MBTI 포켓몬 월드 🎮")
    st.markdown("---")
    
    menu = st.radio(
        "🌟 메뉴를 선택하세요!",
        ["🏠 홈", "📝 MBTI 간이 검사", "🎁 포켓몬 추천", "💕 MBTI 궁합 보기", "📊 통계 보기"]
    )
    
    st.markdown("---")
    st.markdown("### 💡 MBTI란?")
    st.info("성격을 16가지 유형으로 분류하는 심리 검사예요! 🧩")
    
    st.markdown("### 🎮 포켓몬 통계")
    total = sum(len(v) for v in mbti_pokemon.values())
    st.metric("총 포켓몬 수", f"{total}마리 🌟")
    st.metric("MBTI 유형", "16가지 🎨")
    
    st.markdown("---")
    st.markdown("🌐 이미지: [PokeAPI](https://pokeapi.co)")
    st.markdown("Made with 💖 by 당곡고")


# ==================== 1. 홈 화면 ====================
if menu == "🏠 홈":
    st.markdown("<h1 style='text-align: center;'>⚡ MBTI 포켓몬 월드에 오신 걸 환영해요! 🎮</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>당신의 성격과 닮은 포켓몬을 만나보세요! ✨</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #FFE5E5 0%, #FFD6E8 100%); 
                    padding: 30px; border-radius: 20px; text-align: center; height: 250px;'>
            <h1>📝</h1>
            <h3>MBTI 간이 검사</h3>
            <p>12개 질문으로 빠르게<br>나의 MBTI를 알아보세요!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #E5F3FF 0%, #D6E8FF 100%); 
                    padding: 30px; border-radius: 20px; text-align: center; height: 250px;'>
            <h1>🎁</h1>
            <h3>포켓몬 추천</h3>
            <p>나의 MBTI에 어울리는<br>포켓몬 친구를 찾아보세요!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #FFE5F5 0%, #FFD6F0 100%); 
                    padding: 30px; border-radius: 20px; text-align: center; height: 250px;'>
            <h1>💕</h1>
            <h3>MBTI 궁합</h3>
            <p>나와 잘 맞는 MBTI 유형과<br>포켓몬 궁합을 확인하세요!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌟 추천 포켓몬 미리보기")
    
    # 랜덤 포켓몬 4마리 미리보기
    preview_cols = st.columns(4)
    all_pokemons = [(mbti, p) for mbti, plist in mbti_pokemon.items() for p in plist]
    samples = random.sample(all_pokemons, 4)
    
    for i, (mbti_type, poke) in enumerate(samples):
        with preview_cols[i]:
            img = get_pokemon_image(poke['id'])
            if img:
                st.image(img, use_container_width=True)
            st.markdown(f"<p style='text-align:center;'><b>{poke['name_kr']}</b><br><small>{mbti_type}</small></p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size:18px;'>👈 왼쪽 사이드바에서 메뉴를 선택해 시작해보세요! 🎉</p>", unsafe_allow_html=True)


# ==================== 2. MBTI 간이 검사 ====================
elif menu == "📝 MBTI 간이 검사":
    st.markdown("<h1 style='text-align: center;'>📝 MBTI 간이 검사 🔍</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>12개의 질문에 답하고 나의 MBTI를 확인해보세요! ✨</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    answers = {}
    
    for i, q in enumerate(mbti_questions):
        st.markdown(f"### {q['q']}")
        answer = st.radio(
            "선택해주세요",
            [q['a'], q['b']],
            key=f"q{i}",
            label_visibility="collapsed"
        )
        answers[i] = (answer, q['type'], q['a'])
        st.markdown("")
    
    st.markdown("---")
    
    if st.button("🎊 나의 MBTI 확인하기! 🎊", use_container_width=True):
        # MBTI 계산
        scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        
        for i, (ans, mbti_type, a_option) in answers.items():
            if ans == a_option:  # a 선택
                scores[mbti_type[0]] += 1
            else:  # b 선택
                scores[mbti_type[1]] += 1
        
        result_mbti = (
            ("E" if scores["E"] >= scores["I"] else "I") +
            ("S" if scores["S"] >= scores["N"] else "N") +
            ("T" if scores["T"] >= scores["F"] else "F") +
            ("J" if scores["J"] >= scores["P"] else "P")
        )
        
        st.balloons()
        st.markdown(f"<h1 style='text-align: center; color: #FF4757;'>🎉 당신의 MBTI는 {result_mbti} 입니다! 🎉</h1>", unsafe_allow_html=True)
        
        # 결과 포켓몬 미리보기
        pokemon_list = mbti_pokemon[result_mbti]
        result_poke = random.choice(pokemon_list)
        
        col1, col2 = st.columns(2)
        with col1:
            img = get_pokemon_image(result_poke['id'])
            if img:
                st.image(img, use_container_width=True)
        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #FFE5E5 0%, #FFD6E8 100%); 
                        padding: 25px; border-radius: 20px; margin-top: 30px;'>
                <h2 style='text-align:center;'>🌟 당신의 포켓몬 친구 🌟</h2>
                <h1 style='text-align:center;'>{result_poke['name_kr']}</h1>
                <p style='text-align:center; font-size:16px;'>📌 타입: <b>{result_poke['type']}</b></p>
                <p style='text-align:center;'>💬 {result_poke['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.success(f"✨ {result_poke['traits']}")
        st.info("👈 왼쪽 '🎁 포켓몬 추천' 메뉴에서 더 자세한 포켓몬 정보를 확인해보세요!")


# ==================== 3. 포켓몬 추천 ====================
elif menu == "🎁 포켓몬 추천":
    st.markdown("<h1 style='text-align: center;'>🎁 MBTI 포켓몬 추천 ⚡</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>버튼을 누를 때마다 다른 포켓몬이 나와요! 🎲</p>", unsafe_allow_html=True)
    st.markdown("---")
    
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
    
    if st.button("🔮 나의 포켓몬 친구 만나기! 🎊", use_container_width=True):
        pokemon_list = mbti_pokemon[mbti]
        result = random.choice(pokemon_list)
        
        st.balloons()
        st.markdown(f"<h2 style='text-align: center;'>✨ 당신의 MBTI는 <span style='color:#FF6B6B;'>{mbti}</span> ✨</h2>", unsafe_allow_html=True)
        
        col_img, col_info = st.columns([1, 1])
        
        with col_img:
            img_url = get_pokemon_image(result['id'])
            if img_url:
                st.image(img_url, use_container_width=True, caption=f"#{result['id']:03d} {result['name_kr']}")
        
        with col_info:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #FFE5E5 0%, #FFD6E8 100%); 
                        padding: 25px; border-radius: 20px; margin-top: 30px;'>
                <h1 style='text-align:center;'>{result['name_kr']}</h1>
                <p style='text-align:center; font-size:18px;'>📌 타입: <b>{result['type']}</b></p>
                <p style='text-align:center; font-size:16px; color:#FF4757;'>🔢 도감번호: #{result['id']:03d}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 💌 당신에게 보내는 메시지")
        st.info(f"💬 {result['desc']}")
        
        st.markdown("### 📖 포켓몬 상세 설명")
        st.warning(f"🔍 {result['detail']}")
        
        st.markdown("### 🌟 당신의 매력 포인트")
        st.success(result['traits'])
        
        # 다른 추천 포켓몬
        st.markdown("---")
        st.markdown("### 🎁 이 MBTI에 어울리는 다른 포켓몬들")
        other_pokemons = [p for p in pokemon_list if p['name_kr'] != result['name_kr']]
        
        cols = st.columns(len(other_pokemons))
        for i, p in enumerate(other_pokemons):
            with cols[i]:
                other_img = get_pokemon_image(p['id'])
                if other_img:
                    st.image(other_img, use_container_width=True)
                st.markdown(f"<p style='text-align:center;'><b>{p['name_kr']}</b><br><small>{p['type']}</small></p>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("<p style='text-align: center; font-size:18px;'>🎲 다시 눌러서 또 다른 포켓몬을 만나보세요! 🎮</p>", unsafe_allow_html=True)


# ==================== 4. MBTI 궁합 보기 ====================
elif menu == "💕 MBTI 궁합 보기":
    st.markdown("<h1 style='text-align: center;'>💕 MBTI 궁합 보기 💘</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>나와 잘 맞는 MBTI 유형과 포켓몬을 확인해보세요! ✨</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🙋 나의 MBTI")
        my_mbti = st.selectbox("나의 MBTI 선택", list(mbti_pokemon.keys()), key="my")
    with col2:
        st.markdown("### 👫 상대방의 MBTI")
        partner_mbti = st.selectbox("상대방 MBTI 선택", list(mbti_pokemon.keys()), key="partner")
    
    st.markdown("---")
    
    if st.button("💖 궁합 확인하기! 💖", use_container_width=True):
        compat = mbti_compatibility[my_mbti]
        
        # 궁합 점수 계산
        if partner_mbti in compat['best']:
            score = random.randint(90, 100)
            emoji = "💖💖💖"
            level = "환상의 케미!"
            color = "#FF4757"
        elif partner_mbti in compat['good']:
            score = random.randint(75, 89)
            emoji = "💕💕"
            level = "좋은 궁합!"
            color = "#FFA502"
        elif my_mbti == partner_mbti:
            score = random.randint(70, 85)
            emoji = "👯"
            level = "쌍둥이 케미!"
            color = "#5352ED"
        else:
            score = random.randint(50, 74)
            emoji = "💛"
            level = "노력하면 좋아져요!"
            color = "#FFA502"
        
        st.balloons()
        
        # 결과 표시
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #FFE5E5 0%, #FFD6F0 100%); 
                    padding: 40px; border-radius: 25px; text-align: center;'>
            <h1 style='font-size: 50px; margin: 0;'>{emoji}</h1>
            <h1 style='color: {color}; margin: 15px 0;'>{score}점</h1>
            <h2 style='color: #333;'>{level}</h2>
            <p style='font-size: 18px; color: #555;'>{my_mbti} 💞 {partner_mbti}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 💌 궁합 메시지")
        st.info(f"💬 {compat['desc']}")
        
        # 양쪽 포켓몬 비교
        st.markdown("---")
        st.markdown("### 🎮 우리의 포켓몬 친구들")
        
        my_poke = random.choice(mbti_pokemon[my_mbti])
        partner_poke = random.choice(mbti_pokemon[partner_mbti])
        
        col_a, col_heart, col_b = st.columns([2, 1, 2])
        
        with col_a:
            st.markdown(f"<h3 style='text-align:center;'>🙋 나의 포켓몬<br>({my_mbti})</h3>", unsafe_allow_html=True)
            my_img = get_pokemon_image(my_poke['id'])
            if my_img:
                st.image(my_img, use_container_width=True)
            st.markdown(f"<p style='text-align:center;'><b>{my_poke['name_kr']}</b><br>{my_poke['type']}</p>", unsafe_allow_html=True)
        
        with col_heart:
            st.markdown("<h1 style='text-align:center; font-size:100px; margin-top:80px;'>💕</h1>", unsafe_allow_html=True)
        
        with col_b:
            st.markdown(f"<h3 style='text-align:center;'>👫 상대 포켓몬<br>({partner_mbti})</h3>", unsafe_allow_html=True)
            partner_img = get_pokemon_image(partner_poke['id'])
            if partner_img:
                st.image(partner_img, use_container_width=True)
            st.markdown(f"<p style='text-align:center;'><b>{partner_poke['name_kr']}</b><br>{partner_poke['type']}</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown(f"### 💎 {my_mbti}의 최고 궁합 TOP 2")
        cols = st.columns(2)
        for i, best_type in enumerate(compat['best']):
            with cols[i]:
                best_poke = random.choice(mbti_pokemon[best_type])
                best_img = get_pokemon_image(best_poke['id'])
                if best_img:
                    st.image(best_img, use_container_width=True)
                st.markdown(f"<p style='text-align:center;'><b>{best_type}</b><br>{best_poke['name_kr']}</p>", unsafe_allow_html=True)


# ==================== 5. 통계 보기 ====================
elif menu == "📊 통계 보기":
    st.markdown("<h1 style='text-align: center;'>📊 포켓몬 통계 🎮</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    total = sum(len(v) for v in mbti_pokemon.values())
    
    with col1:
        st.metric("🌟 총 포켓몬", f"{total}마리")
    with col2:
        st.metric("🎨 MBTI 유형", "16가지")
    with col3:
        st.metric("🎁 MBTI당", "6마리")
    with col4:
        st.metric("💕 궁합 조합", "256가지")
    
    st.markdown("---")
    st.markdown("### 🎯 MBTI별 추천 포켓몬 전체 보기")
    
    selected_mbti = st.selectbox("📌 MBTI 선택", list(mbti_pokemon.keys()))
    
    pokemons = mbti_pokemon[selected_mbti]
    
    st.markdown(f"### ✨ {selected_mbti}의 포켓몬들")
    
    # 3마리씩 2줄로 표시
    for row in range(2):
        cols = st.columns(3)
        for col_idx in range(3):
            idx = row * 3 + col_idx
            if idx < len(pokemons):
                with cols[col_idx]:
                    poke = pokemons[idx]
                    img = get_pokemon_image(poke['id'])
                    if img:
                        st.image(img, use_container_width=True)
                    st.markdown(f"""
                    <div style='text-align:center; padding:10px; background:#FFF5F5; border-radius:10px;'>
                        <h4>#{poke['id']:03d} {poke['name_kr']}</h4>
                        <p><small>📌 {poke['type']}</small></p>
                        <p style='font-size:13px;'>{poke['traits']}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌈 모든 MBTI 한눈에 보기")
    
    mbti_emojis = {
        "INTJ": "🧬", "INTP": "🔷", "ENTJ": "🔥", "ENTP": "🐵",
        "INFJ": "🌀", "INFP": "🦊", "ENFJ": "🧚", "ENFP": "⚡",
        "ISTJ": "🐢", "ISFJ": "🌱", "ESTJ": "🗿", "ESFJ": "🥚",
        "ISTP": "🐉", "ISFP": "🌺", "ESTP": "👻", "ESFP": "🎤",
    }
    
    rows = [list(mbti_pokemon.keys())[i:i+4] for i in range(0, 16, 4)]
    for row in rows:
        cols = st.columns(4)
        for i, mbti_type in enumerate(row):
            with cols[i]:
                emoji = mbti_emojis.get(mbti_type, "✨")
                st.markdown(f"""
                <div style='text-align:center; padding:20px; background:linear-gradient(135deg, #FFE5E5 0%, #FFD6E8 100%); border-radius:15px; margin:5px;'>
                    <h1>{emoji}</h1>
                    <h3>{mbti_type}</h3>
                    <p><small>{len(mbti_pokemon[mbti_type])}마리</small></p>
                </div>
                """, unsafe_allow_html=True)
