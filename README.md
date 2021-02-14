# hempl
HTML Templates


# Read Standard Template
```python
template = hempl.read_standard_template("dark")
``` 

# Render and Save
```python
renders = []
html = hempl.render(template, renders)
hempl.save(html, "output.html")
``` 

# Top Panel Render
```python
top_pannel_content = hempl.TopPanelContent(
    # Major
    hempl.PanelContent(
        # left
        [
            FakeTitleRender()
        ], 
        # right
        []
    ),
    # Minors
    [
        hempl.PanelContent(
            # left
            [
                hempl.ColoringTextRender("AAA", "green",),
                "BBB",
                colored_box,
                colored_box2
            ],
            # Right
            [
                "CCC"
            ]),

    ]
)

hempl.TopPanelRender(top_pannel_content)
``` 

# Spacer Render
```python
hempl.SpacerRender()
```

#  Toggling Block Render
```python
        hempl.TogglingBlockContent(
            "<span class=\"heading-1\">Block title</span>",
            [
                hempl.TableRender(
                    # Schema
                    [
                        hempl.ColumnDefinition("AAA", "50%"),
                        hempl.ColumnDefinition("BBB", "50%")
                    ],
                    # Style
                    "table-with-head",
                    # Rows Renders
                    [
                        FakeRowRender(2), 
                        FakeRowRender(2), 
                        FakeRowRender(2), 
                        FakeLongRowRender(2)
                    ]
                )
            ]
        )
```


#  Table Render
```python
    hempl.TableRender(
        # Schema
        [
            hempl.ColumnDefinition("AAA", "25%"),
            hempl.ColumnDefinition("BBB", "25%"),
            hempl.ColumnDefinition("CCC", "25%"),
            hempl.ColumnDefinition("DDD", "25%")
        ],
        # Style
        "table-with-head",
        # Rows Renders
        [
            FakeRowRender(4),
            FakeRowRender(4),
        ]
    ),
```


#  Toggling Row Render
```python
tr_class = "red"
visible_columns += f"<td></td>"
toggling_columns = f"<td columnspan=\"{self.columns}\"></td>"


hempl.TogglingTableRowRender(visible_columns, toggling_columns, tr_class)
```

#  Coloring Text Render
```python
hempl.ColoringTextRender("AAA", "green",)
```


#  Boxed Comment Render
```python
colored_box = str(hempl.ColoredBoxRender(
    # Style
    "red", 
    # Content
    "Red Colored Box"
))
```

#  Tooltip Render
```python
tooltip = hempl.ToolTipRender(
    # Style
    "left", 
    hempl.ToolTipContent(
        # Text
        "Red Colored Box With ToolTip",
        # Content 
        ["AAAA", "BBBB", "<p>X</p>", "<p>Y</p>"]
    )
)
```

#  Modal Render
```python
modal_content = hempl.ModalWindowContent(
    "text", 
    # Title
    "Title",
    # Subtitle
     "1. some row",
     # Content blocks 
     ["AAAA"]
)
modal = hempl.ModalWindowRender(modal_content)
```

#  Full Box Render
```python
tooltip = hempl.ToolTipRender("left", hempl.ToolTipContent("text", ["AAAA", "BBBB", "<p>X</p>", "<p>Y</p>"]))
modal_content = hempl.ModalWindowContent(tooltip, "title", "subtitle", ["content"])
modal = hempl.ModalWindowRender(modal_content)
colored_box = str(hempl.ColoredBoxRender("red", modal))
```


#  Image Render
```python
ImageRender.render(path)
```
