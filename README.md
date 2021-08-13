![Logo](https://www.gurobi.com/wp-content/uploads/2018/12/logo-final.png "Gurobi Optimization")
# Quick reference
Maintained by: [Gurobi Optimization](https://www.gurobi.com)

Where to get help: [Gurobi Support](https://www.gurobi.com/support/), [Gurobi Documentation](https://www.gurobi.com/documentation/)

# Supported tags and respective Dockerfile links

* [9.1.2, latest](https://github.com/Gurobi/docker-python-/blob/master/9.1.2/Dockerfile)


When building a production application, we recommend using an explicit version number instead of the `latest` tag.
This way, you are in control of the upgrade process of your application.

# Quick reference (cont.)

Supported architectures: linux amd64

Published image artifact details: https://github.com/Gurobi/docker-python-example

# What is `gurobi/python-example`?
The Gurobi Optimizer is the fastest and most powerful mathematical programming solver available 
for your LP, QP and MIP (MILP, MIQP, and MIQCP) problems. 
More info at the [Gurobi Website](https://www.gurobi.com/products/gurobi-optimizer/).

The Gurobi Optimizer comes with a Python extension module called “gurobipy” that offers convenient 
object-oriented modeling constructs and an API to all Gurobi features. 
More info in the [Quick Start Guide](https://www.gurobi.com/documentation/current/quickstart_windows/cs_python.html).

The `gurobi/python-example` image provides an example to use the `gurobi/python` as a base Docker image.

## Getting a Gurobi license

This image has been created to work with a Web License. The [Web License Service](https://www.gurobi.com/web-license-service/) (WLS) is a new Gurobi licensing service 
  for containerized environments (Docker, Kubernetes...). Gurobi components can automatically request and renew license tokens to 
  the WLS servers available in several regions worldwide. WLS only requires that your container has access to the 
  Internet. Commercial users can request an evaluation and academic users can request a free license.
  Please register to access the [Web License Manager](https://license.gurobi.com) and read the
  [documentation](https://license.gurobi.com/manager/doc/overview)

Please contact your sales representative at [sales@gurobi.com](mailto:sales@gurobi.com) to discuss licensing options. 

## Using the client license

This images has been created to pass the license information in the following environment variables:
* GRB_WLSACCESSID: Access ID for Gurobi Web License Service
* GRB_WLSSECRET: Secret Key for Gurobi Web License Service
* GRB_LICENSEID: License ID for Gurobi Web License Service

# How to use this image?


# License

By downloading and using this image, you agree with the 
[End-User License Agreement](https://www.gurobi.com/EULA) for the Gurobi software contained in this image.

As with all Docker images, these likely also contain other software which may be under other 
licenses (such as Bash, etc from the base distribution, along with any direct or indirect 
dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any use 
of this image complies with any relevant licenses for all software contained within.