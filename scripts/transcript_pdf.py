"""Build the rehearsal transcript LaTeX source from speaking_notes.md.

Usage: python3 -I scripts/transcript_pdf.py speaking_notes.md build/main.nav build/transcript.tex

Each frame section of the notes (title slide, numbered slides, outline frames, backup slides) is matched,
in order, to a frame of the built deck. The section shows the final overlay page of its frame,
taken from build/main.pdf, above its script. The number of [click] cues in a section must equal
the number of overlay steps of its frame.
"""
import re
import sys

FRAME_HEADING = re.compile(r'^## (Title slide|Slide \d+\.|Outline before slide|Backup B\d+\.)')
CLICK = '**[click]**'

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=20mm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{fontspec,unicode-math,graphicx,xcolor,needspace,booktabs,enumitem}
\usepackage[most]{tcolorbox}
\setmainfont{STIXTwoText}[Extension=.otf,UprightFont=*-Regular,BoldFont=*-Bold,
  ItalicFont=*-Italic,BoldItalicFont=*-BoldItalic]
\setmathfont{STIXTwoMath-Regular.otf}
\definecolor{Navy}{HTML}{15324F}
\definecolor{Teal}{HTML}{007F82}
\newcommand{\F}{\mathbb F}
\newcommand{\llbracket}{\mathopen{\lBrack}}
\newcommand{\rrbracket}{\mathclose{\rBrack}}
\DeclareMathOperator{\wt}{wt}
\newcommand{\ket}[1]{\lvert #1\rangle}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\pagestyle{plain}
\newtcolorbox{background}{breakable,colback=black!4,colframe=black!25,boxrule=.4pt,
  left=6pt,right=6pt,top=4pt,bottom=4pt,fontupper=\small}
\newcommand{\click}{\textbf{\color{Teal}[click]}}
\begin{document}
"""


def escape(s):
    out = []
    for ch in s:
        if ch == '\\':
            out.append(r'\textbackslash{}')
        elif ch in '&%$#_{}':
            out.append('\\' + ch)
        elif ch == '~':
            out.append(r'\textasciitilde{}')
        elif ch == '^':
            out.append(r'\textasciicircum{}')
        else:
            out.append(ch)
    return ''.join(out)


MATH = re.compile(r'\$((?:[^$\\]|\\.)+)\$')


def inline(s):
    """Convert inline Markdown to LaTeX. Text between dollar signs is passed to math mode unchanged."""
    s = s.replace(CLICK, '\x00')
    maths = []

    def keep(m):
        maths.append(m.group(1))
        return '\ue000%d\ue001' % (len(maths) - 1)

    s = MATH.sub(keep, s)
    s = escape(s)
    s = s.replace('\x00', r'\click{}')
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    s = re.sub(r'\*\((.+?)\)\*', r'{\\color{black!55}\\itshape (\1)}', s)
    s = re.sub(r'\*(.+?)\*', r'\\emph{\1}', s)
    s = re.sub(r'"(.+?)"', lambda m: '\u201c' + m.group(1) + '\u201d', s)
    return re.sub('\ue000(\\d+)\ue001', lambda m: '$' + maths[int(m.group(1))] + '$', s)


def blocks(lines):
    """Convert a list of Markdown lines (headings, paragraphs, lists, tables) to LaTeX."""
    out, para, i = [], [], 0

    def flush():
        if para:
            out.append(inline(' '.join(para)) + '\n\n')
            para.clear()

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            flush()
            i += 1
        elif line.startswith('# '):
            flush()
            out.append(r'{\Large\bfseries\color{Navy}' + inline(line[2:]) + r'\par}' + '\n')
            i += 1
        elif line.startswith('## '):
            flush()
            out.append(r'\section*{' + inline(line[3:]) + '}\n')
            i += 1
        elif line.startswith('|'):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(set(c) <= set('-: ') for c in cells):
                    rows.append(cells)
                i += 1
            ncol = len(rows[0])
            spec = 'p{.27\\linewidth}p{.08\\linewidth}p{.55\\linewidth}' if ncol == 3 else 'l' * ncol
            out.append(r'{\small\begin{tabular}{@{}' + spec + r'@{}}\toprule' + '\n')
            out.append(' & '.join(r'\textbf{' + inline(c) + '}' for c in rows[0]) + r'\\\midrule' + '\n')
            for r in rows[1:]:
                out.append(' & '.join(inline(c) for c in r) + r'\\' + '\n')
            out.append(r'\bottomrule\end{tabular}\par}' + '\n')
        elif re.match(r'^\s*- ', line):
            flush()
            out.append(r'\begin{itemize}[leftmargin=1.2em,itemsep=1pt,topsep=2pt]' + '\n')
            depth = 0
            while i < len(lines) and re.match(r'^\s*- ', lines[i]):
                d = (len(lines[i]) - len(lines[i].lstrip())) // 2
                while d > depth:
                    out.append(r'\begin{itemize}[leftmargin=1.2em,itemsep=0pt,topsep=0pt]' + '\n')
                    depth += 1
                while d < depth:
                    out.append(r'\end{itemize}' + '\n')
                    depth -= 1
                out.append(r'\item ' + inline(lines[i].strip()[2:]) + '\n')
                i += 1
            while depth > 0:
                out.append(r'\end{itemize}' + '\n')
                depth -= 1
            out.append(r'\end{itemize}' + '\n')
        elif line.startswith('>'):
            flush()
            quoted = []
            while i < len(lines) and lines[i].startswith('>'):
                quoted.append(lines[i][1:].removeprefix(' '))
                i += 1
            out.append(r'\begin{background}' + '\n' + ''.join(blocks(quoted)) + r'\end{background}' + '\n')
        else:
            para.append(line.strip())
            i += 1
    flush()
    return out


def main(notes_path, nav_path, out_path):
    text = open(notes_path, encoding='utf-8').read()
    pages = [(int(a), int(b)) for a, b in
             re.findall(r'\\beamer@framepages \{(\d+)\}\{(\d+)\}', open(nav_path).read())]
    parts = re.split(r'^(## .*)$', text, flags=re.M)
    body = [PREAMBLE, ''.join(blocks(parts[0].split('\n')))]
    frame = 0
    for heading, content in zip(parts[1::2], parts[2::2]):
        if not FRAME_HEADING.match(heading):
            body.append(''.join(blocks([heading] + content.split('\n'))))
            continue
        assert frame < len(pages), f'more frame sections than frames in the deck: {heading}'
        first, last = pages[frame]
        clicks = content.count(CLICK)
        assert clicks == last - first, (
            f'{heading}: {clicks} [click] cues, but the frame has {last - first} overlay steps')
        if frame > 0:
            body.append('\\clearpage\n')
        body.append(r'\section*{' + inline(heading[3:]) + '}\n')
        body.append(r'\begin{center}\includegraphics[page=' + str(last)
                    + r',width=.62\linewidth]{build/main.pdf}\end{center}' + '\n')
        body.append(''.join(blocks(content.split('\n'))))
        frame += 1
    assert frame == len(pages), f'{frame} frame sections, but the deck has {len(pages)} frames'
    body.append('\\end{document}\n')
    open(out_path, 'w', encoding='utf-8').write(''.join(body))


if __name__ == '__main__':
    main(*sys.argv[1:4])
