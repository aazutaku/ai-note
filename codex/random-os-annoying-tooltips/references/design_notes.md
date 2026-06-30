# 概要
このSkillは、ユーザーの作業中に“OS風うざい通知”を意図的に挿入し、ユーモアと懐かしさを演出します。実際のシステムに害を与えず、通知APIのみを利用します。

# 公式ドキュメント抜粋
通知機能は[plyer](https://plyer.readthedocs.io/en/latest/#plyer.notification.notification)のnotification.notifyを使用し、主要OSでの互換性を確保しています。

# 利用例
- 明示呼び出し: `/skills random-os-annoying-tooltips notify`
- 自動発動: `run`サブコマンドで一定間隔ごとに通知
- コマンドラインから `python random_os_annoying_tooltips.py notify` で単発通知

# 注意点
- 通知間隔は1分以上に制限し、過剰な連発を防止
- 通知内容は完全に無害で実害なし
- 一部Linux環境では通知が表示されない場合あり

# 設計方針
- OS依存APIを避け、plyerでクロスプラットフォーム化
- ローカルファイルで最終通知時刻を管理し、頻度を制御
- ユーモアと“うざさ”のバランスを重視