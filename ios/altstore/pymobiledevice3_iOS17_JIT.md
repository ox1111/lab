# JIT Using pymobiledevice3
Some prerequisites for Windows currently is that you need Python and lldb installed somehow. 
In this small guide, I will use scoop, but you can use whatever you like to get the binaries necessary.

## Installing Scoop
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

## Installing Dependencies
```powershell
scoop install git
scoop bucket add versions
scoop install versions/python312
scoop install versions/mingw-winlibs-llvm
python3 -m pip install pymobiledevice3==2.44.0
```

## Actually Enabling JIT
```powershell
python3 -m pymobiledevice3 mounter auto-mount --udid <your-udid>
# This tunnel command must be ran as an admin
python3 -m pymobiledevice3 remote start-tunnel --udid <your-udid>
# This will output your --rsd for the next commands
# You will need a new terminal window for the following commands
python3 -m pymobiledevice3 processes pgrep <whatever app you want> --udid <your-udid>
# This will output a PID you need for the debugger below, like: INFO 727 DolphiniOS
python3 -m pymobiledevice3 developer debugserver start-server --rsd XXXX:XXXX:XXXX::1 61222
# You will put your --rsd here, but this will return a connect://[XX]:61223 (you'll see it like below in the []:)
# You only need the IP/port for lldb
lldb
(lldb) platform select remote-ios
(lldb) gdb-remote [fdcc:71b4:7827::1]:52252
(lldb) settings set target.memory-module-load-level minimal
(lldb) attach -p <PID> # 727 like above
(lldb) continue
(lldb) detach
(lldb) exit
# Then you can exit all terminals as JIT has been enabled.
```
