# 概要
このSkillは、コマンド実行やファイル操作時に毎回異なる謎のサウンドエフェクトを再生し、開発現場にカオスな演出をもたらします。サウンドはSkill内に同梱され、環境依存を最小化。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- playsound: https://github.com/TaylorSMarks/playsound

# 利用例
- コマンド実行時に自動でSE再生
- サウンド一覧や再生履歴の確認
- ログにより再生履歴を追跡可能

# 注意点
- サウンド再生はOS依存。Linuxではaplay/paplay/cvlcが必要
- サウンドファイルはSkill配下のsounds/に配置
- Skill削除で環境に影響を残さない設計

# 設計方針
- 導入・削除が容易で副作用がない
- サウンドは5種類以上を用意し毎回ランダム
- ログ機能・一覧機能で利用状況を可視化