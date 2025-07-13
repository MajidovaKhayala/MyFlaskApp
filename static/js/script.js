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
