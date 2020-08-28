cd ../charts
helm package zstats
cd ..
helm serve --repo-path ./charts --url  https://github.com/zebrium/ze-stats/releases/download/1.39.0
