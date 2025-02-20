ssh-keygen -t ed25519 -C "email"

eval "$(ssh-agent -s)"

ssh-add "path_key"

git clone git@github.com:username/repositoryname.git

the end