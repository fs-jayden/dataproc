# 📦 dataproc

날짜 문자열 전처리 및 마이크로초(microseconds) 단위의 유닉스 타임스탬프 변환을 위한 파이썬 패키지입니다.

---

## 🚀 설치 방법

### 1. 사용자용 (일반 설치)
패키지를 자신의 프로젝트에 가져다 쓰고 싶은 사용자는 아래 명령어를 사용하세요.
```bash
pip install dataproc


### 2. 개발자용 
# 1. 저장소 복제
git clone [https://github.com/SSAFY/dataproc.git](https://github.com/SSAFY/dataproc.git)
cd dataproc

# 2. 개발 의존성(pytest, sphinx 등)을 포함하여 설치
pipenv install --dev
```

### 3. 사용 예시
```python
from dataproc import str_to_datetime, str_to_unixtime

# 1. 문자열을 datetime 객체로 변환
# 지원 형식: ISO 8601 (예: 2026-05-06T11:30:12), %d/%m/%y %H:%M:%S 등
dt = str_to_datetime("2024-05-01 10:30:00")
print(f"Datetime: {dt}")

# 2. 문자열을 마이크로초 단위 유닉스 타임스탬프로 변환
# 결과값은 정밀한 계산을 위해 numpy.int64 타입으로 반환됩니다.
unix_time = str_to_unixtime("2024-05-01 10:30:00")
print(f"Unix Timestamp: {unix_time}")
```

### 4. 프로젝트 구조
```text
dataproc/
├── docs/                # Sphinx 문서 설정 및 리소스
├── src/
│   └── dataproc/        # 실제 패키지 소스 코드
│       ├── __init__.py  # Public API 노출
│       └── transform.py # 날짜 변환 로직
├── tests/               # 단위 테스트 코드
├── Pipfile              # 의존성 관리 (Pipenv)
├── Pipfile.lock         # 의존성 스냅샷
├── pyproject.toml       # 빌드 및 배포 설정
└── README.md            # 프로젝트 가이드
```
### 5. 개발 노트
### 1. 의존성 관리 방식 (Dependency Management)
본 프로젝트는 사용자의 설치 유연성과 개발 환경의 재현성을 위해 두 가지 설정 파일을 전략적으로 분리하여 사용합니다.

* **`pyproject.toml` (Dependency Specifier)**
    * **목적**: 사용자에게 보내는 **"호환성 약속"**입니다.
    * **특징**: `pandas>=2.0,<3.0`과 같이 라이브러리의 버전 범위를 지정합니다. 이는 사용자가 자신의 환경에 맞춰 유연하게 패키지를 설치할 수 있게 도와주며, 버전 충돌을 방지합니다.
* **`Pipfile.lock` (Lock File)**
    * **목적**: 개발자가 사용하는 **"비트 단위 환경 스냅샷"**입니다.
    * **특징**: 특정 시점에 테스트를 통과한 라이브러리의 정확한 버전과 해시(Hash)를 기록합니다. 어느 컴퓨터에서든 `pipenv install`을 통해 100% 동일한 개발/테스트 환경을 재현합니다.

---

### 2. 버전 정책 (Semantic Versioning)
이 프로젝트는 **[Semantic Versioning 2.0.0](https://semver.org/lang/ko/)** 규약을 준수하며, `setuptools-scm`을 활용하여 Git Tag 기반으로 버전을 자동 관리합니다.

버전 번호는 **MAJOR.MINOR.PATCH** 형식을 따릅니다:
1.  **MAJOR**: 기존 기능과 호환되지 않는 중대한 API 변경이 있을 때 올립니다.
2.  **MINOR**: 하위 호환성을 유지하면서 새로운 기능을 추가했을 때 올립니다.
3.  **PATCH**: 하위 호환성을 유지하면서 단순한 버그를 수정했을 때 올립니다.

---

### 3. API 문서화 및 테스트
- **문서화**: 소스 코드 내의 Docstring(NumPy 스타일)을 바탕으로 **Sphinx**가 자동으로 API Reference를 생성합니다.
- **테스트**: **Pytest**를 통해 로직의 정확성을 검증하며, 특히 타임존(UTC/KST) 이슈가 발생하지 않도록 엄격하게 관리합니다.