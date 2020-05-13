# METRICS COLLECTOR DOCKER CONTAINER
Zebrium's metrics collector sends metrics to Zebrium for automated Anomaly detection.
Our github repository is located [here](https://github.com/zebrium/ze-stats).

## Getting Started
1. Clone ze-stats git repo
```
  git clone https://github.com/zebrium/ze-stats.git
```
2. Change to ze-stats docker direcotry:
```
  cd ze-stats/docker
```
2. Edit `docker-compose.yml`, replace all upper case variables (e.g. `YOUR_ZE_STATS_API_URL`) with your log collector settings. ZE_STATS_API_URL and ZE_API_AUTH_TOKEN settings can be found in user settings page in Zebrium portal. 
3. Edit `prometheus/prometheus.yml` to add your targets, replace all upper case variables with your real target settings.
4. Change bind-mount data directoy so container can write to it:
```
chmod -R 777 prometheus
```
4. Bring up ze-stats container:
```
docker-compose up -d
```

## Testing your installation
Once the collector has been created in your environment, your metrics and anomaly detection will be available in the Zebrium UI.

## Contributors
* Anil Nanduri (Zebrium)
* Dara Hazeghi (Zebrium)
* Brady Zuo (Zebrium)
