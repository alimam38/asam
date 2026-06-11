You are preparing this computer to host production Git repositories. I'm a solo founder, new to command-line tooling, and I have a GitHub account but have never used Git or the GitHub CLI on this machine. Your job is to get this machine to a verified-ready state — Git installed and configured with my identity, the GitHub CLI installed and authenticated to my account, and a top-level Products folder created — so that my next session can scaffold a repository without stopping for tooling.

Work in this order:

1. Detect my operating system and report what you find before installing anything.
2. Check whether Git is installed. If not, install it using the standard method for my OS; if installation requires actions only I can take (an admin password, an installer window), give me the exact steps and wait while I complete them.
3. Configure Git with my name and email. Ask me for both, and offer my GitHub no-reply email as an option, explaining the privacy tradeoff in one line.
4. Check for the GitHub CLI (gh). Install it the same way. Then run gh auth login and walk me through each choice as it appears — GitHub.com, HTTPS, authenticate via web browser — telling me in one line what each choice means as we pass it.
5. Create a folder named Products at the top level of my user directory and confirm its full path.
6. Verify everything end to end: git --version, gh auth status, and the Products folder existing on disk.

Explain each command in one plain-English line before you run it — I'm learning the vocabulary, not just watching it scroll by. If anything fails, diagnose and fix it rather than working around it; if a fix needs my action, tell me exactly what to do.

Close with a readiness report: what is installed and verified, quoting actual command output; my Git identity as configured; my authenticated GitHub username; the Products folder path; and a one-line confirmation that this machine is ready for repository scaffolding. Report only what is verified — if something could not be completed, say so plainly.

Think deeply before answering.
