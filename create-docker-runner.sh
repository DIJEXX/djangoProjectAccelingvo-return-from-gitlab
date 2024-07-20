docker run -d --name dj-gitlab-runner --restart always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v dj-gitlab-runner-config:/etc/gitlab-runner \
gitlab/gitlab-runner:latest