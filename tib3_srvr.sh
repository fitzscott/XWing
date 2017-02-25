cd `dirname $0`

NOD=$1
CNT=$2
OPP=$3
CONC=$4

SLPTM=30

run1x() {

PYFL=$1
NOD=$2

PYBAS=`basename ${PYFL} .py`

STTMI=$( date +"%F %T" )
python ${PYFL} > /dev/null
RC=$?
ENTMI=$( date +"%F %T" )
if [ ${RC} -eq 0 ]
then
	echo "Single=Node ${NOD}; Py ${PYBAS}; Iter ${ITER}; Start ${STTMI}; End ${ENTMI}"
else
	echo "Error ${NOD}; Iter ${ITER}; Py ${PYBAS}; Start ${STTMI}; End ${ENTMI}"
fi
}


ITER=0
while [ ${ITER} -lt ${CNT} ]
do
	STARTED=0
	while [ ${STARTED} -lt ${CONC} ]
	do
		run1x ${OPP}vTI.py ${NOD} &
		sleep ${SLPTM}
		let STARTED=${STARTED}+1
	done
	wait
	let ITER=${ITER}+1
done


