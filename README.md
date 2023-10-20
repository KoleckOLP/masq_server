# masq_server
Custom server project for the shockwave game masq.

MASQ is a 2002 adult visual novel that has an online only DRM that was shut down around 2017.

Turns out the whole game is in the executable just needs its DRM to be bypassed

In current state the whole game is beatable but there are some unfinished things

## How to use (on windows) one script does everything.

1. Download and install [Python 3](https://www.python.org/downloads/) if you don't have it already.
2. Download this server or clone it.
3. Install the dependencies for Python `pip install -Ur requirements.txt`
4. Download [masq67.exe](https://web.archive.org/web/20160606064916/http://www.alteraction.com/masq67.exe) and copy it to the server folder.
5. Run `py main-cgi-post-bing.py` you should get 3 messages:
```
SERVER: running on port xxx.xxx.xxx.xxx:80
CLIENT: Game was called.
CLIENT: Server URL was injected in the game successfully.
```
 - At this point the server is running, and the client memory was injected with the server URL, you can play the game now.
 - !!! Do not close the CMD window !!! the CMD window is running the server.

### Troubleshooting
If the game opens and after pressing "I'm online let me play masq!!" it doesn't work, then your network is not routing packets correctly and I can't help you with that.
- Workaround: turn off Wi-Fi and or disable all your network devices, then the game packets have nowhere to go but to the local server.

## plans

Recompiling the game is not possible for me, either because projectorRays isn't done yet, or because I don't understand Director Projects.

Another thing that should be implemented is that currently lives don't subtract if you die, this could be fixed by implementing all the unimplemented requests that the client makes to the server, but I don't have motivation to do so now.

If you want me to work on this thing, please text me some encouragement on discord `koleckolp` <- my nickname there.
