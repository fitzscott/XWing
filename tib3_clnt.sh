#set -x
NOD=$1
CNT=$2
OPP=$3
CONC=$4

if [ "${OPP}" == "" ]
then
	OPP="X"
fi
if [ "${CONC}" == "" ]
then
	CONC=4
fi

ssh -f pi@pi${NOD} python_games/XWing/tib3.sh ${NOD} ${CNT} ${OPP} ${CONC} > n_${NOD}_TIv_${CNT}_${OPP}_${CONC}.dat

