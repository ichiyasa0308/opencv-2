# opencv-2

・コードの説明

11行目でカメラを用いて画像を取得し、変数imに代入する。 14~15行で取得した画像の輝度値の平均値を取って表示し、registerというリストのi番目に代入する。続いてiの値を1増やして代入する番数を１つずらす。 以上の動作を、9行目のwhile文により、18行目のif文によりEnterキーが押されるてbreakするまでの間繰り返す。 最後に、23〜33行で取得した平均値をx,y座標のグラフに表示する。 横軸は時間で、縦軸は輝度値の平均値である。なお、縦軸の表示範囲は、取得した輝度値の平均値の平均±5の範囲で表示するようにした。なお、輝度値の平均値の平均は、最初のあたりに取得される画像の輝度値は脈拍を測るのには乱雑な数値となるため、registerの20番目から平均の計算に含めた。

・使い方

jupyter notebook上でソースコードを「shift+Enter」で実行する。 次に、webカメラ（ノートpcのカメラ）が起動するので、そのカメラに映る画像の平均値が、毎フレームごとにノートブック上に出力されていく。 最後に、「Enter」を押すと、カメラが停止し、輝度値の平均値のグラフが出力される。

・ライブラリー・モジュールのバージョン

python3:version 3.72
jupyter notebook:version 5.74
numpy:version 1.154
matplotlib:version 3.02
opencv:version 3.42

・実行の様子

ソースコードをjupyter notebookで実行し、カメラに指をのせる。 そして毎フレームごとの画像の輝度の平均値が表示され、Enterキーを押してカメラを停止させると輝度の平均値のグラフが表示される。 最後のグラフの結果より、脈拍によって輝度値が変化している様子が見て取れる。

mean-brightness

・参考にしたサイト

https://www.hello-python.com/2018/02/16/numpyとopencvを使った画像のフーリエ変換と逆変換/

フーリエ変換の後、逆フーリエ変換する処理を参考にした。

http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
