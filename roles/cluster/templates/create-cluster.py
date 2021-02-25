# Connect to WebLogic admin server
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass}}', '{{ hostvars[groups['wl_admin'][0]]['ansible_ssh_host'] }}:{{ admin_server_port }}')

edit()
startEdit()

# Create cluster.
cd('/')
cmo.createCluster('{{ ms_cluster_name }}')

cd('/Clusters/{{ ms_cluster_name }}')
cmo.setClusterMessagingMode('unicast')
cmo.setClusterBroadcastChannel('')
cmo.setClusterAddress('{{ ms_cluster_address }}')

save()
activate()

disconnect()
exit()