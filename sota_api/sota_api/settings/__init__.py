import os
if os.environ.get('TARGET') == 'production':
    from .prod import *
else:
    from .dev import *
