import bluetooth

local_bluetooth_address = bluetooth.read_local_bdaddr()
print("Local bluetooth address: {}".format(local_bluetooth_address))
