"""
## Core configuration

Configuration parameters are stored into the `core_config`
collection. Configuration is grouped in documents in order to be
possibly overwritten by user settings. Every configuration document
has a property named `_type`. There should be a single document for
every given `_type` value.

Generally, when one of the configuration keys is missing, the core
will use internal defaults.
"""

from main import Init, init_collection

init_core_config = Init("core_config", [{
    "_type": "sms",
    # session duration in hours
    "sms_session_duration": 24,
    # whether to send an automatic reply or not
    "sms_reply_send": True,
    # content of the automatir reply
    "sms_reply_message": "Thank you for your report. Let us know more about it by telling us: 1) Your name 2) Your location. A reporter may contact you directly."
}])

if __name__ == "__main__": init_collection(init_core_config)
