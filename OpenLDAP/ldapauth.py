import ldap
try:
	#l = ldap.open("127.0.0.1")
	l = ldap.initialize('ldap://10.138.89.66:389')
	# you should  set this to ldap.VERSION2 if you're using a v2 directory
	l.protocol_version = ldap.VERSION3
	# Pass in a valid username and password to get
	# privileged directory access.
	# If you leave them as empty strings or pass an invalid value
	# you will still bind to the server but with limited privileges.

	#username = "cn=Manager, o=anydomain.com"
	#password  = "secret"

	username = "uid=john,ou=People,dc=ldaplocal,dc=com"
	password = "johnldap"

	# Any errors will throw an ldap.LDAPError exception
	# or related exception so you can ignore the result
	ret = l.simple_bind_s(username, password)
	print(ret)

	#deleteDN = "uid=john,ou=People,dc=ldaplocal,dc=com"
	#try:
	# you can safely ignore the results returned as an exception
	# will be raised if the delete doesn't work.
	#	l.delete_s(deleteDN)
	#except ldap.LDAPError, e:
#		print e
#		print "this is error"
except ldap.LDAPError as e:
	print(e)
	print("error")
#except ldap.INVALID_CREDENTIALS:
#	print('wrong password provided')
#	# handle error however you like


# reference links are
#  http://stackoverflow.com/questions/4784775/ldap-query-in-python
#  http://stackoverflow.com/questions/10725891/authenticating-to-active-directory-with-python-ldap-always-returns-97
