# 概要
このSkillは、エラー発生時に“意味不明なカタカナOS風エラー”を毎回ランダム生成し、デスクトップ通知として表示することで、開発現場の雰囲気を和らげるジョーク系演出を提供します。

# 公式ドキュメント抜粋
- subprocess: https://docs.python.org/3/library/subprocess.html
- win10toast: https://pypi.org/project/win10toast/

# 利用例
- コマンド実行時にエラーが発生した場合、通常のエラーメッセージとは別に、謎のカタカナ解説が通知されます。
- `/random-os-error-kaiseki last` で直近のダミーエラー通知を再表示できます。

# 注意点
- 通知機能はLinux/macOS/Windowsで異なります。Linuxはnotify-send、macOSはosascript、Windowsはwin10toastを利用。
- サーバ環境や通知非対応端末では通知が表示されません。

# 設計方針
- 本来のエラー内容は標準出力やstderrで確認でき、通知は完全にジョーク用途です。
- カタカナ解説はsubjects/actionsリストからランダム生成し、毎回異なる文面となります。