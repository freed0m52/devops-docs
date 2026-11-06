"""Формирование строки состояния для учебного репозитория."""


def format_status(version: str, deployed: bool) -> str:
<<<<<<< HEAD
    """Возвращает человекочитаемое состояние публикации."""
=======
    details = "temporary"
>>>>>>> ee670c0 (fix: prepare detailed status message)
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"


if __name__ == "__main__":
    print(format_status("1.0", deployed=True))
