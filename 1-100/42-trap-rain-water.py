def trap_rain_water(height):
    # Stack approach didn't quite work
    ans = 0
    st = []
    for i in range(len(height)):
        while st and height[i] > height[st[-1]]:
            top = st.pop()
            if not st:
                break
            distance = i - st[-1] - 1
            bounded_h = min(height[i], height[st[-1]] -  height[top])
            ans += distance * bounded_h   
        st.append(i)
    return ans

# Thanks user zhengzhicong
def trap_rain_water_two_pointers(height):
    answer = 0
    max_left = 0
    max_right = 0
    left = 0
    right = len(height)-1

    while left < right:
        if height[left] < height[right]:
            if height[left] > max_left:
                max_left = height[left]
            else:
                answer += max_left - height[left]
            left += 1
        else:
            if height[right] > max_right:
                max_right = height[right]
            else:
                answer += max_right - height[right]
            right -= 1
    return answer

def my_attempt(height):
    ans = 0
    l = 0
    r = len(height) - 1
    max_l = 0
    max_r = 0

    while l < r:
        if height[l] < height[r]:
            if height[l] > max_l:
                max_l = height[l]
            else:
                ans += max_l - height[l]
            l += 1
        else:
            if height[r] > max_r:
                max_r = height[r]
            else:
                ans += max_r - height[r]
            r -= 1

    return ans


if __name__ == "__main__":
    # Output has to be 6
    print(my_attempt([0,1,0,2,1,0,1,3,2,1,2,1]))
    # Output has to be 9
    print(my_attempt([4,2,0,3,2,5]))