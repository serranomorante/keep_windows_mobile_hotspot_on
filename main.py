import time

import app.hotspot.mobile_hotspot as mobile_hotspot

hotspot = mobile_hotspot.MobileHotspot()


if __name__ == "__main__":
    while True:
        hotspot.run()
        time.sleep(5)
