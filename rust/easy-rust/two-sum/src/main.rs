use std::collections::HashMap;
#[derive(Debug)]

struct Solution {

}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut compliment: HashMap<i32, i32> = HashMap::new();
        let mut res: Vec<i32> = Vec::new();
        for i in 0..nums.len() {
            compliment.insert(target - nums[i], i as i32);
        } 
        println!("{:?}", compliment);

        for i in 0..nums.len(){
            let current: i32  = match compliment.get(&nums[i]) {
                    Some(&val) => val,
                    None => -1
            };
            if compliment.contains_key(&nums[i]) && current != i as i32 {
                res.push(i as i32);
                res.push(current);
                break;
            }
        }

        res
    }
}
fn main() {
    let vector = vec![3, 2 ,4];
    let test = Solution::two_sum(vector, 6);
    println!("{:?}", test);
}
