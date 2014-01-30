# MacSafe

Keep your MacBook from thieves. MacSafe detects adapter being disconnected.

## Installation

1. Download `macsafe.py`.
2. Open it with an text editor.
3. Change `SOUND_LOCATION` into your sound file location.


---


## Usage

### 1. Foreground

```
$ python macsafe.py
```


### 2. Background

#### 1) With 'nohup' command

**To start:**
```
$ nohup python macsafe.py &
```

**To terminate:**
```
$ ps aux | grep macsafe | awk '{print $2}' | xargs kill -9 2>/dev/null
```

#### 2) With 'screen' command

**To start:**
```
$ screen -t MACSAFE
bash-3.2$ python macsafe.py
```
Press `Control` + `A` + `D`, then you can see:

```
[detached]
```

**To terminate:**
```
$ screen -list
There are screens on:
	10042.ttys000.xoul	(Detached)
1 Sockets in ...
$ screen -r 10042.ttys000.xoul
bash-3.2$ exit
[screen is terminating]
$
```
You can press `Control` + `D` to terminate screen shell.


---


## Screenshot

![macsafe.png](https://raw.github.com/devxoul/macsafe/master/screenshots/macsafe.png)


---


## Copyright

Copyright (c) 2014 Su Yeol Jeon. All rights reserved.


---


## License

MacSafe follows BSD License.