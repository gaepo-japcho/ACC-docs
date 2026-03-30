# ACC Requirements Specification

Adaptive Cruise Control(ACC) 시스템의 요구사항 문서입니다.
[StrictDoc](https://github.com/strictdoc-project/strictdoc) 형식(`.sdoc`)으로 관리됩니다.

## 문서 구조

| 파일 | 설명 |
|------|------|
| `ELI.sdoc` | Elicitation Needs |
| `STK.sdoc` | Stakeholder Requirements |
| `SYS.sdoc` | System Requirements |
| `SWR.sdoc` | Software Requirements |
| `HWR.sdoc` | Hardware Requirements |
| `SAF.sdoc` | Safety Requirements |

## StrictDoc 설치 및 실행

### 설치

```bash
pip install strictdoc
```

### HTML 문서 생성 (export)

```bash
strictdoc export .
```

`output/` 디렉토리에 HTML 문서가 생성됩니다.

### 웹 서버로 편집 (server)

```bash
strictdoc server .
```

브라우저에서 `http://localhost:5111` 로 접속하여 요구사항을 편집할 수 있습니다.
