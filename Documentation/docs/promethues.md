[link to index](/readme.md)  
# Prometheus
Open-source systems monitoring and alerting toolkit with an active eco-system.
- lets you analyse how apps and infrastructure are performing
- uses http endpoints on the targets
- Most compoents are written in Go language
    - easy to build
    - easy to 
- multi-dimensional data model with time series data identified by metric name or key/value pair (labels)
    - `http_requests_total{method="get"}`
- uses PromQL to to make database queries
- no reliance on distributed storage
- plenty of libraries
- can add custom services
- A Fully-fledged system with its own alert manager

## Monitoring tools should:
- Collect or listen for events
- Store the events
- Support a querying feature
- provide graphical monitoring

## Alternatives
- graphite
- influxdb
- openTSDB
- Nagios
- Sensu

