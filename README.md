# KUBERNETES METRICS COLLECTOR DETAILS
Zebrium's Kubernetes metrics collector sends metrics to Zebrium for automated Anomaly detection.
Our github repository is located [here](https://github.com/zebrium/ze-stats).

# ze-stats
## Features
* One step deployment using helm commands
* Sends metrics from all nodes in a Kubernetes cluster
* Runs metrics collector in a Kubernetes cluster.

## Getting Started
### Installing via helm
#### helm version 2
1. If node-exporter has not been installed, install it first:
```
  helm install --set-string service.annotations."prometheus\.io/scrape"=true --set-string service.annotations."prometheus\.zebrium\.io/scrape"=true --namespace zebrium --name node-exporter stable/prometheus-node-exporter
```
2. `helm install --namespace zebrium  --name zstats-collector --repo https://raw.githubusercontent.com/zebrium/ze-stats/master/charts zstats --set zebrium.collectorUrl=YOUR_ZE_STATS_API_URL,zebrium.authToken=YOUR_ZE_API_AUTH_TOKEN,zebrium.deployment=YOUR_DEPLOYMENT_NAME`

#### helm version 3
1. `kubectl create namespace zebrium`
2. If node-exporter has not been installed, install it first:
```
  helm repo add stable https://kubernetes-charts.storage.googleapis.com/
  helm repo update
  helm install node-exporter --set-string service.annotations."prometheus\.io/scrape"=true --set-string service.annotations."prometheus\.zebrium\.io/scrape"=true --namespace zebrium stable/prometheus-node-exporter
```
3. `helm install zstats-collector zstats --namespace zebrium --repo https://raw.githubusercontent.com/zebrium/ze-stats/master/charts --set zebrium.collectorUrl=YOUR_ZE_STATS_API_URL,zebrium.authToken=YOUR_ZE_API_AUTH_TOKEN,zebrium.deployment=YOUR_DEPLOYMENT_NAME`

### Uninstalling via helm

If you used the "helm install" command to install zlog-collector chart, you should use the following command to delete:
```
helm delete --purge zstats-collector
```

## Configuration
No special configuration is required

### Setup
No special setup is required. By default Zebrium's Kubernetes metrics collector and collect metrics from every node.

## Testing your installation
Once the collector has been deployed in your Kubernetes environment, your metrics and anomaly detection will be available in the Zebrium UI.

## Contributors
* Anil Nanduri (Zebrium)
* Dara Hazeghi (Zebrium)
* Brady Zuo (Zebrium)
