from pathlib import Path
p = Path(__file__).with_name('index.html')
s = p.read_text(encoding='utf-8')
style = '''
body{background:radial-gradient(ellipse at 85% 10%,#1a586b,transparent 38%),radial-gradient(ellipse at 10% 90%,#174a53,transparent 38%),#091b30; font-family:Inter,system-ui,sans-serif}
main{position:relative;width:min(100%,760px);max-width:760px;padding:clamp(28px,6vw,64px);text-align:center;border-radius:26px;background:linear-gradient(145deg,#ffffff12,#ffffff05);box-shadow:0 28px 90px #0004;backdrop-filter:blur(14px)}
main:before{content:'SCHOLASTIC SCIENCE ACADEMY';display:block;font-weight:700;letter-spacing:.16em;font-size:.74rem;color:#9eece2;margin-bottom:38px}
.eyebrow{color:#f5d894;letter-spacing:.18em;font-size:.74rem}h1{font-size:clamp(2.7rem,7vw,5rem);letter-spacing:-.055em;max-width:640px;margin:20px auto;color:#f3fbfa}p{max-width:510px;margin:0 auto;color:#c6dbe4;font-size:1.05rem}
.clock{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:20px;margin:36px auto 0;border:1px solid #ffffff20;border-radius:20px;background:#071c2c88}
.unit{min-width:0;padding:16px 6px;background:#ffffff0c;border:1px solid #ffffff12}.unit strong{color:#f5d894;font-size:clamp(2rem,5vw,3rem);letter-spacing:-.04em}.unit span{color:#bbd4dc;letter-spacing:.1em}
.note{margin:20px auto 0;font-size:.85rem}.clock:before{content:'COUNTDOWN TO OUR PLANNED LAUNCH';grid-column:1/-1;color:#a8d8d4;font-weight:700;font-size:.7rem;letter-spacing:.15em;margin-bottom:8px}
@media(max-width:480px){body{padding:16px}main{padding:30px 18px}main:before{margin-bottom:25px}.clock{gap:6px;padding:13px}.unit{padding:12px 2px}.unit span{font-size:.6rem}h1{font-size:2.6rem}}
'''
s = s.replace('</style>', style + '</style>')
s = s.replace('<h1>Our portal is coming soon.</h1><p>We are preparing your academy workspace for launch.</p>', '<h1>Progress has a new home.</h1><p>A clearer, simpler way for our academy community to stay connected with learning and progress.</p>')
p.write_text(s, encoding='utf-8')
