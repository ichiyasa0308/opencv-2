import cv2
import numpy as np
from numpy import uint8

class mouseParam:
    def __init__(self, input_img_name):
        #マウス入力用のパラメータ
        self.mouseEvent = {"x":None, "y":None, "event":None, "flags":None}
        #マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)

    #コールバック関数
    def __CallBackFunc(self, eventType, x, y, flags, userdata):

        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType
        self.mouseEvent["flags"] = flags

    #マウス入力用のパラメータを返すための関数
    def getData(self):
        return self.mouseEvent

    #マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]

    #マウスフラグを返す関数
    def getFlags(self):
        return self.mouseEvent["flags"]

    #xの座標を返す関数
    def getX(self):
        return self.mouseEvent["x"]

    #yの座標を返す関数
    def getY(self):
        return self.mouseEvent["y"]

    #xとyの座標を返す関数
    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])




#入力画像の読み込みと表示
im1 = cv2.imread("images/fuji_g.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("original", im1)

#初期化処理
inp = np.zeros(shape=(im1.shape))
im2 = np.zeros(shape=(im1.shape))
cv2.imshow("input window", inp)

#コールバックの設定
#どのウィンドウでマウスでの処理をするか指定。
mouseData = mouseParam("input window")

#スペクトルの表示
f = np.fft.fft2(im1)
fshift = np.fft.fftshift(f)
Spectrum = 20*np.log(np.abs(fshift))
#print(im1)
#print(Spectrum)
max = int(np.max(Spectrum))
#print(max)
#スペクトルの値が255を超えているので、２５５以下に収まるように調整して表示
cv2.imshow("Spectrum",(Spectrum/max * 255).astype(uint8))

flag=0
while 1:
    #左クリックで１マス更新
    if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
        if flag==0:
            flag=1
        else : flag=0
        im2[:,:] = 0
        y=mouseData.getY()
        x=mouseData.getX()
        inp[y,x] = 1
        im2[y,x] = 1
    #右クリックで広く更新
    if mouseData.getEvent() ==  cv2.EVENT_MOUSEMOVE and flag==1:
            im2[:,:] = 0
            y=mouseData.getY()
            x=mouseData.getX()
            inp[y-3:y+3,x-3:x+3] = 1
            im2[y-3:y+3,x-3:x+3] = 1
    #input windowをクリックした点を白く表示
    cv2.imshow("input window",inp)


    #今回クリックしたsin波を表示

    #fshift:*im2は、今回クリックしたフーリエ変換後の画素のみ抜き出したもの。
    #np.fft.ifftshift() 関数を使って直流成分の位置を画像の左上に戻す。
    fshift_2 = np.fft.fftshift(fshift*im2)
    #np.ifft2() 関数を使って逆フーリエ変換を適用
    fshift_im2=np.fft.ifft2(fshift_2)
    #複素数型の配列の絶対値をとる
    fshift_im2=np.abs(fshift_im2)
    cv2.imshow("sin wave",(fshift_im2 /np.max(fshift_im2) * 255).astype(uint8))


    #今までクリックしたsin波を重ね合わせる

    #fshift*inpは、今までクリックしたフーリエ変換後の画素のみ抜き出したもの。
    fshift_1 = np.fft.fftshift(fshift*inp)
    fshift_im1=np.fft.ifft2(fshift_1)
    fshift_im1=np.abs(fshift_im1)
    cv2.imshow("Synthetic wave",(fshift_im1 /np.max(fshift_im1)* 255).astype(uint8))

    #"q"で終了
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break;


cv2.destroyAllWindows()
