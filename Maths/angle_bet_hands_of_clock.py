class Solution:
    def angleClock (self, hour: int, minutes: int) -> float:
        h_hand = (30 * hour) + (0.5 * minutes)
        m_hand = (6 * minutes)
        diff = abs(h_hand - m_hand)
        return diff if (diff <= 180) else (360 - diff)
