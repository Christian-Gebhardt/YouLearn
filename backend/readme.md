# YouLearn Backend Readme

1. Conda dependencies in `package-list.txt`
2. Needed environment variables: `YT_API_KEY` and `PATH_TO_TRAINED_MODEL_MLP`
3. Run `Endpoint.py` in the environment

## Endpoints

### 1. Filter distractful videos

Endpoint uri: `/api/filterDistractfulVideos`

Input:  list of ids of recommended videos

Output: list of ids of distractful videos

Sample json request:

`{ "recommended_ids" : ["YBN4xI3Z-lc", "gx8_iBO6Sig", "K-MFoZNtt2s", "OmaFy0NKTss"] }`

Sample json response:

`{ "distractful_ids" : ["gx8_iBO6Sig", "K-MFoZNtt2s"] }`

### 2. Filter and sort recommended videos

Endpoint uri: `/api/filterAndSortDistractfulVideos`

Input:  list of ids of recommended videos

Output: list of ids of sorted recommended videos

Sample json request:

`{ "recommended_ids" : ["YBN4xI3Z-lc", "gx8_iBO6Sig", "K-MFoZNtt2s", "OmaFy0NKTss"] }`

Sample json response:

`{ "recommended_and_sorted_ids" : ["XiVAIdxUsZE"] }`

### 3. Feedback

todo

### 4. Get recommendations

todo