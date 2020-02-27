# KUBERNETES STATS COLLECTOR DETAILS
Zebrium's Kubernetes stats collector sends stats to Zebrium for automated Anomaly detection.
Our github repository is located [here](https://github.com/zebrium/ze-stats).

# ze-stats
## Features
* One step deployment using helm commands
* Sends stats from all nodes in a Kubernetes clusters
* Runs a single instance of the stats collector in a Kubernetes cluster, and runs node-exporter on every node in the same kubernetes cluster.

## Getting Started
### Installing via helm
#### helm version 2
1. `helm install --namespace zebrium  --name zstats-collector --repo https://raw.githubusercontent.com/zebrium/ze-stats/master/charts zstats --set zebrium.collectorUrl=YOUR_ZE_STATS_API_URL,zebrium.authToken=YOUR_ZE_API_AUTH_TOKEN,zebrium.deployment=YOUR_DEPLOYMENT_NAME`

#### helm version 3
1. `kubectl create namespace zebrium`
2. `helm install zstats-collector zstats --namespace zebrium --repo https://raw.githubusercontent.com/zebrium/ze-stats/master/charts --set zebrium.collectorUrl=YOUR_ZE_STATS_API_URL,zebrium.authToken=YOUR_ZE_API_AUTH_TOKEN,zebrium.deployment=YOUR_DEPLOYMENT_NAME`

### Uninstalling via helm

If you used the "helm install" command to install zlog-collector chart, you should use the following command to delete:
```
helm delete --purge zstats-collector
```

## Configuration
No special configuration is required

### Setup
By default, Zebrium's kubernetes stats collector will be deployed to all Nodes in your cluster and collect stats from every node.

## Testing your installation
Once the collector has been deployed in your Kubernetes environment, your stats and anomaly detection will be available in the Zebrium UI.

## Contributors
* Anil Nanduri (Zebrium)
* Dara Hazeghi (Zebrium)
* Brady Zuo (Zebrium)
