# 概要
本Skillは、開発現場に“古代OSの謎予言”という非日常的な演出を加えることで、作業の合間に笑いや気分転換を提供することを目的としています。通知は完全に無害で、実業務やデータに影響を与えません。

# 公式ドキュメント抜粋
通知APIにはPythonの[plyer](https://pypi.org/project/plyer/)を利用。plyerはクロスプラットフォームでデスクトップ通知を実現できるため、Windows/Mac/Linuxいずれでも動作します。

# 利用例
- 明示呼び出し: `python prophecy_alert.py once`
- コマンド出力監視: `your_command | python prophecy_alert.py monitor`
- ランダム通知: `python prophecy_alert.py random --min 120 --max 300`

# 注意点
- plyer未インストール時は標準出力のみ。
- 予言内容は完全に架空で、実際のOSやセキュリティには一切関係ありません。

# 設計方針
- 予言テンプレートと変数を分離し、毎回異なる通知を生成。
- 標準入力監視・ランダム発動・明示呼び出しの3モードを用意。
- plyerが使えない場合も必ず標準出力で通知。