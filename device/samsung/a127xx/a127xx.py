from build_kernel.utils.device import register_device
from device.samsung.exynos850 import SamsungExynos850Device

class SamsungExynos850Device(SamsungExynos850Device):
	PRODUCT_DEVICE = "a127xx"
	TARGET_KERNEL_CONFIG = f"halium_defconfig"

register_device(SamsungExynos850Device)