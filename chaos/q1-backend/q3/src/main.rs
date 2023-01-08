// q3
// In `student.psv` there are some fake student datas from UNSW CSE (no doxx!). In each row, the fields from left to right are
//
// - UNSW Course Code
// - UNSW Student Number
// - Name
// - UNSW Program
// - UNSW Plan
// - WAM
// - UNSW Session
// - Birthdate
// - Sex
//
// Write a Rust program to find the course which has the highest average student WAM.

// use std::collections::HashMap;
use csv;
use std::fs::File;
//use std::io::Read;

fn read_from_file(path: &str) {
    let mut rdr = csv::Reader::from_path(path).expect("csv file");
    for result in rdr.records() {
        let record = result;
        println!("{:?}", record);
    }
}

fn main() {
    // Read in the initial psv
    // Group by Course Code, WAM and Total
    read_from_file("./student.psv");
}
