# masq_server
Custom server project for the shockwave game masq.

MASQ is a 2002 adult visual novel that has an online only DRM that was shut down around 2017.

Turns out the whole game is in the executable just needs it's DRM to be bypassed

In current state the whole game is beatable but there are some unfinished things

## How to use (on windows) quick and dirty tutorial.

1. Download this server or clone it.
2. Download and install [Python 3](https://www.python.org/downloads/) if you don't have it already
3. Start the server by running `py main-cgi-post-bing.py` and you get a message "Server started on port xxx.xxx.xxx.xxx:80" (X's will be replaced with your local ip) Do not close the window, the server needs to be running the whole time while you are playing the game.
4. open your hosts file located at `C:\Windows\System32\drivers\etc\hosts`
5. in this file you need to add a line `alteraction.com         xxx.xxx.xxx.xxx` (replace the X's with the ip you say in the server)
6. Download MASQ 67 from https://web.archive.org/web/20160606064916/http://www.alteraction.com/masq67.exe
7. run the game, press I'm online let me play, accept license, say you are over 17, and register

## plans

I don't like that you need to change you host file for the server to work, I found that you can change http://alteraction.com/cgi-bin/ to http://xxx.xxx.xxx.xxx/cgi-bin/ you need to use zero padding so if you ip is 192.168.1.12 you would write is at 192.168.001.012

My plan was to make a script that would automatically find the http://alteraction.com/cgi-bin/ in the memory of the game and inject the modded one, but I can't do it as of now.<br>
(mostly because computers at work where I have the most time to code suck and things just stop working for no readson, probably cursed.)

BTW recompiling the game with the adress changed is not likely I tried and didn't succeed. Don't know if it's the fault of ProjectorRays or mine but prolly mine.

Another thing that should be implemented is lives don't subtrack if you die, this could be fixed by implementing all the unimplemented requests that the client makes to the server, but I don't have motivation to do so now.

If you want to help this project you can tackle one of these or you could altleast text me on discord and tell me that you care or want these to be done.
