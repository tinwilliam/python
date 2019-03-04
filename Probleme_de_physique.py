train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#fonction pour convertir la temperature en Farenheit en degre Celsius
def f_to_c(f_temp):
  return  (f_temp-32)*5/9
#test a 100°F
f100_in_celsius=f_to_c(100)
print(f100_in_celsius)

#fonction pour convertir en degre farenheit
def c_to_f(c_temp):
  return  (c_temp*9/5+32)
#test a 0°C
c0_in_farenheit=c_to_f(0)
print(c0_in_farenheit)

 #fonction pour obtenir la force
def get_force(mass,acceleration):
  return (mass*acceleration)
#test avec les donnees de depart en hypothese
train_force=get_force(train_mass,train_acceleration)
print(train_force)
print("The GE train supplies " +str(train_force)+" Newtons of force")
# definition fonction energie
def get_energy(mass,c=3*10**8):

  return mass*c**2
#test de la fonction energie
bomb_energy=get_energy(bomb_mass)
print(bomb_energy)
print ("A 1kg bomb supplies "+str(bomb_energy)+" Joules.")

#definition fonction travail
def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration)*distance
#test de la fonction travail
train_work=get_work(train_mass,train_acceleration,train_distance)
print(train_work)
print("The GE train does "+str(train_work)+" Joules of work over Y meters.")