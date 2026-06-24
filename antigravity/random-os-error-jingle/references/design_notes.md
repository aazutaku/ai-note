# 概要
このSkillは、コマンド実行時のエラーや例外を即座に音で通知することで、作業者の注意喚起やチーム内でのジョーク演出を目的としています。音源はユーザーが自由に追加・差し替え可能です。

# 公式ドキュメント抜粋
- [playsound](https://github.com/TaylorSMarks/playsound): クロスプラットフォームなシンプルな音声再生ライブラリ。
- [sounddevice](https://python-sounddevice.readthedocs.io/): WAV/OGG等の音量制御や高機能再生が可能。

# 利用例
- 開発中のテスト失敗時に音で即座に気付く
- チーム内で“また鳴った”と盛り上がる
- エラー発生時のストレスを和らげるユーモア演出

# 注意点
- サウンド再生はローカル端末でのみ有効
- 音量制御はsounddevice利用時のみ反映
- 音源ファイルが無い場合は無音

# 設計方針
- 音源の拡張性（WAV/MP3/OGG）
- CLIからの柔軟な操作（list/test/run/mute/volume）
- 依存ライブラリはpipで簡単導入