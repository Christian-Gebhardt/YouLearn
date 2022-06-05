# YouLearn Backend Readme

1. Conda dependencies in `package-list.txt`
2. Needed environment variables: `YT_API_KEY` and `PATH_TO_TRAINED_MODEL_MLP`
3. Run `Endpoint.py` in the environment

## Endpoints

### 1. Filter distractful videos

endpoint uri: `/api/filterDistractfulVideos`

input:  list of ids of recommended videos

output: list of ids of distractful videos

sample json request:

`{ "recommended_ids" : ["YBN4xI3Z-lc", "gx8_iBO6Sig", "K-MFoZNtt2s", "OmaFy0NKTss"] }`

sample json response:

`{ "distractful_ids" : ["gx8_iBO6Sig", "K-MFoZNtt2s"] }`

### 2. Feedback

todo

### 3. Get recommendations

todo