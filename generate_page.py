def get_template(filename):
  with open(filename, 'r') as f:
    return f.read()

def get_news():
  result = """
  <div class="container mt-5 mb-5">
      <h3>News</h3>
      <ul>
          <li><b>June 2024:</b> I will join the University of Lugano (USI) as an assistant professor in September 2024.</li>
          <li><b>May 2024:</b> Our paper "3D Object Detection and Pose Estimation from Semantic Keypoints" has been accepted at CVPR 2024.</li>
          <li><b>March 2024:</b> Our paper "Efficient and Robust 3D Object Detection with Hierarchical Voxel Transformers" has been accepted at ICRA 2024.</li>
      </ul>
  </div>
  """
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