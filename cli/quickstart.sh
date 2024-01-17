# Login to Globus
globus login

# Test you are logged in
globus get-identities -v 'go@globusid.org'
globus endpoint search 'Globus Tutorial Endpoint' --filter-owner-id 'c699d42e-d274-11e5-bf75-1fc5bf53bb24'

# Not supported
globus ls 'ddb59aef-6d04-11e5-ba46-22000b92c6ec:/'
