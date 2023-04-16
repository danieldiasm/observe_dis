from jenkinsapi.jenkins import Jenkins

jenkins_url = 'http://0.0.0.0:8080/'
username = 'agent'
password = ''

def get_server_instance():
    server = Jenkins(jenkins_url, username, password)
    return server

if __name__ == '__main__':
    print(get_server_instance().version)

