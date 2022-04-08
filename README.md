# fermilab-util_makehostkeys

The makehostkeys utility has a long history at Fermilab.

It is useful for generating the traditional host/ftp/http principle keytabs.

This script can be easily modified for any kerberos realm.  Set `REALM=` whatever Kerberos realm you'd like near the top.

If you want to package up this modified script in an RPM, you may want to edit the `spec` file to note your changes and not request the fermilab kerberos config.
