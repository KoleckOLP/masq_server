# masq_server
Custom server project for the shockwave game masq.

MASQ is a 2002 adult visual novel that has an online only drm that was shut down.

My goal is to have some part of the game playable again, from some reverseengineering I think 2 Episodes should be playable.

With the help of reddit user gamstat we managed to get in game but only part of the game is playable if you choose to not register.

registering works now thanks to gamstat,

I've also fixed saving and loading and unlocked episode 2,3 and 4

## How to use (on windows) quick and dirty tutorial.

1. Download this server or clone it.
2. Download and install [Python 3](https://www.python.org/downloads/) if you don't have it already
3. Start the server by running `py main-cgi-post-bing.py` and you get a message "Server started on port xxx.xxx.xxx.xxx:80" (X's will be replaced with your local ip) Do not close the window, the server needs to be running the whole time while you are playing the game.
4. open your hosts file located at `C:\Windows\System32\drivers\etc\hosts`
5. in this file you need to add a line `alteraction.com         xxx.xxx.xxx.xxx` (replace the X's with the ip you say in the server)
6. Download MASQ 67 from https://web.archive.org/web/20160606064916/http://www.alteraction.com/masq67.exe
7. run the game, press I'm online let me play, accept license, say you are over 17, and register

