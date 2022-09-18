#!/usr/bin/python3
import dbus
import dbus.mainloop.glib
from gi.repository import GLib

def signal_received(signal_message):
    print(signal_message)

mainloop = None
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()
bus.add_signal_receiver(signal_received, dbus_interface='com.example.receiver', signal_name='FirstSignal')

mainloop = GLib.MainLoop()
mainloop.run()
