# 概要
このSkillは、ポモドーロタイマーの開始・終了時に、完全にランダムかつジョーク性の高い“失敗通知”を生成し、ユーザーの集中をあえて邪魔するエンタメ体験を提供します。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/3/library/random.html
- subprocess: https://docs.python.org/3/library/subprocess.html

# 利用例
- 明示的に`/random-os-fake-pomodoro-failure-notifier start`や`end`コマンドで呼び出し
- 会話やコード内で「ポモドーロ」「timer start」等のキーワードを含めることで自動発動

# 注意点
- 実際の作業進捗やタイマー管理機能はありません
- 通知内容は完全にフィクションです
- OS通知APIはMac/Linuxのみ対応、Windowsではターミナル出力のみ

# 設計方針
- 環境構築不要・データ損失リスクなし
- 10分以内で動作確認可能
- メッセージは今後追加・カスタマイズ容易な設計