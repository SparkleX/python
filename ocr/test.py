#pip3 install pytesseract
#dnf config-manager --add-repo https://download.opensuse.org/repositories/home:/Alexander_Pozdnyakov/CentOS_8/
#rpm --import https://build.opensuse.org/projects/home:Alexander_Pozdnyakov/public_key
#dnf install tesseract
#dnf install tesseract-langpack-chi-sim


import pytesseract 
from PIL import Image

#pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('small.png'), lang="chi_sim", config="--psm 7")

print(text)