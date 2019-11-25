This playbook helps to mirror OpenShift repository into your local copy.

You will need to define the following variables

| | |
| -- | -- |
| ocp_release | OpenShift version | 
| local_registry |  Your local repository. For example: my-registry.example.com:5000 |local_repository | The local repository for the mirror | 
|local_registry_insecure | Whether to use insure mode(http) to connect to the local repository |

### OpenShift version

Refer to this [article](https://access.redhat.com/solutions/4583231)

Alternatively, run this
`$ curl -sH 'Accept:application/json' 'https://api.openshift.com/api/upgrades_info/v1/graph?channel=stable-4.2' | ./graph.sh | dot -Tsvg | magick - /tmp/graph.png`

graph.sh is available [here](https://github.com/openshift/cincinnati/blob/master/hack/graph.sh)

dot is from Graphviz

magick is from ImageMagick
