set /p src=please input frida server source file path:
set /p fn=please input file name in /data/local/tmp/:
call adb forward tcp:27042 tcp:27042
call adb forward tcp:27043 tcp:27043
call adb push %src% /data/local/tmp/%fn%
call adb shell "setenforce 0"
call adb shell "chmod 777 /data/local/tmp/%fn%"
call adb shell "./data/local/tmp/%fn%"