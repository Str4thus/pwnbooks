# PWNBOOKS


## Core Modules

### config
>`pwnbooks.py config <key> <value>`

Allows configuration of certain values, used by `pwnbooks.py`.

| Key     | Type | Description  | Example |
|:-------:|:----:| -----:| -----:|
| note_dir | Path | Path to the parent directory for notes (**Needs to be a git repo**) | /root/notes |
| template_dir | Path | Path to the template directory used for note creation | /root/notes/__templates |
| blog_dir | Path | Path to the parent directory for blogposts (**Needs to be a git repo**)| /root/blog|

Example: `pwnbooks.py config note_dir /root/notes`

---

### init
> `pwnbooks.py init <lab_name> <box_name>`

Allows creation of notes based on a template stored in the folder specified under `template_dir`.

Example: `pwnbooks.py init htb blue --template ctf`

- Creates a new folder under `note_dir` called `htb` and copies the template called `ctf` into it, renaming it to `blue` 

---

### update
> `pwnbooks.py update`

Allows automated update of the git branch by adding all files found in the repo, committing and then pushing it to the blog repo specified under `note_dir`.


## Blog Extension

### blog_init
>`pwnbooks.py blog_init <blog_title> <folder_name>`

Allows creation of blogposts tailored for GravCMS.

Example: `pwnbooks.py blog_init "HackTheBox: Blue" htb_blue`

- Creates a new directory called `htb_blue` under `blog_dir` and creates a blogpost titled `HackTheBox: Blue`

---

### blog_update
> `pwnbooks.py blog_update`

Allows automated update of the git branch by adding all files found in the repo, committing and then pushing it to the blog repo specified under `blog_dir`.