struct Solution{}

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let expected = (nums.len() * (nums.len() + 1)/2) as i32;
        let mut actual: i32 = 0;
        for num in nums {
            actual = actual + num;
        }
        return expected - actual as i32
    }
}

fn main() {
    let v = vec![1, 0, 3];
    let miss = Solution::missing_number(v);
    println!("{}", miss);
}
