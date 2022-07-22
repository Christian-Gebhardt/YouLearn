# YouLearn Backend Readme

## To run the service

1. Create conda environment, dependencies in `backend/package-list.txt`
2. Setup environment variables
3. Run `Endpoint.py` in the environment

## Environment variables

`BACKEND_PATH` - for testing, `<path to git repo>/backend`

`YT_API_KEY` - key to YouTube Data API

`MONGO_URI` - connection string of running mongodb database (containing collection with training data from kaggle, see python notebooks for details)

`PATH_TO_STATIC_MODEL` - initial model that does not change, serving as fallback if something goes wrong with the dynamic model

`PATH_TO_DYNAMIC_MODEL` - model that is being dynamically trained (should be backed up by a system service eventually). **If not present, copy the static model manually** (and rename the copy to e.g. `model_dynamic.sav`).

`RUNNING_IN_CLOUD` - false for localhost deployment (changes flask host and port)

**More static variables are in Params.py**, e.g. number of training samples, number of feedbacks until retraining.

## Endpoints

### 1. Filter distractful videos

- Endpoint uri: `/api/filterDistractfulVideos`

- Input:  list of ids of recommended videos

- Output: list of ids of distractful videos

- Sample json request:

`{ "recommended_ids" : ["YBN4xI3Z-lc", "gx8_iBO6Sig", "K-MFoZNtt2s", "OmaFy0NKTss"] }`

- Sample json response:

`{ "distractful_ids" : ["gx8_iBO6Sig", "K-MFoZNtt2s"] }`

### 2. Filter and sort recommended videos

- Endpoint uri: `/api/filterAndSortDistractfulVideos`

- Parameter `filter_threshold`: videos with probability of being educational under the threshold will be filtered; if no value is specified, default value is used (0.5)

- Input:  list of ids of recommended videos

- Output: list of ids of filtered and sorted recommended videos

- Sample json request:

URI: 

`/api/filterAndSortDistractfulVideos?filter_threshold=0.82`

Body:

`{ "recommended_ids" : ["YBN4xI3Z-lc", "gx8_iBO6Sig", "K-MFoZNtt2s", "OmaFy0NKTss"] }`

- Sample json response:

`{ "recommended_and_sorted_ids" : ["XiVAIdxUsZE"] }`

### 3. Feedback

- Endpoint: `/api/feedback`

- Input: json with single `video_id` and boolean `distractful`

- Output:

JSON message that the feedback was stored and `Success code 200`

- Sample json request:
 
`{ "video_id": "gx8_iBO6Sig", "distractful": true }`