# 概要
このSkillは、コマンド実行時にシュールな“OS謎サウンド”を再生し、開発現場の雰囲気を一変させる演出用ツールです。サウンドはローカル格納型で、OS標準の再生APIのみを利用しています。

# 公式ドキュメント抜粋
- [Python winsound](https://docs.python.org/ja/3/library/winsound.html)
- [afplay (macOS)](https://ss64.com/osx/afplay.html)
- [aplay (Linux)](https://man7.org/linux/man-pages/man1/aplay.1.html)

# 利用例
- チーム開発での気分転換
- コマンド実行の成功/失敗時の演出
- ハッカソンやイベントでの混乱演出

# 注意点
- サウンドファイルは .claude/skills/random-os-mystery-sound-effect/sounds/ に配置してください。
- 音量・再生デバイスはOS設定依存です。
- サウンド再生が不要な場合はSkillを削除/無効化してください。

# 設計方針
- OS標準APIのみ利用し、追加ライブラリ不要
- サウンドファイルはSkill配下に限定
- 導入・削除が容易で環境に影響を残さない設計