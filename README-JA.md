<div align="center">

# 🍲 How Many Cals (AI 栄養士)

**Google Gemini 2.5 Flashを搭載した、実運用可能なAI栄養士LINE Bot。** <br>
*[fastapi-line-gemini](https://github.com/welltilln/fastapi-line-gemini) ボイラープレート上に構築されています。*

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

## 📖 概要

**How Many Cals** は、あなたのパーソナル栄養士として機能するインテリジェントなLINE公式アカウントです。GoogleのGemini Visionを活用して食事の画像を分析し、正確なカロリー数を抽出し、食事の成分を分解します。

ステートレスな一般的なBotとは異なり、このテンプレートには、ユーザーの1日の総カロリーを追跡し、深夜に自動的にリセットする**永続的なSQLiteメモリシステム**が備わっており、真のAIアシスタント体験を提供します。

---

## ✨ 主な機能

* 📸 **スマート画像解析：** 複雑な料理の画像を送信すると、Botがすべての成分を識別し、正確なカロリーを計算します。
* 🧠 **永続的なSQLite DB：** ユーザーのチャット履歴（1日の総カロリー）はローカルのSQLiteデータベースに安全に保存され、サーバーの再起動後も保持されます。
* 🔄 **毎日の自動リセット：** 日付が変わると、カロリーカウントは自動的にゼロにリセットされます。
* 🎯 **ダイナミック修正システム：** AIが料理を誤認した場合、正しい名前をテキストで送信するだけで、AIが再計算してデータベースを即座に更新します。

---

## 🛠️ クイックスタートガイド

セットアップ手順の詳細については、[English README](README.md)をご参照ください。
