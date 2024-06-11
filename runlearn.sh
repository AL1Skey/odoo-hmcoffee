varian="next"
for var in "$@"
do
    varian="${varian},$var"
    echo "$varian"
done
echo $varian