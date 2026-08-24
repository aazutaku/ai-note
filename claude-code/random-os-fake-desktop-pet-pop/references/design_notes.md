# 概要
このSkillは、作業中のユーザーに“謎のOS公式デスクトップペット”が突然現れるという非日常体験を提供し、集中力のリセットや癒しを目的としたエンタメ型ユーティリティです。

# 公式ドキュメント抜粋
通知表示にはPythonの plyer ライブラリや、macOS/Linux/Windowsの標準通知APIを利用しています。
- plyer: https://pypi.org/project/plyer/
- macOS: osascript display notification
- Linux: notify-send

# 利用例
- `/random-os-fake-desktop-pet-pop` コマンドで即時発動
- 長時間無操作時や「癒し」「通知」などのキーワードで自動発動
- `python desktop_pet_pop.py pop --notify` で通知ウィンドウにペットを表示

# 注意点
- 実際のデスクトップウィンドウ表示やファイル操作は行いません
- 履歴やサマリーは実行時のメモリ上のみで永続化されません

# 設計方針
- ユーザーの作業を物理的に妨げず、頻度を制御
- 出現メッセージやペットの種類を随時拡張可能
- OS依存部分は自動判定し、どの環境でも動作するよう配慮