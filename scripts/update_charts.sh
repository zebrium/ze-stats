cd ../charts
version=`cat zstats/Chart.yaml | awk '/version: / { print $2 }'`
helm package zstats
cd ..
helm serve --repo-path ./charts --url  https://github.com/zebrium/ze-stats/releases/download/$version
