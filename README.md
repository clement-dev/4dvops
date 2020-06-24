## Prérequis:
installer docker
avoir le télécharger le dossier "tools"

## installation de docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

## création des runner, ainsi que de l'image docker de gitlab
se rendre dans le dossier TOOLS/GITLAB
`docker-compose up`
( cette commande nous permet de crée une version local de gitlab )

`docker run -d --name {runner-name} -v /var/run/docker.sock:/var/run/docker.sock -v /srv/{runner-name}/config:/etc/gitlab-runner --rm gitlab/gitlab-runner`
( pensez a changer {runner-name} par le nom de votre runner )

crée un compte ainsi qu'un projet en se rendant sur `localhost:10080` et recuperer le token http://localhost:10080/[username]/[project-name]/-/settings/ci_cd ( dans runner puis set up specific runner )

`docker exec -it {runner-name} gitlab-runner register -n --url http://{your-ip}:10080 --registration-token {registration-token} --clone-url http://{your-ip}:10080 --executor docker --docker-image "docker:latest" --docker-privileged`
Cette commande permet d'executer le runner et de le lier a votre projet gitlab

