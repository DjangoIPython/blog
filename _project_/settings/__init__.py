from .const_settings import *

try:
    from .dev_settings import *
except ImportError:
    from .prod_settings import *
