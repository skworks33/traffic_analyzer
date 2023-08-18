# Traffic Analyzer

Traffic Analyzer is a Python script that uses the Google Maps Directions API to fetch the travel time between two specified locations (origin and destination). It saves the travel time along with the timestamp in a CSV file at regular intervals, allowing for analysis of traffic patterns.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/skworks33/traffic-analyzer.git
```


## Requirements

- Python 3.x

## Installation

1. Install the required Python packages:

```sh
pip install -U googlemaps
```

2. Set the environment variables:


```
export GMAP_API_KEY="your_google_maps_api_key"
export ORIGIN="your_origin_location"
export DESTINATION="your_destination_location"
```

## Usage

Run the script using Python 3:

```
python3 traffic_analyzer.py
```


## Scheduling

You can schedule the script to run at regular intervals using cron. For example, to run the script every 30 minutes:

```bash
*/30 * * * * /usr/bin/python3 /path/to/your/traffic_analyzer.py
```

