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

// function toggleAccordion(header) {
//   const item = header.parentElement;
//   const icon = header.querySelector('.icon');
//   const isActive = item.classList.toggle('active');

//   if (isActive) {
//     icon.classList.remove('fa-chevron-right');
//     icon.classList.add('fa-chevron-down');
//   } else {
//     icon.classList.remove('fa-chevron-down');
//     icon.classList.add('fa-chevron-right');
//   }
// }

function toggleAccordion(header) {
  const currentItem = header.parentElement;
  const allItems = document.querySelectorAll('.accordion-item');

  allItems.forEach(item => {
    if (item !== currentItem) {
      item.classList.remove('active');
      const icon = item.querySelector('.icon');
      if (icon) {
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-right');
      }
    }
  });

  // Toggle current item
  const isActive = currentItem.classList.toggle('active');
  const currentIcon = header.querySelector('.icon');
  if (currentIcon) {
    if (isActive) {
      currentIcon.classList.remove('fa-chevron-right');
      currentIcon.classList.add('fa-chevron-down');
    } else {
      currentIcon.classList.remove('fa-chevron-down');
      currentIcon.classList.add('fa-chevron-right');
    }
  }
}
