# Submission Guide — publishing WEcoS Product Recommendar to GitHub

This is the **one-time** setup guide for the Licensor (Aung Khaing Htun,
CLS) to push the suite to GitHub as
[github.com/AKHtun/wecos-product-recommendar](https://github.com/AKHtun/wecos-product-recommendar).

Estimated total time: **15 minutes** if you've never pushed to GitHub
before, **3 minutes** if you have.

---

## Step 1 — Create the GitHub repository (browser, ~2 min)

1. Go to [github.com/new](https://github.com/new)
2. Fill in:

   | Field | Value |
   |---|---|
   | Owner | `AKHtun` |
   | Repository name | `wecos-product-recommendar` |
   | Description | *Suite of Distributor Lubricant Engineer (DLE) skills for all the fluid product categories — by Aung Khaing Htun, CLS* |
   | Visibility | **Public** |
   | Initialize with... | **None** (no README, no .gitignore, no license — we'll push everything) |

3. Click **Create repository**

---

## Step 2 — Initialise git locally + first commit (terminal, ~3 min)

```bash
cd /workspace/.skills

# Initialise the local repo
git init
git checkout -b main

# Set your identity (use the email tied to your GitHub account)
git config user.name "Aung Khaing Htun"
git config user.email "your-github-email@example.com"

# Stage everything (output/ folders will be skipped thanks to .gitignore)
git add .

# Verify what's staged (sanity check before commit)
git status
git diff --cached --stat | tail -5

# First commit
git commit -s -m "Initial release of WEcoS Product Recommendar v1.0 (Jul 2026)

- 5 skills: lubricant-recommender, coolant-recommender, diesel-recommender,
  adblue-def-recommender, grease-recommender
- Methodology extensions: product currency check, tiered Standard/Upgraded
  output, DSR business email template, reference-ledger integration
- License: PolyForm Noncommercial 1.0.0
- Author: Aung Khaing Htun, CLS (sole author)
- AI-assist: WEcoS Agents, MuleRun Agent, Mavis by MiniMax"
```

> The `-s` flag adds the **DCO sign-off** required by `CONTRIBUTING.md`.

---

## Step 3 — Push to GitHub (terminal, ~1 min)

```bash
git remote add origin git@github.com:AKHtun/wecos-product-recommendar.git
# (or use HTTPS if you don't have SSH keys set up)
# git remote add origin https://github.com/AKHtun/wecos-product-recommendar.git

git push -u origin main
```

If prompted to authenticate, follow the GitHub credential helper
instructions (PAT for HTTPS, SSH key for SSH).

---

## Step 4 — Configure the GitHub repo (browser, ~5 min)

After the push succeeds, go to `https://github.com/AKHtun/wecos-product-recommendar/settings`:

### About (top right ⚙️ on repo main page)

| Field | Value |
|---|---|
| Description | *Suite of Distributor Lubricant Engineer (DLE) skills for all the fluid product categories* |
| Website | (leave blank) |
| Topics (tags) | `lubrication`, `tribology`, `mle`, `distributor`, `mulerun`, `wecos`, `polyform-noncommercial`, `def`, `adblue`, `coolant`, `grease`, `diesel` |

### Features

- ✅ Issues: **Enabled**
- ❌ Wiki: **Disabled** (the methodology lives in `SKILL.md`, not wiki)
- ❌ Projects: **Disabled**
- ❌ Discussions: **Disabled** (use Issues for methodology debate; per `CONTRIBUTING.md`)

### Pull Requests

- ✅ Allow squash merging: **Enabled**
- ✅ Automatically delete head branches: **Enabled**

### Branches → Branch protection rules → Add rule for `main`

| Setting | Value |
|---|---|
| Branch name pattern | `main` |
| Require a pull request before merging | ✅ Yes |
| Require approvals | 1 (you review your own PRs) |
| Dismiss stale pull request approvals when new commits are pushed | ✅ Yes |
| Require status checks to pass before merging | (skip — no CI yet) |
| Require linear history | ✅ Yes |
| Do not allow bypassing the above settings | ✅ Yes |

### Pages

Skip for now — the README is rendered natively by GitHub.

---

## Step 5 — Add repository metadata (browser, ~2 min)

### Topics & description (already done in Step 4)

### Releases

When you're ready for a tagged release:

```bash
git tag -a v1.0.0 -m "v1.0.0 — initial public release (Jul 2026)"
git push origin v1.0.0
```

Then in `github.com/AKHtun/wecos-product-recommendar/releases`, click
**Draft a new release** → pick the `v1.0.0` tag → write release notes
(copy from the commit message + a brief summary of what's in the suite)
→ **Publish release**.

### About → Social preview

Upload a 1280×640 PNG to `Settings → Social preview` so the repo has
a nice preview card when shared on LinkedIn / Twitter. (Optional.)

---

## Step 6 — Pin / star your own repo (browser, ~30 sec)

Visit the repo → click the **☆ Star** (top right) so it shows up in
your stars list and you get notifications on activity. Pin the repo
to your profile (Profile → Customize your pins → Add this repo) so
visitors to your GitHub profile see it first.

---

## Step 7 — Optional: enable GitHub Pages (later)

If you want a public-facing marketing page for the suite:

1. Settings → Pages → Source: **Deploy from a branch** → `main` → `/docs` (or `/`)
2. Add a `docs/index.md` with the README content
3. Site will be at `https://AKHtun.github.io/wecos-product-recommendar/`

(Skip for the initial release — README is enough.)

---

## Step 8 — Tell the world (your call, ~5 min)

Optional announcement channels:

- LinkedIn post with the GitHub URL + a screenshot of the tiered shadow
  table from one of the test runs
- Twitter / X thread with the same
- Email to anyone in your MuleRun / DLE network

We don't recommend launching with a "first post" on Reddit / Hacker
News — wait for at least one external contributor or a real-world
customer case study before driving traffic.

---

## Recap checklist

| # | Step | Time | Status |
|---|---|---|---|
| 1 | Create GitHub repo | 2 min | ☐ |
| 2 | Initialise git locally + first DCO-signed commit | 3 min | ☐ |
| 3 | Push to GitHub | 1 min | ☐ |
| 4 | Configure repo settings (about, features, branch protection) | 5 min | ☐ |
| 5 | Tag + draft release notes for v1.0.0 | 2 min | ☐ |
| 6 | Pin / star your own repo | 30 sec | ☐ |
| 7 | (Optional) GitHub Pages | 10 min | ☐ |
| 8 | (Optional) Announce on social | 5 min | ☐ |
| | **Total** | **~15 min core, +20 min optional** | |

---

## After publishing

Once the repo is live:

- **Watch** the repo so you get notifications on issues / PRs
  (GitHub → repo → **Watch** → **All activity**)
- The `issues` tab is the entry point for commercial-licensing enquiries
  — keep an eye on it
- Future methodology iterations go through PRs against `main`
- When you want a new tagged release, repeat Step 5 with `v1.1.0`,
  `v1.2.0`, etc.

---

## If something goes wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| `git push` rejected — non-fast-forward | You branched from a stale local main | `git pull --rebase origin main && git push` |
| `git push` rejected — secret detected | A PDS URL accidentally contained a private API key | Remove the key from the file, replace with placeholder `YOUR_API_KEY_HERE`, recommit |
| README looks broken | YAML frontmatter was treated as Markdown | Check `---` placement at top of SKILL.md; should be exactly 3 hyphens on lines 1 and (after the metadata block) |
| `git status` shows `output/` files staged | The `*/output/` pattern in `.gitignore` only matches one level | Replace with `**/output/` |
| `git commit -s` asks for identity | First commit on this machine | Run `git config user.name "..."` and `git config user.email "..."` first |
| GitHub branch protection blocks your own merge | "Dismiss stale approvals" + new commit | Re-approve the PR |

---

**That's it.** Once the repo is live, the methodology, the licensing,
and the contribution flow are all in place. Future iterations go through
PRs against `main` and the license stays consistent.

— Aung Khaing Htun, CLS, Licensor