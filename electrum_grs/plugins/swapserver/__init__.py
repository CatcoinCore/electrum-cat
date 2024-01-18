from electrum_grs.i18n import _

fullname = _('SwapServer')
description = """
Submarine swap server for an Electrum-GRS daemon.

Example setup:

  electrum-grs -o setconfig use_swapserver True
  electrum-grs -o setconfig swapserver_port 5455
  electrum-grs daemon -v

"""

available_for = ['cmdline']
