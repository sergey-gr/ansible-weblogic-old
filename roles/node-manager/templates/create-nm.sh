#!/bin/sh
domainHome="{{ domain_home }}"
nmHome="{{ nm_home }}/{{ inventory_hostname }}"

cp -R ${domainHome}/bin/*NodeManager.sh ${nmHome}
sed -i -e "s|NODEMGR_HOME=\"${domainHome}/nodemanager\"|NODEMGR_HOME=\"${nmHome}\"|g" ${nmHome}/startNodeManager.sh
sed -i -e "s|NODEMGR_HOME=\"${domainHome}/nodemanager\"|NODEMGR_HOME=\"${nmHome}\"|g" ${nmHome}/stopNodeManager.sh