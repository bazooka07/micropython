freeze("$(PORT_DIR)/modules")
# freeze("$(MPY_DIR)/tools", ("upip.py", "upip_utarfile.py"))

# uasyncio
include("$(MPY_DIR)/extmod/uasyncio/manifest.py")
#include("../../extmod/uasyncio/manifest.py")

# Libraries from micropython-lib, include only if the library directory exists
if os.path.isdir(convert_path("$(MPY_LIB_DIR)")):
    # file utilities
    freeze("$(MPY_LIB_DIR)/micropython/upysh", "upysh.py")

    # requests
    # freeze("$(MPY_LIB_DIR)/python-ecosys/urequests", "urequests.py")
    # freeze("$(MPY_LIB_DIR)/micropython/urllib.urequest", "urllib/urequest.py")

    # umqtt
    freeze("$(MPY_LIB_DIR)/micropython/umqtt.simple", "umqtt/simple.py")
    #freeze("$(MPY_LIB_DIR)/micropython/umqtt.robust", "umqtt/robust.py")
