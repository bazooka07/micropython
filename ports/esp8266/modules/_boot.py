import gc

gc.threshold((gc.mem_free() + gc.mem_alloc()) // 4)
import uos
from flashbdev import bdev

if bdev:
    try:
        uos.mount(bdev, "/")
    except:
        import inisetup

        inisetup.setup()

try:
    import wifi_config
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        sta_if.connect(wifi_config.WIFI_SSID, wifi_config.WIFI_PASSWD)
except:
    print("No Wifi setting found")

gc.collect()
