
print("INPUT PARAMETERS FOR NPN TRANSISTOR: ")
maxpower = float(input("Max collector power dissipation (mW): ")) / 1000.0
supply = float(input("Supply voltage (V): "))
pn_voltage = float(input("Base p-n opening voltage (mV): ")) / 1000.0
hfe = float(input("Hfe: "))
k = float(input("k: "))

half_supply = supply / 2

maxpower = maxpower * 0.8

Ic = maxpower / half_supply


Rc_plus_e = half_supply / Ic

Re = (half_supply / Ic) / (1+k)

Rc = Re*k

Ube = pn_voltage + Ic*Re

Ib = Ic / hfe

Ibase_delimeter = 10*Ib

Rdelim_bottom = Ube / Ibase_delimeter

Rdelim_top = (supply - Ube) / Ibase_delimeter

Ic_max = supply / (Rc + Re)
Ishort_circuit = supply / Rc # short circuit on load

print("RESULT: ")
#print("Ic = " + str(Ic*1000) + " mA")
print("Rc = " + str(Rc) + " Omh")
print("Re = " + str(Re) + " Omh")
print("Rdelim_bottom = " + str(Rdelim_bottom) + " Omh")
print("Rdelimeter_top = " + str(Rdelim_top) + " Omh")

print("Pc_max = " + str(Rc*Ishort_circuit**2) + " W")
print("Pe_max = " + str(Re*Ic_max**2) + " W")
