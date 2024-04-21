vendors = {'nokia':'SROS', 'cisco': 'IOS', 'juniper': 'JUNOS'}
vendors['arista'] = 'EOS'

for key, value in vendors.items():
    print(f'{key}:{value}')