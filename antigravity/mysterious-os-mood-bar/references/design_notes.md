# 概要
mysterious-os-mood-barは、ターミナル操作時の気分ややる気指数を“超適当”に判定し、OSのメニューバーやステータスバーにランダムな気分ワードを表示するSkillです。実用性よりも、作業中のちょっとした笑い・演出を目的としています。

# 公式ドキュメント抜粋
- macOS: AppleScript (osascript) による通知表示 https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html
- Linux: notify-send または AppIndicator https://python-gtk-3-tutorial.readthedocs.io/en/latest/menus.html

# 利用例
- git statusやlsなどのコマンド実行時、気分温度ややる気指数がメニューバー/通知に表示されます。
- チームで笑いを誘う小ネタ、集中力が切れた時の気分転換などに活用できます。

# 注意点
- 判定ロジックは完全にランダムまたは冗談的です。
- ユーザーの操作ログやデータは一切保存しません。
- OS側APIの仕様変更により通知が表示されない場合があります。

# 設計方針
- コマンド長やgit statusの雰囲気から気分を“それっぽく”生成
- ローカルデータ保存は一切なし
- OSごとに適切な通知APIを選択し、確実に気分ワードを表示