from pymem import Pymem
from pymem.ptypes import RemotePointer
from time import sleep
import subprocess

def run_the_game():
    subprocess.Popen("masq67.exe")
    print("CLIENT: Game was called.")

def change_url_in_ram(local_ip):  # local_ip
    sleep(0.5) # this is perfect on a fast machine
    while True:
        try:
            pm = Pymem("masq67.exe")

            base_address = 0x00400000
            offset_to_pointer = 0x0001E1B8

            pointer_object = RemotePointer(pm.process_handle, base_address + offset_to_pointer)

            address_from_pointer = pointer_object.value  # shouldn't be hex for later use

            # print(f"0. {hex(address_from_pointer)}")

            pointer_object1 = RemotePointer(pm.process_handle, address_from_pointer+0x18)

            address_from_pointer1 = pointer_object1.value  # shouldn't be hex for later use

            # print(f"1. {hex(address_from_pointer1)}")

            pointer_object2 = RemotePointer(pm.process_handle, address_from_pointer1+0x560)

            address_from_pointer2 = pointer_object2.value  # shouldn't be hex for later use

            # print(f"2. {hex(address_from_pointer2)}")

            pointer_object3 = RemotePointer(pm.process_handle, address_from_pointer2+0x534)

            address_from_pointer3 = pointer_object3.value  # shouldn't be hex for later use

            # print(f"3. {hex(address_from_pointer3)}")

            pointer_object4 = RemotePointer(pm.process_handle, address_from_pointer3+0x14)

            address_from_pointer4 = pointer_object4.value  # shouldn't be hex for later use

            # print(f"4. {hex(address_from_pointer4)}")

            pointer_object5 = RemotePointer(pm.process_handle, address_from_pointer4+0x758)

            address_from_pointer5 = pointer_object5.value  # shouldn't be hex for later use

            # print(f"5. {hex(address_from_pointer5)}")

            pointer_object6 = RemotePointer(pm.process_handle, address_from_pointer5+0x0)

            address_from_pointer6 = pointer_object6.value  # shouldn't be hex for later use

            # print(f"6. {hex(address_from_pointer6)}")

            final_address = address_from_pointer6 + 0x10

            value_at_final_address = pm.read_bytes(final_address, 31)

            # print(hex(final_address), value_at_final_address)

            formatted_ip = '.'.join([i.zfill(3) for i in local_ip.split('.')])

            new_url = b'http://'+bytes(formatted_ip, 'ascii')+b'/cgi-bin/'

            pm.write_bytes(final_address, new_url, 31)

            value_final_after_change = pm.read_bytes(final_address, 31)

            # print(hex(final_address), value_final_after_change)
            
            print("CLIENT: Server URL was injected in the game successfully.")
            break
        except Exception as e:
            # print(e)
            sleep(0.5)
            pass
