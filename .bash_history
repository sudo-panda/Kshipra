az webapp deployment user set --user-name Kshipra --password BenettUniversity
az group create --name KshipraRG --location "West Europe"
az appservice plan create --name KshipraSP --resource-group KshipraRG --sku B1 --is-linux
az webapp create --resource-group KshipraRG --plan KshipraSP --name Kshipra --runtime "PYTHON|3.7" --deployment-local-git
git remote add azure https://github.com/Baidya99/Kshipra.git
git init
git remote add azure https://github.com/Baidya99/Kshipra.git
git push azure master
git commit -m "initial commit"
git config --global user.email "kundubaidya99@gmail.com"
git config --global user.name "Baidya99"
git config --global user.email "biswasanish42@gmail.com
"
git config --global user.name "Anoxyde0"
git config user.email "kundubaidya99@gmail.com"
git config user.name "Anoxyde0"
git commit -m "initial commit"
git push azure master
git commit -m "initial commit"
git push azure master
git commit -m "initial commit"
git push azure master --force
touch README
git add README
git add -A
