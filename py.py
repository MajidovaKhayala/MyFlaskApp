 # D:\MyFieldofWork\PYTHON\py.py   

from flask import Flask, render_template_string
from flask import Flask

app = Flask(__name__)

index_html = """
<!DOCTYPE html>
<html lang="az">
<head>
  <meta charset="UTF-8">
  <title>Monitorinq Paneli</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: sans-serif;
      height: 100vh;
      display: flex;
    }

    /* Sidebar */
    .sidebar {
      width: 200px;
      background-color: #2c3e50;
      color: white;
      display: flex;
      flex-direction: column;
      transition: width 0.3s;
      position: relative;
    }

    .sidebar.collapsed {
      width: 60px;
    }

    .sidebar.collapsed a {
      text-align: center;
      font-size: 12px;
    }

    .sidebar a {
      padding: 15px;
      text-decoration: none;
      color: white;
      transition: background 0.3s;
    }

    .sidebar a:hover {
      background-color: #34495e;
    }

    /* Toggle button */
    .toggle-btn {
      background-color: #1abc9c;
      color: white;
      border: none;
      padding: 10px;
      cursor: pointer;
      font-size: 16px;
      text-align: right;
    }

    .header-logo {
      padding: 10px;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .header-logo img#logo-full {
      width: 180px;
      transition: width 0.3s;
    }
    
    .header-logo img#logo-mini {
      width: 40px;
      transition: width 0.3s;
    }

    .sidebar.collapsed .header-logo {
      justify-content: center;
      align-items: center;
      padding: 10px 0;
    }

    .content {
      flex-grow: 1;
    }

    iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  </style>
</head>
<body>

  <div class="sidebar" id="sidebar">
    <div class="header-logo">
      <img src="/static/IKTALOGOAG.png" alt="Logo" id="logo-full" />
      <img src="/static/simvol-white.png" alt="Logo" id="logo-mini" style="display: none;" />
    </div>
    <button class="toggle-btn" onclick="toggleSidebar()">☰ </button>
    <a href="/general" target="contentFrame">1. Ümumi</a>    
    <a href="/telekom" target="contentFrame">1. Telekom</a>
    <a href="/poct" target="contentFrame">2. Poçt</a>
    <a href="/radiospektr" target="contentFrame">3. Radiospektr</a>
  </div>

  <div class="content">
    <iframe name="contentFrame" src="/general"></iframe>
  </div>

    <script>
      function toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        const fullLogo = document.getElementById('logo-full');
        const miniLogo = document.getElementById('logo-mini');
    
        sidebar.classList.toggle('collapsed');
    
        const collapsed = sidebar.classList.contains('collapsed');
    
        if (collapsed) {
          fullLogo.style.display = 'none';
          miniLogo.style.display = 'block';
        } else {
          fullLogo.style.display = 'block';
          miniLogo.style.display = 'none';
        }
      }
    </script>


</body>
</html>
"""

# Məzmun səhifələri

general_html = """
<h1>Ümumi Bölmə</h1>
<p>İKTA fəaliyətlərinə dair məlumatlar burada göstərilir.</p>
"""

telekom_html = """
<h1>Telekom Bölməsi</h1>
<p>Telekommunikasiya xidmətlərinə dair məlumatlar burada göstərilir.</p>
"""

poct_html = """
<h1>Poçt Bölməsi</h1>
<p>Poçt xidmətləri ilə bağlı monitorinq məlumatları burada yerləşir.</p>
"""

radiospektr_html = """
<h1>Radiospektr Bölməsi</h1>
<p>Radiospektr idarəçiliyi və monitorinqə aid məlumatlar burada göstərilir.</p>
"""

# Flask yönləndirmələr
@app.route('/')
def index():
    return render_template_string(index_html)

@app.route('/general')
def general():
    return render_template_string(general_html)

@app.route('/telekom')
def telekom():
    return render_template_string(telekom_html)

@app.route('/poct')
def poct():
    return render_template_string(poct_html)

@app.route('/radiospektr')
def radiospektr():
    return render_template_string(radiospektr_html)
 


app = Flask(__name__)

@app.route('/')
def home():
    return "Salam, Flask!"

# Aşağıdakı sətri SİLİN (Render üçün lazım deyil)
# if __name__ == '__main__':
#     app.run()
# if __name__ == '__main__':
#     app.run(debug=True)
