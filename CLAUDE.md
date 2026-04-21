# CLAUDE.md — ACC-docs

이 저장소는 ACC(Adaptive Cruise Control) 스케일카 프로젝트의 **요구사항 · ASPICE · ISO 26262 · 아키텍처** 문서를 담은 독립 git repo다. 코드가 아닌 프로세스·요구사항 아티팩트 전용이다. 상위 레포지토리 맥락은 `/mnt/c/acc/CLAUDE.md` 참조.

## 디렉토리 구조

| 경로 | 용도 | 주 포맷 |
|---|---|---|
| `reqs/` | 요구사항 데이터베이스 (traceability의 근간) | StrictDoc `.sdoc` |
| `reqs/STK.sdoc` | 이해관계자 요구사항 (STK###) | `.sdoc` |
| `reqs/STK/SYS.sdoc` | 시스템 요구사항 SYS001–SYS035 | `.sdoc` |
| `reqs/STK/SYS/SWR.sdoc` | 소프트웨어 요구사항 SWR001–SWR031 | `.sdoc` |
| `reqs/STK/SYS/SAF.sdoc` | 안전 요구사항 SAF001–SAF017 | `.sdoc` |
| `reqs/STK/SYS/HWR.sdoc` | 하드웨어 요구사항 HWR001–HWR012 | `.sdoc` |
| `autosar/ACC_AUTOSAR_Architecture_Sketch.md` | 5 SWC · 인터페이스 · 런너블 · 데이터타입 기준 문서 | Markdown + Mermaid |
| `ASPICE/` | ASPICE 프로세스 문서 (SYS.1, SYS.2) | `.sdoc` |
| `ISO26262/` | ISO 26262 안전 아티팩트 (현재 비어 있음, `.docx`는 `guide/` 에 있음) | — |
| `guide/README.md` | **ASPICE 4.0 + ISO 26262:2018 tailoring 선언** (250+ 라인) | Markdown |
| `guide/acc_aspice_guide.docx` | ASPICE 상세 가이드 (바이너리) | `.docx` |
| `guide/acc_iso26262_guide.docx` | ISO 26262 상세 가이드 (바이너리) | `.docx` |
| `refs/` | 외부 데이터시트 (MRR-30 LiDAR 등) | `.pdf` |
| `assets/` | 프로세스 다이어그램 | `.png` |
| `발표자료/` | 프로젝트 개요 발표 | `.pptx` |
| `새싹_부품_리스트.xlsx` | BOM | `.xlsx` |
| `strictdoc_config.py` | StrictDoc 빌드 설정 | Python |

## 요구사항 ID 체계

상위→하위 트레이스는 `.sdoc` 파일의 `Parent` 관계로 연결된다.

```
STK (stakeholder, ~15개)
 └─ SYS (system, SYS001–SYS035)
     ├─ SWR (software, SWR001–SWR031)
     ├─ SAF (safety, SAF001–SAF017)
     └─ HWR (hardware, HWR001–HWR012)
```

- **절대로 ID를 재활용하지 말 것** — 삭제된 요구사항은 상태를 `Obsolete` 로 바꾸되 번호는 비워둔다.
- 새 ID는 그 파일의 최대치 +1 로 부여. 코드 주석(`// SWR017`)과 1:1 대응되므로 번호가 변하면 전 레포 grep 필요.

## 빌드 · 렌더링

`reqs/README.md` 에 상세. 핵심만:

```bash
pip install strictdoc

strictdoc export .          # HTML → output/ 생성
strictdoc server .          # localhost:5111 에서 라이브 편집
```

- `output/` 과 `__pycache__/` 는 `.gitignore` 로 제외되어 있음. 커밋하지 말 것.
- `.github/workflows/pages.yml` 이 `main` 푸시 시 자동으로 `strictdoc export .` → GitHub Pages 배포.
- `strictdoc_config.py` 는 `exclude_doc_paths=["README.md"]` 로 README가 요구사항 HTML에 섞이지 않도록 한다. 수정 시 주의.

## Tailoring 요약 (guide/README.md 기반)

**ASPICE 4.0**: SYS.1–5 / SWE.1–6 / SUP.1·8·9·10 full, MAN.5·6 · HW.1–4 lightweight, MAN.4 · ACQ · SPL · REU · PIM 제외.

**ISO 26262:2018**:
- Part 3 (Concept) full — HARA / Safety Goals / FSC
- Part 4 (System) partial — TSR + HSI만
- Part 5 (HW) **제외** — HW 가정을 HSI 로 대체
- Part 6 (SW) full — MISRA-C, MC/DC, fault injection
- Part 8 partial — ASPICE SUP.8/9/10 과 통합

**ASIL**:
- H-01 의도치 않은 가속 → ASIL C
- H-02 감속 불가 → **ASIL D**
- H-03 의도치 않은 감속 → ASIL B
- Independence level **I1** (팀 내부 cross-review)

## 편집 시 지켜야 할 것

- `.sdoc` 은 plain-text — Edit/Write 로 자유롭게 수정. UID 충돌, Parent 누락, status enum 오타 조심.
- `.docx` / `.xlsx` / `.pptx` / `.pdf` 는 **손대지 말 것**. Word/Excel/PPT/데이터시트 원본을 GUI 로 편집 후 커밋.
- 안전 관련(SAF### 또는 SWR 중 ASIL 표시된 것) 변경은 HARA · FSC · TSR 영향도를 함께 검토. `guide/README.md` 의 변경관리 절차 참조.
- 한국어가 기본 — 요구사항 본문·설명·제목 모두 한국어로 유지. 영어 용어(ASIL, SWC, IRV 등)는 그대로.
- README.md 와 `strictdoc_config.py` 의 `exclude_doc_paths` 는 연동되어 있다. 새 파일을 제외하려면 양쪽 모두 반영.

## 참조 순서 (다른 레포에서 이 문서를 볼 때)

- 구현자(AUTOSAR/Arduino/RPi)는 `autosar/ACC_AUTOSAR_Architecture_Sketch.md` 를 1차 레퍼런스로 본다 — CAN DB, 5 SWC 계약, 런너블 주기, 데이터타입이 모두 여기에 있음.
- 요구사항 문구 원문이 필요하면 `reqs/STK/SYS/*.sdoc` 를 직접 열 것. 코드 주석의 `SWR017` 같은 표시는 이 파일의 UID 와 매칭된다.
