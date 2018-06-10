import queue
import collections

class Solution:
    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        for t in tasks:
            if t in d:
                d[t] += 1
            else:
                d[t] = 1

        pq = queue.PriorityQueue()
        for k, v in d.items():
            pq.put(-v)

        ans = 0
        while not pq.empty():
            time = 0
            tmp = []
            while time <= n and not pq.empty():
                v = pq.get()
                if -v > 1:
                    tmp.append(v+1)
                time += 1

            for t in tmp:
                pq.put(t)
            ans += (n+1) if not pq.empty() else time

        return ans



    def leastInterval1(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = [0] * 26
        for t in tasks:
            counts[ord(t) - ord('A')] += 1

        pq = queue.PriorityQueue()
        for c in counts:
            if c != 0:
                pq.put(-c)

        ans = 0
        while not pq.empty():
            tmp = []
            i = 0
            while i <= n:
                if not pq.empty():
                    v = pq.get()
                    if -v > 1:
                        tmp.append(v+1)
                ans += 1
                if pq.empty() and len(tmp) == 0:
                    break
                i += 1

            for t in tmp:
                pq.put(t)

        return ans


    def leastInterval3(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)

        counts = [0] * 26
        for t in tasks:
            counts[ord(t) - ord('A')] += 1
        counts.sort(reverse = True)

        m = counts[0] - 1
        idle = m * n
        i = 1
        while i < 26 and counts[i] > 0:
            idle -= min(counts[i], m)
            i += 1

        return len(tasks) + (idle if idle > 0 else 0)



    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = collections.Counter(tasks).values()
        m = max(counts)
        return max(len(tasks), (m-1)*(n+1) + list(counts).count(m))


        
sol = Solution()

tasks = ["A","A","A","B","B","B"]
n = 2
print(sol.leastInterval(tasks, n))

tasks = ["B","A","A","A","A","A","A","C","D","E","F","G"]
n = 2
print(sol.leastInterval(tasks, n))

