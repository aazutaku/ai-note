# 概要
random-os-excuse-generatorは、開発現場の緊張を和らげるために設計されたジョーク系ツールです。深刻なエラーやバグ発生時に、根拠のない“OSの言い訳”をランダムで表示し、場の雰囲気を和ませます。

# 公式ドキュメント抜粋
- [notify2 (Linux)](https://pypi.org/project/notify2/)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)
- [pync (macOS)](https://github.com/setem/pync)

# 利用例
- チームの朝会やバグ修正作業中に、/random-os-excuse-generator を呼び出す
- テスト失敗時に自動で“言い訳”通知を表示し、笑いを誘う

# 注意点
- 本Skillは実害のないジョーク用途限定です。本番データやシステム設定には一切触れません。
- OS通知は環境によってライブラリの追加インストールが必要です。

# 設計方針
- OS依存部分は複数の通知方法を実装し、ライブラリ未導入時はコマンドライン通知や標準出力にフォールバックします。
- 言い訳リストは拡張可能で、今後カスタマイズも容易です。