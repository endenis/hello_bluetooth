#!/usr/bin/python3
import dbus

bus = dbus.SystemBus()

bus_name = 'org.freedesktop.hostname1'
object_path = '/org/freedesktop/hostname1'
dbus_interface = 'org.freedesktop.DBus.Properties'

proxy = bus.get_object(bus_name, object_path)
interface = dbus.Interface(proxy, dbus_interface)

hostname = interface.Get(bus_name, 'Hostname')

print("dbus hostname: {}".format(hostname))
