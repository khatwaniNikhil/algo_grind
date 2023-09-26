# logic
1. store only leader change data: Map<Integer, 
    tx leader1
    ty leader0
    b/w tx to ty leader1

Query(binary search)
    tx  leader1
    ty  leader0
    t(b/w x and y) tx lookup = leader1

linkedlist of leaderchange events
leaders at change leader timestamp

iterate
    currentRoundWinner
    currentRoundWinnerTotalCount
    update maxVotes
    if currentWinnder not a leader, 
        changeLeader event 
        inc change count

# Approach1

```
class TopVotedCandidate {
    private final int[] time;
    private final int[] leader;
    public TopVotedCandidate(int[] persons, int[] times) {
        LeaderChange head = new LeaderChange();
        LeaderChange tail = head;
        int n = persons.length;
        int[] votes = new int[n];
        int currentLeader = -1;
        int maxVotes = 0;
        int changeCount = 0;
        for (int i = 0; i < n; i++) {
            int p = persons[i];
            int v = ++votes[p];
            if (v >= maxVotes) {
                maxVotes = v;
                if (p != currentLeader) {
                    tail = new LeaderChange(times[i], currentLeader = p, tail);
                    changeCount++;
                }
            }
        }
        time = new int[changeCount];
        leader = new int[changeCount];
        for (int i = 0; i < changeCount; i++) {
            head = head.next;
            time[i] = head.time;
            leader[i] = head.leader;
        }
    }

    public int q(int t) {
        int left = 0;
        int right = time.length;
        while (true) {
            int mid = (left + right) >>> 1;
            if (mid == left)
                break;
            if (time[mid] <= t)
                left = mid;
            else
                right = mid;
        }
        return leader[left];
    }

    private static class LeaderChange {
        final int time;
        final int leader;
        LeaderChange next;

        LeaderChange() {
            time = 0;
            leader = 0;
        }

        LeaderChange(int time, int leader, LeaderChange previous) {
            this.time = time;
            this.leader = leader;
            previous.next = this;
        }
    }
}
```

# Approach2
```
class TopVotedCandidate {

    /** tracks leading person after counting ith vote */
    int[] leaders;

    /** tracks casting time of ith vote */
    int[] times;

    public TopVotedCandidate(int[] persons, int[] times) {
        this.times = times;
        this.leaders = new int[persons.length];

        Map<Integer, Integer> voteCounter = new HashMap<>();
        int max = -1;
        int person = -1;
        for(int v=0;v<persons.length;++v) {
            int p = persons[v];
            int totalVotesForPerson = voteCounter.getOrDefault(p,0)+1;
            if (totalVotesForPerson>=max) {
                max = totalVotesForPerson;
                person = p;
            }
            voteCounter.put(p,totalVotesForPerson);
            leaders[v] = person;
        }
    }
    
    public int q(int t) {
        int v = getVotesCastedForTime(t);
        return leaders[v];
    }

    private int getVotesCastedForTime(int t) {
        int s=0;
        int e=times.length-1;

        while(s<=e) {
            int m = s+(e-s)/2;
            if(times[m]==t) {
                return m;
            } else if(times[m]>t) {
                e = m-1;
            } else {
                s = m+1;
            }
        }
        return e;
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */
```
