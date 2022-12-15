LDAP Injection (Python)
LDAP injection is a type of injection attack. Injection attacks occur when maliciously crafted inputs are submitted by an attacker, causing an application to perform an unintended action. LDAP injection attacks allow an attacker to override authentication protections or manipulate data in your directory information service.

LDAP (Lightweight Directory Access Protocol) is a common method of querying a directory information service that contains information about users, systems and devices. The most common LDAP server is Microsoft's Active Directory, used by Windows domain networks. Code accessing an LDAP server frequently uses parameters coming from an untrusted source to make queries against the user data.

For example: when a user attempts to log into a website, the username parameter supplied in the HTTP request may be incorporated into an LDAP query to check the user's credentials. It is important that LDAP queries run against the directory service are constructed securely, to ensures attackers cannot inject extra statements or change the logic of an existing statement.

