from pathlib import Path
p = Path(__file__).with_name('index.html')
s = p.read_text(encoding='utf-8')
css = '''
body{background:#f5f7f4;color:#152d31}header{background:#f5f7f4;border:0}.nav{padding-top:24px;padding-bottom:24px}.brand{color:#18343a;letter-spacing:.075em}.logo{background:#123b3b;color:#f5e5b6;border-radius:50%;font-family:Georgia,serif}.pill{background:#e7eee9;color:#315b50;padding:10px 15px}.wrap{padding-top:15px}.hero{background:radial-gradient(ellipse at 90% 10%,#557e69 0,transparent 42%),linear-gradient(125deg,#102d30,#1f4a44);border-radius:22px;box-shadow:0 20px 45px #1f403222;gap:48px}.eyebrow{color:#efe0b2;background:#ffffff10;border-color:#ffffff30}.hero h1{font-family:Georgia,serif;font-weight:400;letter-spacing:-.04em}.hero h1 span{color:#e9d39e}.hero p{color:#d8e7de}.launch{background:#f8faf4;border:0;color:#183632;box-shadow:0 18px 36px #061a1830;border-radius:18px}.launch .label{color:#477b66}.launch h2{color:#153933;font-family:Georgia,serif;font-weight:400;font-size:1.8rem}.unit{background:#eaf1ea;border:0}.unit strong{color:#1a5144}.unit span{color:#59746b}.launch .note{color:#526e65}.section-head small{color:#648a76}.section-head h2{font-family:Georgia,serif;font-weight:400}.card{background:#fff;border:1px solid #e5ebe5;box-shadow:0 10px 30px #173e2910;border-radius:16px}.violet,.mint,.gold{background:#eaf2eb;color:#285b48}.card p{color:#5b6b65}footer{color:#70817a}
'''
s = s.replace('</style>', css + '</style>', 1)
p.write_text(s, encoding='utf-8')
