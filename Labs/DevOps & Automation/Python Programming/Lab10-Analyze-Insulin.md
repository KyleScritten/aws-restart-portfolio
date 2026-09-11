# Preparing to Analyze Insulin with Python

## Lab overview

In information technology, Python works well as the programming language of choice for manipulating strings, sequences, and numbers. Python is especially preferred in scientific computing applications such as physics, chemistry, and biology.

In some of the labs for the Python modules, I perform simple sequence manipulations and calculations on human insulin, a well-known hormone in the human body responsible for regulating sugars.

In this lab, I retrieve the protein sequence of human insulin from human preproinsulin.

### Accessing the VS Code IDE

**Visual Studio Code (VS Code)** is a free, lightweight source code editor developed by Microsoft that allows users to write, run, and debug code directly on their local machine. It includes an integrated code editor, debugger, and terminal, and supports virtually all programming languages through a vast library of extensions.

VS Code can run on Windows, macOS, and Linux, and integrates seamlessly with source control systems like Git and GitHub. It can also connect to remote environments — such as EC2 instances, containers, or WSL — through extensions, and is highly customizable through settings, themes, and extensions tailored to individual workflows.

To open the VS Code IDE, I copy the `LabIDEURL` value from the panel to the left of the instructions and paste it into a new browser tab. When prompted, I enter the `LabIDEPassword` value as the password, and the VS Code IDE opens in a new browser tab.












## Conclusion

### Deciding when to automate and when to work manually: A discussion about scope versus time

Automating my work versus working manually is a dilemma for computer programmers. Too much automation wastes time on coding, whereas too little restricts the scope of the program. I try to balance automation with manual work in an effort to create a program with the most scope for the least time spent coding. In this case, it is probably not worth the extra coding time to programmatically clean `insulin-seq.txt` to `insulin-seq-clean.txt`. However, if I needed to download thousands or millions of files and perform the same task, automation would be worth exploring.

Through the completion of this lab, I have prepared data for further processing. Manually preparing these files helps me appreciate the automation that Python can provide.
