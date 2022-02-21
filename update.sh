git stash
git pull
pm2 stop next
yarn remove win-node-env
yarn install
unzip -o .next.zip -d .next
pm2 restart next
