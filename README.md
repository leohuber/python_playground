# Python Playground

## Python Environment

To initialize the Python environment using the `uv` tool, follow these steps:

1. **Install `rustc`, `cargo` and `rustup`**: Install the standalone installer from [https://www.rust-lang.org](https://www.rust-lang.org/tools/install)

2. **Install `uv`**: Install the standalone installer from [https://docs.astral.sh](https://docs.astral.sh/uv/getting-started/installation/)

3. **Initialize or Syncronize the environment**:
    ```sh
    uv sync
    ```

4. **Run scripts**:
    ```sh
    uv run <path_to_script>
    ```

These commands will set up and activate a new Python environment using `uv`.
