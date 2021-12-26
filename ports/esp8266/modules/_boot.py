import gc

gc.threshold((gc.mem_free() + gc.mem_alloc()) // 4)

from machine import Pin, Timer, Signal
from time import sleep_ms

LED_IN = Signal(Pin(2, Pin.OUT, 1), invert=True)
LED_IN.off()

def flash(t=None):
    LED_IN.on()
    sleep_ms(200)
    LED_IN.off()

import uos
from flashbdev import bdev

if bdev:
    try:
        uos.mount(bdev, '/')
    except:
        import inisetup

        inisetup.setup()

timer1 = Timer(-1)
timer1.init(mode=Timer.PERIODIC, period=500, callback=flash)

print('\n\n')

try:
    import wifi_config
    import network

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        for ap in sta_if.scan():
            ssid = ap[0].decode('utf-8')
            # Trying connection with known access points...
            if ssid in wifi_config.aps:
                print('SSID: %s' %(ssid,))
                sta_if.connect(ssid, wifi_config.aps[ssid])
                while sta_if.status() == network.STAT_CONNECTING:
                    print('.', end='')
                    sleep_ms(200)
                print('')

                if sta_if.isconnected():
                    ap_if = network.WLAN(network.AP_IF)
                    ap_if.active(False)
                    break

    if sta_if.isconnected():
        try:
            import uftpd
        except:
            sta_if.ifconfig()

        try:
            import ntptime
            ntptime.settime()
        except:
            pass
except:
    print('No Wifi setting found')
finally:
    timer1.deinit()

try:
    from upysh import *
except:
    pass

gc.collect()
