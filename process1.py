from pymem import Pymem
from pymem.ptypes import RemotePointer

pm = Pymem("masq67.exe")

base_address = 0x00400000
offset_to_pointer = 0x0001E1B8

pointer_object = RemotePointer(pm.process_handle, base_address + offset_to_pointer)

address_from_pointer = pointer_object.value  # shouldn't be hex for later use

print(f"0. {hex(address_from_pointer)}")

pointer_object1 = RemotePointer(pm.process_handle, address_from_pointer+0x18)

address_from_pointer1 = pointer_object1.value  # shouldn't be hex for later use

print(f"1. {hex(address_from_pointer1)}")

pointer_object2 = RemotePointer(pm.process_handle, address_from_pointer1+0x560)

address_from_pointer2 = pointer_object2.value  # shouldn't be hex for later use

print(f"2. {hex(address_from_pointer2)}")

pointer_object3 = RemotePointer(pm.process_handle, address_from_pointer2+0x534)

address_from_pointer3 = pointer_object3.value  # shouldn't be hex for later use

print(f"3. {hex(address_from_pointer3)}")

pointer_object4 = RemotePointer(pm.process_handle, address_from_pointer3+0x14)

address_from_pointer4 = pointer_object4.value  # shouldn't be hex for later use

print(f"4. {hex(address_from_pointer4)}")

pointer_object5 = RemotePointer(pm.process_handle, address_from_pointer4+0x758)

address_from_pointer5 = pointer_object5.value  # shouldn't be hex for later use

print(f"5. {hex(address_from_pointer5)}")

pointer_object6 = RemotePointer(pm.process_handle, address_from_pointer5+0x0)

address_from_pointer6 = pointer_object6.value  # shouldn't be hex for later use

print(f"6. {hex(address_from_pointer6)}")

final_address = address_from_pointer6 + 0x10

value_at_final_address = pm.read_bytes(final_address, 31)

print(f"7. {hex(final_address), value_at_final_address }")

pm.write_bytes(final_address, b'http://192.168.001.111/cgi-bin/', 31)

print(f"8. {hex(final_address), value_at_final_address }")

exit(0)
