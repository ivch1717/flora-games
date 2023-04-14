def delete(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(name)
    for job in current_jobs:
        job.schedule_removal()