# TracklistRec
Really Thanks for marin-m's Shazam client code
https://github.com/marin-m/SongRec<br>

## Installation:<br>
<br>
I just Tried this code on Ubuntu for wsl1 !<br>
<br>
1.First of all you should install Shazam client which is write by marin-m<br>
<br>
sudo apt-add-repository ppa:marin-m/songrec -y -u <br>
sudo apt install songrec -y <br>
songrec <br>
<br>
2. Secondly use pip to install the required libraries for python<br>
<br>
pip3 install -r requirements.txt

## How to use it?

1.Put your music file to the same folder as the test.py
2.Change line 11 :
          file_path="psybient.mp3" to your own music name.
3.Run:
          python3 test.py 
