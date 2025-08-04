# netbox-certificates
A model for Certificates and their distribution in Netbox

## Features

Represent the following items in Netbox:
- Certificate Authorities
- Certificates
- Certificate Instances

Additional data that this plugin affords:
- Certificates
    - Common Names
    - SANs
    - Status (extendable via plugin_configuration option)
    - Type (OV, DV, EV etc.) (extendable via plugin_configuration option)
    - Term
    - Install type
    - Device / VM installed on
    - File system location
    - Vault URLs
    - A place to record the commands to install and make live a certificate
    - A certificate check command that could be used to check the certificate is live (monitoring and back into Netbox)
    - Whether the certificate is used behind a load balancer
    - Is the install automated (ACME, script etc.)
    - The contacts in your business using Netbox's in built Contact model.
    - Instances of the certificate and their status

- Certificate Instances:
    - The certificate authority the instance was ordered through
    - CN
    - Status (extendable via plugin_configuration option)
    - CA reference
    - CA Issuer
    - Public Key Alg., key size and sha1
    - The term of the instance
    - Serial Number
    - Issue Date
    - Expiry
    - Who installed the cert (Netbox Contact)

- Certificate Authorities
    - Name
    - Count of issued instances
    - Status (extendable via plugin_configuration option)
    - CA's org ID
    - ACME URLs (for scripting)
    - Admin URL 
    - Fields for OV and EV profile ID (for automation of new cert requests.)

This plugin makes the distinction between a certificate and it's instances. This way this enables you to track each new 'instance' of the certificate through the certificate lifecycle, which is handy when it comes to things such as monitoring.

This plugin is supposed to be used as a central repository for all certificate related information. It intended audience is for certificate admins that have the ability to use NetBox's API to script the input of certificates from multiple sources (if required) for a global view of certificates and their expiry.

## Compatibility

| NetBox Version | Branch |
|----------------|----------------|
|     4.3+       |      v4.3     |
|  4.0 - 4.2     |      v4.2     |
|     < 3.6+       |      Not supported     |

**THIS PLUGIN CURRENTLY DOES NOT HAVE A PRESENCE ON PYPI.**

## Installation

To install this plugin:

Activate your virtual env and install via pip:
```
pip install git+https://github.com/NetworkSeb/netbox-certificates.git
```

```no-highlight
# echo git+https://github.com/NetworkSeb/netbox-certificates.git >> local_requirements.txt
```

If installing for Netbox version 4.0 - 4.2.x:
```
pip install git+https://github.com/NetworkSeb/netbox-certificates.git@v4.2
```

```no-highlight
# echo git+https://github.com/NetworkSeb/netbox-certificates.git@v4.2 >> local_requirements.txt
```

### Enable the Plugin

In the Netbox `configuration.py` configuration file add or update the PLUGINS parameter, adding `netbox_certificates`:

```python
PLUGINS = [
    'netbox_certificates',
]
```

### Apply Database Migrations

Apply database migrations with Netbox `manage.py`:

```
(venv) $ python manage.py migrate
```

### Restart Netbox

Restart the Netbox service to apply changes:

```
sudo systemctl restart netbox
```

## Screenshots

Coming soon!