# ---- First Menu ---- #
def menu():

    print("=========================")
    print("Menu")
    print("=========================")
    print("")
    print("In this software, you can type your PC Components, and then you will have a complete list.")
    print("")
    print("Note!")
    print("This software doesn't check the compatibilities. You can choose incompatible parts,")
    print("but it prevents unrealistic values automatically.")
    print("")

start = False
while not start:
    menu()
    option = input("Choose 1 to Start and 2 to Exit: " )
    if option == "1":
        print("Starting Program...\n")
        start = True
    elif option == "2":
        print("Exiting....")
        exit()
    else:
        print("invalid option")

# ---- Case; MOBO; CPU; CPU Cooler ---- #

case = input("What is your PC Case? ")
motherboard = input("What is your Motherboard? ")
cpu = input("What is your CPU? ")
cpu_cooler = input("What is your CPU Cooler? ")

# ---- RAM ---- #

ramq = False
while ramq == False:
    ram_quantity = int(input("How many RAM sticks do you have (1-8)? "))
    if ram_quantity in [1,2,4,8]:
        ramq = True
    else:
        print("Invalid! You can have between 1 and 8 RAM sticks.")

ram = input("What is your RAM? ")

# ---- M.2 ---- #

m2q = False
while not m2q:
    m2_quantity = int(input("How many M.2 drives do you have? (0-5) "))
    if 0 <= m2_quantity <= 5:
        m2q = True
    else:
        print("Invalid! You can have between 0 and 5 M.2 Drives.")

m2 = []

for i in range(1, m2_quantity + 1):
    drive = input(f"What is your M.2 drive number {i}? ")
    m2.append(drive)

# ---- SSD ---- #

ssdq = False
while not ssdq:
    ssd_quantity = int(input("How many SSD's do you have? (0-5) "))
    if 0 <= ssd_quantity <= 5:
        ssdq = True
    else:
        print("Invalid! You can have between 0 and 5 SSD's.")

ssd = []

for i in range(1, ssd_quantity + 1):
    drive = input(f"What is your SSD number {i}? ")
    ssd.append(drive)

# ---- HDD ---- #

hddq = False
while not hddq:
    hdd_quantity = int(input("How many HDD's do you have? (0-5) "))
    if 0 <= hdd_quantity <= 5:
        hddq = True
    else:
        print("Invalid! You can have between 0 and 5 HDD's.")

hdd = []

for i in range(1, hdd_quantity + 1):
    drive = input(f"What is your HDD number {i}? ")
    hdd.append(drive)

# ---- GPU ---- #

gpuq = False
while not gpuq:
    gpu_quantity = int(input("How many GPU's do you have? (1-6) "))
    if 1 <= gpu_quantity <= 6:
        gpuq = True
    else:
        print("Invalid! You can have between 1 and 6 GPU's.")

gpu = []

for i in range(1, gpu_quantity + 1):
    drive = input(f"What is your GPU number {i}? ")
    gpu.append(drive)

# ---- Fans ---- #

fanq = False
while not fanq:
    fan_quantity = int(input("How many Fans do you have? (0-20) "))
    if 0 <= fan_quantity <= 20:
        fanq = True
    else:
        print("Invalid! You can have between 0 and 20 Fans.")

fan = []

for i in range(1, fan_quantity + 1):
    drive = input(f"What is your fan number {i}? ")
    fan.append(drive)

# ---- PSU ---- #

psu = input("What is your PSU? ")

# ---- Monitors ---- #

monitorq = False
while not monitorq:
    monitor_quantity = int(input("How many Monitors do you have? (1-9) "))
    if 1 <= monitor_quantity <= 9:
        monitorq = True
    else:
        print("Invalid! You can have between 1 and 9 Monitor's.")

monitor = []

for i in range(1, monitor_quantity + 1):
    drive = input(f"What is your Monitor number {i}? ")
    monitor.append(drive)


# ---- Peripherals ---- #
keyboard = input("What is your Keyboard? ")
mouse = input("What is your Mouse? ")
speaker = input("What is your Speaker? ")
phones = input("What is your Earphone or Headphone? ")
mic = input("What is your Microphone? ")
webcam = input("What is your Webcam? ")

# ---- Thermal Compound ---- #

thermal_compound = input("What is your Thermal Compound? ")

# ---- OS ---- #

osq = False
while not osq:
    os_quantity = int(input("How many OS's do you have? (1-2) "))
    if 0 <= os_quantity <= 5:
        osq = True
    else:
        print("Invalid! You can have between 1 and 2 OS's")

os = []

for i in range(1, os_quantity + 1):
    system = input(f"What is your OS number {i}? ")
    os.append(system)

# ---- Text List ----

def text(items, name):
    if len(items) == 0:
        return f"no {name}s"
    if len(items) == 1:
        return f"a {items[0]} {name}"
    return f"{', '.join(items[:-1])} and {items[-1]} {name}s"


# ---- Final PC List ----

print("\nYour Desktop:\n")
print(f"Case: {case}")
print(f"Motherboard: {motherboard}")
print(f"CPU: {cpu}")

for i in range(ram_quantity):
    print(f"RAM {i+1}: {ram}")

for i in range(m2_quantity):
    print(f"M.2 {i+1}: {m2[i]}")

for i in range(ssd_quantity):
    print(f"SSD {i+1}: {ssd[i]}")

for i in range(hdd_quantity):
    print(f"HDD {i+1}: {hdd[i]}")

for i in range(gpu_quantity):
    print(f"GPU {i+1}: {gpu[i]}")

for i in range(fan_quantity):
    print(f"Fan {i+1}: {fan[i]}")

print(f"PSU: {psu}")

for i in range(monitor_quantity):
    print(f"Monitor {i+1}: {monitor[i]}")

print(f"Keyboard: {keyboard}")
print(f"Mouse: {mouse}")
print(f"Speaker: {speaker}")
print(f"EarphonesHeadphones {phones}")
print(f"Webcam {webcam}")
print(f"Thermal Compound {thermal_compound}")

for i in range(os_quantity):
    print(f"OS {i+1}: {os[i]}")


# ---- Final Text List ----

print("")
print("")
print("")

print(
    f"You have a {case} case, a {motherboard} motherboard with a {cpu} CPU "
    f"cooled by a {cpu_cooler}, {ram_quantity} {ram} RAM sticks, "
    f"{text(m2, 'M.2 drive')}, "
    f"{text(ssd, 'SSD')}, "
    f"{text(hdd, 'HDD')}, "
    f"{text(gpu, 'GPU')}, "
    f"{text(fan, 'fan')}, "
    f"a {psu} PSU, "
    f"{text(monitor, 'monitor')}, "
    f"a {keyboard} keyboard, a {mouse} mouse, "
    f"a {speaker} speaker, {phones} headphones, "
    f"a {webcam} webcam, "
    f"{thermal_compound} thermal compound "
    f"and {text(os, 'operating system')}. " 
)

exit = input("Press Enter to Exit....")

if exit == "":
    exit

else:
    print("Something was wrong.")

input("Press Enter Again to Exit....")
