# Modifs PDFs

Modifs PDFs is a PySide6 desktop app to merge and split PDF files, built with Python 3.12.

![ezgif com-video-to-gif](https://user-images.githubusercontent.com/38250076/82755604-f0fd9680-9dd4-11ea-898c-da4efd574cb5.gif)

## How to use

Drop your PDF files into the window, then click **Fusionner** to merge them or **Séparer** to split one into individual pages.

## Development setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
git clone https://github.com/spacewaterbear/modifs-pdfs.git
cd modifs-pdfs
uv sync
uv run python code/src/main/python/main.py
```

## Building an installer

### Automatic (recommended) — GitHub Actions

Push a version tag to trigger a build for both Windows and Linux automatically:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Once the workflow completes, download the executables from the **Actions** tab → select the run → **Artifacts**.

You can also trigger a build manually from **Actions → Build → Run workflow**.

### Manual — local build

Requirements: `uv sync` done, then run from the `code/` directory:

```bash
cd code
uv run pyinstaller modifs_pdfs.spec
```

The executable is output to `code/dist/`. Note: you can only build for the platform you are currently on (run on Windows to get a `.exe`, run on Linux to get a Linux binary).

#### Running the Linux binary

```bash
chmod +x "./code/dist/Modifs PDFs"
"./code/dist/Modifs PDFs"
```

If you downloaded it from GitHub Actions, unzip the artifact first, then run the same commands.

## Credits

- Logo by <a href="https://www.flaticon.com/authors/dimitry-miroliubov" title="Dimitry Miroliubov">Dimitry Miroliubov</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
- Inspired by the PyConverter by <a href="https://www.linkedin.com/in/thibaulthoudon" title="Thibault Houdon">Thibault Houdon</a> — <a href="https://www.udemy.com/course/applications-bureau-qt-python/" title="Udemy">Créer 5 applications de bureau avec Qt for Python (PySide2)</a>
