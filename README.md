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
  helm install --namespace zebrium --name node-exporter stable/prometheus-node-exporter
```
2. `helm install --namespace zebrium  --name zstats-collector --repo https://raw.githubusercontent.com/zebrium/ze-stats/master/charts zstats --set zebrium.collectorUrl=YOUR_ZE_STATS_API_URL,zebrium.authToken=YOUR_ZE_API_AUTH_TOKEN,zebrium.deployment=YOUR_DEPLOYMENT_NAME`

Please note TCP port 9100 must be accessible from other kubernetes nodes in the same cluster.

#### helm version 3
1. `kubectl create namespace zebrium`
2. If node-exporter has not been installed, install it first:
```
  helm repo add stable https://charts.helm.sh/stable
  helm repo update
  helm install node-exporter --namespace zebrium stable/prometheus-node-exporter
```
3. `helm install zstats-collector zstats --namespace zebrium --repo https://raw.githubusercontent.com/zebrium/ze-stats/master/charts --set zebrium.collectorUrl=YOUR_ZE_STATS_API_URL,zebrium.authToken=YOUR_ZE_API_AUTH_TOKEN,zebrium.deployment=YOUR_DEPLOYMENT_NAME`

Please note TCP port 9100 must be accessible from other kubernetes nodes in the same cluster.

### Uninstalling via helm

If you used the "helm install" command to install zlog-collector chart, you should use the following command to delete:
```
helm delete --purge zstats-collector
```

## Configuration
The Kubernetes metrics collector requires **4GiB memory for every 100 nodes** in your Kubernetes Cluster.

For custom metrics, please run the command below to add Zebrium specific annotation for custom metrics:
```
kubectl annotate service CUSTOM_METRICS_SERVICE_NAME prometheus.zebrium.custom/scrape=true --namespace NAMESPACE
```


### Setup
No special setup is required. By default Zebrium's Kubernetes metrics collector and collect metrics from every node.

## Testing your installation
Once the collector has been deployed in your Kubernetes environment, your metrics and anomaly detection will be available in the Zebrium UI.

## Contributors
* Anil Nanduri (Zebrium)
* Dara Hazeghi (Zebrium)
* Brady Zuo (Zebrium)
