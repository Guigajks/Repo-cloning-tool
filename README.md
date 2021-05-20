# Repo cloning tool

A script for cloning multiple repositories

## Utilization

Create a file, with any name you want, and insert the repositories to clone, a repo link per line (use the **http** version).

### File example

```txt
https://github.com/User1/repo1.git
https://github.com/User1/repo2.git
https://github.com/User1/repo3.git
...
```

Execute the script passing the file path as a param **(-f, --file)**. You can also pass the user param **(-u, --user)** to clone the repo with your user

### Exection example

```bash
python clone.py -f ./repos_list.txt -u repo_user
```

Using the _-u_ param means that the script will clone the repos with the following pattern:

`https://user1@github.com/User1/repo3.git`

#### Notes

Use the destiny param **(-d, --destiny)** to change where the repos will be cloned (current directory is the default).
