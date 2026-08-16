# 概要
このSkillは、開発現場やターミナル操作時に「謎の公式SE」を毎回ランダム再生することで、集中崩壊やコミカルな混乱を演出するために設計されています。音源はSkill内に同梱または公式フリー素材CDNから自動取得します。

# 公式ドキュメント抜粋
- [playsound公式](https://github.com/TaylorSMarks/playsound): クロスプラットフォームなPythonサウンド再生ライブラリ
- OS標準コマンド: afplay(macOS), aplay(Linux), winsound(Windows)

# 利用例
- ターミナルで`python random_os_mystery_sound_effect.py play`実行時に毎回異なるSEが鳴る
- `/skills random-os-mystery-sound-effect`で明示発動

# 注意点
- 音量や再生タイミングはOS依存
- Skill削除時に一時ファイルも自動削除し、環境汚染なし

# 設計方針
- 複数のSEを用意し、毎回ランダム選択
- サウンドファイルは一時保存し、Skill削除時にクリーンアップ
- CLIサブコマンドで管理・確認・クリーンアップ容易