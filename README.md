# KUBERNETES METRICS COLLECTOR DETAILS
Zebrium's Kubernetes metrics collector sends metrics to Zebrium for automated Anomaly detection.
Our github repository is located [here](https://github.com/zebrium/ze-stats).

# ze-stats
## Features
* One step deployment using helm commands
* Sends metrics from all nodes in a Kubernetes cluster
* Runs a single instance of the metrics collector in a Kubernetes cluster, and runs node-exporter on every node in the same Kubernetes cluster.

## Getting Started
### Installing via helm
#### helm version 2
1. `helm install --namespace zebrium  --name zstats-collector --repo https://raw.githubusercontent.com/zebrium/ze-stats/master/charts zstats --set zebrium.collectorUrl=YOUR_ZE_STATS_API_URL,zebrium.authToken=YOUR_ZE_API_AUTH_TOKEN,zebrium.deployment=YOUR_DEPLOYMENT_NAME`

#### helm version 3
1. `kubectl create namespace zebrium`
2. `helm install zstats-collector zstats --namespace zebrium --repo https://raw.githubusercontent.com/zebrium/ze-stats/master/charts --set zebrium.collectorUrl=YOUR_ZE_STATS_API_URL,zebrium.authToken=YOUR_ZE_API_AUTH_TOKEN,zebrium.deployment=YOUR_DEPLOYMENT_NAME`

*IMPORTANT* The two helm commands for version 2 and version 3 above, install node-exporter pods automatically on all nodes. If node-exporter is already installed in the kubernetes cluster, the helm command line option `nodeExporter.enabled=false` should be used to avoid duplicated node-exporter deployments.

### Uninstalling via helm

If you used the "helm install" command to install zlog-collector chart, you should use the following command to delete:
```
helm delete --purge zstats-collector
```

## Configuration
No special configuration is required

### Setup
By default, Zebrium's Kubernetes metrics collector will be deployed to all Nodes in your cluster and collect metrics from every node.

## Testing your installation
Once the collector has been deployed in your Kubernetes environment, your metrics and anomaly detection will be available in the Zebrium UI.

## Contributors
* Anil Nanduri (Zebrium)
* Dara Hazeghi (Zebrium)
* Brady Zuo (Zebrium)
