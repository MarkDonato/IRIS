# API Datasheet Reference

## request_job
request_job is an api GET request that tells the client what to do next. The job type depends on the first key. The format for each job Type is below:

job_type => creator
> {"job_type": string, "job_id": string, "pylon_source": string, "target_directory": string, "hash_algorithm": string, "response_time": float}

job_type => runner
> {"job_type": string, "job_id": string, "pylon_path": string, "hash_algorithm": string, "response_time": float}

job_type => none
> {"job_type": string, "response_time": float}

## inform_iris
inform_iris is an api post request that informs the IRIS server the results of its latest run. The job ID is the primary key and the api will already know what it requested based on it, so it does not need any more information replied back to it that came from request_job. After this call lands, if the results were a success the data is stored in the database. The format for this is below:

> {"job_id": string, "run_result": string, "return_data": string}

## request_config
request_config is a get request made by the client to get the config it is supposed to be using so that if the expected config changes the client will know to follow suit. The format is the same as what is in config.yaml

> See Config.yaml for data design properties

## test_attendant
This api method is simply to test to make sure the attendant is up and running. If it is online this is what the api call will return
> {'status': 'online'}
