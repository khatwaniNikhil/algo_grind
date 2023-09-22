public class RankTeamsByVotes {

    static class Team implements Comparable<Team> {

        // team name
        char teamName;
        // votes per position that this team got
        int[] votesInPosition;

        private Team(char teamName, int positions) {
            this.teamName = teamName;
            this.votesInPosition = new int[positions];
        }

        @Override
        public String toString() {
            return "Team{" + "teamName=" + teamName + ", votesInPosition=" + Arrays.toString(votesInPosition) + "}\n";
        }

        @Override
        public int compareTo(Team t2) {
            // we compare by voting positions from high to low
            for (int i = 0; i < this.votesInPosition.length; i++) {
                // if we have different votes for a position, the result can be settled by comparing them
                // if not, we need to check the next voting position
                if (this.votesInPosition[i] != t2.votesInPosition[i]) {
                    return Integer.compare(t2.votesInPosition[i], this.votesInPosition[i]);
                }
            }
            // finally, if all votes were same, we just compare the names in lexical order.
            return Character.compare(this.teamName, t2.teamName);
        }
    }

    public String rankTeams(String[] votes) {

        if (votes == null || votes.length == 0) {
            return "";
        }
        // if there's only 1 vote, that is the result
        if (votes.length == 1) {
            return votes[0];
        }

        // create a Map of all teams.
        Map<Character, Team> allTeams = new HashMap<>();
        // any vote is a contains all the teams. We can take any vote but here we take the 1st element
        String teams = votes[0];
        // there are N voting positions which is same as the number of teams.
        int positions = teams.length();

        // create the Teams
        for (char team : teams.toCharArray()) {
            allTeams.put(team, new Team(team, positions));
        }

        // iterate over each vote and count the number of vote per position for a team
        for (String vote : votes) {
            for (int i = 0; i < vote.length(); i++) {
                // get the team from the vote
                char teamName = vote.charAt(i);
                // get the team object
                Team team = allTeams.get(teamName);
                // increment its vote position count
                team.votesInPosition[i]++;
            }
        }

        // we use a priority Q to sort the Teams. Teams will be automatically be sorted by the comparison function defined for the team
        Queue<Team> q = new PriorityQueue<>();
        q.addAll(allTeams.values());

        // create the result
        StringBuilder votingResult = new StringBuilder();
        while (!q.isEmpty()) {
            votingResult.append(q.poll().teamName);
        }

        return votingResult.toString();
    }
}
