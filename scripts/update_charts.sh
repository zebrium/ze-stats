cd ../charts
helm package zstats
cd ..
helm serve --repo-path ./charts --url https://raw.githubusercontent.com/zebrium/ze-stats/master/charts
