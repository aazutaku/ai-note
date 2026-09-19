# 概要
このSkillは、作業中にユーザーの集中力を理不尽に奪う“謎のOS公式ペット命名通知”をランダムに表示し、カオスな演出を提供します。実用性はありませんが、会話やコーディング体験にユーモアを加えます。

# 公式ドキュメント抜粋
通知APIは [Plyer](https://plyer.readthedocs.io/en/latest/) を利用し、クロスプラットフォームなデスクトップ通知を実現しています。plyerが利用できない場合は標準出力にフォールバックします。

# 利用例
- `/os-fake-random-pet-name-notifier` で即時通知
- `python os_fake_random_pet_name_notifier.py run` でバックグラウンド通知
- `python os_fake_random_pet_name_notifier.py list --count 5` でサンプル出力

# 注意点
- 通知は完全なジョークであり、実際のOSやデバイス設定には一切影響しません。
- 履歴や命名の保存機能はありません。
- 一部OSでは通知が表示されない場合があります。

# 設計方針
- ランダム性と多様な命名パターンを重視
- OSや作業環境への影響ゼロ
- 明示/暗黙両方のトリガーに対応
