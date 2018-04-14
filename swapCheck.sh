#!/bin/bash
#The server to be checked will be based on the user's input
echo -e -n -E "Which host(s) would you like to check (wa | ma | tx):
read COLO

function memory (){
echo "########"
hostname
echo "########"
echo "Total swap found : "  $(free -h | grep Swap | fmt -u | cut -d " " -f 2)
echo "Total swap used  : "  $(free -h | grep Swap | fmt -u | cut -d " " -f 3)
echo "Swap remaining   : "  $(free -h | grep Swap | fmt -u | cut -d " " -f 4)

swapTotal=$(free  | grep Swap | fmt -u | cut -d " " -f 2)
swapTotalFloat="$(bc <<< $swapTotal*1.00)"

swapUsed=$(free  | grep Swap | fmt -u | cut -d " " -f 3)
swapUsedFloat="$(bc <<< $swapUsed*1.00)"

swapRemaining=$(free  | grep Swap | fmt -u | cut -d " " -f 4)

swapPercent="0.25"
swapThreshold="$(bc <<< $swapTotalFloat*$swapPercent)"
swapThresholdInteger=$(echo $swapThreshold | cut -d "." -f 1)

if [[ $swapRemaining -ge $(bc <<< $swapTotal-$swapThresholdInteger) ]]; then 
echo
echo "There is more than 25% of swap remaining on this host"
echo
else
echo "Swap needs to be addressed on this host"
echo
fi
}

#If the user input is ma run the following if-then-elif statement

if [[ ${COLO} == xx ]]; then
for i in <server>; do
ssh -q -o StrictHostKeyChecking=no $i "
$(cat << EOT
${typeset -f}
memory
EOT
)"
done

elif [[ ${COLO} == xx ]];then

for i in <server>;do
ssh -q -o StrictHostKeyChecking=no $i "
$(cat << EOT
${typeset -f}
memory
EOT
)"
done

fi
