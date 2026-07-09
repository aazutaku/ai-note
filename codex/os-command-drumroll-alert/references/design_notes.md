# 概要
このSkillは、重大コマンド実行前にエンジニアの注意を引きつけるため、OSネイティブのサウンド再生・通知APIを組み合わせて演出を行います。演出は毎回ランダムで、作業の緊張感を高めるユーモアを提供します。

# 公式ドキュメント抜粋
- [notify-send](https://specifications.freedesktop.org/notification-spec/latest/): Linuxのデスクトップ通知標準
- [Python playsound](https://github.com/TaylorSMarks/playsound): クロスプラットフォームなサウンド再生

# 利用例
- `python drumroll_alert.py --command "git push"`
- Skillメニューやエディタ拡張から自動呼び出し

# 注意点
- サウンドファイル(wav)はスクリプトと同じディレクトリに配置してください。
- OSごとに通知APIやサウンド再生コマンドが異なるため、動作環境に応じて依存パッケージやコマンドのインストールが必要です。
- コマンド実行自体は行いません。演出後は手動でコマンドを実行してください。

# 設計方針
- OS標準APIのみを利用し、追加の外部ライブラリ依存を最小化。
- 重大コマンド判定は先頭部分一致で判定し、柔軟にカスタマイズ可能。
- ユーザー体験を損なわないよう演出時間は短く抑えています。