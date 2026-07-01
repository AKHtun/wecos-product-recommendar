"""Convert a markdown recommendation report to PDF.

Tries ReportLab first (no external dependency on a browser). Falls back to
weasyprint if installed, then to pandoc. Keeps it dependency-light.

Usage:
    python3 scripts/render_pdf.py path/to/report.md path/to/report.pdf
"""
from __future__ import annotations
import sys
import re
import shutil
import subprocess
from pathlib import Path


def render_with_reportlab(md_text: str, out_pdf: Path) -> None:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    )

    styles = getSampleStyleSheet()
    body = ParagraphStyle("body", parent=styles["BodyText"], fontName="Helvetica",
                          fontSize=10, leading=13)
    h1 = ParagraphStyle("h1", parent=styles["Heading1"], fontName="Helvetica-Bold",
                        fontSize=16, leading=20, spaceAfter=8, textColor=colors.HexColor("#1F4E78"))
    h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Helvetica-Bold",
                        fontSize=13, leading=17, spaceBefore=10, spaceAfter=6,
                        textColor=colors.HexColor("#1F4E78"))
    h3 = ParagraphStyle("h3", parent=styles["Heading3"], fontName="Helvetica-Bold",
                        fontSize=11, leading=15, spaceBefore=8, spaceAfter=4)

    flow = []
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        # Table block detection: header | --- | rows
        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?[\s\-:|]+\|?\s*$", lines[i + 1]):
            header_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = [header_cells]
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            # Normalize row widths
            width = max(len(r) for r in rows)
            rows = [r + [""] * (width - len(r)) for r in rows]
            # Wrap cell text in Paragraphs for wrapping. Auto-scale font for wide tables.
            ncols = width
            if ncols <= 6:
                cell_font_size, cell_pad = 9, 4
            elif ncols <= 9:
                cell_font_size, cell_pad = 8, 3
            else:
                cell_font_size, cell_pad = 7, 2
            cell_style = ParagraphStyle("cell", parent=body, fontSize=cell_font_size,
                                        leading=cell_font_size + 2)
            wrapped = [[Paragraph(c or "&nbsp;", cell_style) for c in r] for r in rows]
            t = Table(wrapped, repeatRows=1, hAlign="LEFT")
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E78")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTSIZE", (0, 0), (-1, -1), cell_font_size),
                ("LEFTPADDING", (0, 0), (-1, -1), cell_pad),
                ("RIGHTPADDING", (0, 0), (-1, -1), cell_pad),
                ("TOPPADDING", (0, 0), (-1, -1), cell_pad),
                ("BOTTOMPADDING", (0, 0), (-1, -1), cell_pad),
            ]))
            flow.append(t)
            flow.append(Spacer(1, 6))
            continue
        if line.startswith("# "):
            flow.append(Paragraph(line[2:], h1))
        elif line.startswith("## "):
            flow.append(Paragraph(line[3:], h2))
        elif line.startswith("### "):
            flow.append(Paragraph(line[4:], h3))
        elif line.strip().startswith(("- ", "* ")):
            flow.append(Paragraph("&bull;&nbsp;" + line.strip()[2:], body))
        elif line.strip() == "---":
            flow.append(Spacer(1, 6))
        elif line.strip() == "":
            flow.append(Spacer(1, 4))
        else:
            # Inline bold / italic
            text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line)
            text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
            flow.append(Paragraph(text, body))
        i += 1

    doc = SimpleDocTemplate(
        str(out_pdf), pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=18 * mm, bottomMargin=18 * mm,
        title="Lubricant Recommendation Report",
    )
    doc.build(flow)


def render_with_weasyprint(md_text: str, out_pdf: Path) -> None:
    import markdown as md
    from weasyprint import HTML, CSS
    html = md.markdown(md_text, extensions=["tables", "fenced_code"])
    css = CSS(string="""
        @page { size: A4; margin: 18mm; }
        body { font-family: Arial, sans-serif; font-size: 10pt; color: #222; }
        h1 { color: #1F4E78; }
        h2 { color: #1F4E78; border-bottom: 1px solid #ccc; padding-bottom: 2px; }
        table { border-collapse: collapse; width: 100%; font-size: 9pt; }
        th { background: #1F4E78; color: white; padding: 6px; text-align: left; }
        td { border: 1px solid #999; padding: 5px; vertical-align: top; }
    """)
    HTML(string=html).write_pdf(str(out_pdf), stylesheets=[css])


def render_with_pandoc(md_path: Path, out_pdf: Path) -> None:
    subprocess.run(["pandoc", str(md_path), "-o", str(out_pdf)], check=True)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("Usage: render_pdf.py <input.md> <output.pdf>")
    md_path, out_pdf = Path(sys.argv[1]), Path(sys.argv[2])
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    md_text = md_path.read_text()

    try:
        render_with_reportlab(md_text, out_pdf)
        print(f"reportlab -> {out_pdf}")
        return
    except Exception as e:
        print(f"reportlab failed: {e}", file=sys.stderr)

    try:
        render_with_weasyprint(md_text, out_pdf)
        print(f"weasyprint -> {out_pdf}")
        return
    except Exception as e:
        print(f"weasyprint failed: {e}", file=sys.stderr)

    if shutil.which("pandoc"):
        render_with_pandoc(md_path, out_pdf)
        print(f"pandoc -> {out_pdf}")
        return

    sys.exit("No PDF renderer available. Install reportlab, weasyprint, or pandoc.")


if __name__ == "__main__":
    main()
