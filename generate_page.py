import yaml
import markdown
import re

def get_template(filename):
  with open(filename, 'r') as f:
    return f.read()


def get_news(yaml_file="data/news.yaml"):
  with open(yaml_file, 'r', encoding='utf-8') as f:
      entries = yaml.safe_load(f)

  def parse_date(date_str):
    month = date_str.split(' ')[0]
    year = date_str.split(' ')[1]
    return month[:3] + ' ' + year

  result = """
    <div class="container mt-5 mb-5">
      <h3>News</h3>
      <div class="news-scrollable">
        <table class="table-borderless">
  """

  for i, entry in enumerate(entries):
    date = entry.get('date', '')
    text = entry.get('text', '')
    news_html = markdown.Markdown(extensions=['extra']).convert(text)
    news_html = re.sub(r'(\d+)(st|nd|rd|th)', r'\1<sup>\2</sup>', news_html)
    news_html = re.sub(r'^<p>|</p>$', '', news_html.strip())

    result += f"""
    <tr>
      <td style="vertical-align: top;"><b style="display: inline-block; min-width: 85px; ">{parse_date(date)}</b>
      <td>{news_html}</td>
    </tr>
    """

  result += """
        </table>
      </div>
    </div>
  """
  return result


def get_publications(yaml_file="data/publications.yaml"):

  with open(yaml_file, 'r', encoding='utf-8') as f:
      entries = yaml.safe_load(f)
  with open('data/conferences.yaml', 'r', encoding='utf-8') as f:
      conferences = yaml.safe_load(f)
  with open('data/authors.yaml', 'r', encoding='utf-8') as f:
    authors_dict = yaml.safe_load(f)

  result = """
    <div class="container mt-5 mb-5">
      <h3>Publications</h3>
      <ul class="list-unstyled">
  """

  def get_award(award):
    result = ''
    if award:
      awards = award.split(',')
      result = f'<span class="p-award badge badge-success mb-2">{awards[0]}</span>'
      if len(awards) > 1:
        result += f' <span class="mb-2">({awards[1].strip()})</span>'
      result += '<br />'
    return result

  def get_bibtex(title, authors, conference_abbrev, conference, year):
    first_author_lastname = authors.split(',')[0].strip().split(' ')[-1]
    title_first_word = title.split(' ')[0]
    bibtex_short = f'{first_author_lastname}{year}{title_first_word}'.replace('*', '').replace(':', '')
    bibtex = f"""@inproceedings{{{bibtex_short},
  title={{{title}}},
  author={{{authors}}},
  booktitle={{{conference} ({conference_abbrev})}},
  year={{{year}}}
}}"""
    return bibtex_short, bibtex

  def format_authors(author_list, authors_dict):
    formatted = []
    for author in author_list:
        author = author.strip()
        shared = False
        if author[-1] == '*':
            shared = True
            author = author[:-1]
        website = authors_dict.get(author)
        if author == 'Francis Engelmann':
           formatted.append(f'<b>{author}</b>')
        elif website:
            formatted.append(f'<a href="{website}" target="_blank">{author}</a>')
        else:
            formatted.append(author)
        if shared:
            formatted[-1] += '<sup>*</sup>'
    return ', '.join(formatted)

  def get_paper(paper):
    if paper:
      return f'<a class="mr-3" target="_blank" href="{paper}"><i class="fas fa-file-pdf"></i> Paper</a>'
    else:
      return ''

  def get_project(project):
    if project:
      return f'<a class="mr-3" target="_blank" href="{project}"><i class="fas fa-cube"></i> Project</a>'
    else:
      return ''

  def get_code(code):
    if code:
      return f'<a class="mr-3" target="_blank" href="{code}"><i class="far fa-file-code"></i> Code</a><br />'
    else:
      return ''

  for i, entry in  enumerate(entries):
    title = entry.get('title', '')
    authors = entry.get('authors', '')
    authors_list = authors.split(',')
    conference_abbrev = entry.get('conference', '')
    conference  = conferences.get(conference_abbrev, conference_abbrev)
    year = entry.get('year', '')
    paper = entry.get('paper', '')
    project = entry.get('project', '')
    code = entry.get('code', '')
    award = entry.get('award', '')
    teaser = entry.get('teaser', '')

    bibtex_short, bibtex = get_bibtex(title, authors, conference_abbrev, conference, year)

    result += f"""
    <li class="media">
      <div class="media-body text-center">
        <img src="{teaser}" class="mr-4 p-teaser float-sm-left mb-sm-1" style="padding-bottom: 35px;" />
        <p class="text-left">
          <span class="p-title">{title}</span></br>
          <span class="p-authors">{format_authors(authors_list, authors_dict)}</span></br>
        <span class="p-conference">{conference} ({conference_abbrev}), {year}.</span></br>
          {get_award(award)}
          {get_paper(paper)}
          <a class="mr-3" data-toggle="collapse" href="#{bibtex_short}" role="button" aria-expanded="false" aria-controls="{bibtex_short}"><i class="far fa-file-alt"></i> BibTeX</a>
          {get_project(project)}
          {get_code(code)}
          <div class="collapse" id="{bibtex_short}">
            <div class="card card-body"><pre class="p-bibtex">{bibtex}</pre></div>
          </div>
        </p>
      </div>
    </li>
    """

  result += "</ul></div>"
  return result


def get_projects():
  result = """
  <div class="container mt-5 mb-5">
      <h3>Projects</h3>
      <ul>
          <li><a href=" #">Project 1</a>: Description of project 1.</li>
          <li><a href=" #">Project 2</a>: Description of project 2.</li>
      </ul>
  </div>
  """
  return result


def generate_page(filename):
  html_content = f"""
  <!doctype html>
  <html lang="en">
    <head>
      {get_template("templates/header.html")}
    </head>
    <body>
      {get_template("templates/bio.html")}
      {get_news()}
      {get_publications()}
      {get_template("templates/footer.html")}
    </body>
  </html>"""

  with open(filename, 'w') as f:
    f.write(html_content)


if __name__ == "__main__":
  generate_page("index.html")