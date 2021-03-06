# BrickGateProperties.py

# For Pi2Go (full model)

'''
 This software is part of the brickgate application.
 It is Open Source Free Software, so you may
 - run the code for any purpose
 - study how the code works and adapt it to your needs
 - integrate all or parts of the code in your own programs
 - redistribute copies of the code
 - improve the code and release your improvements to the public
 However the use of the code is entirely your responsibility.
 '''

'''
History:

V1.00 - Jul 2015: - First public release
V1.01 - Oct 2015: - Fixed: Robot replaced by RobotInstance.getRobot()
V1.02 - Dec 2015: - Adapted to new Display class API
V1.03 - Jan 2016: - Minor changes in doc
V1.04 - Apr 2016: - Adapted to support new firmware option (Standalone mode)
V1.05 - Apr 2017: - Added: Support for Oled, Beeper
'''

BRICKGATE_VERSION = "1.05 - April 2017"

# Enable very verbose debugging infos to stdout
DEBUG = False

# Default sound level
# Must be int
SOUNDVOLUME = 70

# Default IP port
# Must be int
IP_PORT = 1299

# Folder for Python scripts
# Must be valix Linux directory without trailing /
# Must be string
SCRIPT_FOLDER = "/home/pi/scripts"

# Options for the DUC (Dynamic Update Client)
# -------------------
# Enable/disable DUC
# Must be boolean
DUC_ENABLED = False

# URL for the update host
# Must be string
DUC_HOST_URL = "http://dynupdate.no-ip.com/nic/update"

# IP alias for the brick
# Must be string
DUC_RASPI_URL = "robobot.zapto.org"

# User:Password for the host authentication
# Must be string
DUC_USER_PASS = "raspirobot:mypassword"

# Interval in minutes between DUC requests
# when a direct client is connected
# A request is performed when DUC starts
# and when the direct EV3 client disconnects.
# Must be int
DUC_UPDATE_INTERVAL = 30

# Interval in minutes between DUC requests
# when no direct client is connected
# Must be int
DUC_IDLE_UPDATE_INTERVAL = 1
