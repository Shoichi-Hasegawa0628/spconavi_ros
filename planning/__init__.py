#coding:utf-8
#This file for setting parameters
#Akira Taniguchi 2018/12/13-
import numpy as np

#################### Folder PATH ####################
#Setting of PATH for a folder of learned spatial concept parameters
datafolder    = "/home/akira/Dropbox/SpCoSLAM/data/"  #"/mnt/hgfs/D/Dropbox/SpCoSLAM/data/"
#Setting of PATH for output folder
outputfolder  = "/home/akira/Dropbox/SpCoSLAM/data/"  #"/home/akira/Dropbox/SpCoNavi/data/"

#音声ファイルフォルダ
speech_folder    = "/home/akira/Dropbox/Julius/directory/SpCoSLAM/*.wav"    #音声の教示データフォルダ
speech_folder_go = "/home/akira/Dropbox/Julius/directory/SpCoSLAMgo/*.wav"  #評価用の音声データフォルダ
lmfolder = "/home/akira/Dropbox/SpCoSLAM/learning/lang_m/"  #Language model (word dictionary)

#Navigation folder (他の出力ファイルも同フォルダ)
navigation_folder = "/navi/"  #outputfolder + trialname + / + navigation_folder + contmap.csv
#SpCoSLAMのフォルダ形式に従うようにしている

#Cost map folder
costmap_folder = navigation_folder



#################### Parameters ####################
T_horizon = 50     #計画区間(予測ホライズン)
N_best    = 10     #N of N-best (N<=10)
NbestNum = N_best      #N of N-best (N<=10)
N_best_number = N_best #N of N-best (N<=10) for PRR

step = 50     #使用するSpCoSLAMの学習時のタイムステップ(教示回数)

#自己位置の初期値(候補：目的地以外の理想的な位置分布のデータ平均)
X_candidates = []

#近似手法の選択(Proposed:0, samplingCtit:1, xの次元削減とか...)
Approx = 0

#状態遷移のダイナミクス(動作モデル)の仮定(確率的:1, 近似:2, 決定的:0)
Dynamics = 1

MotionModelDist = "Gauss"  #"Gauss"：ガウス分布、"Triangular":三角分布

#オドメトリ動作モデルパラメータ(AMCL or gmappingと同じ値にする)
odom_alpha1 = 0.2 #(ダブル、デフォルト：0.2)ロボットの動きの回転移動からオドメトリの回転移動のノイズ
odom_alpha2 = 0.2 #(ダブル、デフォルト：0.2)ロボットの動きの平行移動からオドメトリの回転移動のノイズ
odom_alpha3 = 0.2 #(ダブル、デフォルト：0.2)ロボットの動きの平行移動からオドメトリの平行移動のノイズ
odom_alpha4 = 0.2 #(ダブル、デフォルト：0.2)ロボットの動きの回転移動からオドメトリの平行移動のノイズ
#srr = 0.1 #(float, default: 0.1)  #オドメトリの誤差．平行移動に起因する平行移動の誤差．
#srt = 0.2 #(float, default: 0.2)  #オドメトリの誤差．回転移動に起因する平行移動の誤差．
#str = 0.1 #(float, default: 0.1)  #オドメトリの誤差．平行移動に起因する回転移動の誤差．
#stt = 0.2 #(float, default: 0.2)  #オドメトリの誤差．回転移動に起因する回転移動の誤差．

#ROSのトピック名
MAP_TOPIC = "/map"
COSTMAP_TOPIC = "/move_base/global_costmap/costmap"

#地図のyamlファイルと同じ値にする
resolution = 0.050000
origin =  np.array([-30.000000, -20.000000]) #, 0.000000]

#地図のサイズの縦横(length and width)があらかじめ分かる場合はこちらに記載しても良いかも
#map_length = 0
#map_width  = 0

#Julius parameters
##Please see "syllable.jconf" in Julius folder
JuliusVer      = "v4.4"   #"v.4.3.1"
HMMtype        = "DNN"    #"GMM"
lattice_weight = "AMavg"  #"exp" #音響尤度(対数尤度："AMavg"、尤度："exp")
wight_scale    = -1.0
#WDs = "0"   #DNN版の単語辞書の音素を*_Sだけにする("S"), BIE or Sにする("S"以外)

if (JuliusVer ==  "v4.4"):
  Juliusfolder = "/home/akira/Dropbox/Julius/dictation-kit-v4.4/"
else:
  Juliusfolder = "/home/akira/Dropbox/Julius/dictation-kit-v4.3.1-linux/"

if (HMMtype == "DNN"):
  lang_init = 'syllableDNN.htkdic' 
else:
  lang_init = 'syllableGMM.htkdic' # 'trueword_syllable.htkdic' #'phonemes.htkdic' # 初期の単語辞書(./lang_mフォルダ内)

dimx = 2           #The number of dimensions of xt (x,y)
margin = 10*0.05   #地図のグリッドと位置の値の関係が不明のため(0.05m/grid)*margin(grid)=0.05*margin(m)


####################Particle Class (structure)####################
class Particle:
  def __init__(self,id,x,y,theta,weight,pid):
    self.id = id
    self.x = x
    self.y = y
    self.theta = theta
    self.weight = weight
    self.pid = pid
    #self.Ct = -1
    #self.it = -1


####################Option setting (NOT USE)####################
wic = 1         #1:wic重みつき(理論的にはこちらがより正しい)、0:wic重みなし(Orignal paper of SpCoSLAM)
UseFT = 1       #画像特徴を使う場合(１)、使わない場合(０)
UseLM = 1       #言語モデルを更新する場合(１)、しない場合(０)[Without update language modelのため無関係]

##Initial (hyper) parameters
##Posterior (∝likelihood×prior): https://en.wikipedia.org/wiki/Conjugate_prior
alpha0 = 10.0        #Hyperparameter of CRP in multinomial distribution for index of spatial concept
gamma0 = 1.0         #Hyperparameter of CRP in multinomial distribution for index of position distribution
beta0 = 0.1          #Hyperparameter in multinomial distribution P(W) for place names 
chi0  = 0.1          #Hyperparameter in multinomial distribution P(φ) for image feature
k0 = 1e-3            #Hyperparameter in Gaussina distribution P(μ) (Influence degree of prior distribution of μ)
m0 = np.zeros(dimx)  #Hyperparameter in Gaussina distribution P(μ) (prior mean vector)
V0 = np.eye(dimx)*2  #Hyperparameter in Inverse Wishart distribution P(Σ)(prior covariance matrix)
n0 = 3.0             #Hyperparameter in Inverse Wishart distribution P(Σ) {>the number of dimenssions] (Influence degree of prior distribution of Σ)
k0m0m0 = k0*np.dot(np.array([m0]).T,np.array([m0]))
