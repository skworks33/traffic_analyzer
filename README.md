# sv_story_gpt

This is a simple Python script that selects a random phrase from a text file, asks ChatGPT to generate an interesting story based on the selected phrase, and then posts the story to a Slack channel.

## Requirements

- Python 3.x
- `openai` Python package
- `slack-sdk` Python package
- `requests` Python package

## Installation

1. Install the required Python packages:

```sh
pip install openai slack-sdk requests
```

2. Clone this repository:

```
git clone 
cd 
```

## Configuration

1. 

```
export 
export
/path/to/python3 /path/to/traffic_analyzer/traffic_analyzer.py
```

2. Make sure the run_script.sh file is executable:

```
chmod +x run_script.sh
```

3. Update the sv.txt file with your desired list of phrases, one per line.

## Usage

1. Run the run_script.sh script:

```
./run_script.sh
```

## Schedule Daily Execution

To schedule the script to run daily at 10 AM JST, add the following line to your crontab:

```
0 10 * * * /path/to/run_script.sh > /path/to/output.log 2>&1
```

Make sure to replace /path/to/run_script.sh with the actual path to the run_script.sh file in your system.

