class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # # Function to calculate the gain in pass ratio for adding a student to a class
        # def pass_ratio_gain(passi, totali):
        #     return (passi + 1) / (totali + 1) - passi / totali
        
        # # Max-heap to store the gain, -gain because heapq is a min-heap by default
        # heap = []
        # for passi, totali in classes:
        #     gain = pass_ratio_gain(passi, totali)
        #     heappush(heap, (-gain, passi, totali))
        
        # # Distribute the extra students
        # for _ in range(extraStudents):
        #     # Pop the class with the maximum gain
        #     gain, passi, totali = heappop(heap)
        #     # Add one student to this class
        #     passi += 1
        #     totali += 1
        #     # Recalculate gain and push back into heap
        #     new_gain = pass_ratio_gain(passi, totali)
        #     heappush(heap, (-new_gain, passi, totali))
        
        # # Calculate the final average pass ratio
        # total_ratio = 0
        # for _, passi, totali in heap:
        #     total_ratio += passi / totali
        
        # return total_ratio / len(classes)

        classes = [(num/denom - (num+1)/(denom+1), num, denom) for num, denom in classes]
        heapify(classes)
        if classes[0][0]==0:
            return 1
        for i in range(extraStudents):
            _, num, denom = heappop(classes)
            heappush(classes, ((num+1)/(denom+1) - (num+2)/(denom+2), num+1, denom+1))

        return sum([c[1]/c[2] for c in classes])/len(classes)