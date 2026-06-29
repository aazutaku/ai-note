# 概要
random-os-fake-boot-soundは、作業開始時に“謎OSの起動音”を毎回ランダムで再生することで、日常の開発環境に遊び心や混乱をもたらすSkillです。音源はユーザーが自由に追加・差し替え可能。

# 公式ドキュメント抜粋
- [playsound](https://pypi.org/project/playsound/) : シンプルなPython音声再生ライブラリ。OS標準の再生機能を利用。
- [os](https://docs.python.org/ja/3/library/os.html): ファイル・ディレクトリ操作用標準ライブラリ。
- [random](https://docs.python.org/ja/3/library/random.html): ランダム選択用標準ライブラリ。

# 利用例
- ターミナル起動時に自動でサウンドを鳴らす
- /skills menu から明示的に呼び出して楽しむ

# 注意点
- サウンドファイルは必ずローカル保存し、著作権に注意してください。
- OSや環境によっては音声再生がサポートされない場合があります。

# 設計方針
- シンプルなディレクトリ構成とCLIサブコマンドで、サウンド管理やテストも容易に。
- 音源差し替えは sounds/ フォルダへのファイル追加のみで完結。