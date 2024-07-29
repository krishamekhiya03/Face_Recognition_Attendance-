from fpdf import FPDF

title = '20,000 Leagues Under the Sea'

class PDF(FPDF):
    def header(self):
        # logo
        self.image('logoai - Copy.png', 10, 8, 25)
        # font
        self.set_font('helvetica', 'B', 20)
        # calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)

        # colors of frame, background, and text
        self.set_draw_color(0, 80, 180)  # border = blue
        self.set_fill_color(230, 230, 0)  # background = yellow
        self.set_text_color(220, 50, 50)  # text = red

        # thickness of frame (border)
        self.set_line_width(1)

        # position for title
        x = self.get_x()
        y = self.get_y()

        # title
        self.cell(title_w, 10, title, border=1, align='C', fill=True)

        # restore position after title
        self.set_xy(x, y + 20)  # adjust Y position as needed

        # Draw the top border
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)
        self.line(10, 10, doc_w - 10, 10)  # Top border
        self.line(10, 10, 10, self.h - 10)  # Left border
        self.line(doc_w - 10, 10, doc_w - 10, self.h - 10)  # Right border

    # page footer
    def footer(self):
        # set position of the footer
        self.set_y(-15)
        # font
        self.set_font('helvetica', 'I', 10)
        # set font color grey
        self.set_text_color(169, 169, 169)

        # page number
        self.cell(0, 10, f'Page {self.page_no()}/{self.alias_nb_pages()}', align='C')

        # Draw the bottom border
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)
        self.line(10, self.h - 10, self.w - 10, self.h - 10)  # Bottom border

    def chapter_title(self, ch_num, ch_title):
        # set font
        self.set_font('helvetica', '', 12)
        # background color
        self.set_fill_color(200, 220, 255)
        # chapter title
        chapter_title = f'Chapter {ch_num} : {ch_title}'
        self.cell(0, 5, chapter_title, align='L', fill=1)

    def chapter_body(self, name):
        # read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # set font
        self.set_font('times', '', 12)
        # insert text
        self.multi_cell(0, 5, txt)
        # line break
        self.ln()
        # end each chapter
        self.set_font('times', 'I', 12)
        self.cell(0, 5, 'END OF CHAPTER')

    def print_chapter(self, ch_num, ch_title, name):
        self.add_page()
        self.chapter_title(ch_num, ch_title)
        self.chapter_body(name)

    def add_table(self, data, col_widths, row_height=10):
        self.set_fill_color(200, 220, 255)
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)
        self.set_font('helvetica', '', 12)

        for row in data:
            for item, col_width in zip(row, col_widths):
                self.cell(col_width, row_height, item, border=1, align='C', fill=True)
            self.ln(row_height)

# create FPDF object
pdf = PDF('P', 'mm', 'Letter')

# metadata
pdf.set_title(title)
pdf.set_author('Jules Verne')

# get total page numbers
pdf.alias_nb_pages()

# set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# specify font
pdf.set_font('helvetica', 'BIU', 16)
pdf.set_font('times', '', 12)

# Add text
for i in range(1, 10):
    pdf.set_x(15)  # Adjust X position as needed
    pdf.set_y(pdf.get_y() + 10)  # Adjust Y position as needed
    pdf.cell(0, 10, f'This is {i} line')

# Add a table
data = [
    ['Header 1', 'Header 2', 'Header 3'],
    ['Row 1 Col 1', 'Row 1 Col 2', 'Row 1 Col 3'],
    ['Row 2 Col 1', 'Row 2 Col 2', 'Row 2 Col 3'],
    ['Row 3 Col 1', 'Row 3 Col 2', 'Row 3 Col 3']
]

col_widths = [60, 60, 60]

pdf.add_page()
pdf.add_table(data, col_widths)

pdf.output('pdf_1.pdf')
