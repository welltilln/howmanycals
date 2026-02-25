<div align="center">

# 🍲 How Many Cals (AI 영양사)

**Google Gemini 2.5 Flash로 구동되는 프로덕션 레벨의 AI 영양사 LINE 봇입니다.** <br>
*[fastapi-line-gemini](https://github.com/welltilln/fastapi-line-gemini) 보일러플레이트를 기반으로 완벽하게 구축되었습니다.*

<p align="center">
    <a href="README.md">English</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-TH.md">ภาษาไทย</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-ZH.md">简体中文</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-JA.md">日本語</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-KO.md">한국어</a>
</p>

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a67d?logo=fastapi)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?logo=google)](https://ai.google.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-Persistent_Storage-003B57?logo=sqlite)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

<br/>

## 📖 개요

**How Many Cals** 는 개인 영양사 역할을 하는 지능형 LINE 공식 계정입니다. Google의 Gemini Vision을 활용하여 음식 이미지를 분석하고 정확한 칼로리를 추출하며 식사 구성 요소를 분석합니다.

일반적인 챗봇과 달리 이 템플릿에는 사용자의 일일 총 칼로리를 추적하고 자정에 자동으로 재설정하는 **영구 SQLite 메모리 시스템**이 있어 진정한 AI 비서 경험을 제공합니다.

---

## ✨ 핵심 기능

* 📸 **스마트 비전 분석:** 복잡한 요리의 사진을 보내면 봇이 모든 단일 구성 요소를 식별하고 정확한 칼로리를 계산합니다.
* 🧠 **영구 SQLite DB:** 사용자 채팅 기록(일일 총 칼로리)은 로컬 SQLite 데이터베이스에 안전하게 저장되어 서버 재시작 시에도 유지됩니다.
* 🔄 **자동 일일 재설정:** 새로운 하루가 시작되면 칼로리 계산이 자동으로 '0'으로 재설정됩니다.
* 🎯 **동적 수정 시스템:** AI가 요리를 잘못 식별한 경우, 사용자가 올바른 이름을 문자로 보내면 봇이 즉시 다시 계산하고 데이터베이스를 업데이트합니다.

---

## 🛠️ 빠른 시작 가이드

자세한 설정 방법은 [English README](README.md)를 참조하십시오.
