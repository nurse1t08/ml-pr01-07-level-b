from pathlib import Path
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent
notebook = root / "notebooks" / "pr01.ipynb"
nb = nbformat.read(notebook, as_version=4)
client = NotebookClient(nb, timeout=300, kernel_name="python3",
                        resources={"metadata": {"path": str(root / "notebooks")}})
client.execute()
nbformat.write(nb, notebook)
print("Notebook выполнен и сохранён:", notebook)
