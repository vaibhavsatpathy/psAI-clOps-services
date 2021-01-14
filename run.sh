docker run -d \
-p "8080:8080" \
-v "$(pwd)/:/app" \
-v "${filesystem_path}:/app/temp" \
-v "$(pwd)/logs:/app/logs" \
--user "0:0" \
-e "shm_size=1024m" \
--name mlops mlops

if [[ "$(docker ps -q -f name=mlops)" ]]; 
then
    echo -e "
    \033[31;1m  ____    _  _____  _    _   _ _   _ ____  
    \033[31;1m |  _ \  / \|_   _|/ \  | | | | | | | __ ) 
    \033[31;1m | | | |/ _ \ | | / _ \ | |_| | | | |  _ \ 
    \033[31;1m | |_| / ___ \| |/ ___ \|  _  | |_| | |_) |
    \033[31;1m |____/_/   \_\_/_/   \_\_| |_|\___/|____/ 
    \033[0;00m
    "                      
fi