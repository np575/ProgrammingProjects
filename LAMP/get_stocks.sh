function stocks() {
date=`date +"%Y_%m_%d_%H_%M_%S"`
index_page='https://finance.yahoo.com/most-active'
hfn=yahoo_${date}.html
wget -O yahoo_${date}.html $index_page
echo $hfn
}

x=0
while [[ $x -le 600 ]]; do
	stocks
	sleep 2
	x=`expr $x + 1`
done
