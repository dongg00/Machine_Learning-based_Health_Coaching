# 피지컬:로그 (Physical:Log) – 유사군 비교 기반 점진 코칭 & 게이미피케이션 헬스케어 플랫폼  

<p align="center">
  <img src="Images/찐막_로고.png" alt="Physical:Log Banner" width="150"/>
</p>

**피지컬:로그(Physical:Log)** 는 건강에 관심은 있지만 행동 실천율이 낮은 사용자를 위해  
**유사군 비교 코칭**, **건강 점수화**, **게이미피케이션 보상**을 활용하여  
지속 가능한 건강 행동 변화를 유도하는 **디지털 헬스케어 솔루션**입니다.  
***

## 기술 스택

| 구분          | 사용 기술 |
|---------------|-----------|
| **언어**       | Python |
| **데이터 처리/분석** | pandas, numpy |
| **머신러닝/모델링** | scikit-learn (Classification/Clustering, HistGradientBoostingClassifier), imbalanced-learn (SMOTE) |
| **데이터베이스** | MariaDB (PyMySQL 연동) |
| **시각화/리포트** | matplotlib|

| 구분          | 사용 기술 |
|---------------|-----------|
| 언어          | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| 데이터 처리/분석 | ![pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white) ![numpy](https://img.shields.io/badge/numpy-013243?style=flat&logo=numpy&logoColor=white) |
| 머신러닝/모델링 | ![scikit-learn](https://img.shields.io/badge/scikit--learn-FF6F00?style=flat&logo=scikitlearn&logoColor=white) ![imbalanced-learn](https://img.shields.io/badge/imbalanced--learn-FF6600?style=flat) ![Model](https://img.shields.io/badge/Model-HistGradientBoosting-orange) ![Model](https://img.shields.io/badge/Model-Clustering-blueviolet) |
| 데이터베이스   | ![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat&logo=mariadb&logoColor=white) ![PyMySQL](https://img.shields.io/badge/PyMySQL-4479A1?style=flat&logo=mysql&logoColor=white) |
| 시각화/리포트  | ![matplotlib](https://img.shields.io/badge/matplotlib-11557C?style=flat) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) |

***

## 시스템 아키텍처

![아키텍처](images/physical_log_architecture.png)
***

## 주요 기능

### 1. 건강 점수 산출
> 국민건강영양조사(KNHANES) 기반 질병 지표(고혈압, 당뇨, 비만 등) 분석  
> **사용자 건강 점수 + 캐릭터 시각화** 제공  

---

### 2. 유사군 비교 코칭
> 나와 동일한 질병 단계 중, 나보다 조금 더 건강한 생활습관을 가진 그룹을 찾아  
> **점진적 맞춤형 코칭 가이드** 제공  

---

### 3. 생활습관 리포트 생성
> 걷기, 식습관, 음주·흡연 데이터를 분석해  
> **개인별 건강 리포트 및 개선 피드백** 제공  

---

### 4. 게이미피케이션 & 인센티브
> 건강 점수 변화에 따라 **캐릭터 진화**  
> 실천률 70% 이상 → 굿즈 리워드 제공 (예: 캐릭터 커스터마이징 수저세트)  

---

### 5. 조직 단위 확장
> 개인 비교에서 확장 → **조직 단위 배틀 & 건강 리포트** 제공  
> 기업 복지팀·지자체 건강증진 사업 연계 가능  
***

## 핵심 기여
- **데이터 처리**: 국민건강영양조사(KNHANES) 기반 질병 데이터 전처리 및 EDA 수행  
- **모델 개발**: 분류/군집 모델 설계 및 고위험군 예측 알고리즘 개발  
- **UX 기여**: 건강 점수·캐릭터 시각화 및 리포트 자동화 파이프라인 구축  
- **시스템 통합**: 데이터 분석 → 리포트 생성 → 보상 시스템까지 End-to-End 워크플로우 설계  
***

## 폴더 구조 (예시)
<pre>
📂 PhysicalLog/
 ┣ 📜 app.py              # Streamlit 메인 실행 파일
 ┣ 📜 model.py            # 질병 분류/군집 모델 정의
 ┣ 📜 data_preprocess.py  # KNHANES 데이터 전처리 모듈
 ┣ 📜 report.py           # 개인/조직 리포트 생성 모듈
 ┣ 📂 images/             # 아키텍처/결과 캡처 이미지
 ┣ 📜 requirements.txt    # 실행 환경 의존성
 ┣ 📜 README.md           # 프로젝트 설명 문서
</pre>
***
