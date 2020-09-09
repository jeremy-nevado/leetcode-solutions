fn main() {

}

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count = 0;
        let mut candidate = 0;
        for num in nums {
            if count == 0 {
                candidate = num;
            }
            if num == candidate {
                count = count + 1;
            } else {
                count = count - 1;
            }
        }
        candidate
    }
}
