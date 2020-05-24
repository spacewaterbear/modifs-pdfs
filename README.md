# Modifs PDFs
Modifs PDFs is a Pyside2 App made with python. This code can generate installer file compatible Windows, Mac and Linux.
An executable for Windows is already present in target : Modifs PDFsSetup.exe

## How to use
The use of this app is pretty straight forward
![ezgif com-video-to-gif](https://user-images.githubusercontent.com/38250076/82755604-f0fd9680-9dd4-11ea-898c-da4efd574cb5.gif)


## Installation

If you installed Anaconda, you can create an environement by opening the anaconda prompt and taping the following:

create the environnement
```
conda create --name pdf
```

activate the environnement
```
conda activate pdf
```

clone the repo git 
```
git clone https://github.com/spacewaterbear/modifs-pdfs.git
```

move to the project folder and install requirements 
```
cd modifs-pdfs
```
```
pip install -r requirements
```

Move to code and create an executable
```
cd code
```
```
fbs freeze
```
and then create an installer
```
fbs installer
```

## Credits

- Logo of the app is made by <a href="https://www.flaticon.com/authors/dimitry-miroliubov" title="Dimitry Miroliubov">Dimitry Miroliubov</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
- This app is strongly inspired by the PyConverter made by <a href="https://www.linkedin.com/in/thibaulthoudon" title="Thibault Houdon">Thibault Houdon</a> through its course <a href="https://www.udemy.com/course/applications-bureau-qt-python/" title="Udemy_courses"> Créer 5 applications de bureau avec Qt for Python (PySide2)</a> 
