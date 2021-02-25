### Playbook for WebLogic cluster installation

#### Before you begin

Download [Linux x64 Compressed Archive](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html) and place archive to:

```
./roles/jdk/files/jdk-8u271-linux-x64.tar.gz
```

Also set archive name as variable in file [infra.yml](group_vars/infra.yml)

```yml
jdk_installer_archive: 'jdk-8u271-linux-x64.tar.gz'
```

Download [Generic Installer for Oracle WebLogic Server 12.2.1.4](https://www.oracle.com/middleware/technologies/weblogic-server-installers-downloads.html), extract archive and place installer to:

```
./roles/wls/files/fmw_12.2.1.4.0_wls.jar
```

Also set installer name as variable in file [infra.yml](group_vars/infra.yml)

```yml
fmw_installer: 'fmw_12.2.1.4.0_wls.jar'
```

<br>

Configure [hosts.ini](hosts.ini) file:

```ini
[all:vars]
ansible_user='<sudo_user>'
ansible_password='<sudo_user_pass>'
...

[all]
<host_name1> ansible_ssh_host=<host_ip> ansible_ssh_port=22
<host_name2> ansible_ssh_host=<host_ip> ansible_ssh_port=22
<host_name3> ansible_ssh_host=<host_ip> ansible_ssh_port=22

[wl_admin]
<host_name1>

[wl_node]
<host_name2>
<host_name3>
```

Edit variables for your needs in files:

```
./group_vars/infra.yml
./group_vars/secrets.yml
```

<br>

#### Shared WebLogic domain - check nfs [configuration](group_vars/nfs_infra.yml) file.

* `nfs_external_source: true` - will mount external share on all cluster servers
* `nfs_external_source: false` - will set up nfs server => admin server / client => all hosts under wl_node group

```shell
$ ansible-playbook nfs.yml
```

#### Run installation playbook

* Weblogic console URL after installation: http://<admin_host_ip>:{{ admin_server_port }}/console

```shell
$ ansible-playbook weblogic.yml
```

#### Uninstall cluster

```shell
$ ansible-playbook reset.yml
```