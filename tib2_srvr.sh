cd `dirname $0`

NOD=$1
CNT=$2
OPPS=$3

OPPFL="topps"
SLPTM=30


run1x() {

PYFL=$1
NOD=$2

PYBAS=`basename ${PYFL} .py`

STTMI=$( date +"%F %T" )
python ${PYFL} > /dev/null
RC=$?
ENTMI=$( date +"%F %T" )
#time python ${PYFL}
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
	for OPP in `sort -R ${OPPFL} | head -${OPPS}`
	do
		run1x ${OPP}vTI.py ${NOD} &
		sleep ${SLPTM}
	done
	wait
	let ITER=${ITER}+1
done


