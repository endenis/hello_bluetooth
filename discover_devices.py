import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)

for addr, name in nearby_devices:
    print("Bluetooth device {} with lookup name {}".format(addr, name))
