devices = {
    "room1": [
        {"id": 1, "type": "computer", "status": "on"},
        {"id": 2, "type": "printer", "status": "off"},

    ],
    "room2": [
        {"id": 3, "type": "lamp", "status": "on"},
        {"id": 4, "type": "computer", "status": "off"},

    ]

}

def add_device(room_id, device_id, device_type, status):
    device = {"id": device_id, "type": device_type, "status": status}
    if room_id in devices:
        devices[room_id].append(device)
    else:
        devices[room_id] = [device]

def toggle_device(room_id, device_id):
    for device in devices[room_id]:
        if device["id"] == device_id:
            device["status"] = "on" if device["status"] == "off" else "off"

def find_devices(device_type, status):
    found_devices = []
    for room_id, room_devices in devices.items():
        for device in room_devices:
            if device["type"] == device_type and device["status"] == status:
                found_devices.append((room_id, device))
    return found_devices

def get_all_devices(room_id):
    return devices[room_id]

def count_devices_by_type():
    device_counts = {}
    for room_id, room_devices in devices.items():
        for device in room_devices:
            if device["type"] in device_counts:
                device_counts[device["type"]] += 1
            else:
                device_counts[device["type"]] = 1
    return device_counts

print(get_all_devices("room1"))
