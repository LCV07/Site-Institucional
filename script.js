// Navegação móvel e rolagem suave
document.addEventListener('DOMContentLoaded',function(){
  const toggle = document.getElementById('nav-toggle');
  const nav = document.getElementById('main-nav');
  toggle.addEventListener('click',()=>{
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    if(!expanded){
      nav.setAttribute('aria-hidden','false');
    } else {
      nav.setAttribute('aria-hidden','true');
    }
  });

  // smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click',function(e){
      const targetId = this.getAttribute('href').slice(1);
      const target = document.getElementById(targetId);
      if(target){
        e.preventDefault();
        target.scrollIntoView({behavior:'smooth',block:'start'});
        // close mobile nav if open
        if(window.innerWidth < 800){
          nav.setAttribute('aria-hidden','true');
          toggle.setAttribute('aria-expanded','false');
        }
      }
    });
  });

  // fill current year
  const year = document.getElementById('year');
  if(year) year.textContent = new Date().getFullYear();

  // simple contact form handler (demo)
  const form = document.getElementById('contact-form');
  if(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      alert('Obrigado! Sua mensagem foi recebida (demo).');
      form.reset();
    });
  }
});