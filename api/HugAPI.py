# Python Hug API for IRIS

"""First API, local access only"""
import hug


@hug.local()
# results of this will change based on what is in the queue to get hit next
def request_job(hug_timer=3):
    return dict{'job_id': '1'}
