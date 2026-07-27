# 概要
このSkillは、開発現場や作業中に“緊急OSパッチ通知”風のジョークをデスクトップ通知としてランダム表示し、無駄な緊張感や笑いを演出する目的で設計されています。実害ゼロ・ローカル通知のみ。

# 公式ドキュメント抜粋
- macOS: osascriptによる通知 (AppleScript)
- Linux: notify-send (libnotify)
- Windows: win10toast (pip install win10toast)

# 利用例
- `/skills os-fake-urgent-patch-alert` で即時発動
- `python os_fake_urgent_patch_alert.py log -n 3 -i 2` で3回・2秒間隔通知
- チームの朝会やペアプロ時のアイスブレイクに

# 注意点
- 通知は一切のデータ変更や記録を行いません
- Windowsではwin10toastのインストールが必要
- Linuxではnotify-sendが動作する環境のみ対応

# 設計方針
- 実在APIのみを使用し、OS依存部分は自動判別
- 通知内容は毎回ランダム生成
- コマンドラインからもSkill経由でも同じ挙動
- 業務システムや本番環境での混乱回避のため、明示的な注意書きを同梱