# 概要
本Skillは「見られたくない作業を即座にカモフラージュする」ことを目的に設計されています。Excel風のウィンドウ画像を生成し、GUIで表示することで、監督者や同僚の視線を欺きます。

# 公式ドキュメント抜粋
- [tkinter](https://docs.python.org/ja/3/library/tkinter.html): 標準GUIライブラリ。クロスプラットフォーム。
- [Pillow](https://pillow.readthedocs.io/en/stable/): 画像生成・描画・保存。
- [ImageGrab](https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html): 画面キャプチャ用。

# 利用例
- 急な上司の巡回時にターミナルやエディタを一瞬でExcel画面に切り替え
- 開発者同士のジョークやエンタメ用途
- オンライン会議中の画面共有で“真面目なフリ”を演出

# 注意点
- 本Skillはあくまで「演出用」。実際の業務データやセキュリティ保護は行いません。
- 一部のLinux環境や仮想環境ではImageGrabが動作しない場合があります。
- ウィンドウの最前面化やショートカットのカスタマイズはOS依存です。

# 設計方針
- 依存は標準GUI(tkinter)とPillowのみ
- 画像生成でリアルなExcel風UIを再現
- 画面キャプチャで元作業の復元性を担保
- シンプルなCLIと明快な終了方法