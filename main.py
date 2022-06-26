import time

import app.hotspot.mobile_hotspot as mobile_hotspot



if __name__ == "__main__":
    print("Keep mobile hotspot running")
    print("==============================")
    while True:
        hotspot = mobile_hotspot.MobileHotspot()
        hotspot.run()
        time.sleep(5)
