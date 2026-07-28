class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int):

        max_sum = 0
        current_sum = 0

        # Pehli window (0 se minutes-1 tak)
        # Agar owner grumpy hai to us minute ke customers save ho sakte hain
        for i in range(minutes):
            if grumpy[i] == 1:
                current_sum += customers[i]

        # Pehli window ko hi maximum maan lo
        max_sum = current_sum

        # Window ke just aage wale element se lekar last tak
        for i in range(minutes, len(customers)):

            # Window ka left element bahar ja raha hai
            if grumpy[i - minutes] == 1:
                current_sum -= customers[i - minutes]

            # Naya right element window me aa raha hai
            if grumpy[i] == 1:
                current_sum += customers[i]

            # Ab tak ki best window
            max_sum = max(max_sum, current_sum)

        # Jo customers pehle se hi satisfied the (grumpy == 0)
        # Unhe final answer me add kar do
        for i in range(len(customers)):
            if grumpy[i] == 0:
                max_sum += customers[i]

        return max_sum