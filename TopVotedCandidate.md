# Approach
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
