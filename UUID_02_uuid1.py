import uuid
from datetime import datetime, timezone

u = uuid.uuid1()

UUID_EPOCH_START = 0x01B21DD213814000
timestamp = (u.time - UUID_EPOCH_START) / 1e7
dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)

mac = ':'.join(f"{(u.node >> i) & 0xff:02x}" for i in range(40, -1, -8))

print("UUID:", u)
print("Time:", dt)
print("MAC :", mac)
print("Clock sequence:", u.clock_seq)