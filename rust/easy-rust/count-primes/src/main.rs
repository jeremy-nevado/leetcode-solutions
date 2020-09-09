#[derive(Debug)]
struct Solution {}

impl Solution { 
    pub fn count_primes(n: i32) -> i32 {
        if n < 3 {
            return 0
        }
        let mut primes = vec![2];
        for i in 2..n {
            let mut isprime = true;
            for &prime in &primes {
                let check = i.rem_euclid(prime);
                if check == 0 {
                    isprime = false;
                    break;
                } 
            }
            println!("{}", isprime);
            if isprime {
                primes.push(i);
            }
        }
        primes.len() as i32
    }
}
fn main() {
    let num_primes = Solution::count_primes(2);
    println!("{}", num_primes);
}

