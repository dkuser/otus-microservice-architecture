 while true 
 do 
    ./ab -n 50 -c 5 http://arch.homework/users 
    ./ab -n 10 -c 1 http://arch.homework/
    ./ab -n 20 -c 1 http://arch.homework/error
    sleep 3
done