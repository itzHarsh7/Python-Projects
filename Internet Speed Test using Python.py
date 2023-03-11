import speedtest
wifi  = speedtest.Speedtest()
print("Wifi Download Speed(in kb/s) is ", wifi.download())
print("Wifi Upload Speed(in kb/s) is ", wifi.upload())