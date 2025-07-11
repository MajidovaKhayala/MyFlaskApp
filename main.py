from flask import Flask, render_template_string

app = Flask(__name__)

index_html = """
<!DOCTYPE html>
<html lang="az">
<head>
  <meta charset="UTF-8">
  <title>Monitorinq Paneli</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.0/font/bootstrap-icons.css" rel="stylesheet">
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

    .sidebar a {
      padding: 15px;
      text-decoration: none;
      color: white;
      transition: background 0.3s;
      display: flex;
      align-items: center;
      white-space: nowrap;
    }

    .sidebar a:hover {
      background-color: #34495e;
    }

    .sidebar.collapsed a {
      justify-content: center;
    }

    .menu-text {
      margin-left: 10px;
      transition: opacity 0.3s;
    }

    .sidebar.collapsed .menu-text {
      display: none;
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
      display: flex;
      justify-content: flex-end;
      align-items: center;
    }

    .sidebar.collapsed .toggle-btn {
      justify-content: center;
    }

    .header-logo {
      padding: 10px;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 60px;
    }

    .header-logo img#logo-full {
      width: 180px;
      transition: all 0.3s;
    }
    
    .header-logo img#logo-mini {
      width: 40px;
      transition: all 0.3s;
      display: none;
    }

    .sidebar.collapsed .header-logo {
      justify-content: center;
      padding: 10px 0;
    }

    .sidebar.collapsed #logo-full {
      display: none;
    }

    .sidebar.collapsed #logo-mini {
      display: block;
    }

    .content {
      flex-grow: 1;
    }

    iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    .menu-icon {
      font-size: 1.2em;
      min-width: 20px;
      text-align: center;
    }
  </style>
</head>
<body>

  <div class="sidebar" id="sidebar">
    <div class="header-logo">
      <img src="/static/IKTALOGOAG.png" alt="Logo" id="logo-full" />
      <img src="/static/simvol-white.png" alt="Logo" id="logo-mini" />
    </div>
    <button class="toggle-btn" onclick="toggleSidebar()">
      <span class="menu-icon">☰</span>
    </button>
    <a href="/general" target="contentFrame">
      <i class="bi bi-speedometer2 menu-icon"></i>
      <span class="menu-text">Ümumi</span>
    </a>    
    <a href="/telekom" target="contentFrame">
      <i class="bi bi-wifi menu-icon"></i>
      <span class="menu-text">Telekom</span>
    </a>
    <a href="/poct" target="contentFrame">
      <i class="bi bi-envelope menu-icon"></i>
      <span class="menu-text">Poçt</span>
    </a>
    <a href="/radiospektr" target="contentFrame">
      <i class="bi bi-broadcast menu-icon"></i>
      <span class="menu-text">Radiospektr</span>
    </a>
  </div>

  <div class="content">
    <iframe name="contentFrame" src="/general"></iframe>
  </div>

  <script>
    function toggleSidebar() {
      const sidebar = document.getElementById('sidebar');
      const toggleBtn = document.querySelector('.toggle-btn .menu-text');
      
      sidebar.classList.toggle('collapsed');
      
      if (sidebar.classList.contains('collapsed')) {
        toggleBtn.textContent = 'Göstər';
      } else {
        toggleBtn.textContent = 'Gizlət';
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

if __name__ == '__main__':
    app.run(debug=True)
