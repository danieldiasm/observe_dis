import pprint
import jenkins

# Replace these with your Jenkins URL, username, and password or API token
JENKINS_URL = "http://0.0.0.0:8080/"
JENKINS_UUSERNAME = "agent"
JENKINS_TOKEN = "TOKEN"

def get_job_list(server):
    all_jobs = server.get_all_jobs()
    job_list = list()

    for job in all_jobs:
        job_list.append(job["fullname"])
    
    return job_list


def get_last_job_build_no(server, job_name):
    last_build_info = dict()
    last_build_info['name'] = server.get_job_info(job_name)['name']
    last_build_info['number'] = server.get_job_info(job_name)['lastBuild']['number']
    return last_build_info


def get_job_build_info(server, job_name):
    last_build_no = get_last_job_build_no(server, job_name)
    build_info = server.get_build_info(last_build_no["name"], last_build_no["number"])
    return build_info


def get_running_jobs(server):
    running_jobs = []
    all_jobs = server.get_all_jobs()

    for job in all_jobs:
        job_info = server.get_job_info(job["fullname"])
        if "lastBuild" in job_info and job_info["lastBuild"] is not None:
            last_build_number = job_info["lastBuild"]["number"]
            build_info = server.get_build_info(job["name"], last_build_number)

            if build_info["building"]:
                running_jobs.append((job["name"], last_build_number))

    return running_jobs


def main():
    jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_UUSERNAME, password=JENKINS_TOKEN)
    job_list = get_job_list(jenkins_server)

    job_details = get_job_build_info(jenkins_server, "Dummy-Job")

    print("-------------Dummy-Job-------------")
    print(f"Build name: {job_details['fullDisplayName']}")
    print(f"Is it running: {job_details['inProgress']}")
    print(f"Build ID: {job_details['id']}")

    # if running_jobs:
    #     print("Running jobs:")
    #     for job_name, build_number in running_jobs:
    #         print(f"{job_name} - Build #{build_number}")
    # else:
    #     print("No jobs are currently running.")
    


if __name__ == "__main__":
    main()