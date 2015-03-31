from random import randint
from operator import itemgetter
import time
from SimpleCV import *

listRouge = ['angry','kick', 'tango', 'volcano', 'run', 'blood']
listOrange = ['breakfast','afternoon', 'fire', 'cuba', 'sand', 'autumn']
listJaune = ['sun','holiday', 'beach', 'eggs', 'happy', 'summer']
listVert = ['forest','slow', 'jungle', 'vegetarian', 'weed', 'reggae']
listCyan = ['sky','polynesia', 'wakeup', 'soft', 'angel', 'air']
listBleu = ['sea','sleep', 'dream', 'ice', 'ill', 'vomiting']
listViolet = ['electric','lighting', 'nebula', 'funerals', 'devil', 'milkyway']
listMagenta = ['mouth','flower', 'wig', 'lipstick', 'spring', 'romantic']

# define the function blocks
def PickRedItem():
  redItem = randint(0,5)
  return listRouge[redItem]

def PickOrangeItem():
  orangeItem = randint(0,5)
  return listOrange[orangeItem]

def PickYellowItem():
  yellowItem = randint(0,5)
  return listJaune[yellowItem]

def PickGreenItem():
  greenItem = randint(0,5)
  return listVert[greenItem]

def PickCyanItem():
  cyanItem = randint(0,5)
  return listCyan[cyanItem]

def PickBlueItem():
  blueItem = randint(0,5)
  return listBleu[blueItem]

def PickVioletItem():
  violetItem = randint(0,5)
  return listViolet[violetItem]

def PickMagentaItem():
  magentaItem = randint(0,5)
  return listMagenta[magentaItem]

def EmptyItem():
  return ""


# map the inputs to the function blocks
options = {"rouge" : PickRedItem,
           "orange" : PickOrangeItem,
           "jaune" : PickYellowItem,
           "vert" : PickGreenItem,
           "cyan" : PickCyanItem,
           "bleu" : PickBlueItem,
           "violet" : PickVioletItem,
           "magenta" : PickMagentaItem,
           "rien" : EmptyItem,

}

def CouleurDominante(valColor):
  if((0<=valColor<13) or (160<=valColor<180)):
   return "rouge"
  elif(13<=valColor<27):
   return "orange"
  elif(27<=valColor<31):
   return "jaune"
  elif(31<=valColor<73):
   return "vert"
  elif(73<=valColor<93):
   return "cyan"
  elif(93<=valColor<120):
   return "bleu"
  elif(120<=valColor<145):
   return "violet"
  elif(145<=valColor<160):
   return "magenta"
  else:
   return "rien"

cam = Camera()


NomFichier = "initfile.txt"
pathname = os.path.dirname(__file__)
filename = os.path.join(pathname, 'camera') 
Fichier = open(filename+"/"+NomFichier,'w')
Fichier.close()


while 1:
  img = cam.getImage()
  peaks = img.huePeaks()



  if not peaks:
    print ""
  else :
    peak = max(peaks,key=itemgetter(1))[0]
    itemColor = options[CouleurDominante(peak)]()
    os.rename(filename+"/"+NomFichier, filename+"/"+itemColor+".txt")
    NomFichier = itemColor+".txt"
    print ""

  time.sleep(1)










