# Connect to WebLogic admin server
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass}}', '{{ hostvars[groups['wl_admin'][0]]['ansible_ssh_host'] }}:{{ admin_server_port }}')

edit()
startEdit()

# Setting domain JTA transaction timeout seconds
cd('/JTA/{{ domain_name }}')
# Maximum time, an active transaction is allowed to be in the first phase of a transaction
cmo.setTimeoutSeconds({{ jta_timeout_sec }})

# The maximum number of simultaneous in-progress transactions allowed
# cmo.setMaxTransactions(20000)
# The time  a transaction manager waits for transactions involving the resource to complete
# cmo.setUnregisterResourceGracePeriod(25)
# maximum time a transaction manager persists in attempting to complete the second phase
# cmo.setAbandonTimeoutSeconds(80000)
# Indicates that XA calls are executed in parallel if there are available threads
# cmo.setParallelXAEnabled(true)
# automatically performs an XA Resource forget for heuristic transaction completions
# cmo.setForgetHeuristics(true)
# the two-phase commit protocol is used
# cmo.setTwoPhaseEnabled(true)
# maximum cycles that the transaction manager performs the beforeCompletion synchronization
# cmo.setBeforeCompletionIterationLimit(20)
# interval the transaction manager creates a new transaction log           
# cmo.setCheckpointIntervalSeconds(200)
# Specifies transport security mode required by WebService Transaction endpoints
# cmo.setSecurityInteropMode('default')
# XA calls are executed in parallel if there are available threads
# cmo.setParallelXAEnabled(false)
# Maximum number of concurrent requests to resources allowed for each server
# cmo.setMaxResourceRequestsOnServer(60)
# transport security mode required by WebService Transaction endpoints
# cmo.setWSATTransportSecurityMode('SSLNotRequired')
# Maximum allowed time duration, in milliseconds, for XA calls to resources
# cmo.setMaxXACallMillis(100000)
# maximum time, in seconds, a transaction manager waits for all resource managers to respond
# cmo.setCompletionTimeoutSeconds(0)
# Maximum duration time, in milliseconds, that a resource is declared dead
# cmo.setMaxResourceUnavailableMillis(1500000)

save()
activate()

disconnect()
exit()