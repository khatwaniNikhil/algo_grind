startTime[]  endTime[]  profit[i]

1. 2D array  startTime.length * 3
  				startTime		endTime		profit
 JOB1
 JOB2
 JOBN 				

2. sort array by end Time

3. TreeMap   endTime		MaxProfit
				0				0

4. 	iterate jobs with inc. endTIme and add to tree map if found larger profit than most recent/last endTime in Map

		int maxProfitAtCurentEndTime = job[2] + profit at largest end time just before current job start time
		if(maxProfitAtCurentEndTime>treeMap.lastEntry)

5. return last entry of TreeMap as it has max profit		


Ops
TreeMap lastEntry
TreeMap find key greatest entry less than input: binary search

