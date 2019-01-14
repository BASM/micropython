import gc
gc.threshold((gc.mem_free() + gc.mem_alloc()) // 4)
import uos
import gc
from flashbdev import bdev
import webrepl
import machine

def ota():
    machine.RTC().memory('yaotaota')
    machine.reset()

try:
    if bdev:
        uos.mount(bdev, '/')
    gc.collect()
except OSError:
    import inisetup
    inisetup.setup()

webrepl.start()
gc.collect()
