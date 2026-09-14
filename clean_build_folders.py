"""Elimina carpetas de compilacion llamadas exactamente ``bin`` u ``obj``."""

from pathlib import Path
import shutil


ROOT_DIRECTORY = Path(__file__).resolve().parent
BUILD_FOLDER_NAMES = {"bin", "obj"}


def find_build_folders(root: Path) -> list[Path]:
    """Devuelve las carpetas bin y obj que deben eliminarse."""
    folders = sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_dir() and path.name in BUILD_FOLDER_NAMES
        ),
        key=lambda path: len(path.parts),
    )
    top_level_folders: list[Path] = []

    for folder in folders:
        if not any(parent in folder.parents for parent in top_level_folders):
            top_level_folders.append(folder)

    return top_level_folders


def main() -> None:
    folders = find_build_folders(ROOT_DIRECTORY)
    deleted_count = 0

    for folder in folders:
        print(f"Eliminando: {folder}")
        try:
            shutil.rmtree(folder)
        except OSError as error:
            print(f"Error al eliminar '{folder}': {error}")
        else:
            deleted_count += 1

    print(f"Carpetas eliminadas: {deleted_count}")


if __name__ == "__main__":
    main()
