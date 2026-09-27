# Module 1 — Git & GitHub

**Student:** Bondoc, Julien Mark
**Date:** September 27, 2026

---

Git can be compared to the Track Changes function, except much more powerful. It works right from your computer and keep track of every change that you make to the code that you write. In case anything goes wrong, it is very easy to go back in time to the old functioning version.

GitHub can be compared to Google Drive for your code. It is a website, which allows you to upload a code that is tracked using Git. Using GitHub makes it extremely easy to both backup and share the code.

The problem, without Git, keeping changes requires making multiple copies such as project_v1, project_v2, or project_FINAL_final. In case anything goes wrong, tracking the exact place is a challenge. With Git, this is solved by recording every change made on the local computer so that any earlier version can be accessed effortlessly.

---

## Key vocabulary (in your own words)

- repository: The root directory in which all the work is stored along with a record of every single change to the project’s code.
- commit: Snapshot of your changes to your code along with a brief description of the changes you have made in your work.
- branch: This is basically an isolated copy of the source code where you can freely develop new features without modifying the codebase of your working project
- push / pull:  sends your commits from your local machine to a remote server such as GitHub, whereas Pull updates your local machine with the latest changes made by other developers in GitHub.
- pull request: This is basically a formal request to your teammates in GitHub asking for their approval on the changes made in your branch code.
- merge conflict: Error arises when there is any sort of difference between the work done by two people at the same point in the code.

---

## Walking through what I did

I made a different branch where I could implement the new feature without making changes to the master branch, added an appropriate comment while committing to the local branch, pushed the branch to GitHub, and made a pull request.
```
1. git checkout -b feature/login-form
2. git status
3. git add index.php style.css
4. git commit -m "Add responsive login form UI and styling"
5. git push -u origin feature/login-form
```

---

## A mistake I made (or one I want to avoid)

Making a commit to the main branch directly due to an oversight.

Once you open up your terminal and get started coding without thinking about creating another branch, there’s a high probability that you might do a git commit directly to the main branch. This results in pushing code that doesn’t work to the main branch. When starting your work, always remember to use git status or git branch right away to confirm that you know what branch you are on, Sir. If, by mistake, you have worked on the main branch without committing those changes, you can execute git checkout -b feature/your-feature-name.
---

## How this connects to something else

In fact, version control is similar to the timeline of history feature in design applications as well as backup facilities provided by databases. In the same way that you can revert to the previous state in case something goes wrong when updating a database transaction, Git provides a secure system for your source code so that you don't lose anything while experimenting.
