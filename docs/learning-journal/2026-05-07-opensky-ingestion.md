# OpenSky Ingestion

## Completed

- Connected to OpenSky API
- Filtered flights by Malaysia/SEA region
- Built live flight endpoint
- Added aggregated statistics endpoint

## Lessons Learned

- OpenSky returns positional arrays, not objects
- Parsing layer is important for maintainability
- Regional filtering dramatically reduces noise
- FastAPI makes rapid API prototyping easy

## Next Steps

- PostgreSQL persistence
- Historical snapshots
- Background schedulers
- Grafana dashboards
