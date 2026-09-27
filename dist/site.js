(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const layers = [...document.querySelectorAll('[data-depth]')];
  const hero = document.querySelector('.hero');
  let current = scrollY, frame = 0;
  function paint() {
    frame = 0;
    if (reduce.matches) { layers.forEach(el => el.style.transform = ''); return; }
    const target = Math.min(scrollY, hero.offsetHeight);
    current += (target - current) * 0.12;
    const mobile = innerWidth < 641 ? 0.55 : 1;
    layers.forEach(el => el.style.transform = `translate3d(0,${(current * Number(el.dataset.depth) * mobile).toFixed(2)}px,0)`);
    if (Math.abs(target - current) > .1) frame = requestAnimationFrame(paint);
  }
  function schedule() { if (!frame) frame = requestAnimationFrame(paint); }
  addEventListener('scroll', schedule, {passive:true});
  addEventListener('resize', schedule, {passive:true});
  reduce.addEventListener('change', schedule);
  schedule();
})();
