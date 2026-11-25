# 概要
本Skillは「作業の合間に謎の古文調＋現代顔文字混成メッセージを巻物風に通知する」ことを目的としています。エンタメ性・意外性・脱力感を重視し、通知内容は完全ランダム生成です。

# 公式ドキュメント抜粋
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/

# 利用例
- コマンド実行後や長時間作業時の気分転換
- チームでの話題作りやアイスブレイク
- 意味不明な通知で集中しすぎを防ぐ

# 注意点
- Windowsデスクトップ通知には未対応
- 意味や文脈の整合性は保証されません
- ログ保存や履歴参照機能はありません

# 設計方針
- キーワード検出・明示呼び出し・無操作時の3種トリガーに対応
- 古文調フレーズと現代顔文字・記号をランダム合成
- ターミナル・デスクトップ両出力に対応し、環境依存性を考慮
- 冗長な繰り返しや既視感を減らすため、直近のフレーズ再利用を避ける