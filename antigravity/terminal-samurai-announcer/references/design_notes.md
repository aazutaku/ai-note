# 概要
terminal-samurai-announcerは、ターミナル作業の進行を時代劇風に演出することで、作業の緊張感や単調さを和らげることを目的としています。コマンド実行時に毎回異なる侍ナレーションを自動付与し、ユーザー体験を向上させます。

# 公式ドキュメント抜粋
- Python subprocess: コマンド実行と標準出力の取得に利用
- shlex: コマンドのパースに利用
- os/pathlib: 設定ファイルやホームディレクトリ管理

# 利用例
- `python samurai_announce.py run ls`
- `python samurai_announce.py toggle` でON/OFF切替
- `python samurai_announce.py status` で状態確認

# 注意点
- Skill本体はコマンドの実行結果自体は変更しません。
- 除外コマンドやパス設定も容易に拡張可能です。
- スクリプト自体をコマンドラッパーとして利用する設計です。

# 設計方針
- 既存の作業フローを壊さないこと
- シンプルなON/OFF切替と、拡張性のあるセリフ管理
- サブコマンド型CLI設計で柔軟な運用を実現