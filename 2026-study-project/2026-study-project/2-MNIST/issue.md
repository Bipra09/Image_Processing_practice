# MNISTの手書き数字認識モデルの作成

MNISTの手書き数字認識モデルを作成する．
作成したモデルの精度，学習時間，推論時間を測定し競う．

- MNISTのトレーニングデータと検証データは本レポジトリの`2026-study-project/2-MNIST/dataset`に存在する．
  - データセットは`git lfs`で管理しているため，レポジトリからpullするには，`git lfs`をインストールをインストールする必要がある．
- MNISTのデータを読み込むコードは本レポジトリの以下に存在する．
  - Python: `2026-study-project/2-MNIST/python_code/`
  - C++: `2026-study-project/2-MNIST/c_plus_plus_code/`

作成したモデルの精度，学習時間，推論時間は以下に添付されているExcelに記入してください．

- <http://192.168.6.5/intfour/2026-study-project/-/wikis/MNIST%E3%81%AE%E6%89%8B%E6%9B%B8%E3%81%8D%E6%95%B0%E5%AD%97%E8%AA%8D%E8%AD%98%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E9%80%9F%E5%BA%A6%EF%BC%8C%E7%B2%BE%E5%BA%A6%E8%A9%95%E4%BE%A1>

## レギュレーション

- なるべく標準ライブラリ以外使用不可[^ライブラリ]
- ただし並列化に必要なライブラリは使用可[^並列化]
- 使用言語は何でもOK (おすすめはPython)

[^ライブラリ]: Numpyなどのライブラリの有無で処理速度の差が大きいため．ただ，ライブラリなしだと固有値と固有ベクトルの求解やSVMの実装が難しいため，最初はライブラリありで実装してみるのはありだと思います．
[^並列化]: Pthread, OpenMP, MPI, OpenACC, CUDAなど(NPUを使っても面白いかもしれません)

## 何をやっていけば良いかわからない人向けのモデル

- [ ] Histograms of Oriented Gradients(HOG) + Nearest Neighbor(NN)を組み合わせたモデル
- [ ] HOG + サポートベクターマシン(SVM)を組み合わせたモデル
- [ ] 深層学習

## 参考文献

- 認識モデルを作成するのに使えそうな資料
  - ディジタル画像処理
  - ゼロから作るDeep Learning Pythonで学ぶディープラーニングの理論と実装
  - Dive into Deep Learning
- 高速化に使えそうな資料
  - パターソン&ヘネシー コンピュータの構成と設計 上
  - パターソン&ヘネシー コンピュータの構成と設計 下
  - Computer Architecture: A Quantitative Approach (The Morgan Kaufmann Series in Computer Architecture and Design)
  - programming massively parallel processors
- 手っ取り早く学習したい人向けの資料
  - <https://github.com/oreilly-japan/deep-learning-from-scratch>
  - プログラマーのためのCPU 入門 CPU は如何にしてソフトウェアを高速に実行するか
