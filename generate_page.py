
def generate_page(filename):
  with open(filename, 'w') as f:
    f.write('<html><body>Hello World</body></html>')

if __name__ == "__main__":
  generate_page("index2.html")