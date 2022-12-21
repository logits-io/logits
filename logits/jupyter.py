import typing

import ipywidgets as widgets
from IPython.display import display

from logits.session import Session


def run(session: Session) -> None:
    textarea = widgets.Textarea(
        description="Prompt:", placeholder="Normalize data", disabled=False
    )
    submit_btn = widgets.Button(
        description="Submit", disabled=False, button_style="info"
    )

    def on_submit(_: typing.Any) -> None:
        prompt: str = textarea.value
        res: str = session.query(prompt)

        print("Prompt:", prompt)
        print("---")
        print(res)

    display(textarea, submit_btn)

    submit_btn.on_click(on_submit)
