#!/bin/bash

typeset -A c
c[A0]="11B"
c[A1]="01C"
c[B0]="00A"
c[B1]="01D"
c[C0]="11D"
c[C1]="11H"
c[D0]="10E"
c[D1]="00D"
c[E0]="11F"
c[E1]="10B"
c[F0]="11A"
c[F1]="11E"
typeset -r c

typeset -a a=([0]=0)
typeset p=0
typeset l=0
typeset x
typeset i="00A"
typeset st
typeset et
typeset tt

log(){
	echo "Start Time (Sec)  : ${st}"
	echo "End Time (Sec)    : ${et}"
	echo "Total Time (Sec)  : ${tt}"
	echo "Loop Count        : ${l}"
	echo "Array Count       : ${#a[@]}"
	echo "Array Position    : ${p}"
	echo "Array Symbol      : ${a[${p}]}"
	echo "Working Card      : ${x}"
	echo "Card Symbol       : ${i:0:1}"
	echo "Card Direction    : ${i:1:1}"
	echo "Card Next Card    : ${i:2:1}"
	echo "Array             : ${a[@]}"
}

st=$(date +%s)
while [ ${i:2:1} != H ];do
	x=${i:2:1}${a[${p}]:-0}
	i=${c[${x}]}
	a[${p}]=${i:0:1}
	p=$((${p}+${i:1:1}))
	if [ ${i:1:1} == 0 ];then
		if [ ${p} == 0 ];then
			a=(0 ${a[@]})
		else
			((p--))
		fi
	fi
	((l++))
	echo ${a[@]}
done
et=$(date +%s)
tt=$((${et}-${st}))
echo "HALT"
log
exit 0;
