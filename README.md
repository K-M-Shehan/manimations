# Manimations

> This directory contains a bunch of animations built with [Manim](https://docs.manim.community/) and managed using [uv](https://github.com/astral-sh/uv).

## Setup
Make sure that you have `uv` installed. 

If you haven't set up the environment:

```bash
uv venv
uv add manim
```

Activate it with:

```bash 
source .venv/bin/activate
```

## Dependencies

See `pyproject.toml` and `uv.lock`

## Run an animation

```bash
uv run manim scenes/fileName.py sceneName -pqh
```
Don't forget to replace sceneName with the actual scene name and fileName with the actual file name.
