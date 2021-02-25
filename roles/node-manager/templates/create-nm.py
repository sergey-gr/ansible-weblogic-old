# Connect to WebLogic admin server
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass}}', '{{ hostvars[groups['wl_admin'][0]]['ansible_ssh_host'] }}:{{ admin_server_port }}')

nmEnroll('{{ domain_home }}', '{{ nm_home }}/{{ inventory_hostname }}')

edit()
startEdit()

# Create the node manager reference.
cd('/')
cmo.createUnixMachine('{{ inventory_hostname }}')
cd('/Machines/{{ inventory_hostname }}//NodeManager/{{ inventory_hostname }}')
cmo.setListenAddress('{{ ansible_ssh_host }}')
cmo.setListenPort(int('{{ nm_listen_port }}'))
cmo.setNMType('Plain')
cmo.setName('{{ inventory_hostname }}')
cmo.setNodeManagerHome('{{ nm_home }}/{{ inventory_hostname }}')

save()
activate()

disconnect()
exit()