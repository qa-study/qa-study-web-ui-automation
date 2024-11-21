# qa-study-ui-automation
## Introduce
- 네이버 웹 애플리케이션 자동화 스터디를 위한 협업 프로젝트 Repository입니다.
- 네이버 각 페이지에 대한 자동화 테스트 케이스를 구성하고, 이를 자동화 케이스로 구현할 수 있는 `경험`, `코드 리뷰`, `개발 능력` Upgrade를 목적으로 합니다.
- 자동화 케이스로 구현하기 전 상호간의 `TC Review` 시간을 가지고, 어떻게 구현할 것인지 논의를 진행한 다음 `Pull Request`를 통해 기여할 수 있도록 합니다.

## Tools
- Language : `Python` 3.12.x
- A/T Framework : `Selenium`
- Test Framework : `Pytest`
- HTML Report : `Allure`

## Pre-Condition
- 본격적인 자동화 테스트 프로젝트 수행 전, 기본적으로 설치되어 있어야 하는 모듈이 있습니다.
- Mac의 경우 `homebrew` 를 이용해 `brew install allure` 명령어로 라이브러리 설치가 먼저 필요합니다.
- Window의 경우 `scoop` 을 이용해 `scoop install allure` 명령어로 라이브러리 설치가 먼저 필요합니다.

## Structure
- 논의 중<img width="1121" alt="image" src="https://github.com/user-attachments/assets/c50f406c-0999-4b84-9ef2-ae5f69e46647">
- Page Object Model 을 어떻게 구성할까?

## Test Execute
- 논의 중
- 자동화 테스트는 어떻게 실행할까?
  
## PR Guide
1. 각 인원들은 main브랜치에서 별도의 브랜치를 생성합니다. 브랜치명은 아래와 같은 규칙을 준수합니다.
   - `{{본인 이름 이니셜}}_{{YYYYMMDD}}`
2. 브랜치 생성 후, 맡은 범위의 테스트 케이스를 약속한 코드 스타일에 맞게 구현하고, Reviewer를 지정하여 PR 을 생성합니다.
3. 생성한 PR을 main브랜치에 merge하기 위해서는 기본적으로 main브랜치 보호 룰이 적용되어 있기 때문에, 정해진 Reviewer의 일정 승인이 필요합니다.

## Comment
- 매주 목요일 정기적으로 오프라인에서 자동화 협업을 진행합니다.
- 개인적으로 온라인에 진행한 뒤 PR을 생성해도 무방합니다.
