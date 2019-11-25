# Logging

## Requirements

Download OC command and ensure that it is is in your `$PATH` For example
```
# curl -O https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/openshift-client-linux-4.2.7.tar.gz
# tar xvzf openshift-client-linux-4.2.7.tar.gz
# cp oc /usr/local/bin
```
Install podman
``` yum install -y podman ```

Install Ansible and its dependencies
``` pip install -r requirements.txt```

## Playbook

The `logging.yml` playbook uses the `mirror-operator` and `deploy-logging` roles. The playbook assumes you have Internet connection and is able to reach OpenShift and your local registry. 

The local registry is the repository that OpenShift is using for disconnected install. 

The playbook uses a `local` connection. 

The following variables should be defined:

| Name | Description |
| -- | -- |
| k8s_api_endpoint | OpenShift API endpoint. Example api.ocp.example.com:6443|
| k8s_admin  | cluster-admin user. Default is kubeadmin. |
| k8s_validate_certs | Whether to validate API cert. Default is true. |
[ocp_local_registry | The local registry. Example `my-registry.example.com:5000`. |
|ocp_local_registry_validte_carts | Whether to validate the registry cert. Default is true. |
|ocp_local_registry_insecure | Whether to use insecure (http). Default is false. Otherwise add your registry cert into ca-bundle | 
| registry_auth| Auth token for the local registry and registry.redhat.io. |
| logging_cr | [Logging Custom Resource](https://docs.openshift.com/container-platform/4.2/logging/cluster-logging-deploying.html) |

registry.redhat.io authentication can be taken from [cloud.redhat.com](https://cloud.redhat.com) pull secret or by creating a Service Account at [registry.redhat.io](https://registry.redhat.io).

`registry_auth` should be created in vault.yml in this format:
```
registry_auth:
  auths:
    my-registry.example.com:5000: 
      auth: XXX
    registry.redhat.io:
      auth: XXX
```
### Running the playbook
```ansible-playbook --ask-vault-pass logging.yml ```

## Known Issues
### RHEL7 jinja2
On RHEL 7, the python-jinja2 is too old and needs to be updated. You can use a virtualenv to prevent messing up the system's python site-packages.  

``` virtualenv --system-site-packages my-virtual-env```, this will prevent the  libselinux-python issue in the virtual environment

