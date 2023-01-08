1.  Identify one problem in the below code block, will this code compile? Discuss the related Rust feature regarding the problem you have identified, why does Rust choose to include this feature? A few sentences are good enough.

    ```rust
        let data = vec![1, 2, 3];
        let my_ref_cell = RefCell::new(69);
        let ref_to_ref_cell = &my_ref_cell;

        std::thread::spawn(move || {

            println!("captured {data:?} by value");

            println!("Whats in the cell?? {ref_to_ref_cell:?}")

        }).join().unwrap();
    ```

    A: This code will not compile, due to how the Rust compiler puts great importance on memory-safety, especially when it comes to multi-threading and passing in variables by value/reference.

    In this case, there exists the my_ref_cell, as well as a reference to the my_ref_cell. By moving in both the original value and a reference to the original value into a Thread, Rust realises there are significant dangers to this; This could include setting up a Race condition where multiple threads attempt to operate on the same referenced-value which is not locked across threads, causing unintended behaviour/errors as the variable changes. Since RefCells are not synchronised across multiple threads, Rust will not let you move the variables into a new Thread; Instead you'd have to utilise Mutex to achieve multithreading.

2.  Shortly discuss, when modelling a response to a HTTP request in Rust, would you prefer to use `Option` or `Result`?

    A: In this case, both Option and Result could deal with a success/failure when it comes to making a response to an HTTP request; Both can deal with very black and white situations where there is either a success or a failure. However, I'd prefer to use a Result, due to the greater number of failure cases and complexity of fail conditions involved in making HTTP requests that Results are more suited to deal with than Options. 

    With Results, one could describe the variety of different reasons or causes regarding a failed HTTP request as part of the Err option, such as the HTTP Error Code and resulting response from the server with more information. In comparison, Options lack such an ability, being able to only handle an error by returning a single object of the Option generic type or None. Since Options are more suited to simpler conditions such as if a value was missing or not, I would instead opt for a Result.

3.  In `student.psv` there are some fake student datas from UNSW CSE (no doxx!). In each row, the fields from left to right are

    - UNSW Course Code
    - UNSW Student Number
    - Name
    - UNSW Program
    - UNSW Plan
    - WAM
    - UNSW Session
    - Birthdate
    - Sex

    Write a Rust program to find the course which has the highest average student WAM. **Write your program in the cargo project q3**.

