# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Not enough time to earn profit
        if len(prices) < 2:        return 0

        # The maximum price from here to the end
        maxFromHere = prices[-1]

        # The maximum profit, we could earn.
        # Could initialize it with any valid profit.
        maxProfit = prices[1] - prices[0]

        for index in xrange(len(prices)-2, -1, -1):
            price = prices[index]

            # The maximum profit, if we buy it here.
            profit = maxFromHere - price

            maxProfit = max(maxProfit, profit)
            maxFromHere = max(maxFromHere, price)

        # If maxProfit is negative, we would not take
        # any transaction.
        #
        # If we initialize the maxProfit with 0, this
        # step is not necessary.
        maxProfit = max(0, maxProfit)

        return maxProfit

s = Solution()

print s.maxProfit([1,2,3,65,2,5,6,87,1,34,57,78,34,342,22])