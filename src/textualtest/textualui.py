from textual.app import App
from textual.widgets import Footer, Header, Placeholder


class MyTextualApp(App):
    async def on_mount(self) -> None:
        grid = await self.view.dock_grid(edge="top", name="main")

        grid.add_column("col", fraction=1)
        grid.add_row("row", fraction=1)
        grid.add_areas(
            main="col-start|col-end,row-start|row-end",
        )

        grid.place(main=Placeholder(name="Main Area"))

        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")


if __name__ == "__main__":
    main = MyTextualApp()
    main.run()
