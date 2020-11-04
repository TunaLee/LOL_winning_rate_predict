## csv 파일
### high_diamond_ranked_10min.csv
- kaggle League of Legends Diamond Ranked Games (10 min) 데이터셋 원본 데이터
- [참조](https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min)

## Pickle 파일

각 데이터 - python pickle 형식의 데이터로 처리했습니다.

### champion_id_and_name_list.pickle 
저장된 데이터 - 딕셔너리 하나
키 - champion ID
값 - 키값에 해당하는 챔피언의 영문 이름

### participant_data.pickle
저장된 데이터 - (랭크게임, 일반게임, 자유랭크게임) 클래식모드 게임 중 플레이어 정보 저장, 딕셔너리 모은 리스트 형태로 저장
참조 : https://www.kaggle.com/gyejr95/league-of-legendslol-ranked-games-2020-ver1
리스트 데이터 : 919200
각 원소 - 딕셔너리 형태
예시 : {'gameId': 3508539941, 'summonerName': 'Isla', 'championId': 3, 'teamId': 100, 'role': 'SOLO', 'lane': 'MIDDLE', 'win': False}
설명 
- gameId - Riot에서 정한 게임 Id
- summonerName - 플레이어 이름
- championId - 플레이어가 사용한 챔피언의 id번호
- teamid - 100이면 블루, 200이면 레드
- role - 'SOLO', 'DUO_AD', 'DUO_SUPPORT', 'NONE'(정글러)
- lane - 'TOP', 'MIDDLE', 'BOTTOM', 'JUNGLE' 중 하나.
- win - 게임 승패여부. 

### match_data_version.pickle
- 원본 데이터 
- [참조](https://www.kaggle.com/gyejr95/league-of-legendslol-ranked-games-2020-ver1) 

### raw_match_data.pickle
- 3번 파일에서 클래식 랭겜, 맵버전 13번, 일부 컬럼 소거해서 만든 91920개의 게임 데이터

### valid_user_data.pickle
- participant_data.pickle에서 중복하지 않은 닉네임 약 13만개 정도 추출한 리스트.

### df_keras_winloss.pickle
- Tensorflow keras를 이용해서 승패예측을 위한 학습용 데이터 입력.

## ipynb 파일

### LOL Regression_test.ipynb
- kaggle League of Legends Diamond Ranked Games (10 min) 데이터셋 원본 데이터를 머신러닝 알고리즘을 이용해 승패예측 실험
- LOL Regression_test.html에 데이터 결과 확인 가능.

### LOL 승패예측모델.ipynb
- raw_match_data.pickle의 게임 데이터를 추출함
- 또한 raw_match_data의 participant 컬럼의 오브젝트를 해체해서 요소를 뽑은 뒤 일부 컬럼들을 제거하고 530개의 요소와 91920 매칭 데이터를 이용해 실험
- TensorFlow keras 이용해서 승패예측
- keras 모델은 LOL_win_loss_predict.h5에 저장
- 줄인 Pandas 데이터프레임은 df_keras_winloss.pickle에 저장
- 학습:테스트 9:1로 테스트 결과 적중률 100%까지도 달성했음.

### ToyModel.ipynb
포지션 5개, 각 포지션별로 6명씩 모두 30명의 가상 챔피언을 정규분포를 이용한 난수를 이용해 1억개의 가상 매칭 데이터 생성
생성 후 LinearRegression과 실제 승률을 비교해 LinearRegression을 사용할 수 있는지 검증하는 시험 모델
(1억개 매칭데이터는 용량이 매우 커져서 pickle 파일은 미첨부)

  