# Terminal Joyride
The JetPack Joyride game on your terminal.


## Compile and Run

If you don't have python or colorama installed, run the following lines on your terminal.
```shell
sudo apt-get install python3
python3 -m pip install coloroma
```

And then to run the game:
```shell
python3 game.py
```

## Class Structure

* Frame
* OS manager
* GameObject
  * Background
  * People
    * Player
    * Boss Enemy
  * Spawnable
    * Fire Beams
    * Magnet
  * Bullets
    * My Bullets
    * Boss Bullets
  * Powerups
    * Speed Power-Up
    * Shield Power-Up

