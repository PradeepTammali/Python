import ldap
l = ldap.initialize("ldap://127.0.0.1:389")
l.protocol_version = ldap.VERSION3
l.set_option(ldap.OPT_REFERRALS, 0)
l.simple_bind_s("uid=john,ou=People,dc=ldaplocal,dc=com", "johnldap")
