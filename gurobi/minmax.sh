agent=5
city=50
for num in {1..1000..1}
do
    python3 entrance.py $city $agent $num 3600
done