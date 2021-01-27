"""
1. Find the one node that has no connection to outside nodes
   Make sure there's just one
​
2. Make sure all other nodes point to it
"""
​
def find_judge(n, trust):
    trust_map = {}   # key is the truster, value is list of trustees
    #trusted_by_map = {}
​
    for truster, trustee in trust:
        if truster not in trust_map:
            trust_map[truster] = []
​
        trust_map[truster].append(trustee)
​
        """
        if trustee not in trusted_by_map:
            trusted_by_map[trustee] = []
​
        trusted_by_map[trustee].append(truster)
        """
​
​
    # Find the person who trusts nobody
    trusts_nobody = None
​
    for i in range(1, n+1):
        if i not in trust_map:
​
            #print(f"{i} doesn't trust anyone")
​
            if trusts_nobody is not None:  # Too many people trust no one
                return -1
​
            trusts_nobody = i
​
    # This _might_ be the judge
    candidate = trusts_nobody;
​
    # Make sure everyone trusts the candidate
    for i in range(1, n+1):
        if i == candidate:  # Except the judge doesn't have to trust themselves
            continue
​
        this_person_trusts = trust_map[i]
​
        if candidate not in this_person_trusts:
            return -1
​
    # if we get here, candidate is the judge
    return candidate
​
print(find_judge(2, [[1,2]]))  # 2
print(find_judge(2, []))  #  -1
print(find_judge(3, [[1,3], [2,3]]))  # 3
print(find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) # 3