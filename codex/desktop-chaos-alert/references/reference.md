# 概要
このSkillは、開発現場やオンライン会議などで突然「謎のOS緊急アラート」をデスクトップ通知として表示し、場の空気を和ませたり、意図的にカオスを演出するためのものです。通知内容は完全に無意味かつ無害なジョークメッセージのみです。

# 公式ドキュメント抜粋
- macOS: [AppleScript display notification](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/DisplayDialogandNotifications.html)
- Linux: [notify-send (libnotify)](https://specifications.freedesktop.org/notification-spec/latest/)
- Windows: [win10toast PyPI](https://pypi.org/project/win10toast/)

# 利用例
- チームの雑談タイムやリモート会議中のアイスブレイク
- 長時間の集中作業の合間に笑いを誘う
- 業務外のイベントやLT会での演出

# 注意点
- 通知は一時的で、履歴やファイル保存は行いません
- 通知が不要な場合は `disable` サブコマンドで簡単に停止できます
- Windowsではwin10toastライブラリが必要です（pipでインストール可能）

# 設計方針
クロスプラットフォーム対応を重視し、実害ゼロ・ログ非保存・即時停止可能な設計としています。通知APIの標準仕様のみを利用し、外部サービス連携や実システムへの影響は一切ありません。