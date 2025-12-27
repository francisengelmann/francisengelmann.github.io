import yaml
import markdown
import re

def get_template(filename):
  with open(filename, 'r') as f:
    return f.read()


def parse_date(date_str):
  month = date_str.split(' ')[0]
  year = date_str.split(' ')[1]
  return month[:3] + ' ' + year

def get_news(yaml_file="news.yaml"):
  with open(yaml_file, 'r', encoding='utf-8') as f:
      entries = yaml.safe_load(f)

  result = """
    <div class="container mt-5 mb-5">
      <h3>News</h3>
      <table class="table-borderless">
  """
      # <ul class="list-unstyled">
    
  for i, entry in enumerate(entries):
    date = entry.get('date', '')
    text = entry.get('text', '')
    news_html = markdown.Markdown(extensions=['extra']).convert(text)
    news_html = re.sub(r'(\d+)(st|nd|rd|th)', r'\1<sup>\2</sup>', news_html)
    news_html = re.sub(r'^<p>|</p>$', '', news_html.strip())

    if i == 10:
      result += """
      </table>
      <a data-toggle="collapse" href="#more_news" role="button" aria-expanded="false" style="display: inline-block; margin: auto; margin-top: 10px;">
      Previous news
      </a>
        
      <div class="collapse" id="more_news">
      <table class="table-borderless">
      """   

    result += f"""
    <tr>
      <td style="vertical-align: top;"><b style="display: inline-block; min-width: 85px; ">{parse_date(date)}</b>
      <td>{news_html}</td>
    </tr>
    """

  result += "</table></div>"
  return result




    # <li>
    # <b class="mr-4 float-sm-left  mb-sm-1 p-teaser" style="display: inline-block; min-width: 120px; ">October 2024</b>
    # We have 2 papers accepted at <a href="https://wacv2025.thecvf.com/">WACV'25</a>.
    # </li>
    


    # <li style='margin-bottom: 5px'>
    #     <b class="mr-4 p-teaser float-sm-left mb-sm-1" style='min-width: 80px'>June 2025</b>
    #     <a href="https://super-dec.github.io/">SuperDec</a> is an <b>🏆 Oral</b> (top 2.3%) at <a href="https://iccv.thecvf.com/">ICCV'25</a> in Hawaii 🌸,
    #     amazing work with <a target="_blank" href="https://elisabettafedele.github.io/" target="_blank">Elisabetta Fedele</a> and <a href="https://boysun045.github.io/boysun-website/" target="_blank">Boyang Sun</a>.
    #   </li>



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