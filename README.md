# MarketDataUnificationPipeline
A market data unification pipeline ingesting diverse data shapes and normalizing them into a time-ordered stream. 

Schema 
- Find 3 data sources, create data classes based on pydantic BaseModels 
Adapters 
- Find a way to shape the data in similar ways 
Ingestion 
- Call APIs for 3 different data sources or set up webhooks, feeding into schema + adapter
Alignment 
- Create an aligning engine for incoming data to align it as one timestamp 
Pipeline 
- Store aligned data in influxDB 
