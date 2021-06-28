def electionsWinners(votes, k):
    if k == 0:
        if votes.count(max(votes))==1:
            return 1
        else:
            return 0
    org = votes
    after_vote = []
    for i in votes:
        after_vote.append(i+k)
    org_max = max(votes)
    after_vote_max = max(after_vote)

    if after_vote.count(after_vote)>1:
        return 0

    winners = 0

    for i in range(len(org)):
        if after_vote[i]>org_max:
            winners += 1
    return winners
