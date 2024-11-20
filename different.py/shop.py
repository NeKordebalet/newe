import json
file = open("sw_templates.json", 'r')
data = json.load(file) # read
data['access+trunk'] =['switchport mode access', #добавляем еще один эл-т в переменную
'switchport mode access',
  'switchport access vlan',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable',
 'switchport trunk encapsulation dot1q',
  'switchport mode trunk',
  'switchport trunk native vlan 999',
  'switchport trunk allowed vlan']


file.close()

file = open("sw_templates.json", 'w') #открываю файл на запись
json.dump(data,file,sort_keys = True, indent=2)  #записываю новое значение в файл целиком 
#file.write(json)                                 #записываю новое значение в файл целиком

file.close()
