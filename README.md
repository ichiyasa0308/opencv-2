# opencv-2

#コードの説明

5~42行：マウスイベントの処理を関数にしている。

51~58行：

コールバックの設定。つまり、どのウインドウでマウス操作の処理を受け付けるか指定する。

60~69行：スペクトルの表示。

高速フーリエ変換の関数である、関数np.fft.fft2()により画像のフーリエ変換を行う。
フーリエ変換をしたとき、端に出る低周波成分をnp.fft.fftshift() 関数により中心に寄せる。

73~91行：マウスイベントの処理。

一度左クリックするとflagを立てて、再びクリックするとフラグを降ろす。
フラグの立った状態でドラッグすると、広い範囲を連続で更新できる。

94~103行：
クリックした点のサイン波を表示。

具体的には、クリックした画素のみ１となる画像を、変換後の画像と掛け合わせることで逆変換した単体のサイン波が抜き出せる。これを表示する。

106~112行：今までクリックした全ての点に対して、上の内容と同様にしてサイン波の重ね合わせを表示する。

114〜116行：「q」ボタンを押すとwhile文のループを抜け、同時にウインドウを閉じる。



#使い方


jupyter notebook上でソースコードを「shift+Enter」で実行する。 
次にウインドウが表示されるので、「input window」を左クリックで1マス更新する。一度左クリックすると、ドラッグで連続で広く更新できる。
もう一度左クリックするとドラッグしても更新されなくなる。
「q」を押せばシステムは終了する。



#ライブラリー・モジュールのバージョン

python3:version 3.72

jupyter notebook:version 5.74

numpy:version 1.154

opencv:version 3.42


#実行の様子



![oie_animation](https://user-images.githubusercontent.com/48341900/62425026-60ed4400-b711-11e9-942c-71e2b9bb83ba.gif)

#参考にしたサイト

・numpyとopenCVを使った画像のフーリエ変換と逆変換
フーリエ変換の処理の具体的な中身について参考にした。
https://www.hello-python.com/2018/02/16/numpyとopencvを使った画像のフーリエ変換と逆変換/

・OpenCV-Pythonチュートリアル-フーリエ変換
フーリエ変換の後、逆フーリエ変換する処理を参考にした。
http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html

・OpenCVで表示した画像にマウスクリックした場所を取得する方法 (Python)
http://whitecat-student.hatenablog.com/entry/2016/11/09/225631


