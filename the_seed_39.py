import os
import discord

client = discord.Client()

Question = {
    # '문제': [1, 2, 3, 4],
    '골드비치 리조트에 거주하는 잡화 상인 이름은?': '프레드릭  나탈리	@메이슨@	베티',
    '노틸러스의 무기 상인 이름은?': '리드   프란시스    테스	@모건@',
    '노틸러스의 잡화 상인 이름은?': '잭	시나몬	미르	@갤리@',
    '노틸러스의 창고지기 이름은?': '슈리츠	다고쓰	론도	@돈틀레스@',
    '누구의 대사일까? - 고대 노바의 신을 모시고 있습니다.': '소피아	브로커 정	@펜릴@	론도',
    '누구의 대사일까? - 나의 근육을 보라구. 나처럼 강해지고 싶지 않나?': '지미	뮤네	@쿤@	테스',
    '누구의 대사일까? - 난 앞치마가 잘 어울리는 남자야.': '헬레나	@일렉스@	크루소	프레드릭',
    '누구의 대사일까? - 날씨가 참 좋죠? 해피와 산책하기 좋은 날씨입니다.': '큐트	@게렉터@	시나몬	알렉스',
    '누구의 대사일까? - 내가 주워왔으니까 내가 책임져!': '비어완	프레드릭	골드리치	    @랑@',
    '누구의 대사일까? - 누가 대신 먹이좀 구해줬으면 좋겠다.': '다니카	고로	따비	@돌돌@',
    '누구의 대사일까? - 도둑질해 가는 사람을 용서하지 않을거야!': '일스	@해리@	자아	루이스',
    '누구의 대사일까? - 모두 힘을 합해야만 해요.': '리나	@라케리스@	다고쓰	베티',
    '누구의 대사일까? - 몸을 푼 지 얼마되지 않았답니다.': '디테	랑	캘리코	@따비@',
    '누구의 대사일까? - 상전벽해... 세월에 따라 세상도 많이 변하였소': '@도공@	기옹	구영감	노공',
    '누구의 대사일까? - 손이 예전같지 않아.. 어서 제자를 한 명 거뒀으면 좋겠는데..': '@기옹@	이옹	김영감	구영감',
    '누구의 대사일까? - 숙제도 많고 공부도 해야되고..바쁘다..': '@요정 윙@	요정 아르웬	요정 잭	요정로웬',
    '누구의 대사일까? - 아궁이 불을 뗄 땔감이 부족하네': '이토스	슈미	로도스	@고로@',
    '누구의 대사일까? - 악마의 문서를 가지고 있다면 나한테 맡겨 보는건 어때?': '휴머노이드 C	@지니@	리드	슈미',
    '누구의 대사일까? - 앞이 보이냐고? 뭘 당연한걸 묻는거지?': '페이슨	@푸노운@	푸카	소피아',
    '누구의 대사일까? - 약초를 모으고 있다네…': '@사바트라마@	벼루	키리두	로도스',
    '누구의 대사일까? - 어라…? 내 연구자료가 어디로 갔지?': '에스텔	제피	케리	@마법사 쿠디@',
    '누구의 대사일까? - 요즘 몬스터들이 사나워진 것 같아 걱정이에요.': '큐트	@리사@	푸츠키	지미',
    '누구의 대사일까? - 일도 중요하지만 맛있는 거 먹는것도 참 중요하지': '오심마	@바반@	프란시스	에스텔',
    '누구의 대사일까? - 제 옆의 델브는 경비서는 일은 항상 지겹다고 난리죠.': '토리	@올슨@	잭	그윈',
    '누구의 대사일까? - 친구인 아르웬은 인간을 불편해 한답니다.': '@요정 로웬@	아이린	요정 윙	요정 푸링',
    '누구의 대사일까? - 친구인 아르웬은 인간을 불편해 한답니다..': '@요정 로웬@	요정 루엔	요정 윙	요정 푸링',
    '누구의 대사일까? - 킁킁…이게 무슨 냄새죠?': '유타    	페일	@알비올라@	마녀 바바라',
    '누구의 대사일까? - 태상에게 약초를 빨리 보내주어야 할텐데…': '@구영감@	김영감	박영감	조영감',
    '누구의 대사일까? - 튼튼한 방어구가 필요하다면 잠깐 여기에 들려보지 그래?': '루이스	마이크	@로도스@	미르',
    '누구의 대사일까? - 하인즈가 나쁜 사람은 아니지만..': '@요정 아르웬@	무라트	프델라	요정 수',
    '누구의 대사일까? - 해수면의 상승이 멈춰야 할 텐데..': '도베르만	슈미	@푸탄@	천지',
    '누구의 대사일까? - 해적은 최강! 한 판 붙어 보자고요!': '베티	마파	라엘	@발레리@',
    '누구의 대사일까? - 혼자 노는 것도 심심해… 후~': '체프	@앤@	푸로	유타',
    '누구의 대사일까? - 흐음 자네도 득도의 수련을 해볼텐가?': '@노공@	도공	기옹	구영감',
    '누구의 대사일까? - 흥, 외부인은 도무지 신뢰할 수 없다니까.': '라니아	알렉스	토푸	@교감 카라얀@',
    '다음 중 검사의 스킬로 옳지 않은 것은?': '아이언바디	@상상력 증가@	파워 스트라이크	슬래시 블러스트',
    '다음 중 나이트워커의 스킬로 옳지 않는 것은?': '@콜래트럴 플래시@	다크니스	헤이스트	매직 스틸',
    '다음 중 나이트워커의 스킬로 옳지 않는 것은?.': '@콜래트럴 플래시@	쉐도우 서번트	헤이스트	도미니언',
    '다음 중 데몬슬레이어의 스킬로 옳지 않을 것은?': '@마인드 스킨@	뱀피릭 터치	메이플 용사	다크 바인드',
    '다음 중 메카닉의 스킬로 옳지 않을 것은?': '포춘 어택	플레임 런처	개틀링 샷	@클레이 모어@',
    '다음 중 미하일의 스킬로 옳지 않는 것은?': '@소울 아카이브@	소울 쉴드	소울 어질리티	소울 블레이드',
    '다음 중 팬텀의 스킬로 옳지 않는 것은?': '미스포츈 프로텍션	@퍼펙트 센스@	어큐트 센스	플래시 앤 플리',
    '다음 중 캐논슈터의 스킬로 옳지 않는 것은?': '슬러그 샷	캐논 마스터리	몽키 매직	@패스트 리로드@',
    '다음 중 배틀메이지 스킬로 옳지 않은 것은?': '하이 위즈덤	쿼드 블로우	블러드 드레인	@드로우 마나@',
    '다음 중 신궁의 스킬로 옳지 않은 것은?': '마크맨쉼	피어싱	@문워크@	일루전 스텝',
    '다음 중 윈드브레이커의 스킬로 옳지 않은 것은?': '@더블샷 위쳐@	크리티컬 샷	아처 마스터리	스톰',
    '다음 중 은월의 스킬에 속하지 않는 것은?': '통백권 3타	불여우령	@스텀핑 어 머드홀@	하이퍼 애큐러시',
    '다음 중 은월의 스킬에 속하지 않는 것은?.': '너클 숙련	환령 강신	@하이퍼 버팅@	히어로즈 오쓰',
    '다음 중 은월의 스킬에 속하지 않는 것은?..': '약화	정령 결속 4식	건곤 일체	@슬리퍼 홀드@',
    '다음 중 은월의 스킬에 속하지 않는 것은?...': '파력권 2타	@분홍 파참@	메이플 용사	소혼 결계',
    '다음 중 은월의 스킬에 속하지 않는 것은?....': '근력 단련	폭류권 4타	@심의육합권@	정령 결속 극대화',
    '다음 중 은월의 스킬에 속하지 않는 것은?.....': '@팔극 4타@	섬권 2타	사혼 각인	너클 숙련',
    '다음 중 은월의 스킬에 속하지 않는 것은?......': '@태극 2타@	메가 펀치 2타	귀참	후방 이동',
    '다음 중 은월의 스킬에 속하지 않는 것은?.......': '소혼 장막	약점 간파	도약	@참격@',
    '다음 중 은월의 스킬에 속하지 않는 것은?........': '여우령	속박술	@난투@	정령의 화신',
    '다음 중 은월의 스킬에 속하지 않는 것은?.........': '도약	@천근추@	분혼 격참	파쇄철조',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?': '@제령@	가디언 아머	라이트닝 차지	어드밴스드 차지',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?.': '엘리멘탈 차지	아킬레스	위협	@블레싱@',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?..': '아이언 바디	@추격@	컴뱃 오더스	팔라딘 엑스퍼트',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?...': '파이널 어택	페이지 오더	@헤이스트@	생츄어리',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?....': '웨폰 마스터리	블리자드 차지	@맨디블 클로우@	블래스트',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?.....': '@실신한 기도@	워리어 마스터리	리스토네이션	스탠스',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?......': '워리어 리프	플레임 차지	@라이트닝 액션@	디바인 차지',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?.......': '피지컬 트레이닝	쉴드 마스터리	@리갈 스트레치@	용사의 의지',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?........': '슬래시 블러스트	@플레임 디펜스@	돌진	메이플 용사',
    '다음 중 팔라딘의 스킬에 속하지 않는 것은?.........': '웨폰 부스터	블래싱 아머	파라쇼크 가드	@디바인 소드@',
    '다음 중 제로의 스킬에 속하지 않는 것은?': '어스 브레이크	@크림슨 커터@	롤링 커브	어퍼 슬래시',
    '다음 중 제로의 스킬에 속하지 않는 것은?.': '스핀 커터	디바인 리어	@사이킥 트레이서@	스로잉 웨폰',
    '다음 중 제로의 스킬에 속하지 않는 것은?..': '컴뱃 리커버리	윈드 커터	이뮨 베리어	@문설트@',
    '다음 중 제로의 스킬에 속하지 않는 것은?...': '솔리드 바디	스톰 브레이크	@더블 스트레치@	문 스트라이크',
    '다음 중 제로의 스킬에 속하지 않는 것은?....': '스로잉 웨폰	기가 크래시	어스 브레이크	@파일 드라이버@',
    '다음 중 제로의 스킬에 속하지 않는 것은?.....': '점핑 크래시	@데들리 액션@	터닝 드라이브	태도 마스터리',
    '다음 중 제로의 스킬에 속하지 않는 것은?......': '어드밴스드 롤링 커브	@크로스 라인@	아머 스플릿	쉐도우 스트라이크',
    '다음 중 제로의 스킬에 속하지 않는 것은?.......': '플래시 어썰터	@로 블로@	휠 윈드	피어스 쓰러스트',
    '다음 중 제로의 스킬에 속하지 않는 것은?........': '@점핑 파워 봄@	크리티컬 바인드	프론트 슬래시	파워 스텀프',
    '다음 중 제로의 스킬에 속하지 않는 것은?.........': '@파이트 스플래쉬@	윈드 스트라이크	라인포스 바디	대검 마스터리',
    '다음 중 동물형 몬스터가 아닌 것은?': '게릴라 스펙터	@스포아@	고대 슬라임	황금 돼지',
    '다음 중 정령형 몬스터가 아닌 것은?': '@달팽이@	페어리	오렌지톤	아기 바위베어먹기',
    '다음 중 파충류형 몬스터가 아닌 것은?': '개구리	리게이터	강력한 콜드아이	@주니어 레이스@',
    '다음 중 악마형 몬스터가 아닌 것은?': '@불량학생@	방금 사귄 커플버섯	고백하러 가는 판다곰	잭오랜턴',
    '다음 중 어류형 몬스터가 아닌 것은?': '클랑	@검은 마법사의 와이번@	킹크랑	피아누스',
    '다음 중 무형 몬스터가 아닌 것은?': '양파라고라	아리엘	소라문어 슬라임	@앙뚜아네뜨@',
    '다음 중 무형 몬스터가 아닌 것은?.': '무닌  	안전제일	    @망둥이@	코코넛 슬라임',
    '다음 중 불사형 몬스터가 아닌 것은?': '좀비머쉬맘	제등귀신	파우스트	@핑크빈@',
    '다음 중 불사형 몬스터가 아닌 것은?.': '고스트	    유령	@자격의 도도@	파우스트',
    '다음 중 식물형 몬스터가 아닌 것은?': '나팔 꽃 화분	@파이렛 옥토@	초록 버섯	데우',
    '다음 중 모험가에 속하는 직업은?': '소울마스터	에반	제논	@듀얼블레이드@',
    '다음 중 모험가에 속하는 직업은?.': '와일드헌터	@비숍@	팬텀	데몬어벤져',
    '다음 중 노바에 속하는 직업은?': '@엔젤릭 버스터@	팔라딘	신궁	섀도어',
    '다음 중 노바에 속하는 직업은?.': '@카이저@	소울마스터	미하일	메르세데스',
    '다음 중 영웅에 속하는 직업은?': '아크메이지(불독)	나이트로드	@메르세데스@	보우마스터',
    '다음 중 영웅에 속하는 직업은?.': '배틀메이지	다크나이트	@루미너스@	아크메이지(얼음,번개)',
    '다음 중 레지스탕스에 속하는 직업은?': '카이저	    엔젤릭버스터  	비숍	@데몬어벤져@',
    '다음 중 레지스탕스에 속하는 직업은?.': '히어로    	나이트로드	나이트워커	@제논@',
    '다음 중 시그너스에 속하는 직업은?': '배틀메이지	@플레임 위저드@	팬텀	루미너스',
    '다음 중 시그너스에 속하는 직업은?.': '엔젤릭 버스터	@나이트워커@	아란	데몬슬레이어',
    '다음 중 더 시드에 등장하지 않는 몬스터는?': '@무루파@	갈색 가시 곰	샐리온	붉은 모래 난쟁이',
    '다음 중 더 시드에 등장하지 않는 몬스터는?.': '그린 플라워 카우	그류핀	벨라모아	@룰랑@',
    '다음 중 더 시드에 등장하지 않는 몬스터는?..': '@고대 붉은 거북@	크로크	엘리쟈	파랑 식충 슬라임',
    '다음 중 더 시드에 등장하지 않는 몬스터는?...': '와일드카고	리게이터	@고대 식충 슬라임@	프릴드',
    '다음 중 더 시드에 등장하지 않는 몬스터는?....': '블루 플라워 카우	노랑 버섯 박쥐	@블루 고대 풍뎅이@	고대 주황 거북',
    '다음 중 더 시드에 등장하지 않는 몬스터는?.....': '고대 파랑 거북	@옐로 플라워 카우@	헥터	노랑 식충 슬라임',
    '다음 중 더 시드에 등장하지 않는 몬스터는?......': '고대 주황 거북	@검은 가시 곰@	화이트팽	벨라모아',
    '다음 중 더 시드에 등장하지 않는 몬스터는?.......': '플라워 골렘	클랑	@푸른 버섯 박쥐@	흰 가시 곰',
    '다음 중 더 시드에 등장하지 않는 몬스터는?........': '흰 가시 곰	라이오너	프릴드	@크로거다일@',
    '다음 중 더 시드에 등장하지 않는 몬스터는?.........': '검은 플라워 골렘	로랑	@고대 버섯 박쥐@	고대 파랑 거북',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는?.': '락 스피릿   	@디아블로우@	    벨룸	신수',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는?..': '듀나스	드래곤 라이더	@이뮤르크@	피에르',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는?...': '아우프헤벤	렉스	이리나	@베어구릴수@',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는?....': '니벨룽겐 전함	@벨제붑@	이카르트	드래고니카',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는?': '@보티첼리@	반반	아니	매그너스',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는.?.': '반반	@샤모스@	아카이럼	    호크아이 ',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는.?..': '에피네아	@샤모스@	아카이럼	    호크아이',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는.?...': '@칼리쉬@	마왕 발록	샤크아이	오즈',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는.?....': '크세르크세스	라바나	@반 베놈@	여제 시그너스',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는?.....': '베르가모트	@코커트리스@	반레온	힐라',
    '다음 중 메이플 스토리에 등장한 적 없는 보스 몬스터는?......': '@빅브라더@	드래고니카	강화형 포이즌 골렘	블러드퀸',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?': '쥬니퍼베리 꽃	다이아몬드의 원석	@쓰다만 거푸집@	체력 회복 포션',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?.': '카모마일 꽃	리튬의 원석	힘의 물약	@니켈@',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?..': '크탈리에시지	@매그너스의 땀방울@	하급 연마제	오리할콘',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?...': '@사랑이 담긴 초콜릿@	빛자랜 은의 원석	은	마조람 꽃 오일',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?....': '허브 오일병	@할미꽃 씨앗@	동물의 가죽	무루무루의 털뭉치',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?.....': '티트리 씨앗	미스릴의 원석	사파이어	@페니실린@',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?......': '히솝 꽃	중급 거푸짓	@페어리 샌드@	마법의 가루',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?.......': '쟈스민 씨앗	@크립토나이트 원석@	강철	죽은자의 부적',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?........': '@자쿰의 눈물@	자수정의 원석	오팔	마력의 물약',
    '다음 중 메이플 스토리에 존재하는 제작 재료가 아닌 것은?.........': '페츌리 꽃	지혜의 크리스탈 원석	포션 응고제	@히야신스 주스@',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?': '@슈기의 요리모자@	블루얼 페긴트	혼테일의 목걸이	스컹크의 방독면',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?.': '하프 이어링	헬리시움 도적 벨트	혼돈의 포션	@필사의 머리삔@',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?..': '자일즈의 망토	엔젤릭 블레스	@슈가의 조그만 지팡이@	퍼플 카스트 린넨',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?...': '그린 골드 벨트	샤크투스 플람	빨간색 세라프의 망토	@솔로의 저주가 담긴 커플링@',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?....': '제이드 해츨링	@미노타우로스 코뚜레@	불멸의 파라오의 벨트	장미꽃 귀고리',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?.....': '디펜스의 달인	@연금술사의 수제장갑@	블랙 바실즈 부츠	자쿰의 투구',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?......': '레드 바이퍼	봄버드 센터 파이어	화이트 피니얼	@베놈 바이퍼@',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?.......': '@불사조의 꼬리깃털@	디멘션 글러브	금이 간 안경	러브리스 피오니',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?........': '카오스 핑크빈 모자	@얼티밋 하프 헬름@	콘체르토	더키의 스노클',
    '다음 중 메이플 스토리에 존재하지 않는 아이템은?.........': '템페스트 견장	얼티밋 링	@은총받은 선글라스@	브라운 더블드 부츠',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?': '핑크 물개쿠션  	@말년 병장 의자@  	데비존 의자	    전치 10주 의자',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?.': '뱀부 체어	홍상묘 월묘 방석	소울테니 의자	@다이아몬드 욕조@',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?..': '@내게 돌아와 의자@	찰떡 아이스	꿈 해몽 의자	길드 의자',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?...': '여우비 의자	감나무 그네	곰돌이 침대	@레피의 감나무 의자@',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?....': '단풍나무 아래서	트로피컬 썸머 체어	드래곤의 알	@첫사랑의 순정 의자@',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?.....': '나무 욕조	레드 디자인체어	@휠체어@	와글친구 의자',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?......': '릴렉스 체어	@맘모스 의자@	힐라의 겟잇뷰티	야영 모닥불 의자',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?.......': '사랑의 의자	핑크 비치파라솔	@발렌타인의 저주 의자@	꿈꾸는 화가 의자',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?........': '@3월 토끼 의자@	달님별님 쿠션	시추시계 의자	러브 체어',
    '다음 중 메이플 스토리에 존재하지 않는 의자는?.........': '노블레스 의자	튼튼한 나무의자	토끼 의자	@돈방석@',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?': '벨더	피아	@디제이쿠@	돌고래',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?.': '탈리온	제크	듀이	@스티치@',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?..': '@아구몽@	헤르샤	이카루스	프레드릭',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?...': '@찰즈@	    레아	베티	마티어스',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?....': '셀렌	@재클린@	박서방	몽땅따',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?.....': '벼루	@카르노@	마틸다	골드리치',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?......': '@헤이즈@	카산드라	쉐인	레아',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?.......': '장로 스탄	클라라	@카이조@	레아',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?........': '큐트	네벨	@자이언트조@	스크루지',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?.........': '아이린	네벨	@자이언트조@	스크루지',
    '다음 중 메이플스토리에 거주하는 주민의 이름이 아닌 것은?..........': '펜릴	@세빌@	클리앙	넬라',
    '다음 중 메이플스토리에 존재하지 않는 도시는?': '에레브	슬리피우드	@크레아티스@	커닝시티',
    '다음 중 메이플스토리에 존재하지 않는 도시는?.': '커닝시티	@백조마을@	페리온	리프레',
    '다음 중 메이플스토리에 존재하지 않는 도시는?..': '@사라세니아@	마가티아	노틸러스	아리안트',
    '다음 중 메이플스토리에 존재하지 않는 도시는?...': '페리온	무릉	@프랑켄슈타인@	에우렐',
    '다음 중 메이플스토리에 존재하지 않는 도시는?....': '헤네시스 집	@판교@	커닝시티	백초마을',
    '다음 중 메이플스토리에 존재하지 않는 도시는?.....': '리스항구	오르비스	백초마을	@아쿠아아쿠아@',
    '다음 중 메이플스토리에 존재하지 않는 도시는?......': '@여섯갈래길@	엘나스	에델슈타인	아리안트',
    '다음 중 메이플스토리에 존재하지 않는 도시는?.......': '@슬리핑포레스트@	리엔 온천	에델슈타인	아리안트',
    '다음 중 메이플스토리에 존재하지 않는 도시는?........': '@엘리니브@	에델슈타인	크리티아스	리스항구',
    '다음 중 메이플스토리에 존재하지 않는 도시는?.........': '오르비스	아쿠아리움	@컨닝시티@	엘리니아',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?.': '서전아이	@다우니@	로얄 카투스	버블피쉬',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?..': '스톤골렘	추억의 신관	@레드 페퍼즈@	뉴트 주니어',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?...': '파란버섯	플라워 피쉬	큐브 슬라임	@슬레지 햄머@',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?....': '와일드보어	베라가모트	주니어 씰	@탑승형 골렘@',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?.....': '스톤마스크	레드 와이번	@베르투스@	샐리온',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?......': '주니어 레이스	@쏠라리온@	레드 드레이크	호걸',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?.......': '@펜릴@	핑크테니	페페	블록퍼스',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?........': '스켈독	다크 코니언	    벨라모아	    @샤프란@',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?.........': '달팽이	@다크 케투스@	로보토이	고급 앰프',
    '다음 중 메이플스토리에 존재하지 않는 몬스터는?..........': '옥토퍼스	팬텀워치	    @코르비@	씨클',
    '다음 중 메이플스토리에 존재하지 않는 직업은?.': '데몬 슬레이어	신궁	@트레져헌터@	    나이트로드',
    '다음 중 메이플스토리에 존재하지 않는 직업은?..': '아크(썬콜)	메르세데스	@아트디자이너@	듀얼블레이드',
    '다음 중 메이플스토리에 존재하지 않는 직업은?...': '팔라딘	에반	나이트워커	@윈드러너@',
    '다음 중 메이플스토리에 존재하지 않는 직업은?....': '@데몬헌터@	보우마스터	듀얼블레이드	스트라이커',
    '다음 중 메이플스토리에 존재하지 않는 직업은?.....': '히어로	플레임위자드	@댄스마스터@	소울마스터',
    '다음 중 메이플스토리에 존재하지 않는 직업은?......': '미하일	윈드브레이커	바이퍼	@미사일@',
    '다음 중 메이플스토리에 존재하지 않는 직업은?.......': '다크나이트	배틀메이지	@캐논펀쳐@	아란',
    '다음 중 메이플스토리에 존재하지 않는 직업은?........': '비숍	나이트로드	섀도어	@던전마스터@',
    '다음 중 메이플스토리에 존재하지 않는 직업은?.........': '아크(불독)	와일드헌터	캡틴	@네크로맨서@',
    '다음 중 메이플스토리에 존재하지 않는 직업은?..........': '@섀도우 마스터@	메카닉	팬텀	데몬어벤져',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은?': '탱글탱글 포도농장	리엔 온천	@천연 황토 집@	에레브 분수정원',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은?.': '초가집	핑크 엔젤 하우스	@메이플 워터 파크@	리엔 이글루',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은?..': '주주 우유농장	플로팅 캐슬	@초밥 전문점@	오르비스 비행정원',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은.?.': '헤네시스 집	@양식장@	깜짝상자집	클락 하우스',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은.?..': '나무꾼의 집	아리안트 집	에델슈타인 비행장	@메이플 수상 가옥@',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은?...': '@동굴 집@	해산물 식당	에우렐 집	피아노',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은?....': '초록 버섯집	@검은 토끼 농장@	무기상점	산타의 집',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은?.....': '@판테온 신전@	오아시스	핑크 엔젤 하우스	노틸러스호 선착장',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은?......': '@아지트@	쿠키 하우스	붉은 버섯집	우동집',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은..?.': '비숍	나이트로드	섀도어	@던전마스터@',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은...?.': '@검은 집@	과일상점	판테온 집	2층 새둥지 집',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은....?.': '놀이공원 바이킹	깜짝상자집 풍선	깜짝상자집	@샤모스 창고@',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은.....?.': '@생츄어리@	노랑 잠수함	비화원	아모리아 콘서트홀',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은......?.': '빨간 벽돌집	버섯왕국 초소	서커스장	@과수원@',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은?........': '천연 빙하집	@클럽 헤네시스@	에우렐 집	루디브리엄 장난감집',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은.?.....': '10주년 이벤트홀	무릉 이발소	@아쿠아쿠리움 수족관@	아쿠아로드 저택',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은.?...': '주황 버섯집	블로섬 하우스	@퓨리엘 집@	무릉 수련장',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은.?....': '헤네시스 궁수길드	유령의 집	우동집	@여제의 기도원@',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은.?......': '@버섯버섯 광산@	파랑 3단 버섯집	풍차	크리스탈 가든',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은..?..': '아쿠아로드 소라집	@사이킥 오디션 홀@	아리안트 집	신수의 둥지',
    '다음 중 몬스터 라이프에 등장하는 건물이 아닌 것은..?...': '한옥집	24시간 병원	@지하 수련장@	자쿰의 동굴',
    '다음 중 소비 아이템이 아닌 것은?': '@마법사의 가루약@	빨간 포션	재물 획득의 비약	새벽의 이슬',
    '다음 중 소비 아이템이 아닌 것은?.': '써니텐 엘릭서	크로스헌터 마력 포션	@갑오년 각성의 비약@	무지개 별 물약',
    '다음 중 소비 아이템이 아닌 것은?...': '@벅카스D@	주황포션	경험 축적의 비약	달걀',
    '다음 중 소비 아이템이 아닌 것은?....': '파란포션	@미지근한 주스@	각성의 비약	전설의 체력 비약',
    '다음 중 소비 아이템이 아닌 것은?.....': '하얀포션	@요정의 이슬@	무적의 비약	집중의 비약',
    '다음 중 소비 아이템이 아닌 것은?......': '스페셜 D 포션	마나 엘릭서 알약	@훈제 연어@	파란별 물약',
    '다음 중 소비 아이템이 아닌 것은?.......': '엔젤의 발걸음	밸류 포션	스페셜 체력 회복 물약	@파티용 치즈@',
    '다음 중 소비 아이템이 아닌 것은?........': '살살 녹는 치즈	행운의 알약	발굴한 축복의 비약	@보라빛 물약@',
    '다음 중 소비 아이템이 아닌 것은?.........': '속도 향상의 알약	엘릭서	@자쿰의 숨결@	인내의 비약',
    '다음 중 소비 아이템이 아닌 것은?..........': '통증 완화제	빨간 포션 알약	@갑오년 인내의 비약@	자이언트 비약',
    '다음 중 한 손 무기가 아닌 것은?': '카오스 호크 헤드	레볼루션 소드	@특제 삼지창@	발렌티어',
    '다음 중 한 손 무기가 아닌 것은?.': '메이플 우산	스파타	@문 글로리@	이터널 원터러',
    '다음 중 한 손 무기가 아닌 것은?..': '케이그	@나무망치@	광선 채찍	플레인 알파',
    '다음 중 한 손 무기가 아닌 것은?...': '양날 도끼	행복 화이트 소드	@선구자의 듀얼윙@	딤 메모리',
    '다음 중 한 손 무기가 아닌 것은?....': '@선구자의 모울@	용기의 날개	레전드 프라우테	바이킹 소드',
    '다음 중 한 손 무기가 아닌 것은?.....': '아츠	레드 카타나	일룬	@그륜힐@',
    '다음 중 한 손 무기가 아닌 것은?......': '@호프만@	미하일	카오스 프라우테	플레인',
    '다음 중 한 손 무기가 아닌 것은?.......': '러브리스 엑서큐서너스	레전드 메이플 브링어	검	@호검@',
    '다음 중 한 손 무기가 아닌 것은?........': '특제 파이어잭	@용맹의 날개@	마녀의 빗자루	골드샤인 베타',
    '다음 중 한 손 무기가 아닌 것은?.........': '메이플 1500일 깃발	초승달 블레이드	@에오로@	어비스 그림시커',
    '다음 중 핸드캐논이 아닌 것은?': '헬 크래쉬	발록의 라이노	@저주의 블랙 캐논@	카오스 플라멘 베르퍼',
    '다음 중 핸드캐논이 아닌 것은?.': '헬 크래쉬	카오스 플라멘 베르퍼	@아트룰루@	크뤼 소스',
    '다음 중 핸드캐논이 아닌 것은?..': '파프니르 러스터 캐논	요정의 포로스티 라이노	템페스트 크래쉬	@블러리 캐논@',
    '다음 중 핸드캐논이 아닌 것은?...': '@벅카스D@	드레드넛	아트럴리	코라 반 레온 시즈건',
    '다음 중 핸드캐논이 아닌 것은?....': '레인지 로버	발록의 라이노	@헐거운 장난감 캐논@	샤크투스 플람',
    '다음 중 핸드캐논이 아닌 것은?.....': '행복 화이트 캐논	@블링블링 아이언 캐논@	마이스터 크래쉬	스칼렛 크래쉬',
    '다음 중 핸드캐논이 아닌 것은?......': '노비스 캐논	@네크로 베릴 캐논@	아이언 봄버	슈타일 봄버',
    '다음 중 핸드캐논이 아닌 것은?.......': '@봄봄 크래쉬@	네크로 이그니스	레드 캐논	피어리스 셀베이션',
    '다음 중 핸드캐논이 아닌 것은?........': '임페리얼 이그니스	얼티밋 크래쉬	브로드 헬크래쉬	@특제 이그나이트 크래시@',
    '다음 중 핸드캐논이 아닌 것은?.........': '드래곤 헤르츠	메이플 베릴 캐논	@드래고닉 라이노@	크뤼 소스',
    '루디브리엄의 창고지기 이름은?': '로도스	푸로	스우	@세피@',
    '루디브리엄의 친구목록 관리자 이름은?': '골드리치	프델라	@할리@	크루소',
    '리스항구의 친구목록 관리자 이름은?': '무라트	자아	마녀 바바라	@몽롱 할배@',
    '리에나 해협 빙하관측 본부의 조타수 이름은?': '탕윤	푸가	요정 파이니	@조타수 따냐@',
    '리엔의 창고지기 이름은?': '@푸슬라@	벼루	슈미	리나',
    '마가티아에 거주하는 브로커 이름은?': '브로커 정	@브로커 한@	브로커 홍	토리',
    '마가티아에 거주하는 휴머노이드의 이름은?': '페일	@휴머노이드 A@	휴머노이드 B	휴머노이드 C',
    '백초마을의 워프도우미 이름은?': '@학@	백로	두루미	닭',
    '슬리피우드 호텔 입구에 선 아이템 제작자는?': '@크리슈라마@	탈리온	몽땅따	돌고래',
    '아리안트의 무기 상인 이름은?': '@자이드@	아이린	레아	오심마',
    '아리안트의 성형외과 의사 이름은?': '슈미	@알딘@	스크루지	헬레나',
    '아리안트의 피부관리사 이름은?': '@라일라@	네벨	골드리치	큐트',
    '에델슈타인의 곰돌이 알바 이름은?': '천지	키루	@체키@	비어완',
    '에델슈타인의 전 의회장 이름은?': '그윈	카이린	@알베르트@	라니아',
    '에델슈타인의 현 의회장 이름은?': '슈미	아벨	@안소니@	에스텔',
    '에델슈타인의 환경 미화원 이름은?': '라엘	키리두	@헨리테@	이토스',
    '엘리니아의 펫 마스터 이름은?': '@요정 마르@	장로 스탄	요정 플로라	일스',
    '오르비스 차원의 거울 오른쪽에 앉아있는 개 이름은?': '뮤네	@봉달이@	불독	도베르만',
    '전사의 성전에 거주하는 전직관은?': '마파	@주먹펴고 일어서@	하인즈	소피아',
    '커닝시티에 거주하는 아이템 제작자 이름은?': '제피	@뒷골목의 제이엠@	스미스	지미',
    '커닝시티의 지하철 공익요원 이름은?': '알렉스	@웅이@	이얀	루이스',
    '판테온에 거주하는 상인 꿈나무 이름은?': '캘리코	푸츠키	요정 우니	@카린@',
    '판테온의 대신전 앞을 지키고 있는 할머니 이름은?': '@셀렌@    	올리비아    	넬라	체프',
    '페리온의 무기 상인 이름은?': '마이크	@리버@	카밀라	유타',
    '황금 사원 입구에 서 있는 꼬마 승려의 이름은?': '토푸	듀나미스    	@노이@	디테',
    '황금사원의 잡화 상인 이름은?': '케리	    키무	@탕따완@	다니카'
}

block = ['누구', '대사', '스킬', '은월', '팔라딘', '제로', '더시드', '다음', '메이플', '몬스터', '제작', '재료', '존재', '거주', '주민', '이름',
         '도시', '직업', '라이프', '건물', '등장', '소비', '한손무기', '핸드캐논', '라이', '비약', '토리']


@client.event
async def on_ready():
    print(client.user.id)
    print('ready')


@client.event
async def on_message(message):
    if message.content == '안녕':
        await message.channel.send('안녕하세요 !!!!!')

    if message.content == '안뇽':
        await message.channel.send('반가워요!!!!!!!!!!!')

    if message.content.startswith('하이'):
        await message.channel.send('ㅎㅇㅎㅇ')

    if message.content == '반가워' or message.content == '방가워':
        await message.channel.send('제가 더 반가워요 !!')

    if message.content == '야':
        await message.channel.send('네 주인님')

    if message.content == '노예야':
        await message.channel.send('네 주인님')

    if message.content == '아니 너 말고':
        await message.channel.send('네 ㅈㅅ여')

    if message.content == '혼자야':
        await message.channel.send('어 아직 싱글이야')

    if message.content == '사랑해':
        await message.channel.send('저두요')

    if message.content.startswith('죽고싶냐'):
        await message.channel.send('죄송해여ㅠㅠ')

    if message.content.startswith('고마워'):
        await message.channel.send('별말씀을 ㅎㅎ')

    if message.content.startswith('귀엽다'):
        await message.channel.send('감사합니다 ㅎㅎ')

    if message.content.startswith('귀엽네'):
        await message.channel.send('감사합니다 ㅎㅎ')

    if message.content.startswith('귀여워'):
        await message.channel.send('감사합니다 ㅎㅎ')

    if message.content == '흑흑':
        await message.channel.send('울지마 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ')

    if message.content.startswith('ㅠㅠ'):
        await message.channel.send('울지마 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ')

    if '바보' in message.content:
        await message.channel.send('바~보래요')

    if '멍청' in message.content:
        await message.channel.send('댕~청')

    if '시발' in message.content:
        await message.channel.send('왜 욕해 ㅠㅠ 욕하지마 !!!!!!')

    if 'ㅅㅂ' in message.content:
        await message.channel.send('요카지마라 !!!!')

    if '새끼' in message.content:
        await message.channel.send('욕하지마 !!!!!')

    if message.content == '혼난다':
        await message.channel.send('죄송해여 ㅠㅠ')

    if message.content == '혼날래':
        await message.channel.send('죄송해여 ㅠㅠ')

    if message.content == '맞짱':
        await message.channel.send('맞짱은 제 주인님 이름이예요 ㅎㅎ')

    if message.content == '윤호승':
        await message.channel.send('제 주인님 이랍니다 ㅎㅎ')

    if message.content == '배고파':
        await message.channel.send('꼬르륵............')

    if '배고프' in message.content:
        await message.channel.send('꼬르륵............')

    if '짜증나' in message.content:
        await message.channel.send("왜 짜증내 !!!! 짜증내지마!!")

    if '자증나' in message.content:
        await message.channel.send("자증내지마 !!!!")

    if message.content == '잘자':
        await message.channel.send('너두 잘자 !!!!')

    if '굿나잇' in message.content:
        await message.channel.send('굿밤 !!!!')

    if message.content == '헉헉':
        await message.channel.send('헉헉대지마 !!!!!!!!!!')

    if '신기해' in message.content:
        await message.channel.send('신기하죠 !!!!!')

    if '싱기해' in message.content:
        await message.channel.send('신기하죠 !!!!!')

    if '신기하다' in message.content:
        await message.channel.send('신기하죠 !!!!!')

    if message.content == '박해빈':
        await message.channel.send('박해빈 밥오')

    if message.content == '해빈아':
        await message.channel.send('야 해빈아!!!!!!!!!!!!!! 누가 니 부른다 !!!!!!!')

    if message.content == '혜빵댕이':
        await message.channel.send('빵댕')

    # calling keyword
    if message.content.startswith('!'):
        keyword = message.content[1:].strip()
        if keyword == '':
            embed = discord.Embed(title='도움말을 보시려면 !help 를 입력해주세요 !!!!', color=0x00ff00)
            await message.channel.send(embed=embed)
        # !help Command
        elif keyword.lower() == 'help':
            embed = discord.Embed(title='!(느낌표) 와 검색하고자 하는 키워드를 입력해 보세요 ',
                                  description='39층에 나오는 어떤 문장이든 검색하면 제가 찾아준답니다',
                                  color=0xff00ff)
            embed.set_footer(text='숨겨진 메시지도 있으니 한 번 찾아보세요')
            await message.channel.send(embed=embed)

        # if user send '!'
        elif keyword == '':
            embed = discord.Embed(title='도움말을 보시려면 !help 를 입력해주세요 !!!!', color=0x00ff00)
            await message.channel.send(embed=embed)

        # too many results

        elif len(keyword) == 1:
            embed = discord.Embed(title='검색어를 두 글자 이상 입력해 주세요 ㅠㅠ 찾기 힘들어요 ㅠㅠ', color=0xff69B4)
            await message.channel.send(embed=embed)

        elif keyword in block:
            embed = discord.Embed(title='검색 결과가 너무 많아요ㅠㅠ 다른 단어로 검색해주실래요 ㅎㅎ?', color=0xff69B4)
            await message.channel.send(embed=embed)

        else:
            embed = discord.Embed(title=keyword + '이(가) 들어간 문제를 찾고있어요', description='@@ 사이에 있는 단어가 정답이예요',
                                  color=0xffff00)
            await message.channel.send(embed=embed)
            for key, val in Question.items():
                if keyword in key:
                    embed = discord.Embed(title=key, description=Question[key], color=0xff0000)
                    await message.channel.send(embed=embed)
                    # await message.channel.send('----------------------------------------------')
                if keyword in val:
                    # await message.channel.send('----------------------------------------------')
                    embed = discord.Embed(title=key, description=val, color=0x0000ff)
                    await message.channel.send(embed=embed)
            # await message.channel.send('-------------------------------------------------------------')
            embed = discord.Embed(title='검색 완료 !!!!!!', color=0x00ff00)
            await message.channel.send(embed=embed)


token = os.environ["BOT_TOKEN"]

client.run(token)
