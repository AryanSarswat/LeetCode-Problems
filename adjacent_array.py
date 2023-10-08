class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0
        for idx in range(len(flowerbed)):
            if self.canPlace(flowerbed, idx):
                flowerbed[idx] = 1
                placed += 1
            
            if placed >= n:
                return True
        
        return placed >= n

    def canPlace(self, flowerbed, idx):
        left = None
        right = None

        if flowerbed[idx] == 1:
            return False
        elif len(flowerbed) == 1 and flowerbed[idx] == 0:
            return True
 

        if idx - 1 >= 0:
            left = flowerbed[idx - 1]
        if idx + 1 < len(flowerbed):
            right = flowerbed[idx + 1]
        
        if left is None and right is not None:
            if flowerbed[idx + 1] != 1:
                return True
        if right is None and left is not None:
            if flowerbed[idx - 1] != 1:
                return True
        if right is not None and left is not None:
            if flowerbed[idx + 1] != 1 and flowerbed[idx - 1] != 1:
                return True
        
        return False