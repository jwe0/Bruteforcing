use std::io::{self, Write, BufRead, BufReader};
use std::fs::File;
use std::process::exit;
use std::{thread, time::Instant};
use colored::Colorize;
use sha2::{Digest, Sha256, Sha224, Sha384, Sha512};
use md5;



fn art() {
    println!(r#"
    ____             __     ______                __            
   / __ \__  _______/ /_   / ____/________ ______/ /_____  _____
  / /_/ / / / / ___/ __/  / /   / ___/ __ `/ ___/ //_/ _ \/ ___/
 / _, _/ /_/ (__  ) /_   / /___/ /  / /_/ / /__/ ,< /  __/ /    
/_/ |_|\__,_/____/\__/   \____/_/   \__,_/\___/_/|_|\___/_/     

    "#);
}



fn md5_method(hash: &str, word: &str, time: u64) {
    let digest = md5::compute(word.as_bytes());        
    let digest_str = format!("{:x}", digest);
    if digest_str == hash.to_string() {
        println!("[{}] Cracked password: {}\n[{}] Took: {}s", "✔".green(), word,"✔".green(), time);
        exit(0);
    }
}

fn sha224_method(hash: &str, word: &str, time: u64) {
    let mut hasher = Sha224::new();
    hasher.update(word.as_bytes());
    let result = hasher.finalize();
    let hash_result = format!("{:x}", result);
    if hash_result == hash.to_string() {
        println!("[{}] Cracked password: {}\n[{}] Took: {}s", "✔".green(), word,"✔".green(), time);
        exit(0);
    }
}

fn sha384_method(hash: &str, word: &str, time: u64) {
    let mut hasher = Sha384::new();
    hasher.update(word.as_bytes());
    let result = hasher.finalize();
    let hash_result = format!("{:x}", result);
    if hash_result == hash.to_string() {
        println!("[{}] Cracked password: {}\n[{}] Took: {}s", "✔".green(), word,"✔".green(), time);
        exit(0);
    }
}

fn sha512_method(hash: &str, word: &str, time: u64) {
    let mut hasher = Sha512::new();
    hasher.update(word.as_bytes());
    let result = hasher.finalize();
    let hash_result = format!("{:x}", result);
    if hash_result == hash.to_string() {
        println!("[{}] Cracked password: {}\n[{}] Took: {}s", "✔".green(), word,"✔".green(), time);
        exit(0);
    }
}   




fn sha256_method(hash: &str, word: &str, time: u64) {
    let mut hasher = Sha256::new();
    hasher.update(word.as_bytes());
    let result = hasher.finalize();
    let hash_result = format!("{:x}", result);

    if hash_result == hash.to_string() {
        println!("[{}] Cracked password: {}\n[{}] Took: {}s", "✔".green(), word,"✔".green(), time);
        exit(0);
    }
}


fn main() {
    art();
    print!("[{}] Hash: ", "?".yellow());
    io::stdout().flush().unwrap();
    let mut hash = String::new();
    io::stdin().read_line(&mut hash).unwrap();
    let hash = hash.trim();

    print!("[{}] Wordlist: ", "?".yellow());
    io::stdout().flush().unwrap();
    let mut wordlist = String::new();
    io::stdin().read_line(&mut wordlist).unwrap();
    let wordlist = wordlist.trim();


    print!("[{}] Algorithm: ", "?".yellow());
    io::stdout().flush().unwrap();
    let mut algorithm = String::new();
    io::stdin().read_line(&mut algorithm).unwrap(); 
    let algorithm = algorithm.trim();

    let file = File::open(wordlist).unwrap();
    let reader = BufReader::new(file);

    let start = Instant::now();

    println!("\n[{}] Begun cracking\n", ">".purple());

    for line in reader.lines() {
        let algorithm2 = algorithm.to_string();
        let hash2 = hash.to_string();
        thread::spawn(move || {
            let word = line.unwrap();
            if algorithm2 == "md5" {
                md5_method(hash2.as_str(), word.as_str(), start.elapsed().as_secs());
            } else if algorithm2 == "sha256" {
                sha256_method(hash2.as_str(), word.as_str(), start.elapsed().as_secs());
            } else if algorithm2 == "sha224" {
                sha224_method(hash2.as_str(), word.as_str(), start.elapsed().as_secs());
            } else if algorithm2 == "sha384" {
                sha384_method(hash2.as_str(), word.as_str(), start.elapsed().as_secs());
            } else if algorithm2 == "sha512" {
                sha512_method(hash2.as_str(), word.as_str(), start.elapsed().as_secs());
            }
        });
    }
    println!("[{}] Failed to crack password", "✘".red());
        
}


