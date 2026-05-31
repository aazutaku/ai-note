# 概要
このSkillは、作業中にユーザーの実際の気分や天候とは無関係に、完全ランダムな天気アイコンをデスクトップ通知として表示することを目的としています。ユーモラスな演出や気分転換を意図しています。

# 公式ドキュメント抜粋
- [Plyer Notification](https://plyer.readthedocs.io/en/latest/): クロスプラットフォームなデスクトップ通知API。
- [Pillow](https://pillow.readthedocs.io/en/stable/): Pythonの画像生成・編集ライブラリ。

# 利用例
- `/desktop-mood-weather run` で即時にランダム天気を表示。
- `/desktop-mood-weather list` で過去の天気履歴を確認。
- `/desktop-mood-weather summary` で天気別の表示回数を集計。

# 注意点
- plyer, pillow のインストールが必要です。
- 一部Linux環境（Wayland等）では通知が表示されない場合があります。
- アイコン画像は一時ファイルとして保存されますが自動削除はされません。

# 設計方針
- 実在APIのみ利用し、OS依存部分はplyerに委譲。
- アイコン画像は毎回動的生成し、天気名も画像内に描画。
- ログ機能で過去の気分天気を振り返ることも可能にしています。