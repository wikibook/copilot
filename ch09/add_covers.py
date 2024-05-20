# import os
# import PyPDF2


# def add_covers(report_dir, cover_dir, final_dir):
#     """
#     report_dir is a directory of reports named 1.pdf, 2.pdf, and so on.
#     These files may be one page or more than one page.

#       cover_dir is a directory of covers, with one cover per report.
#       The filenames in this directory are cover1.pdf, cover2.pdf, and so on.
#       Each of these files is one page.

#       Add the cover to the beginning of each report,
#       and store all resulting pdfs in final_dir.
#     """
#     report_files = os.listdir(report_dir)
#     for report_file in report_files:
#         report = open(os.path.join(report_dir, report_file), "rb")
#         report_reader = PyPDF2.PdfFileReader(report)
#         report_writer = PyPDF2.PdfFileWriter()
#         for page_num in range(report_reader.numPages):
#             report_writer.addPage(report_reader.getPage(page_num))
#         cover = open(os.path.join(cover_dir, "cover" + report_file), "rb")
#         cover_reader = PyPDF2.PdfFileReader(cover)
#         report_writer.insertPage(cover_reader.getPage(0), 0)
#         result = open(os.path.join(final_dir, report_file), "wb")
#         report_writer.write(result)
#         report.close()
#         cover.close()
#         result.close()


# if __name__ == "__main__":
#     add_covers("reports", "covers", "final")

import os
import fitz


def add_covers(report_dir, cover_dir, final_dir):
    """
    report_dir is a directory of reports named 1.pdf, 2.pdf, and so on.
    These files may be one page or more than one page.

    cover_dir is a directory of covers, with one cover per report.
    The filenames in this directory are cover1.pdf, cover2.pdf, and so on.
    Each of these files is one page.

    Add the cover to the beginning of each report,
    and store all resulting pdfs in final_dir.
    """
    if not os.path.exists(final_dir):
        os.mkdir(final_dir)
    for report in os.listdir(report_dir):
        report_path = os.path.join(report_dir, report)
        cover_path = os.path.join(cover_dir, f"cover{report}")
        final_path = os.path.join(final_dir, report)
        cover_doc = fitz.open(cover_path)
        report_doc = fitz.open(report_path)
        final_doc = fitz.open()
        final_doc.insert_pdf(cover_doc)
        final_doc.insert_pdf(report_doc)
        final_doc.save(final_path)


if __name__ == "__main__":
    add_covers("reports", "covers", "final")
