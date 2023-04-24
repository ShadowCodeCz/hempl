import os
import datetime
import base64
import io
from PIL import Image

def render(template, body_renders, page_title=""):
    body = "\n".join([str(render) for render in body_renders])
    tmp = template.replace("<title>Title</title>", f"<title>{page_title}</title>")
    return tmp.replace("</body>", f"{body}</body>")


def save(html, path):
    with open(path, "w+") as output:
        output.write(html)


def read_standard_template(name):
    d = os.path.dirname(__file__)
    td = os.path.join(d, "template")
    t = os.path.join(td, f"{name}.html")

    with open(t, "r") as f:
        return f.read()


class SpacerRender:
    def __str__(self):
        return "<div class=\"top-spacer\"></div>"


class PanelContent:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class TopPanelContent:
    def __init__(self, major, minors):
        self.major = major
        self.minors = minors


class TopPanelRender:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"""
        <div class="top-panel">
            {self.render_major()}
            {self.render_minors()}
        </div>
        """

    def render_major(self):
        left = "\n".join([str(render) for render in self.content.major.left])
        right = "\n".join([str(render) for render in self.content.major.right])

        return f"""
            <div class="major">
                <div style="float: left">{left}</div>
                <div style="float: right;padding-right: 7px">{right}</div>
            </div>
        """

    def render_minors(self):
        r = ""
        for minor in self.content.minors:
            left = "\n".join([str(render) for render in minor.left])
            right = "\n".join([str(render) for render in minor.right])
            r += f"""
            <div class="minor">
                <div style="float: left">{left}</div>
                <div style="float: right;padding-right: 7px">{right}</div>
            </div>
            """
        return r


class BottomPanelRender:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"""
        <div class="bottom-panel">
            {self.render_content()}
        </div>
        """

    def render_content(self):
        return "\n".join([str(render) for render in self.content])


class TogglingBlockContent:
    def __init__(self, heading, blocks):
        self.heading = heading
        self.blocks = blocks


class TogglingBlockRender:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        t = str(datetime.datetime.now().timestamp()).replace(".", "-")
        return f"""
        <div>
            <label for="toggle-{t}">{str(self.content.heading)}</label>
            <input id="toggle-{t}" type="checkbox" style="visibility:hidden">

            <div class="toggling-div2">
                {self.render_blocks()}
            </div>
        </div>
        """

    def render_blocks(self):
        return "\n".join([str(render) for render in self.content.blocks])


class ColumnDefinition:
    def __init__(self, title, size):
        self.title = title
        self.size = size


class TableRender:
    def __init__(self, schema, style, rows):
        self.schema = schema
        self.style = style
        self.rows = rows

    def __str__(self):
        return f"""
        <table class="{self.style}">
        <tbody>
            {self.render_head()}
            {self.render_rows()}
        </tbody>
        </table>
        """

    def render_head(self):
        r = "<tr>"
        for column in self.schema:
            r += f""" <th style="width:{str(column.size)};">{str(column.title)}</th>"""
        r += "</tr>"
        return r

    def render_rows(self):
        return "\n".join([str(row) for row in self.rows])


class ColoredBoxRender:
    def __init__(self, color, content):
        self.color = color
        self.content = content

    def __str__(self):
        return f"""
        <div class="box  {self.color}">
            {str(self.content)}
        </div>
        """


class ToolTipContent:
    def __init__(self, title, blocks):
        self.title = title
        self.blocks = blocks


class ToolTipRender:
    def __init__(self, style, content):
        self.style = style
        self.content = content

    def __str__(self):
        return f"""
        <span class="reference">
            <span class="tooltip">{self.content.title}</span>
            <div class="tooltip-box {self.style}">
                {self.render_blocks()}            
            </div>
        </span>
        """

    def render_blocks(self):
        return "\n".join([str(render) for render in self.content.blocks])


class ModalWindowContent:
    def __init__(self, link, title, row, blocks):
        self.link = link
        self.title = title
        self.row = row
        self.blocks = blocks


class ModalWindowRender:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        t = str(datetime.datetime.now().timestamp()).replace(".", "-")
        return f"""
        <a href="#modal-{t}">{self.content.link}</a>
        <div id="modal-{t}" class="modal-box">
            <div>
                <div class="modal-head">
                    <span class="modal-title">{self.content.title}</span>
                    <span class="modal-close-button">
                        <a class="closeWindow" href="#close">X</a>
                    </span>
                </div>
                <div class="modal-row-view">
                    <span class="modal-row-view-align">{self.content.row}</span>
                </div>
                <div class="modal-content">
                    <div>
                        {self.render_blocks()}
                    </div>
                </div>
            </div>
        </div>
        """

    def render_blocks(self):
        return "\n".join([str(render) for render in self.content.blocks])


class TogglingTableRowRender:
    def __init__(self, visible_columns, toggling_columns, row_classes):
        self.visible_columns = visible_columns
        self.toggling_columns = toggling_columns
        self.row_classes = row_classes

    def __str__(self):
        t = str(datetime.datetime.now().timestamp()).replace(".", "")
        return f"""
            <tr class="{self.row_classes}">
                <td class="collapse-column"><a href="#" class="toggler" data-prod-hidden-row="{t}">+</a></td>
                {str(self.visible_columns)}
            </tr>
            <tr class="hidden-row{t}" style="display:none">
                {str(self.toggling_columns)}
            </tr>
        """


# class TogglingTableRowHelper:
#     def __init__(self, toggling_columns):
#         self.toggling_columns = toggling_columns
#
#     def render(self):
#         t = str(datetime.datetime.now().timestamp()).replace(".", "")
#         return f"""<td class="collapse-column"><a href="#" class="toggler" data-prod-hidden-row="{t}">+</a></td>""", f"""<tr class="hidden-row{t}" style="display:none">{str(self.toggling_columns)}</tr>"""


class SeparatorRowRender:
    def __init__(self, text, columns):
        self.text = text
        self.columns = columns

    def __str__(self):
        return f"<tr class=\"separator\"><td colspan=\"{self.columns}\">{self.text}</td></tr>"


class ColoringTextRender:
    def __init__(self, text, color):
        self.text = text
        self.color = color

    def __str__(self):
        return f"<span class=\"{self.color}-text\">{self.text}</span>"


def file_suffix(path):
    return path.split(".")[-1].lower()


class ImageRender:
    @staticmethod
    def render(path):
        img = Image.open(path)

        img_format = file_suffix(path)
        img_format = "jpeg" if img_format == "jpg" else img_format

        buffer = io.BytesIO()
        img.save(buffer, format=img_format)
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.read()).decode('ascii')

        return f'<img src="data:image/{img_format};base64,{img_base64}">'