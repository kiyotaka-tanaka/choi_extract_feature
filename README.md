# choi_extract_feature

必要なファイル：

　  VGG_FACE.caffemodel 　VGG-16ネットワークを2622人顔画像で最初から学習させたネットワークである。
  
    VGG_FACE_deploy.prototxt VGG ネットワークの　caffe　様な定義ファイルです。

  
  
  VGG_FACEについて草しくは　http://www.robots.ox.ac.uk/~vgg/software/vgg_face/　を参考にしてください。
 
 


コードの説明：



 extract.lua は指定されたフォルダーの中にある全ての画像に対して、特徴量を指定された特徴量用なフォルダーに　image_name.h5という形で書き込む。
 
 extract.py は　パラメータで受け取った画像の特徴量をフォルダーから読み取ってtextファイルに書くようなコードになっています。
 


使い方： python extract.py image_name   ＊	：指定画像の特徴量ファイルに書き出す時　extract.shを使った方が良いです。



extract.sh ２つのパラメータを受け取る。image_name と　output_file_name
 
 




使い方： bash extract.sh image_path output_file
