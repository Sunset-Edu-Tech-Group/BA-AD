## FAQ

### Why the switch to rust?

- `BA-AD` is getting slow, and I want to learn rust, so I decided to make `BA-AD` in rust and might as well add new
  stuff that I didn't add before like Global asset download.

### Why a library?

- This helps the process of porting `BA-AD` to another project.
  Instead of rewriting or passing as an executable, this exposes functions so you can implement the functions easily.
  This also helps when porting to another language because you can bind it with `Cdylib`

### Why no search UI?

- It just makes the project more complex.
  The main goal is to make a simple CLI/Library to download Blue Archive assets.
  The UI can be implemented on another project like `BA-AD-GUI` or `BA-AD-TUI`.

### Why no extracting?

- Extracting has been removed from `BA-AD` because It's challenging to maintain and makes the codebase messy.
  So I opt in to make it into a separate thing.
  But if you still want the old extracting functionality, you can
  use [BA-AD-py-2.1.0](https://github.com/Deathemonic/BA-AD/archive/743f69db3964f654bba33b6ce8ebd214010fd53d.zip)
