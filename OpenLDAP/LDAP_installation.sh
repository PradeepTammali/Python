
# LDAP instalaltion guide

# Get the software
# You can obtain a copy of the software by following the instructions on the OpenLDAP Software download page (http://www.openldap.org/software/download/). It is recommended that new users start with the latest release.

wget ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/openldap-2.4.44.tgz

mkdir /opt/ldap/

mv openldap-2.4.44.tgz /opt/ldap/

cd /opt/ldap/

# Unpack the distribution
# Pick a directory for the source to live under, change directory to there, and unpack the distribution using the following commands:

gunzip -c openldap-2.4.44.tgz | tar xvfB -

# then relocate yourself into the distribution directory:

cd openldap-2.4.44

# Run configure
# You will need to run the provided configure script to configure the distribution for building on your system. The configure script accepts many command line options that enable or disable optional software features. Usually the defaults are okay, but you may want to change them. To get a complete list of options that configure accepts, use the --help option:

# ./configure --help


# However, given that you are using this guide, we'll assume you are brave enough to just let configure determine what's best:

./configure

# Build the software.
# The next step is to build the software. This step has two parts, first we construct dependencies and then we compile the software:

make depend

make

# Both makes should complete without error.

# Test the build.
# To ensure a correct build, you should run the test suite (it only takes a few minutes):

make test
# Tests which apply to your configuration will run and they should pass. Some tests, such as the replication test, may be skipped.

# Install the software.
# You are now ready to install the software; this usually requires super-user privileges:

su root -c 'make install'

# Everything should now be installed under /opt/ldap/ (or whatever installation prefix was used by configure).

# Edit the configuration file.
# Use your favorite editor to edit the provided slapd.ldif example (usually installed as /usr/local/etc/openldap/slapd.ldif) to contain a MDB database definition of the form:

dn: olcDatabase=mdb,cn=config
objectClass: olcDatabaseConfig
objectClass: olcMdbConfig
olcDatabase: mdb
OlcDbMaxSize: 1073741824
olcSuffix: dc=ldapdomain,dc=com
olcRootDN: cn=Manager,dc=ldapdomain,dc=com
olcRootPW: secret
olcDbDirectory: /opt/ldap/var/openldap-data
olcDbIndex: objectClass eq

# Import the configuration database
# You are now ready to import your configration database for use by slapd(8), by running the command:

su root -c /usr/local/sbin/slapadd -f /usr/local/etc/cn=config -l /usr/local/etc/openldap/slapd.ldif

# Start SLAPD.
# You are now ready to start the Standalone LDAP Daemon, slapd(8), by running the command:

su root -c /usr/local/libexec/slapd -f /usr/local/etc/cn=config

# To check to see if the server is running and configured correctly, you can run a search against it with ldapsearch(1). By default, ldapsearch is installed as /usr/local/bin/ldapsearch:

ldapsearch -x -b '' -s base '(objectclass=*)' namingContexts

# Note the use of single quotes around command parameters to prevent special characters from being interpreted by the shell. This should return:
#	dn:
#	namingContexts: dc=example,dc=com

# Add initial entries to your directory.
# You can use ldapadd(1) to add entries to your LDAP directory. ldapadd expects input in LDIF form. We'll do it in two steps:

# create an LDIF file
# run ldapadd

# Use your favorite editor and create an LDIF file that contains:

dn: dc=ldapdomain,dc=com
objectclass: dcObject
objectclass: organization
o: NIFI
dc: ldapdomain

dn: cn=Manager,dc=ldap,dc=com
objectclass: organizationalRole
cn: Manager

# Now, you may run ldapadd(1) to insert these entries into your directory.

ldapadd -x -D "cn=Manager,dc=ldapdomain,dc=com" -W -f ldapdomain.ldif

# where example.ldif is the file you created above.

# See if it works.
# Now we're ready to verify the added entries are in your directory. You can use any LDAP client to do this, but our example uses the ldapsearch(1) tool.

ldapsearch -x -b 'dc=ldapdomain,dc=com' '(objectclass=*)'

# This command will search for and retrieve every entry in the database.

# You are now ready to add more entries using ldapadd(1) or another LDAP client, experiment with various configuration options, backend arrangements, etc..


