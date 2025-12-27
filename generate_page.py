import yaml
import markdown
import re

def get_template(filename):
  with open(filename, 'r') as f:
    return f.read()

def get_news(yaml_file="news.yaml"):
  with open(yaml_file, 'r', encoding='utf-8') as f:
      entries = yaml.safe_load(f)

  result = """<h3 class="mb-3 text-center text-sm-left">News</h3>
  <ul class="list-unstyled">
  """
    
  for entry in entries:
    date = entry.get('date', '')
    text = entry.get('text', '')
    news_html = markdown.Markdown(extensions=['extra']).convert(text)
    # Handle superscripts for ordinal numbers (e.g., "6th" -> "6<sup>th</sup>")
    news_html = re.sub(r'(\d+)(st|nd|rd|th)', r'\1<sup>\2</sup>', news_html)
    result += f"""  <li style='margin-bottom: 5px'>
    <b class="mr-4 p-teaser float-sm-left mb-sm-1" style='min-width: 80px'>{date}</b>
    {news_html}
    </li>
    """
  result += "</ul>"
  return result

def get_publications():
  result = """
  <div class="container mt-5 mb-5">
      <h3>Publications</h3>
      <ul>
          <li>Engelmann, F., et al. "3D Object Detection and Pose Estimation from Semantic Keypoints." CVPR 2024.</li>
          <li>Engelmann, F., et al. "Efficient and Robust 3D Object Detection with Hierarchical Voxel Transformers." ICRA 2024.</li>
      </ul>
  </div>
  """
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
  news = get_news()
  publications = get_publications()
  projects = get_projects()

  html_content = f"""
  <!doctype html>
  <html lang="en">
    <head>
      {get_template("templates/header.html")}
    </head>
    <body>
      {get_template("templates/bio.html")}
  {news}
  {publications}
  {projects}
  {get_template("templates/footer.html")}
    </body>
  </html>"""

  with open(filename, 'w') as f:
    f.write(html_content)


if __name__ == "__main__":
  generate_page("index2.html")