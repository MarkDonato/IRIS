# API Datasheet Reference

## MasterRequestData
MasterRequestData is an api GET request that tells the client what to do next. The job type depends on the first key. The format for each job Type is below:

Call Runner
> {"job": string, "job_id": int, "pylon_path": string, "hash_algorithm": string, }

Call Creator
> {"job": string, "job_id": int, "source_pylon": string, "target_directory": string, "hash_algorithm": string, }

## MasterResponseData
MasterResponseData is an api post request that informs the IRIS server the results of its latest run. The job ID is the primary key. After this call lands, if the results were a success the data is stored in the database. The format for this is below:

> {"job_id": int, "run_result": boolean, "returnData": string}

## ConfigData - get
ConfigData is a get request made by the client to get the config it is supposed to be using so that if the expected config changes the client will know to follow suit. The format is the same as what is in config.yaml

> See Config.yaml for data design properties
