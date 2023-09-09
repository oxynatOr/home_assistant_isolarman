from datetime import timedelta

DOMAIN = 'isolarman'

DEFAULT_PORT_INVERTER = 8899
DEFAULT_INVERTER_MB_SLAVEID = 1
DEFAULT_LOOKUP_FILE = 'deyesunX.yaml'




LOOKUP_FILES = [
    'deyesunX.yaml'
    ## all are untested for me.
    # 'deye_4mppt.yaml',
    # 'deye_hybrid.yaml',
    # 'deye_sg04lp3.yaml',
    # 'deye_string.yaml',
    # 'sofar_lsw3.yaml',
    # 'sofar_wifikit.yaml',
    # 'solis_hybrid.yaml',
    # 'solis_1p8k-5g.yaml',
    # 'sofar_g3hyd.yaml',
    # 'sofar_hyd3k-6k-es.yaml',
    # 'zcs_azzurro-ktl-v3.yaml',
    ,'custom_parameters.yaml'
]

# will be as dynmiac as we can make it... sooner, rahter then later :)
DEFAULT_TIME_OUT = 15
DEFAULT_MAX_ATTEMPTS = 5
MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=DEFAULT_TIME_OUT)

CONF_INVERTER_HOST = 'inverter_host'
CONF_INVERTER_PORT = 'inverter_port'
CONF_INVERTER_SERIAL = 'inverter_serial'
CONF_INVERTER_MB_SLAVEID = 'inverter_mb_slaveid'
CONF_LOOKUP_FILE = 'lookup_file'

CONF_TIME_OUT = 'lookup_file'
CONF_MAX_ATTEMPTS = 'lookup_file'


SENSOR_PREFIX = 'Solarman'
