#set -x
NOD=$1
CNT=$2
OPPCNT=$3

if [ "${OPPCNT}" == "" ]
then
	OPPCNT=5
fi

ssh -f pi@pi${NOD} python_games/XWing/tib.sh ${NOD} ${CNT} ${OPPCNT} > n_${NOD}_TIv_${CNT}_${OPPCNT}.dat

