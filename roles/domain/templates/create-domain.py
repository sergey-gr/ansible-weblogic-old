import os

# Open basic domain template
readTemplate(os.environ['WL_HOME']+'/common/templates/wls/wls.jar')

# Set base options
setOption('DomainName', '{{ domain_name }}')
setOption('JavaHome', '{{ java_home }}')
setOption('ServerStartMode', '{{ start_mode }}')

# Configure the Administration Server port
cd('/Server/{{ admin_server_name }}')
cmo.setListenPort(int('{{ admin_server_port}}'))

# Define the default user password.
cd('/Security/base_domain/User/weblogic')
cmo.setName('{{ weblogic_admin }}')
cmo.setPassword('{{ weblogic_admin_pass }}')

# Save the domain
writeDomain('{{ domain_home }}')

# Close the current domain template
closeTemplate()
exit()