# Game of Life

Basic version of the game of life, coded in python

### Prerequisites

Need to install the next librairies :
```
opencv
numpy
matplotlib
keyboard
```

### Runing

```
python gameoflife.py board.txt
```

### Testing your own file

You can create your own game of life by creating a txt file like the board one
Create a square full of 0 separated by a comma. Then replace the 0 with a 1 where you want a square
Then you can launch it :

```
python gameoflife.py yournewfile.txt
```

If it doesn't work, check if the EOF of your file is just after the last value (0 or 1)

## Creating a video

You can create a video of your game of life by following the next steps :
1) Edit gameoflife.py by replacing 
```
record=False
```
to
```
record=True
```
2) Launch the gameoflife.py file
The steps will be saved in the img folder, be careful of the size of your storage

3) Now you can create the video by running :
```
python tovideo.py
```

## Authors

**Raphael Teitgen** - *Initial work*
