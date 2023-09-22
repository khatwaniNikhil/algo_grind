int getPossibleDecodedPattern(char[] numArr, int start, int end, int length) {
	int count = 0;
	if(end >= numArr || start >= numArr) {
		Return count;
	}
	if(length == numArr) {
		return 1;
	}
	
	int num = getIntegerNum(int start, int end);
	if(num <= 26) {
		Length += num < 10 ? 1: 2;
		if(start == end) {
			Count +=getPossibleDecodedPattern(numArr, start, end+1, Length);
		}
		Count +=getPossibleDecodedPattern(numArr, start+1, end+1, Length);
	}
	return count;
}
}

