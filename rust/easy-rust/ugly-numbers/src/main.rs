struct Solution {}

impl Solution {
    pub fn is_ugly(num: i32) -> bool {
        let mut temp = num;
        if num == 0 {
            false;
        }
        if num == 1 {
            true;
        }
        for i in [2, 3, 5].iter() {
            while temp % i == 0 && 0 < temp {
                temp = temp / i;
            }
        }
        temp == 1
    }
}

fn main() {
    let test = Solution::is_ugly(14);
    println!("{}", test)
}
